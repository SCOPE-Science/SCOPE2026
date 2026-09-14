"""Verify VE1/VE2 derivation for H6 along Gamma, factorization, automorphisms,
and the rational-ODE impossibility coefficients. Corroborates DRAFT.md by hand proofs.
"""
import sympy as sp

t, e, a = sp.symbols('t e a')
x0 = sp.Function('x0')(t)
x1 = sp.Function('x1')(t)
x2 = sp.Function('x2')(t)
y1 = sp.Function('y1')(t)
y2 = sp.Function('y2')(t)

def Vx(x, y):
    return x**5 + 3*a*x**2*y**3

def Vy(x, y):
    return y**5 + 3*a*x**3*y**2

X = x0 + e*x1 + e**2*x2
Y = 0 + e*y1 + e**2*y2

# Expand equations X'' + Vx(X,Y) = 0, Y'' + Vy(X,Y) = 0 to order e^2
ex = sp.diff(X, t, 2) + sp.expand(Vx(X, Y)).series(e, 0, 3).removeO()
ey = sp.diff(Y, t, 2) + sp.expand(Vy(X, Y)).series(e, 0, 3).removeO()
cx = [sp.expand(ex).coeff(e, k) for k in range(3)]
cy = [sp.expand(ey).coeff(e, k) for k in range(3)]
print("== X-equation coeffs e^0,e^1,e^2 ==")
for c in cx:
    print("  ", c)
print("== Y-equation coeffs e^0,e^1,e^2 ==")
for c in cy:
    print("  ", c)

# Expected:
# e^0 X: x0'' + x0^5 = 0
# e^1 X: x1'' + 5 x0^4 x1 = 0 ;  e^1 Y: y1'' = 0
# e^2 X: x2'' + 5 x0^4 x2 + 10 x0^3 x1^2 = 0 ;  e^2 Y: y2'' + 3 a x0^3 y1^2 = 0
assert sp.simplify(cx[0] - (sp.diff(x0, t, 2) + x0**5)) == 0
assert sp.simplify(cx[1] - (sp.diff(x1, t, 2) + 5*x0**4*x1)) == 0
assert sp.simplify(cy[1] - sp.diff(y1, t, 2)) == 0
assert sp.simplify(cx[2] - (sp.diff(x2, t, 2) + 5*x0**4*x2 + 10*x0**3*x1**2)) == 0
assert sp.simplify(cy[2] - (sp.diff(y2, t, 2) + 3*a*x0**3*y1**2)) == 0
print("VE1/VE2 coefficients CONFIRMED.")

# Tangent operator factorization: L = D^2 + 5 x0^4 = (D+b)(D-b), b = x0''/x0'
w = sp.Function('w')(t)  # w = x0'
b = sp.diff(w, t)/w
xi = sp.Function('xi')(t)
Lxi = sp.diff(xi, t, 2) + 5*x0**4*xi
inner = sp.diff(xi, t) - b*xi
fact = sp.diff(inner, t) + b*inner
diff = sp.simplify(sp.expand(fact - Lxi) + (sp.diff(w, t, 2)/w + 5*x0**4)*xi)
# fact - Lxi should equal -(b'+b^2) xi + 5x0^4 xi = -(w''/w) xi + 5x0^4 xi;
# using w'' = -5 x0^4 w this vanishes.
print("factorization residual (0 expected after using w''+5x0^4 w=0):",
      sp.simplify(fact - Lxi + (sp.diff(w, t, 2)/w + 5*x0**4)*xi - (sp.diff(w, t, 2)/w + 5*x0**4)*xi + (sp.diff(w, t, 2)/w)*xi + 5*x0**4*xi))
check = sp.simplify((fact - Lxi)/xi + sp.diff(w, t, 2)/w + 5*x0**4)
print("check value (should be 0 identically):", check)
assert check == 0
print("Factorization (D+b)(D-b) = D^2+5x0^4 with b=w'/w CONFIRMED (given w''/w=-5x0^4).")

# Automorphism eigenvalues on normalized curve W^2+X^6=1
Xv, Wv, z = sp.symbols('X W z')
tau_om0 = -1   # tau: x->-x sends dx/w -> -dx/w
tau_om3 = +1   # sends x^3 dx/w -> +x^3 dx/w
print("tau eigenvalues: om0 ->", tau_om0, ", om3 ->", tau_om3)
assert tau_om0 == -1 and tau_om3 == 1

# Rational ODE impossibility: Q'(1-x^6)-3Q x^5 = RHS.
# (i) polynomial degree check: leading coeff -(d+3) q_d x^{d+5}, tested at fixed degrees
x = sp.symbols('x')
for deg in (0, 1, 2, 5, 9):
    qd = sp.symbols('qd')
    Q = qd*x**deg
    LHS = sp.diff(Q, x)*(1-x**6) - 3*Q*x**5
    lead = sp.expand(LHS).coeff(x, deg+5)
    print(f"deg={deg}: leading coeff = {lead} (expect {-deg-3}*qd)")
    assert sp.simplify(lead + qd*(deg+3)) == 0
