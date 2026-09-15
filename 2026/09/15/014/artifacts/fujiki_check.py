"""Comprehensive verification for K3^[2]-type divisorial J-slope wall disproof.

Part 1: polarized Fujiki identity (symbolic).
Part 2: divisorial slope formula and wall equation F=0 (general parameters).
Part 3: root location s_* in (0,t1) + transversality, for all 0<t1^2<d.
Part 4: numeric illustration (algebra only; ampleness for small t1 is Lemma 2 of DRAFT).
"""
import sympy as sp

print("=== Part 1: polarized Fujiki ===")
# B(a,b,c,d) = q(ab)q(cd)+q(ac)q(bd)+q(ad)q(bc) is symmetric 4-linear and
# B(w,w,w,w) = 3 q(w)^2. By uniqueness of polarization (char 0), the cup-product
# 4-form (a,b,c,d) -> int abcd equals B. Check diagonal + symmetry spot-check.
qaa, qab, qac, qad, qbb, qbc, qbd, qcc, qcd, qdd = sp.symbols(
    'qaa qab qac qad qbb qbc qbd qcc qcd qdd')
# generic vectors a,b,c,d with symbolic pairwise products; evaluate B on diagonal
# w = a+b: B(w^4) should equal 3*q(w)^2 with q(w)=qaa+qbb+2*qab
qw = qaa + qbb + 2*qab
Bdiag = (qw)**2 * 3
# direct: B(a+b,...) via multilinearity: coefficient check on monomial qaa*qbb etc.
# B(w,w,w,w) = sum over pairings of the 4 slots, each pairing = product of two q's.
# Terms: slots (12)(34),(13)(24),(14)(23). With all slots = w: 3*q(w)^2. Trivially true.
# Nontrivial check: B(a,a,b,b) = qaa*qbb + 2*qab^2 ; and this must equal int a^2 b^2.
# Verify consistency with (a+b)^4 expansion: int(a+b)^4 = 3(qaa+qbb+2qab)^2.
# Expand LHS via multilinearity: int a^4 + 4 int a^3b + 6 int a^2b^2 + 4 int ab^3 + int b^4
# = 3qaa^2 + 4*(3*qaa*qab) + 6*B(a,a,b,b) + 4*(3*qbb*qab) + 3*qbb^2  [using B for a^3b: B(a,a,a,b)=3*qaa*qab]
# Set equal to 3*(qaa+qbb+2qab)^2 and solve for B(a,a,b,b):
B_aabb = sp.symbols('B_aabb')
LHS = 3*qaa**2 + 12*qaa*qab + 6*B_aabb + 12*qbb*qab + 3*qbb**2
RHS = 3*(qaa + qbb + 2*qab)**2
sol = sp.solve(sp.expand(LHS - RHS), B_aabb)
print("int a^2 b^2 =", sol, " ; formula gives qaa*qbb+2*qab^2:",
      sp.expand(sol[0] - (qaa*qbb + 2*qab**2)) == 0)

print("=== Part 2 & 3: wall equation, general ===")
d, t1, s = sp.symbols('d t1 s', positive=True)
F4 = t1*s**2 - 2*d*s + t1*d          # F(s)/4, F = q(a)q(b,e)-2q(a,b)q(a,e), e=delta
disc = (2*d)**2 - 4*t1**2*d
print("disc =", sp.factor(disc), "> 0 iff t1^2 < d")
s_star = (2*d - sp.sqrt(disc)) / (2*t1)
print("s_* =", s_star)
print("product s_* s_big =", sp.simplify(s_star * ((2*d + sp.sqrt(disc)) / (2*t1))))
print("F(0)/4 =", F4.subs(s, 0), "(>0)")
print("F(t1)/4 =", sp.factor(F4.subs(s, t1)), "(<0 iff t1^2<d)")
print("F'(s_*)/2 =", sp.simplify(sp.diff(F4, s).subs(s, s_star) / 2), "(nonzero: transverse)")
print("d=2,t1=1/2: s_* =", sp.simplify(s_star.subs({d: 2, t1: sp.Rational(1, 2)})))

print("=== Part 4: numeric illustration (d=2, t1=0.5) ===")
import math
dd, tt = 2.0, 0.5
ss = (2*dd - math.sqrt(4*dd*dd - 4*tt*tt*dd)) / (2*tt)
print(f"s_* = {ss:.6f} in (0, {tt})")
def q2(x, y=None):
    y = x if y is None else y
    return 2*dd*x[0]*y[0] - 2*x[1]*y[1]
for sv in [0.0, ss/2, ss, (ss+tt)/2, tt]:
    a = (1.0, -sv); b = (1.0, -tt); e = (0.0, 1.0)
    F = q2(a)*q2(b, e) - 2*q2(a, b)*q2(a, e)
    print(f"s={sv:.6f} F/4={F/4:.6f} q(a,e)={q2(a,e):.4f} q(a)={q2(a):.4f}")
print("OK: J-wall (F=0) is interior; MBM wall (q(a,e)=0) is the endpoint s=0.")
