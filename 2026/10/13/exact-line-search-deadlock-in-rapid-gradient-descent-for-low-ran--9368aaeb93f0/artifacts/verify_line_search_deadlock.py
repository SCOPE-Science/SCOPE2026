from fractions import Fraction as F
import sympy as sp

# Exact rational witness rho=1/4.
rho=F(1,4)
u=F(289,576)
v=F(289,2304)
Gu=F(2023,13824)
Gv=-F(2023,55296)

assert u == (F(17,24))**2
assert v == (F(17,48))**2
assert Gu == u*F(17,48)-rho*v
assert Gv == v*F(17,24)-rho*u

R=u*v-rho
C=Gu*Gv
B=v*Gu+u*Gv
assert R == -F(248255,1327104)
assert B == 0
assert C < 0 and R < 0
assert R*C > 0

# F(alpha)-F(0) = R*C*alpha^2 + (C^2/2)*alpha^4 > 0 for alpha != 0.
for a in [F(-10),F(-1),F(-1,1000),F(1,1000),F(1),F(10)]:
    diff=R*C*a*a + F(1,2)*C*C*a**4
    assert diff > 0

# Symbolic parametric family.
r=sp.symbols('r', positive=True)
u_s=sp.Rational(289,36)*r**2
v_s=sp.Rational(289,144)*r**2
Gu_s=sp.Rational(2023,216)*r**3
Gv_s=-sp.Rational(2023,864)*r**3
assert sp.simplify(v_s*Gu_s+u_s*Gv_s)==0
assert sp.simplify(Gu_s*Gv_s + sp.Rational(4092529,186624)*r**6)==0
R_s=sp.simplify(u_s*v_s-r)
assert sp.simplify(R_s-r*(sp.Rational(83521,5184)*r**3-1))==0

print('VERIFY_OK')
