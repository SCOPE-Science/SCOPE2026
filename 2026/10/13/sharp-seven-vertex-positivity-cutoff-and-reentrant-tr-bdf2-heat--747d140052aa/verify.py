#!/usr/bin/env python3
"""Standalone exact polynomial certificates and finite numerical checks for a TR-BDF2 cycle positivity theorem."""
from fractions import Fraction as F
from math import comb, cos, pi, sqrt, sinh, acosh


def add(p, q):
    z=[F(0)]*max(len(p),len(q))
    for i,v in enumerate(p): z[i]+=v
    for i,v in enumerate(q): z[i]+=v
    return z

def mul(p,q):
    z=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): z[i+j]+=a*b
    return z

def scale(p,a): return [a*v for v in p]

def U_poly(m):
    if m==0: return [F(1)]
    a,b=[F(1)],[F(0),F(2)]
    if m==1: return b
    for _ in range(2,m+1):
        a,b=b,add(mul([F(0),F(2)],b),scale(a,-1))
    return b

def compose_affine(p,lo,hi):
    out=[F(0)]
    for ai in reversed(p):
        out=add(mul(out,[lo,hi-lo]),[ai])
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def bernstein_coefficients(poly,lo,hi):
    a=compose_affine(poly,lo,hi)
    N=len(a)-1
    return [sum((a[j]*F(comb(k,j),comb(N,j)) for j in range(k+1)),F(0)) for k in range(N+1)]

s_up=F(283,200)
assert s_up*s_up>2
u6=U_poly(6)
assert u6==[F(-1),F(0),F(24),F(0),F(-80),F(0),F(64)]
p7=add(mul([-s_up,F(1)],u6),[7*(1+s_up)])
segments=[(F(1),F(6,5)),(F(6,5),F(13,10)),(F(13,10),s_up)]
mins=[]
for lo,hi in segments:
    coeff=bernstein_coefficients(p7,lo,hi)
    assert len(coeff)==8 and all(v>2 for v in coeff)
    mins.append(min(coeff))
assert mins==[F(1667336,390625),F(165684017,65625000),F(4853759,1562500)]
# The n=8 negative witness at q=1/2, c=5/4; sqrt(2)>7/5.
witness_upper=F(5,4)-F(7,5)+(1+F(7,5))*F(3072,65535)
assert witness_upper==F(-16383,436900)<0
# 2nd-order consistency of stability function (1+alpha*z)/(1-beta*z)^2.
S=sqrt(2.0);alpha=S-1;beta=1-S/2
assert abs(alpha+2*beta-1)<1e-14
assert abs(2*alpha*beta+3*beta**2-0.5)<1e-14


def U_numeric(m,c):
    if m==0:return 1.0
    a,b=1.0,2.0*c
    for _ in range(2,m+1):a,b=b,2*c*b-a
    return b

def g(n,c):
    return c-S+(1+S)*n/U_numeric(n-1,c)

def cycle_step(n,h):
    return [sum(((1-alpha*h*(2-2*cos(2*pi*j/n)))/(1+beta*h*(2-2*cos(2*pi*j/n)))**2)*cos(2*pi*j*k/n) for j in range(n))/n for k in range(n)]

cases=0
for n in range(3,21):
    for h in [0.05,0.3,1,2,4,4.15,4.5,5,7,12,20,100,500]:
        c=1+1/(2*beta*h)
        a=cycle_step(n,h)
        # Algebraic diagonal decision matches the complete circulant matrix decision.
        assert (min(a)>=-1e-10)==(g(n,c)>=-1e-10), (n,h,min(a),g(n,c))
        # Diagonal has smallest G^2/G, hence a nonnegative diagonal implies all entries nonnegative.
        if a[0]>1e-9: assert min(a)>-1e-10
        assert abs(sum(a)-1)<5e-12
        cases+=1


def bisect(fn,lo,hi):
    vlo=fn(lo)
    assert vlo*fn(hi)<0
    for _ in range(90):
        mid=(lo+hi)/2
        if (fn(mid)>0)==(vlo>0):lo=mid
        else:hi=mid
    return (lo+hi)/2

bounds={}
for n in (8,9,12,16):
    low=bisect(lambda c:g(n,c),1+1e-10,F(5,4))
    high=bisect(lambda c:g(n,c),F(5,4),S)
    hfirst=1/(2*beta*(high-1))
    hreturn=1/(2*beta*(low-1))
    assert 0<hfirst<hreturn
    assert min(cycle_step(n,(hfirst+hreturn)/2))<0
    bounds[n]=(hfirst,hreturn)
assert 4.62<bounds[8][0]<4.65
assert 10.39<bounds[8][1]<10.42
print('VERIFY_OK', len(segments)*8,'exact positive Bernstein coefficients;',cases,'cycle Fourier positivity tests;',len(bounds),'two-root brackets')
print('bernstein_minima',*[str(x) for x in mins])
print('eight_vertex_interval',tuple(round(x,9) for x in bounds[8]))
