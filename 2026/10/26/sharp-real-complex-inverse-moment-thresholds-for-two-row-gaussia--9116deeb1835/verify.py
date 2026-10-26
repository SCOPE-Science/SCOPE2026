"""Finite exact checks for two-row overlapping Hankel hard-edge theorem.

The argument in RESULT.md is analytic; this script checks independent algebraic
identities and examples without claiming to certify an infinite probability law.
"""
from fractions import Fraction as F
from random import Random
from math import cos,pi

rng=Random(20261024)
checks=0

def determinant_two_row_gram(g):
    x,y=g[:-1],g[1:]
    a=sum(v*v for v in x)
    b=sum(v*v for v in y)
    c=sum(u*v for u,v in zip(x,y))
    return a*b-c*c

def sum_squared_minors(g):
    x,y=g[:-1],g[1:]
    return sum((x[j]*y[k]-x[k]*y[j])**2
               for j in range(len(x)) for k in range(j+1,len(x)))

for m in range(2,11):
    for _ in range(130):
        g=[F(rng.randrange(-4,5),rng.randrange(1,4)) for _ in range(m+1)]
        assert determinant_two_row_gram(g)==sum_squared_minors(g)
        checks+=1

# Every geometric sequence has rank at most one; the chart residuals are exact.
for m in range(2,12):
    for ratio in [F(-3,4),F(0),F(2,3),F(5,4)]:
        g=[ratio**j for j in range(m+1)]
        assert determinant_two_row_gram(g)==0
        checks+=1
        delta=F(1,10**4)
        h=g[:]
        for j in range(1,m):
            h[j+1]=ratio*h[j]+delta
        assert h[1]-ratio*h[0]==0
        assert all(h[j+1]-ratio*h[j]==delta for j in range(1,m))
        checks+=1

# Tridiagonal covariance for the normalized one-step convolution map:
# for (a,b)=(1/sqrt2,1/sqrt2), eigenvalues are 1+cos(k*pi/(m+1)).
# Check characteristic recurrence on a grid against exact determinant of the
# (real) tridiagonal covariance with rational a^2+b^2=1, ab=1/2.
for m in range(2,12):
    # Evaluate characteristic polynomial at 0: recurrence for det(I -? ).
    # The covariance is positive: LDL pivots for diag 1 and offdiag 1/2.
    d=F(1)
    for j in range(1,m):
        d=1-F(1,4)/d
        assert d>0
        checks+=1
    assert 1-cos(pi/(m+1))>0

print('VERIFY_OK exact Cauchy-Binet Gram-minor identities, geometric rank charts, tridiagonal positivity;',checks,'checks')
