#!/usr/bin/env python3
"""Exact F_3 certificate for two 2023 conic-line arrangements.
Requires Python 3 standard library only. Nothing relies on numeric sampling.
"""
from collections import Counter
from itertools import product, combinations

MOD=3
ONE={(0,0,0):1}
ZERO={}
def cn(n):
    n%=MOD
    return {(0,0,0):n} if n else {}
def add(a,b):
    d=a.copy()
    for e,v in b.items():
        w=(d.get(e,0)+v)%MOD
        if w:d[e]=w
        else:d.pop(e,None)
    return d
def neg(a):return {e:(-v)%MOD for e,v in a.items()}
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    d={}
    for e,v in a.items():
        for f,w in b.items():
            g=tuple(ei+fi for ei,fi in zip(e,f))
            d[g]=(d.get(g,0)+v*w)%MOD
    return {e:v for e,v in d.items() if v}
def powp(a,n):
    b=ONE
    for _ in range(n):b=mul(b,a)
    return b
def scale(a,n):return mul(a,cn(n))
X,Y,Z=({tuple(1 if i==j else 0 for i in range(3)):1} for j in range(3))
V=[X,Y,Z]
def lin(a,b,c):return add(add(scale(X,a),scale(Y,b)),scale(Z,c))
def chain(*args):
    p=ONE
    for q in args:p=mul(p,q)
    return p
def mod_form(poly,line):
    # Exact division test by substituting one variable in the line equation.
    j=next(i for i,c in enumerate(line) if c%3)
    inv=pow(line[j],-1,MOD)
    repl=ZERO
    for i,c in enumerate(line):
        if i!=j:repl=add(repl,scale(V[i],-inv*c))
    ans=ZERO
    for powers,coef in poly.items():
        factor=cn(coef)
        for i,exp in enumerate(powers):
            factor=mul(factor,powp(repl if i==j else V[i],exp))
        ans=add(ans,factor)
    return ans
def projective(v):
    w=tuple(t%3 for t in v)
    i=next(t for t in w if t)
    return tuple(t*pow(i,-1,MOD)%3 for t in w)
def cross(a,b):
    return projective((a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]))
def degree(p):return max((sum(e) for e in p),default=-1)
def det_cols(u,v,w):
    a= sub(mul(v[1],w[2]),mul(v[2],w[1]))
    b= sub(mul(v[0],w[2]),mul(v[2],w[0]))
    c= sub(mul(v[0],w[1]),mul(v[1],w[0]))
    return add(sub(mul(u[0],a),mul(u[1],b)),mul(u[2],c))
def derive(theta,ell):
    p=ZERO
    for i,c in enumerate(ell):p=add(p,scale(theta[i],c))
    return p

# Source integral conic: -x^2+xy-y^2+z^2.
q=add(sub(add(neg(powp(X,2)),mul(X,Y)),powp(Y,2)),powp(Z,2))
assert q == chain(sub(sub(Z,X),Y),add(add(Z,X),Y))

b0=[(1,0,0),(1,0,1),(1,0,-1)]
bl=[(0,1,0),(0,1,1),(0,1,-1),(-1,1,-1),(-1,1,1),(-1,1,0),(-1,-1,1),(1,1,1)]
assert len({projective(v) for v in b0+bl})==11
P=chain(*[lin(*c) for c in bl])
F15=chain(X,sub(X,Z),add(X,Z),P)
F16=mul(F15,Z)
# Verify the reduction of the *unfactored* two source products.
source_lines=chain(X,Y,sub(X,Z),add(X,Z),add(Y,Z),sub(Y,Z),sub(sub(Y,X),Z),add(sub(Y,X),Z),sub(Y,X))
assert chain(source_lines,q)==F15
assert chain(source_lines,Z,q)==F16

# Account for all F3-rational projective lines, including the deleted ones.
alllines={projective(v) for v in product(range(3),repeat=3) if any(v)}
assert len(alllines)==13
s15={projective(v) for v in b0+bl}
s16=s15 | {(0,0,1)}
H=projective((1,1,0)); T=(0,0,1)
assert alllines-s15=={H,T}
assert alllines-s16=={H}

# Each pair of F3-rational lines meets in a F3-rational point;
# classify the entire geometric singular support.
points={projective(v) for v in product(range(3),repeat=3) if any(v)}
assert len(points)==13
for ls,target,nn in [(s15,{2:1,3:6,4:6},55),(s16,{3:4,4:9},66)]:
    counts=Counter(sum(sum(a*b for a,b in zip(p,l))%3==0 for l in ls) for p in points)
    assert counts==target,(counts,target)
    pairs={cross(a,b) for a,b in combinations(ls,2)}
    assert pairs==points and sum(m*(m-1)//2*n for m,n in counts.items())==nn

E=[X,Y,Z]
D3=[powp(X,3),powp(Y,3),powp(Z,3)]
T8=[ZERO,P,ZERO]
# The normal vector fields E,D3,T8 give a Saito basis for F16.
for t in (E,D3,T8):
    for ell in s16:assert mod_form(derive(t,ell),ell)==ZERO
assert det_cols(E,D3,T8)==F16
assert [degree(X),degree(D3[0]),degree(P)]==[1,3,8]

# Delete z. Construct a degree-seven polynomial logarithmic field by
# cancelling T8 modulo z before dividing by z.
B=scale(chain(powp(Y,2),powp(sub(Y,X),2),add(X,Y)),-1)
P0=mod_form(P,(0,0,1))
assert P0==mul(B,mul(Y,sub(powp(Y,2),powp(X,2))))
N=[add(sub(T8[i],mul(B,D3[i])),mul(mul(powp(X,2),B),E[i])) for i in range(3)]
assert all(e[2]>0 for f in N for e in f)
T7=[{(e[0],e[1],e[2]-1):v for e,v in f.items()} for f in N]
for t in (E,D3,T7):
    for ell in s15:assert mod_form(derive(t,ell),ell)==ZERO,(ell,t)
assert det_cols(E,D3,T7)==F15
assert max(degree(f) for f in T7)==7
assert degree(F15)==11 and degree(F16)==12
print('VERIFY_OK: source reductions; projective-plane missing lines; 13-point incidence spectra; explicit Saito bases (1,3,7) and (1,3,8)')
