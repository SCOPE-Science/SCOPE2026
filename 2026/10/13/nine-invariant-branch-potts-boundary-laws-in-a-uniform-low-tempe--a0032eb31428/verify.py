#!/usr/bin/env python3
import math

def bisect(f,a,b,n=120):
    fa,fb=f(a),f(b)
    if fa==0: return a
    if fb==0: return b
    assert fa*fb<0,(a,b,fa,fb)
    for _ in range(n):
        m=(a+b)/2; fm=f(m)
        if fa*fm<=0: b,fb=m,fm
        else: a,fa=m,fm
    return (a+b)/2

def ftheta(x,th):
    ex=math.exp(x)
    return math.log((th*ex+2)/(th+ex+1))

def check(k,th):
    F=lambda t:t**(k+1)-th*t**k+(th+1)*t-2
    assert F(0)<0 and F(2/th)>0 and abs(F(1))<1e-12 and F(th/2)<0 and F(th)>0
    ts=[bisect(F,0,2/th),1.0,bisect(F,th/2,th)]
    total=0; worst=0.0
    for t in ts:
        H=lambda y:t*y**k-th*t*y**(k-1)+(th+1)*y-2
        if t<1-1e-9:
            pts=[(0,1),(1,th/2)]
            hi=th/2
            while H(hi)<=0: hi*=2
            pts.append((th/2,hi))
        elif t>1+1e-9:
            pts=[(0,3/th),(3/th,1)]
            hi=max(2.0,t*2)
            while H(hi)<=0: hi*=2
            pts.append((1,hi))
        else:
            pts=[(0,0.5),(0.5,2)]
            hi=2.0
            while H(hi)<=0: hi*=2
            pts.append((2,hi))
        ys=[bisect(H,a,b) for a,b in pts]
        assert len(ys)==3
        alpha=t**(1/(k-1))
        h=k*math.log(t)
        for y in ys:
            x=alpha*y
            l=(k-1)*math.log(x)
            r1=h-k*ftheta(h,th)
            r2=l-ftheta(h,th)-(k-1)*ftheta(l,th)
            worst=max(worst,abs(r1),abs(r2))
            total+=1
    assert total==9
    return worst

worst=0.0; cases=0
for k in [4,5,6,8,12]:
    for th in [25.0,30.0,50.0,100.0]:
        worst=max(worst,check(k,th)); cases+=1
print(f"VERIFY_OK cases={cases} solutions_per_case=9 worst_residual={worst:.3e}")
