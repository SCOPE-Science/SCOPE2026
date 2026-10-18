#!/usr/bin/env python3
"""Reproducible finite checks of an analytic ecological chain theorem.
Requires Python 3 standard library only. These checks are not the proof.
"""
from fractions import Fraction as F
from math import log

def rhs(x,r,delta,p):
    s=sum(x)
    return [x[i]*(r[i]*(1-delta-s) -(p[i-1]*x[i-1] if i else 0.0)) for i in range(len(x))]

def rk4(x0,r,delta,p,dt,steps):
    x=list(map(float,x0)); n=len(x)
    for _ in range(steps):
        a=rhs(x,r,delta,p)
        b=rhs([v+dt*t/2 for v,t in zip(x,a)],r,delta,p)
        c=rhs([v+dt*t/2 for v,t in zip(x,b)],r,delta,p)
        d=rhs([v+dt*t for v,t in zip(x,c)],r,delta,p)
        x=[max(0.,v+dt*(u+2*w+2*z+t)/6) for v,u,w,z,t in zip(x,a,b,c,d)]
    return x

def groups(x):
    out=[]; i=0
    while i<len(x):
        if x[i]==0: i+=1;continue
        a=i
        while i+1<len(x) and x[i+1]>0: i+=1
        out.extend(range(a,i+1,2))
        i+=1
    return out

def check_exact():
    count=0
    for n in range(2,9):
        for k in range(1,16):
            r=[F(2+((i+k)%5),1+((3*i+k)%4)) for i in range(n)]
            p=[F(1+((i+2*k)%7),3+((2*i+k)%5)) for i in range(n-1)]
            delta=F(1+((k+1)%3),7)
            x=[F((i+1)*(k%5+1),100*n) for i in range(n)]
            s=sum(x)
            f=[x[i]*(r[i]*(1-delta-s)-(p[i-1]*x[i-1] if i else 0)) for i in range(n)]
            W=sum(a*b for a,b in zip(r,x))
            G=sum(p[i]*x[i]*x[i+1] for i in range(n-1))
            assert sum(f)==(1-delta-s)*W-G
            for i in range(1,n):
                assert f[i]/(r[i]*x[i])-f[0]/(r[0]*x[0])==-p[i-1]*x[i-1]/r[i]
                count+=1
    return count

def main():
    count=check_exact()
    cases=[
      ([.15,.05,.12,.05,.1],[2,2.1,2.2,2.3,2.4],1/3,[4,5,3,4]),
      ([0,.12,.07,0,.04,.09],[5,4,3,2,7,2],.25,[1,1.5,.7,1.3,.6]),
      ([.13,.05,.11,.04,.1,.04,.09],[2.1,2.2,1.9,2.3,2.2,2.,2.1],.43,[3.,4.,3.,4.,3.,4.]),
      ([.15,.10,.08,.07],[1.,1.,1.,1.],.4,[2.,3.,4.]),
    ]
    for x0,r,delta,p in cases:
        x=rk4(x0,r,delta,p,0.02,50000)
        keep=set(groups(x0))
        for i,xi in enumerate(x):
            if i in keep: assert xi>1e-4,(i,x,keep)
            else: assert xi<5e-5,(i,x,keep)
        assert abs(sum(x)-(1-delta))<1e-5,(sum(x),1-delta)
        print('run',len(x0),'initial support', [i+1 for i,v in enumerate(x0) if v>0], 'survivors',[i+1 for i in keep], 'limit',[round(v,10) for v in x])
    print(f'VERIFY_OK: {count} exact rational per-capita/total-derivative identities; {len(cases)} independently integrated ecological chains with heterogeneous vital rates and arbitrary initial support')
if __name__=='__main__': main()
