#!/usr/bin/env python3
import sympy as sp

G,C,S,LAM = sp.symbols("gamma c s lambda", real=True)
I = sp.I
X = sp.Matrix([[0,1],[1,0]])
Y = sp.Matrix([[0,-I],[I,0]])
I2 = sp.eye(2)
K = sp.kronecker_product
XX = K(X,X)
YY = K(Y,Y)
U = (sp.eye(4)-I*XX)/sp.sqrt(2) * (C*sp.eye(4)-I*S*YY)
Ry = (I2-I*Y)/sp.sqrt(2)
ROT = K(Ry,I2)

def pt_b(m):
    out = sp.zeros(4)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    out[2*a+d,2*c+b] = m[2*a+b,2*c+d]
    return out

def mems_rank2():
    return sp.Matrix([
        [G/2,0,0,I*G/2],
        [0,1-G,0,0],
        [0,0,0,0],
        [-I*G/2,0,0,G/2],
    ])

def mems_rank3():
    return sp.Matrix([
        [sp.Rational(1,3),0,0,I*G/2],
        [0,sp.Rational(1,3),0,0],
        [0,0,0,0],
        [-I*G/2,0,0,sp.Rational(1,3)],
    ])

def charpoly_pt(rho):
    sigma = sp.simplify(U.conjugate().T * ROT * rho * ROT.conjugate().T * U)
    pt = pt_b(sigma)
    return sp.expand((LAM*sp.eye(4)-pt).det())

def remainder_mod_trig(expr):
    p = sp.Poly(sp.expand(expr), C, domain='EX')
    q = sp.Poly(C**2 + S**2 - 1, C, domain='EX')
    return sp.factor(sp.rem(p,q).as_expr())

cp2 = charpoly_pt(mems_rank2())
expected2 = sp.expand(LAM**2*(LAM-G)*(LAM-(1-G)))
assert remainder_mod_trig(cp2-expected2) == 0

cp3 = charpoly_pt(mems_rank3())
expected3 = sp.expand(
    LAM*(LAM-sp.Rational(1,3))
    *(LAM-(sp.Rational(1,3)-G/2))
    *(LAM-(sp.Rational(1,3)+G/2))
)
assert remainder_mod_trig(cp3-expected3) == 0

rho2 = mems_rank2()
rho3 = mems_rank3()
mu2 = sp.simplify(sp.trace(rho2*rho2))
mu3 = sp.simplify(sp.trace(rho3*rho3))
assert sp.simplify(mu2-(G**2+(1-G)**2)) == 0
assert sp.simplify(mu3-(sp.Rational(1,3)+G**2/2)) == 0
assert sp.simplify(mu2.subs(G,sp.Rational(2,3))-sp.Rational(5,9)) == 0
assert sp.simplify(mu3.subs(G,sp.Rational(2,3))-sp.Rational(5,9)) == 0

print("VERIFY_OK")
print("rank2_pt_spectrum = 0,0,1-gamma,gamma")
print("rank3_pt_spectrum = 0,1/3,1/3-gamma/2,1/3+gamma/2")
print("trig_relation = c^2+s^2-1")
print("purity_join = 5/9 at gamma=2/3")
