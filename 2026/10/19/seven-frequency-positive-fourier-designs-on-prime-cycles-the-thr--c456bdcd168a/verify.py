#!/usr/bin/env python3
"""Exact rational-interval verification of seven-node Fourier quadrature at prime 11.
Run: python3 verify.py (Python 3 standard library only).
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial, cos, sin, pi

P=11
S=10**12

def arctan_bounds(den, terms):
    t=sum(((-1)**j*F(1, den**(2*j+1)*(2*j+1)) for j in range(terms)),F(0))
    rem=F(1,den**(2*terms+1)*(2*terms+1))
    return ((t-rem,t) if terms%2 else (t,t+rem))

a,b=arctan_bounds(5,24)
c,d=arctan_bounds(239,8)
plo,phi=16*a-4*d,16*b-4*c
PI0=F(3141592653589793,10**15)
assert plo>PI0-F(1,10**15) and phi<PI0+F(1,10**15)

def trig_enclosure(k):
    if k==0:return (S,S),(0,0)
    assert -5<=k<=5
    x=F(2*k,11)*PI0
    c=sum(((-1)**j*x**(2*j)/factorial(2*j) for j in range(16)),F(0))
    sn=sum(((-1)**j*x**(2*j+1)/factorial(2*j+1) for j in range(16)),F(0))
    # Taylor's theorem and the verified pi enclosure, using |x|<4.
    errc=F(4**32,factorial(32))+F(1,10**15)
    errs=F(4**33,factorial(33))+F(1,10**15)
    assert errc<F(1,10**14) and errs<F(1,10**14)
    cm=round(float(c)*S);sm=round(float(sn)*S)
    assert abs(c-F(cm,S))+errc<F(1,S)
    assert abs(sn-F(sm,S))+errs<F(1,S)
    return (cm-1,cm+1),(sm-1,sm+1)

C,SIN={},{}
for k in range(-5,6):C[k],SIN[k]=trig_enclosure(k)

def red(k):return ((k+5)%11)-5

def iadd(a,b):return a[0]+b[0],a[1]+b[1]
def ineg(a):return -a[1],-a[0]
def isub(a,b):return iadd(a,ineg(b))
def ceildiv(a,b):return -((-a)//b)
def imul(a,b):
    m=[x*y for x in a for y in b]
    return min(m)//S,ceildiv(max(m),S)
def idiv(a,b):
    assert not (b[0]<=0<=b[1]), (a,b)
    m=[F(x*S,y) for x in a for y in b]
    return min(m).__floor__(),max(m).__ceil__()
def contains0(a):return a[0]<=0<=a[1]
def mid(a):return a[0]+a[1]

def solve(nodes):
    A=[]
    A.append([(S,S) for _ in nodes])
    for k in range(1,4):
        A.append([C[red(k*j)] for j in nodes])
        A.append([SIN[red(k*j)] for j in nodes])
    b=[(S,S)]+[(0,0)]*6
    # Pivoted interval Gauss--Jordan elimination; enclosure arithmetic is outward-rounded.
    for j in range(7):
        pivot=max(range(j,7),key=lambda i:abs(mid(A[i][j])))
        A[j],A[pivot]=A[pivot],A[j]
        b[j],b[pivot]=b[pivot],b[j]
        assert not contains0(A[j][j]), (nodes,j,'pivot')
        piv=A[j][j]
        for k in range(j,7):A[j][k]=idiv(A[j][k],piv)
        b[j]=idiv(b[j],piv)
        for i in range(7):
            if i==j:continue
            t=A[i][j]
            for k in range(j+1,7):A[i][k]=isub(A[i][k],imul(t,A[j][k]))
            b[i]=isub(b[i],imul(t,b[j]))
            A[i][j]=(0,0)
    return b

def orbit(nodes):
    return {tuple(sorted(((s*j+a)%11 for j in nodes))) for s in (1,-1) for a in range(11)}

seen=set();positive=[];negative=[];all_rows=[]
for t in combinations(range(11),7):
    if t in seen:continue
    o=orbit(t)
    assert not (seen & o)
    seen.update(o)
    weights=solve(t)
    if all(w[0]>0 for w in weights):
        assert all(25*w[0]>S for w in weights)
        positive.append((t,len(o),weights))
        sign='POS'
    else:
        bad=[i for i,w in enumerate(weights) if w[1]<0]
        assert bad, (t,weights)
        assert 25*weights[bad[0]][1]<-S
        negative.append((t,len(o),bad[0],weights[bad[0]]))
        sign='NEG'
    all_rows.append((t,len(o),sign))
assert len(seen)==330
assert len(all_rows)==20
assert len(positive)==3 and sum(o for _,o,_ in positive)==33
assert len(negative)==17
assert all(o==11 for _,o,_ in positive)
print('VALIDATED prime=11 orbit representatives=20, positive_orbits=3, positive_supports=33, negative_orbits=17')
for t,size,w in positive:
    print('POS',','.join(map(str,t)),'orbit_size',size,'weight_intervals',[(round(a/S,9),round(b/S,9)) for a,b in w])
for t,size,j,v in negative:
    print('NEG',','.join(map(str,t)),'orbit_size',size,'witness_index',j,'upper_bound',round(v[1]/S,8))
print('VERIFY_OK exact rational pi/Taylor enclosures, interval Gaussian elimination, all 330 supports via 20 dihedral orbits')
