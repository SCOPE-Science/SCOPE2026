"""Reproducible finite-grid checks for the Lee-two-ball positive-type mass threshold.

Only uses Python's standard library. Finite tests complement, but do not prove,
the cyclotomic classification for all grid orders.
"""
import math
from fractions import Fraction

V=[(0,0),(1,0),(-1,0),(0,1),(0,-1)]
for n in range(5,41):
    D={((a-c)%n,(b-d)%n) for a,b in V for c,d in V}
    assert len(D)==13,(n,len(D))
    cnt={d:sum(((a-c)%n,(b-dv)%n)==d for a,b in V for c,dv in V) for d in D}
    assert cnt[(0,0)]==5
    for d in D:
        u,v=d
        typ= sorted((min(u,n-u),min(v,n-v)))
        target= 5 if typ==[0,0] else (1 if typ==[0,2] else 2)
        assert cnt[d]==target,(n,d,cnt[d],target)

# Exact rational witness showing a substantial strict excess at order six.
# Values of cos(2*pi*k/6) all lie in {1, 1/2, -1/2, -1}.
X6=[Fraction(1),Fraction(1,2),Fraction(-1,2),Fraction(-1)]
for u in X6:
    for v in X6:
        p=Fraction(1)+Fraction(6,7)*(u+v)+Fraction(4,7)*(2*u*u+2*v*v-2)+Fraction(12,7)*u*v
        assert p>=0,(u,v,p)
assert Fraction(1)+4*(Fraction(3,7)+Fraction(2,7)+Fraction(3,7))==Fraction(39,7)

x5=(math.sqrt(5)-1)/4
y5=-(math.sqrt(5)+1)/4
assert abs(x5+y5+.5)<1e-14
assert abs(x5*y5+.25)<1e-14
assert abs(x5*x5+y5*y5-.75)<1e-14

all_orders=range(5,241)
for n in all_orders:
    xs=[math.cos(2*math.pi*k/n) for k in range(n)]
    samples=[(x,y) for x in xs for y in xs]
    data=[]
    for x,y in samples:
        K=1+2*x+2*y
        p0=K*K/5
        gradient=2*(x+y)+6*((2*x*x-1)+(2*y*y-1))+4*x*y
        data.append((x,y,p0,gradient))
    zeros=[(x,y,p,g) for x,y,p,g in data if p<1.e-20]
    predicted=[]
    if n%5==0:
        predicted.extend([(x5,y5),(y5,x5)])
    if n%6==0:
        predicted.extend([(-1.,.5),(.5,-1.)])
    if n%12==0:
        predicted.extend([(0.,-.5),(-.5,0.)])
    assert bool(zeros)==bool(predicted),(n,'zero_existence')
    for x,y,p,g in zeros:
        assert any(abs(x-a)+abs(y-b)<1e-8 for a,b in predicted),(n,x,y)
    for a,b in predicted:
        assert any(abs(x-a)+abs(y-b)<1e-8 for x,y,p,g in zeros),(n,a,b)
    if n%5==0 or n%12==0:
        continue
    if n%6:
        mu=min(p for _,_,p,_ in data)
        assert mu>1e-20
        eps=mu/10
        assert min((1+eps)*p-eps for _,_,p,_ in data)>-1e-10
        assert 5+4*eps>5
    else:
        assert zeros
        assert all(abs(g)<1e-8 for _,_,p,g in zeros)
        positive=[p for _,_,p,_ in data if p>1e-20]
        m=min(positive)
        maxR=max(abs(g) for _,_,p,g in data)
        eps=m/(4*(1+maxR))
        assert all(p+eps*g>-1e-9 for _,_,p,g in data),(n,eps)
        assert 5+20*eps>5
print('CHECKER_PASS: exact integer difference counts n=5..40; exact rational order-six witness; algebraic contact identities; supplementary grid zeros/perturbations n=5..240')
