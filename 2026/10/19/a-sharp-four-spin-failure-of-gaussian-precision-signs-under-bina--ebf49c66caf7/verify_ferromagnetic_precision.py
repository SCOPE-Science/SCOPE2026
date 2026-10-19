#!/usr/bin/env python3
"""Exact-rational verification for a four-spin ferromagnetic precision sign law."""
from fractions import Fraction as F
from itertools import product
from sympy import Matrix, Rational, symbols, factor

def distribution(a,b,u,v,r,s,t):
    states=list(product((0,1),repeat=4))
    weights=[a**x*b**y*u**z*v**w*r**(x*(z+w))*s**(y*(z+w))*t**(z*w)
             for x,y,z,w in states]
    total=sum(weights)
    return {state:wgt/total for state,wgt in zip(states,weights)}

def covariance(law):
    mean=[sum(p*s[i] for s,p in law.items()) for i in range(4)]
    return Matrix(4,4,lambda i,j:sum(p*s[i]*s[j] for s,p in law.items())-mean[i]*mean[j])

def delta(a,r):
    return a*r*r/(1+a*r*r)-2*a*r/(1+a*r)+a/(1+a)

def check(a,b,u,v,r,s,t):
    law=distribution(a,b,u,v,r,s,t)
    assert all(p>0 for p in law.values())
    for i,j in product(range(4),repeat=2):
        if i>=j:continue
        for rest in product((0,1),repeat=2):
            other=[k for k in range(4) if k not in (i,j)]
            def pr(x,y):
                q=[0]*4
                q[i],q[j]=x,y
                for kk,c in zip(other,rest):q[kk]=c
                return law[tuple(q)]
            assert pr(0,0)*pr(1,1)>=pr(0,1)*pr(1,0)
    C=covariance(law)
    assert C.det()>0
    prec=C.inv()
    marginal={(z,w):sum(p for (x,y,zz,ww),p in law.items() if zz==z and ww==w)
              for z,w in product((0,1),repeat=2)}
    varH=1/sum(1/p for p in marginal.values())
    B=C[:2,:2]-C[:2,2:]*C[2:,2:].inv()*C[2:,:2]
    assert B.det()>0
    assert B[0,1]==delta(a,r)*delta(b,s)*varH
    assert prec[0,1]==-B[0,1]/B.det()
    if r>1 and s>1:
        target=(a*r-1)*(b*s-1)
        assert (prec[0,1]>0)==(target<0)
        assert (prec[0,1]==0)==(target==0)
        assert (prec[0,1]<0)==(target>0)
    return prec[0,1]

if __name__=='__main__':
    a,r=symbols('a r',positive=True)
    assert factor(delta(a,r))==-a*(r-1)**2*(a*r-1)/((a+1)*(a*r+1)*(a*r*r+1))
    witness=(F(1,8),F(2),F(1),F(1),F(2),F(2),F(1))
    assert check(*witness)==F(235,60966)
    n=0
    for aa,bb,rr,ss in product((F(1,8),F(1,2),F(2)),(F(1,8),F(1,2),F(2)),(F(2),F(3)),(F(2),F(3))):
        n+=1
        check(aa,bb,F(2),F(1,3),rr,ss,F(3,2))
    print('PASS: symbolic curvature factorization; exact 4-spin witness 235/60966; 36 rational model sign and MTP2 checks.')
