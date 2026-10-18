"""Finite numerical and exact-rational checks for the equilateral-triangle
log-cosh transition-level theorem. The infinite angular extremum proof
is analytical and not replaced by this checker.
"""
from fractions import Fraction
import math


def lc(z):
    q = abs(z)
    return q + math.log1p(math.exp(-2*q)) - math.log(2)


def angular(t, theta):
    return sum(lc(t*math.cos(theta-2*math.pi*j/3)) for j in range(3))


def fmax(t):
    return lc(t) + 2*lc(t/2)


def fmin(t):
    return 2*lc(math.sqrt(3)*t/2)


def bisection(c):
    lo, hi = 0.0, c+5.0
    for _ in range(75):
        mid = (lo+hi)/2
        if fmax(mid)>c:hi=mid
        else:lo=mid
    return (lo+hi)/2


def inverse_lc(c):
    return c+math.log1p(math.sqrt(-math.expm1(-2*c)))


def check():
    A=Fraction(3,4)
    # Newton recurrence for three normals: P_k=A*P_(k-2)+B*P_(k-3).
    for B in [Fraction(0),Fraction(1,8),Fraction(1,4),Fraction(-1,4)]:
        P=[Fraction(3),Fraction(0),2*A]
        for m in range(3,11):P.append(A*P[m-2]+B*P[m-3])
        assert P[2]==Fraction(3,2)
        assert P[4]==2*A*A
        assert P[6]==2*A**3+3*B**2
    total=0
    greatest=0.0
    for t in (0.1,0.25,0.5,0.9,1.5,2.5,4,8,15):
        l,r=fmin(t),fmax(t)
        assert r>l
        for j in range(1801):
            theta=(math.pi/6)*j/1800
            val=angular(t,theta)
            excess=max(0.0,l-val,val-r)
            greatest=max(greatest,excess)
            assert excess<4e-11
            total+=1
    for c in [0.0001,0.01,0.1,0.5,1,3,10,30,100]:
        a=bisection(c)
        b=(2/math.sqrt(3))*inverse_lc(c/2)
        assert abs(fmax(a)-c)<2e-12
        assert abs(fmin(b)-c)<2e-12
        assert 1<b/a<2/math.sqrt(3)
    print('PASS',total,'angle samples, exact recurrence identities, radius inversions; maximum excess',greatest)
    print('Small-c coefficient:',Fraction(2,405),'; limiting ratio:',2/math.sqrt(3))

if __name__=='__main__':check()
