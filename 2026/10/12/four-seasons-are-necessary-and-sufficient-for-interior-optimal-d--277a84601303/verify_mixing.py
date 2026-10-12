"""Exact rational checks supplementary to the period-three endpoint theorem.

Run with Python 3: python verify_mixing.py
The analytic inequalities in RESULT.md, rather than these finite tests,
prove the universal one-to-three-period statement.
"""
from fractions import Fraction as F
from itertools import product


def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in (0,1)) for j in (0,1)) for i in (0,1))


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def trace(a):
    return a[0][0]+a[1][1]


def period(fitness,d):
    half=F(d,2)
    M=((1-half,half),(half,1-half))
    P=((F(1),F(0)),(F(0),F(1)))
    for a,b in fitness:
        G=((F(a),F(0)),(F(0),F(b)))
        P=mul(mul(M,G),P)
    return P


n=0
rr=(F(-3,4),F(-1,2),F(0),F(1,3),F(2,3))
xx=(F(0),F(1,7),F(1,2),F(4,5),F(1))
for k in (2,3):
    for rs in product(rr,repeat=k):
        fitness=tuple((1+r,1-r) for r in rs)
        Q=F(1)
        for r in rs: Q*=1-r*r
        if k==2:S=rs[0]*rs[1]
        else:S=rs[0]*rs[1]+rs[1]*rs[2]+rs[2]*rs[0]
        for x in xx:
            p=period(fitness,1-x)
            assert trace(p)==(1+2*S*x+x*x if k==2 else 1+S*(x+x*x)+x**3)
            assert det(p)==Q*x**k
            # The endpoint comparison may be tested without computing square roots:
            # If the larger endpoint eigenvalue is <= 1, chi_x(1)>=0;
            # else if larger endpoint eigenvalue >= 1, chi_x(L)>=0.
            A=F(1)
            B=F(1)
            for r in rs:A*=1+r; B*=1-r
            L=max(A,B)
            z=max(F(1),L)
            assert z*z-trace(p)*z+det(p)>=0
            n+=1
witness=((1,2),(1,3),(5,1),(6,1))
p=period(witness,F(24,25))
assert p==((F(4161198,390625),F(8647704,390625)),
           (F(3926052,390625),F(8159046,390625)))
assert trace(p)==F(12320244,390625)
assert det(p)==F(36,78125)
chi=F(63,2)**2-F(63,2)*trace(p)+det(p)
assert chi==-F(1959399,1562500),chi
assert trace(period(witness,F(0)))==F(36)
assert trace(period(witness,F(1)))==F(63,2)
assert max(F(1*1*5*6),F(2*3*1*1))==F(30)
assert F(3,2)*F(2)*F(3)*F(7,2)==F(63,2)
print(f'VERIFY_OK exact_traces_determinants_endpoint_characteristic={n} witness_negative_polynomial=1')
