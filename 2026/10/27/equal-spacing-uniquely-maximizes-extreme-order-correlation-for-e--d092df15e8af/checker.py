#!/usr/bin/env python3
"""Exact arithmetic spot checks of the stated probability theorem."""
from fractions import Fraction as Q
from itertools import product

def analytic(n,t):
    a,b=Q(1,3)**n,Q(2,3)**n
    A,B,C,D,F=b*(1-b),a*(1-a),a*(1-b),a*b,(a-b)**2-a
    vu=A*t*t+B*(1-t)**2+2*C*t*(1-t)
    vv=B*t*t+A*(1-t)**2+2*C*t*(1-t)
    cov=D+F*t*(1-t)
    return vu,vv,cov

def brute(n,t):
    vals=[Q(0),t,Q(1)]
    m=n*n*0+3**n
    sumu=sumv=sumuu=sumvv=sumuv=Q(0)
    for xx in product(vals,repeat=n):
        u,v=min(xx),max(xx)
        sumu+=u; sumv+=v;sumuu+=u*u;sumvv+=v*v;sumuv+=u*v
    eu,ev=sumu/m,sumv/m
    return sumuu/m-eu*eu,sumvv/m-ev*ev,sumuv/m-eu*ev

tests=0
for n in range(2,8):
    for t in (Q(1,5),Q(1,2),Q(5,7)):
        assert analytic(n,t)==brute(n,t)
        tests+=1
for n in range(2,71):
    a,b=Q(1,3)**n,Q(2,3)**n
    A,B,D,F=b*(1-b),a*(1-a),a*b,(a-b)**2-a
    L=2*a*(a-b)*(b-1)*(a-b-1)
    K=(a-b)**2*(a-b+1)**2
    h0=2*F*A*B-D*L
    h1=F*L-2*D*K
    assert F>=0 and h0>0 and h0+h1/4>0
    assert h0==2*a*b*(1-b)*(a*a-a*b-a+b*b)
    rhs=a*Q(1,2)*(2*b**3*(1-b)-a*b*(1-b)*(3-2*b)-a*a*b*(1-b)-a*a*(1-a)**2)
    assert h0+h1/4==rhs
    predicted=((a+b)**2-a)/(b+3*a-(a+b)**2)
    v1,v2,cov=analytic(n,Q(1,2))
    assert v1==v2 and cov/v1==predicted
    for t in (Q(1,8),Q(1,4),Q(2,5),Q(1,2),Q(3,5),Q(3,4)):
        vu,vv,c=analytic(n,t)
        w=t*(1-t)
        assert vu*vv==A*B+L*w+K*w*w
        assert c*c <= predicted*predicted*vu*vv
        tests+=2
    tests+=5
assert analytic(2,Q(1,2))[2]/analytic(2,Q(1,2))[0]==Q(8,19)
assert analytic(3,Q(1,2))[2]/analytic(3,Q(1,2))[0]==Q(1,4)
tests+=2
print('PASS:',tests,'exact-rational assertions')
