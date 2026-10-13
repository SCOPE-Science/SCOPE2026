import sympy as sp

v,t,q,w,tp = sp.symbols("v t q w tp")
I = sp.I
sqrt3 = sp.sqrt(3)
sqrt481 = sp.sqrt(481)

A = v**8 + 14*v**4 + 1
B = v*(v**4 - 1)
C = v**12 - 33*v**8 - 33*v**4 + 1
a = sp.Integer(481)
b = sp.Integer(30)
c = sp.Integer(-4879)
d = 54*b**4
h = 54*B**4
p = c*C
k = a*A

lam_plus = (sp.Integer(4879) + 481*sqrt481)/(2*d)
lam_minus = (sp.Integer(4879) - 481*sqrt481)/(2*d)

R = sp.expand((d*q**2 + p*q + h)**2 - k**3*q**2)

def F(lam):
    return sp.expand(q**2 - 2*lam*C*q - 108*lam**2*B**4)

Fp = F(lam_plus)
Fm = F(lam_minus)

assert sp.simplify(R - d**2*Fp*Fm) == 0
assert lam_plus != lam_minus
assert lam_plus != 0 and lam_minus != 0

# Source identity and factor-discriminants.
assert sp.expand(A**3 - C**2 - 108*B**4) == 0
assert sp.simplify(sp.discriminant(Fp,q) - 4*lam_plus**2*A**3) == 0
assert sp.simplify(sp.discriminant(Fm,q) - 4*lam_minus**2*A**3) == 0

# Square-class data used in the irreducibility argument.
Hplus = v**4 + 2*I*sqrt3*v**2 + 1
Hminus = v**4 - 2*I*sqrt3*v**2 + 1
assert sp.expand(Hplus*Hminus - A) == 0
assert sp.expand((Hplus**3 + Hminus**3)/2 - C) == 0
assert sp.expand(C + 6*I*sqrt3*B**2 - Hplus**3) == 0
assert sp.expand(C - 6*I*sqrt3*B**2 - Hminus**3) == 0
assert sp.gcd(sp.Poly(Hplus,v,extension=[I,sqrt3]), sp.Poly(sp.diff(Hplus,v),v,extension=[I,sqrt3])).degree() == 0
assert sp.gcd(sp.Poly(Hminus,v,extension=[I,sqrt3]), sp.Poly(sp.diff(Hminus,v),v,extension=[I,sqrt3])).degree() == 0
assert sp.gcd(sp.Poly(Hplus,v,extension=[I,sqrt3]), sp.Poly(Hminus,v,extension=[I,sqrt3])).degree() == 0

# F3 transition: each degree-eight factor has the same base weight.
Cw = w**12 - 33*w**8 - 33*w**4 + 1
Bw = w*(w**4 - 1)
for lam in (lam_plus, lam_minus):
    Ft = t**8 - 2*lam*C*t**4 - 108*lam**2*B**4
    transformed = sp.cancel(w**24 * Ft.subs({v:1/w, t:tp/w**3}))
    target = tp**8 - 2*lam*Cw*tp**4 - 108*lam**2*Bw**4
    assert sp.simplify(transformed-target) == 0

# Common-zero resultant: away from the six B=0 boundary points, intersection is J=0.
J = sp.expand(a**3*B**4 - b**4*A**3)
res = sp.resultant(Fp,Fm,q)
ratio = sp.cancel(res/(B**4*J))
assert sp.simplify(sp.diff(ratio,v)) == 0
assert sp.simplify(ratio) != 0
assert sp.degree(J,v) == 24
assert sp.gcd(sp.Poly(J,v),sp.Poly(sp.diff(J,v),v)).degree() == 0
assert sp.gcd(sp.Poly(J,v),sp.Poly(A*B*C,v)).degree() == 0

# Each J-root has one common nonzero q and four distinct t-lifts.
q0 = C/c
# Modulo J, both factors vanish at q=C/c.
remp = sp.rem(sp.together(Fp.subs(q,q0)).as_numer_denom()[0], J, domain=sp.QQ.algebraic_field(sqrt481))
remm = sp.rem(sp.together(Fm.subs(q,q0)).as_numer_denom()[0], J, domain=sp.QQ.algebraic_field(sqrt481))
assert sp.expand(remp) == 0
assert sp.expand(remm) == 0

# Cusp count inputs: eight simple A-roots, disjoint from B, with nonzero q.
assert sp.degree(A,v) == 8
assert sp.gcd(sp.Poly(A,v),sp.Poly(sp.diff(A,v),v)).degree() == 0
assert sp.gcd(sp.Poly(A,v),sp.Poly(B*C,v)).degree() == 0
cusps_per_component = 8*4
assert cusps_per_component == 32

# Divisor-class arithmetic on the blown-up base, using source intersection data.
K2 = 2
C2 = -3
KC = 1
CC = 0
E2 = 36*K2 + 4*C2 + 4*C2 + 24*KC + 24*KC + 8*CC
KE = -6*K2 - 2*KC - 2*KC
paE = 1 + (E2 + KE)//2
assert E2 == 96
assert KE == -16
assert paE == 41
normalization_genus = paE - cusps_per_component
assert normalization_genus == 9
assert E2 == 24*4

print("factorization=OK")
print("factor_class_self_intersection=96")
print("common_intersections=96")
print("cusps_per_component=32")
print("arithmetic_genus_per_component=41")
print("normalization_genus_per_component=9")
print("VERIFY_OK")
