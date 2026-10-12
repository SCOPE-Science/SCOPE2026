#!/usr/bin/env python3
"""Exact checks for all-size SAGA mean-square stability law.

Requires Python 3 and sympy (tested 1.13.1).
This checker confirms universal polynomial identities and independently
enumerates all sampled updates for selected exact rational cases.
Mathematical proof of positive definiteness and convergence is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
import sympy as S

def symbolic_checks():
    n, s = S.symbols('n s', nonzero=True)
    Q = n + (n-1)**2*s
    K = 1+(n-1)*s
    P = (2*n*n-3*n+1)*s*s + (-2*n*n+5*n-2)*s-2*n
    M = S.Matrix([
        [(1-s)**2, 0, 0, s*s],
        [(1-s)/n, (1-s)*(n-1)/n, 0, -s/n],
        [1/n**2, 2*(n-1)/n**2, (n-1)**2/n**2, 1/n**2],
        [(n-1)/n**2, -2*(n-1)/n**2, (n-1)/n**2, (n*n-n-1)/n**2]
    ])
    w = S.Matrix([Q,-n*(n-1)*s*s,
                  n*(n-1)*s*s*K/2,
                  n*(2*n-1)*s*s*K/2])
    r = (M.T-S.eye(4))*w
    assert all(S.factor(r[j]) == 0 for j in range(1,4))
    assert S.factor(r[0]-s*P)==0
    assert S.factor(2*Q*K-n*(n-1)*s*s-(2*n+2*(n-1)*(2*n-1)*s+(n-1)*(2*n-1)*(n-2)*s*s))==0
    assert S.factor((S.eye(4)-M).det()+2*s*P/n**4)==0
    assert S.factor(P.subs(s,1)+1)==0
    assert S.factor(P.subs(s,2)-4*n*(n-1))==0
    assert S.factor(P.subs(n,n+1)-P-(s-1)*((4*n-1)*s+2))==0

def direct_enumeration():
    cases=0
    for n in (2,3,4,5,7):
        for s in (F(1,10),F(1,2),F(1),F(11,10),F(6,5),F(7,4)):
            for x in (F(-2),F(0),F(3,2)):
                for t in (-1,0,2):
                    y=[F(((j*7 + t*3)%11)-5,3) for j in range(n)]
                    m=sum(y)/n
                    v=sum((yi-m)**2 for yi in y)/n
                    Q=n+(n-1)**2*s
                    K=1+(n-1)*s
                    P=(2*n*n-3*n+1)*s*s +(-2*n*n+5*n-2)*s-2*n
                    def V(a,ys):
                        mm=sum(ys)/n
                        vv=sum((yi-mm)**2 for yi in ys)/n
                        return (Q*a*a-n*(n-1)*s*s*a*mm
                                +F(n*(n-1),2)*s*s*K*mm*mm
                                +F(n*(2*n-1),2)*s*s*K*vv)
                    old=V(x,y)
                    new=F(0)
                    for idx in range(n):
                        xx=(1-s)*x+s*(y[idx]-m)
                        yy=list(y); yy[idx]=x
                        new+=V(xx,yy)/n
                    assert new-old == s*P*x*x, (n,s,x,t,new-old,s*P*x*x)
                    cases+=1
    return cases

if __name__=='__main__':
    symbolic_checks()
    cases=direct_enumeration()
    print('VERIFY_OK symbolic_general_n_s=PASS exact_enumerations='+str(cases))
