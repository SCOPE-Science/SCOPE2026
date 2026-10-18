"""Standalone numerical and exact-arithmetic checks for two-sided moment-ratio envelopes."""
from fractions import Fraction as F
from math import comb
from random import Random
from scipy.optimize import linprog
import numpy as np

def moments(ps,xs,h):
    return sum(p*x**h for p,x in zip(ps,xs))

def extremal(a,b,m,v):
    c=m-v/(b-m); d=m+v/(m-a)
    p_plus=(m-c)/(b-c)
    p_minus=(m-a)/(d-a)
    return (c,b,p_plus),(a,d,p_minus)

def quotient_poly(h,lam,roots):
    # quotient of x^(h+1)-lam*x^h by monic cubic polynomial with roots provided
    s1=sum(roots); s2=sum(roots[i]*roots[j] for i in range(3) for j in range(i+1,3)); s3=roots[0]*roots[1]*roots[2]
    # Polynomial exact divide, ascending order
    p=[F(0)]*(h+2);p[h+1]=F(1);p[h]=-lam
    g=[-s3,s2,-s1,F(1)]; rem=list(p); q=[F(0)]*(h-1)
    for k in range(h-2,-1,-1):
        coef=rem[k+3];q[k]=coef
        for j in range(4):rem[k+j]-=coef*g[j]
    assert all(t==0 for t in rem[3:])
    return q,rem[:3]

rng=Random(2214)
count=0
for j in range(500):
    a=F(rng.randint(1,7),rng.randint(2,9)); b=a+F(rng.randint(2,10),rng.randint(1,4))
    xs=[a+(b-a)*F(k,6) for k in range(7)]
    ps=[F(rng.randint(1,7)) for _ in xs]; ps=[x/sum(ps) for x in ps]
    m=moments(ps,xs,1);v=moments(ps,xs,2)-m*m
    if v==0:continue
    (c,B,pplus),(A,d,pminus)=extremal(a,b,m,v)
    assert a<=c<m<d<=b
    for h in range(1,10):
        u=moments(ps,xs,h+1)/moments(ps,xs,h)
        up=((1-pplus)*c**(h+1)+pplus*b**(h+1))/((1-pplus)*c**h+pplus*b**h)
        low=((1-pminus)*a**(h+1)+pminus*d**(h+1))/((1-pminus)*a**h+pminus*d**h)
        assert low<=u<=up, (a,b,m,v,h,low,u,up)
        if h>=2:
            for roots,lam in (([b,c,c],up),([a,d,d],low)):
                q,rem=quotient_poly(h,lam,roots)
                assert all(z>=0 for z in q), (roots,lam,q)
        count+=1
print('PASS',count,'exact rational finite moment inequalities and polynomial quotient certificates')
# Independent finite grid linear-fractional programming: optimize ratio via bisection feasibility
for trial in range(24):
    a=1.;b=2.+trial/5.; m=a+(b-a)*(0.18+0.02*(trial%12)); vmax=(m-a)*(b-m); v=vmax*(0.1+0.07*(trial%12))
    if v>vmax:v=vmax*0.9
    (c,_,pplus),(_,d,pminus)=extremal(a,b,m,v)
    xs=np.linspace(a,b,1001); Aeq=np.array([np.ones_like(xs),xs,xs*xs]); beq=np.array([1,m,m*m+v]);
    for h in [2,3,4,7,12]:
        lo=((1-pminus)*a**(h+1)+pminus*d**(h+1))/((1-pminus)*a**h+pminus*d**h)
        hi=((1-pplus)*c**(h+1)+pplus*b**(h+1))/((1-pplus)*c**h+pplus*b**h)
        # positive objective for violations of either exact ratio bound
        for cvec in [xs**h*(xs-hi),xs**h*(lo-xs)]:
            r=linprog(-cvec,A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs')
            assert r.success and -r.fun<2e-6*max(1,np.max(abs(cvec))), (trial,h,-r.fun)
print('PASS 240 numerical extremality feasibility tests')
