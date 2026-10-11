"""Exact rational checks for a weighted fourth-power cycle identity."""
from fractions import Fraction as F
from math import cos, pi, sqrt, copysign
from itertools import product

def trial_norm(a, x):
    n=len(x)
    b=[(a[j-1]+a[j])/2 for j in range(n)]
    numer=sum(a[j]*(x[j]-x[(j+1)%n])**4 for j in range(n))
    denom=sum(b[j]*x[j]**4 for j in range(n))
    return numer/denom

def check():
    vals=[F(i,3) for i in range(-2,3)]
    for n in [3,4,5]:
        a=[F((j*j+2*j+3)%7+1,4) for j in range(n)]
        b=[(a[j-1]+a[j])/2 for j in range(n)]
        for x in product(vals,repeat=n):
            if not any(x):continue
            u=[(-1)**j*x[j] for j in range(n)]
            end=-u[0] if n%2 else u[0]
            uu=u+[end]
            defect=sum(a[j]*(8*(uu[j]**4+uu[j+1]**4)-(uu[j]+uu[j+1])**4) for j in range(n))
            assert defect==16*sum(b[j]*x[j]**4 for j in range(n))-sum(a[j]*(x[j]-x[(j+1)%n])**4 for j in range(n))
            assert defect>=0
            assert trial_norm(a,x)<=16
        if n%2==0:
            assert trial_norm(a,[(-1)**j for j in range(n)])==16
    for n in [11,51,201,501]:
        x=[]
        for j in range(n):
            w=sqrt(2)*cos(pi*j/n)
            x.append((-1)**j*copysign(sqrt(abs(w)),w))
        q=trial_norm([1.0]*n,x)
        assert 0<n*n*(16-q)<6*pi*pi+0.1
    print('WEIGHTED_CYCLE_CHECK_OK')
if __name__=='__main__':check()