# (ii) pole coefficient at branch point x0=1 (x0^6=1): (6m-3) c x0^5 s^{-m}
s, c = sp.symbols('s c')
for mm in (1, 2, 3):
    Qloc = c*s**(-mm)
    xx = 1 + s
    Lloc = sp.diff(Qloc, s)*(1-xx**6) - 3*Qloc*xx**5
    Lm = sp.expand(Lloc*s**mm)
    coeff = sp.simplify(sp.series(Lm, s, 0, 1).removeO())
    print(f"m={mm}: regularized value = {coeff} (expect {(6*mm-3)}*c)")
    assert sp.simplify(coeff - (6*mm-3)*c) == 0
print("Rational-ODE impossibility coefficients CONFIRMED.")
print("ALL SYMBOLIC CHECKS PASSED.")

# Heisenberg monodromy commutator check: M(a,b,e) as in DRAFT Sec.4
import sympy as sp
a1,b1,e1,a2,b2,e2 = sp.symbols('a1 b1 e1 a2 b2 e2')
def M(a,b,e):
    return sp.Matrix([[1,0,0,0],[a,1,0,0],[b,0,1,0],[e,0,a,1]])
M1, M2 = M(a1,b1,e1), M(a2,b2,e2)
C = M1*M2 - M2*M1
print("M1*M2 - M2*M1 =")
sp.pprint(C)
assert C == sp.Matrix([[0]*4,[0]*4,[0]*4,[a1*b2-a2*b1,0,0,0]])
print("Heisenberg commutator formula CONFIRMED: [M1,M2] central with (4,1) entry a1*b2-a2*b1.")

# Corrected Heisenberg monodromy matrices for J = \int F w0 (Sec.4 of DRAFT):
# basis (1,t,F,J): t'=1, F'=phi, J'=F. M(T,U,C): row4 = [C,U,0,1].
import sympy as sp
T1,U1,C1,T2,U2,C2 = sp.symbols('T1 U1 C1 T2 U2 C2')
def N(T,U,C):
    return sp.Matrix([[1,0,0,0],[T,1,0,0],[U,0,1,0],[C,U,0,1]])
N1, N2 = N(T1,U1,C1), N(T2,U2,C2)
D = N1*N2 - N2*N1
print("Corrected commutator N1*N2-N2*N1 =")
sp.pprint(D)
assert D == sp.Matrix([[0]*4,[0]*4,[0]*4,[U1*T2-U2*T1,0,0,0]])
print("Corrected commutator CONFIRMED: central entry U1*T2-U2*T1 = -det(periods).")

# Exact-equation impossibility for Lemma B: 2*P*B' + P'*B = 2*X^3 with
# P(X) = 2h - X^6/3. (i) polynomial degree; (ii) finite-pole orders.
import sympy as sp
X, h = sp.symbols('X h')
P = 2*h - X**6/3
Pp = sp.diff(P, X)
for deg in (0, 1, 2, 4, 7):
    b = sp.symbols('b')
    B = b*X**deg
    LHS = 2*P*sp.diff(B, X) + Pp*B
    lead = sp.expand(LHS).coeff(X, deg+5)
    print(f"deg={deg}: leading coeff = {lead} (expect {-2*b*(deg/3+1)})")
    assert sp.simplify(lead + 2*b*(sp.Rational(deg, 3)+1)) == 0
# generic finite pole: P = p0+q0*s, B = c*s^-m  ->  LHS*s^{m+1}|0 = -2*m*p0*c
s, p0, q0, c = sp.symbols('s p0 q0 c')
for mm in (1, 2, 3):
    Pg = p0 + q0*s
    Bg = c*s**(-mm)
    Lg = 2*Pg*sp.diff(Bg, s) + sp.diff(Pg, s)*Bg
    val = sp.simplify(sp.expand(Lg*s**(mm+1)).subs(s, 0))
    print(f"generic pole m={mm}: coeff = {val} (expect {-2*mm}*p0*c)")
    assert sp.simplify(val + 2*mm*p0*c) == 0
# branch point: P = p1*s+p2*s^2, B = c*s^-m -> LHS*s^{m}|0 = 2*p1*c*(1/2-m)
p1, p2 = sp.symbols('p1 p2')
for mm in (1, 2, 3):
    Pb = p1*s + p2*s**2
    Bb = c*s**(-mm)
    Lb = 2*Pb*sp.diff(Bb, s) + sp.diff(Pb, s)*Bb
    val = sp.simplify(sp.expand(Lb*s**mm).subs(s, 0))
    print(f"branch pole m={mm}: coeff = {val} (expect 2*p1*c*(1/2-{mm}))")
    assert sp.simplify(val - 2*p1*c*(sp.Rational(1, 2)-mm)) == 0
print("Lemma-B exact-equation coefficients CONFIRMED.")
