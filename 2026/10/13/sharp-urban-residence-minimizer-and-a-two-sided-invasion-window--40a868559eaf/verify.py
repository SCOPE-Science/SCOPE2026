"""Exact-arithmetic checks for a four-compartment host-vector invasion theorem."""
from fractions import Fraction as Q
from math import isclose, sqrt
from random import Random


def polynomial(y, x, A, B, C):
    return y*y-y*(A*x*x+B*(1-x)*(1-x)+C)+A*C*x*x


def quadratic_roots(x, A, B, C):
    s=A*x*x+B*(1-x)*(1-x)+C
    disc=s*s-4*A*C*x*x
    return (float(s)+sqrt(float(disc)))/2, (float(s)-sqrt(float(disc)))/2


def optimum(A, B, C, x0):
    return Q(1) if A <= C else max(x0, (B+C)/(A+B))


def verify_exact():
    A, B, C = Q(12, 5), Q(3, 5), Q(3, 5)
    k, NA, NH = Q(1), Q(1), Q(4)
    x0=k*NA/(k*NA+NH)
    xstar=(B+C)/(A+B)
    pstar=Q(1)-(k*NA/NH)*(1-xstar)/xstar
    assert x0 == Q(1,5) and xstar == Q(2,5)
    assert pstar == Q(5,8)
    ystar=A*(B+C)/(A+B)
    assert ystar == Q(24,25)
    assert polynomial(ystar,xstar,A,B,C)==0
    assert polynomial(Q(1),x0,A,B,C)==Q(-14,625)
    assert polynomial(Q(1),Q(1),A,B,C) == (Q(1)-A)*(Q(1)-C)
    # The exact threshold polynomial after x(p)=1/(5-4p).
    for p in [Q(0),Q(1,8),Q(1,4),Q(1,2),Q(5,8),Q(3,4),Q(7,8),Q(1)]:
        xp=1/(5-4*p)
        expected=(6-80*(p-Q(1,2))**2)/(25*(5-4*p)**2)
        assert polynomial(Q(1),xp,A,B,C)==expected
        y,lower=quadratic_roots(xp,A,B,C)
        assert lower < float(C)+1e-10
        assert (y < 1) == (expected > 0), (p,y,expected)
    for x in [Q(1,5),Q(2,5),Q(3,5),Q(1)]:
        root, lower = quadratic_roots(x,A,B,C)
        assert root >= lower >= -1e-12
        assert abs(float(polynomial(Q(str(root)),x,A,B,C))) < 1e-8
    assert quadratic_roots(x0,A,B,C)[0] > 1
    assert isclose(quadratic_roots(xstar,A,B,C)[0], Q(24,25), abs_tol=1e-12)
    assert quadratic_roots(Q(1),A,B,C)[0] > 1


def verify_general_samples():
    rng=Random(925076)
    for _ in range(1200):
        A=Q(rng.randint(1,60),rng.randint(1,18))
        B=Q(rng.randint(1,60),rng.randint(1,18))
        C=Q(rng.randint(1,60),rng.randint(1,18))
        x0=Q(rng.randint(1,10),rng.randint(11,25))
        candidate=optimum(A,B,C,x0)
        val=quadratic_roots(candidate,A,B,C)[0]
        for j in range(81):
            x=x0+(1-x0)*Q(j,80)
            y=quadratic_roots(x,A,B,C)[0]
            assert y+1e-9>=val, (A,B,C,x0,candidate,x,y,val)
        if A>C and x0< (B+C)/(A+B):
            assert candidate == (B+C)/(A+B)
            assert abs(val-float(A*(B+C)/(A+B)))<1e-9


if __name__ == '__main__':
    verify_exact()
    verify_general_samples()
    print('VERIFY_OK')
