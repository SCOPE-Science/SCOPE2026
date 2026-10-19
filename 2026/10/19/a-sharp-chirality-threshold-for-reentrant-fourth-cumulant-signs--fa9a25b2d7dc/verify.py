#!/usr/bin/env python3
"""Exact checks for the two-reversal radial fourth-cumulant theorem.

Requires Python 3 and SymPy. All assertions are reproducible without external data.
"""
from itertools import permutations
import sympy as sp

r, u, x = sp.symbols('r u x', positive=True)
P = (80*r**4 + (28*x+560)*r**3 + (96*x+1360)*r**2
     + (-4*x**2+72*x+1360)*r + x**2+4*x+480)
B = 28*r**3+96*r**2+72*r+4
C = 80*r**4+560*r**3+1360*r**2+1360*r+480
D = (3*r+x+9)*(4*r+x+4)**2*(8*r+x+16)
M2 = 2*(r+1)/(4*r+x+4)
M4 = (28*r**3+(8*x+168)*r**2+(20*x+308)*r+7*x+168)/(
    (3*r+x+9)*(4*r+x+4)*(8*r+x+16))
CHECKS = 0

def check(v):
    global CHECKS
    assert v
    CHECKS += 1


def moments_generator():
    """Triangular stationary generator hierarchy, symbolically in r and u."""
    F = {(0, 0): (sp.Rational(1, 2), sp.Rational(1, 2))}
    for n in range(1, 5):
        for p in range(n+1):
            q = n-p
            h = q-p
            v0 = p*F[p-1, q][0] if p else 0
            v1 = p*F[p-1, q][1] if p else 0
            if q:
                v0 += q*F[p, q-1][0]
                v1 += q*F[p, q-1][1]
            a = n+h*h+r
            t = h*u
            det = sp.expand(a*a+t*t-r*r)
            F[p, q] = (
                sp.cancel(((a+sp.I*t)*v0+r*v1)/det),
                sp.cancel((r*v0+(a-sp.I*t)*v1)/det))
    return sp.factor(sum(F[1, 1])), sp.factor(sum(F[2, 2]))


def moments_ordered_integral(p, q, rr, uu):
    """Independent ordered-time integral via Fourier-semigroup resolvents.

    Labeled factors are integrated over the 4! orderings of their past ages;
    one inverse matrix per time gap integrates the angle-switching correlation.
    """
    n = p+q
    charges = (1,)*p + (-1,)*q
    pi = sp.Matrix([[sp.Rational(1, 2),sp.Rational(1, 2)]])
    ones = sp.ones(2, 1)
    acc = 0
    for ordering in permutations(charges):
        product = sp.eye(2)
        for j in range(1, n):
            h = sum(ordering[:n-j])
            G = sp.Matrix([[-rr+sp.I*h*uu-h*h,rr],
                           [rr,-rr-sp.I*h*uu-h*h]])
            product *= (j*sp.eye(2)-G).inv()
        acc += (pi*product*ones)[0]/n
    return sp.simplify(acc)


def main():
    a, b = moments_generator()
    check(sp.factor(a-M2.subs(x,u*u))==0)
    check(sp.factor(b-M4.subs(x,u*u))==0)
    check(sp.factor(b-2*a*a+P.subs(x,u*u)/D.subs(x,u*u))==0)

    # A nontrivial independently derived matrix-integral representation.
    for rr, uu in [(sp.Integer(1), sp.Integer(10)),
                   (sp.Rational(3,4), sp.Integer(9)),
                   (sp.Integer(1), sp.Integer(4))]:
        aa = moments_ordered_integral(1,1,rr,uu)
        bb = moments_ordered_integral(2,2,rr,uu)
        check(aa == sp.factor(M2.subs({r:rr,x:uu**2})))
        check(bb == sp.factor(M4.subs({r:rr,x:uu**2})))
        check(sp.factor(bb-2*aa**2 + P.subs({r:rr,x:uu**2})/D.subs({r:rr,x:uu**2}))==0)

    # Sharp onset arguments have exact polynomial sign witnesses.
    check(sp.expand(P-((1-4*r)*x*x+B*x+C)) == 0)
    check(sp.expand(sp.diff(P,r,2) - (960*r*r+6*(28*x+560)*r+2*(96*x+1360))) == 0)
    check(P.subs({r:sp.Rational(3,4),x:81}) == -sp.Rational(4533,8))
    check(P.subs({r:1,x:100}) == -6160)
    q8 = 7504*r*r-10416*r+4832
    check(sp.expand(P.subs(x,64) - (80*r**4+2352*r**3+q8))==0)
    check(10416**2 -4*7504*4832 == -36544256)
    check(P.subs({r:0,x:100})>0)
    check(P.subs({r:sp.Rational(1,4),x:100})>0)
    for rr in [sp.Rational(2,5),sp.Rational(1,2),sp.Rational(7,5),sp.Rational(8,5)]:
        check(P.subs({r:rr,x:100}) != 0)
    check(P.subs({r:sp.Rational(2,5),x:100})>0)
    check(P.subs({r:sp.Rational(1,2),x:100})<0)
    check(P.subs({r:sp.Rational(7,5),x:100})<0)
    check(P.subs({r:sp.Rational(8,5),x:100})>0)

    # High-chirality scaling: small root approaches 1/4; large root is ~ u/sqrt(7).
    check(sp.expand(P).coeff(x,2)==1-4*r)
    check(sp.expand(P).coeff(x,1)==B)
    check(sp.limit(P.subs({r:sp.Rational(1,4)+sp.Symbol('c')/x})/x,x,sp.oo)==sp.Rational(455,16)-4*sp.Symbol('c'))
    y,t=sp.symbols('y t',positive=True)
    check(sp.limit((P.subs({r:y/t,x:1/t**2})*t**5),t,0)==28*y**3-4*y)

    # Exact positive radial fourth cumulant in a fully specified parameter case.
    rr, uu = sp.Integer(1),sp.Integer(10)
    kv = sp.factor(-P.subs({r:rr,x:uu**2})/D.subs({r:rr,x:uu**2}))
    check(kv == sp.Rational(55,1446336))
    check(moments_ordered_integral(2,2,rr,uu)-2*moments_ordered_integral(1,1,rr,uu)**2 == kv)
    print('PASS: %d exact symbolic/rational assertions; generator, independent ordered-time integrals, onset and asymptotics.'%CHECKS)

if __name__=='__main__':
    main()
