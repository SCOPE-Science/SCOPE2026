#!/usr/bin/env python3
"""Finite arithmetic spot checks for the stated deterministic cubic network identities."""
from fractions import Fraction as F

def step(v, gamma, a):
    n=len(v); c=F(n,n-1); m=sum(v)/n
    z=[x-m for x in v]
    return [x-gamma*c*u+gamma*a*(c*u)**3 for x,u in zip(v,z)]

def check_exact(v,gamma,a):
    n=len(v); c=F(n,n-1); lam=1-gamma*c; b=gamma*a*c**3
    m=sum(v)/n; z=[x-m for x in v]; s3=sum(x**3 for x in z)/n
    nxt=step(v,gamma,a); m1=sum(nxt)/n; z1=[x-m1 for x in nxt]
    assert m1==m+b*s3
    assert z1==[lam*x+b*(x**3-s3) for x in z]
    return b,lam

for n in range(2,8):
    for gamma in [F(1,3),F(2,3),F(1,1)]:
        if gamma>=F(2*(n-1),n):continue
        a=F(1,4)
        v=[F(j*j-3*j+2,29) for j in range(n)]
        check_exact(v,gamma,a)
for gamma in [F(1,3),F(2,3),F(1,1)]:
    assert sum(step([F(2,5),F(3,5)],gamma,F(1,4)))==F(1,1)

# Exact third-order coefficient in a three-agent witness.
n=3;c=F(3,2);a=F(1,4);gamma=F(1,1)
b=gamma*a*c**3; lam=1-gamma*c
assert (b*F(6,3)/(1-lam**3))==F(3,2)

# Finite trajectory comparison. A decreasing scaled remainder is corroborative,
# not a proof of the asymptotic expansion.
ratios=[]
for h in [0.1,0.05,0.025,0.0125]:
    zz=[2*h,-h,-h]; m=0.
    for t in range(1000):
        cubic=sum(q**3 for q in zz)/3
        m+=float(b)*cubic
        zz=[float(lam)*q+float(b)*(q**3-cubic) for q in zz]
    leading=1.5*h**3
    assert abs(m-leading)<4*h**5
    ratios.append(m/h**3)
assert all(ratios[k]>ratios[k+1] for k in range(len(ratios)-1))
assert abs(ratios[-1]-1.5)<0.001
print('VERIFY_OK: exact finite network identities, dimension-two cancellation and cubic consensus coefficient')
