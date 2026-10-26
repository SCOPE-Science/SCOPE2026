#!/usr/bin/env python3
"""Exact census of smooth blocking ternary cubics over GF(3).

Requirements: Python 3, NumPy.  All field and group operations are exact.
Output reports coefficient-form counts, group orbits and line-incidence spectrum.
"""
import itertools
from collections import Counter
import numpy as np

P = 3
MON = [(a, b, 3-a-b) for a in range(4) for b in range(4-a)]
POINTS = sorted({tuple((a * pow(next(v for v in u if v), -1, 3)) % 3 for a in u)
                 for u in itertools.product(range(3), repeat=3) if any(u)})
LINES = [tuple(j for j, p in enumerate(POINTS) if sum(a*b for a,b in zip(co,p)) % 3 == 0)
         for co in POINTS]
EVAL = np.array([[pow(x,a,3)*pow(y,b,3)*pow(z,c,3) % 3 for a,b,c in MON]
                 for x,y,z in POINTS], dtype=np.int16)
COEFS = np.zeros((3**10-1, 10), dtype=np.int16)
indices = np.arange(1, 3**10, dtype=np.int64)
for j in range(10):
    COEFS[:,j] = indices % 3
    indices //= 3
VANISH = (COEFS @ EVAL.T) % 3 == 0
BLOCK = np.ones(len(COEFS), dtype=bool)
for line in LINES:
    BLOCK &= VANISH[:,line].any(axis=1)
C = COEFS[BLOCK]


def field_tables(n):
    """Construct GF(3^n) using t^2=2 (n=2) or t^3=t+1 (n=3)."""
    order = 3**n
    def digs(k):
        return [(k//(3**i))%3 for i in range(n)]
    def enc(v):
        return sum((int(a)%3)*3**i for i,a in enumerate(v))
    MUL = np.zeros((order,order),dtype=np.int16)
    for i in range(order):
        aa = digs(i)
        for j in range(order):
            bb = digs(j)
            cc = [0]*(2*n-1)
            for a in range(n):
                for b in range(n): cc[a+b] += aa[a]*bb[b]
            for k in range(2*n-2,n-1,-1):
                if n==2: cc[k-2] += 2*cc[k]
                else: cc[k-3] += cc[k]; cc[k-2] += cc[k]
            MUL[i,j] = enc(cc[:n])
    POW = np.ones((order,4),dtype=np.int16)
    for v in range(order):
        for k in range(1,4): POW[v,k] = MUL[POW[v,k-1],v]
    return MUL,POW,digs


def smooth_over_extension(n):
    Q=3**n
    MUL,POW,digits=field_tables(n)
    pts = [(1,a,b) for a in range(Q) for b in range(Q)] + \
          [(0,1,b) for b in range(Q)] + [(0,0,1)]
    mats=[]
    for derivative in range(4):
        val = np.zeros((10,len(pts),n),dtype=np.int16)
        for i,m in enumerate(MON):
            ex=list(m)
            scalar=1 if derivative==0 else ex[derivative-1]%3
            if derivative: ex[derivative-1]-=1
            if scalar==0: continue
            for j,p in enumerate(pts):
                t=1
                for a,k in zip(p,ex): t=int(MUL[t,POW[a,k]])
                val[i,j,:]=[(scalar*b)%3 for b in digits(t)]
        mats.append(val.reshape(10,-1))
    smooth=np.zeros(len(C),dtype=bool)
    for offset in range(0,len(C),250):
        batch=C[offset:offset+250]
        singular=None
        for mat in mats:
            values=((batch@mat)%3).reshape(len(batch),len(pts),n)
            zero=(values==0).all(axis=2)
            singular=zero if singular is None else singular&zero
        smooth[offset:offset+len(batch)]=~singular.any(axis=1)
    return smooth

# A singular plane cubic has a singular closed point of degree <=3:
# geometrically integral cubics have arithmetic genus 1; reducible cubics
# have components of degrees (1,2), (1,1,1), or repeated lines, and Bezout
# bounds the degrees of their intersection points by 3. GF(9) and GF(27)
# jointly contain all closed points of degrees 1, 2 or 3.
GOOD=smooth_over_extension(2)&smooth_over_extension(3)
SMOOTH=C[GOOD]

def canon(v):
    v=tuple(int(a)%3 for a in v)
    lead=next(a for a in v if a)
    return tuple((a*(1 if lead==1 else 2))%3 for a in v)

# Generate GL(3,3) by two coordinate swaps, a transvection, and a sign.
# Matrix action on ternary cubics is calculated as exact substitution.
def poly_product(a,b):
    out={}
    for u,cu in a.items():
        for v,cv in b.items():
            key=tuple(u[k]+v[k] for k in range(3))
            out[key]=(out.get(key,0)+cu*cv)%3
    return {m:c for m,c in out.items() if c}
def substitution(images):
    M=np.zeros((10,10),dtype=np.int16)
    for i,(a,b,c) in enumerate(MON):
        out={(0,0,0):1}
        for img,k in zip(images,(a,b,c)):
            for _ in range(k):out=poly_product(out,img)
        for j,m in enumerate(MON):M[i,j]=out.get(m,0)
    return M
X={(1,0,0):1};Y={(0,1,0):1};Z={(0,0,1):1}
ADD={(1,0,0):1,(0,1,0):1}
NEG={(1,0,0):2}
GENERATORS=[substitution(G) for G in [(Y,X,Z),(X,Z,Y),(ADD,Y,Z),(NEG,Y,Z)]]
UNSEEN={canon(row) for row in SMOOTH}
ORBIT_SIZES=[]
while UNSEEN:
    rep=min(UNSEEN)
    orb={rep}; stack=[rep]
    while stack:
        v=np.array(stack.pop(),dtype=np.int16)
        for transform in GENERATORS:
            nxt=canon(v@transform)
            assert nxt in UNSEEN or nxt in orb, 'group closure error'
            if nxt not in orb:orb.add(nxt);stack.append(nxt)
    UNSEEN-=orb
    ORBIT_SIZES.append(len(orb))

# Explicit smooth blocking representative:
# y^2 z - x^3 - x^2 z + x z^2 =0.
example=np.zeros(10,dtype=np.int16)
for m,c in [((0,2,1),1),((3,0,0),2),((2,0,1),2),((1,0,2),1)]:
    example[MON.index(m)]=c
assert canon(example) in {canon(row) for row in SMOOTH}
example_idx=np.flatnonzero((COEFS==example).all(axis=1))[0]
example_pts=VANISH[example_idx]
line_spectrum=Counter(sum(bool(example_pts[i]) for i in L) for L in LINES)
print('projective_points=',len(POINTS))
print('projective_lines=',len(LINES))
print('nonzero_cubic_forms=',len(COEFS))
print('blocking_cubic_forms=',len(C))
print('smooth_blocking_cubic_forms=',len(SMOOTH))
print('smooth_blocking_point_counts=',dict(sorted(Counter(VANISH[BLOCK][GOOD].sum(axis=1)).items())))
print('projective_equations_mod_scalars=',len({canon(row) for row in SMOOTH}))
print('PGL3_order=',(27-1)*(27-3)*(27-9)//2)
print('projective_orbit_sizes=',sorted(ORBIT_SIZES))
print('projective_stabilizer_orders=',sorted([5616//s for s in ORBIT_SIZES]))
print('example_rational_points=',int(example_pts.sum()))
print('example_line_spectrum=',dict(sorted(line_spectrum.items())))
assert len(SMOOTH)==1872
assert ORBIT_SIZES==[936]
assert dict(sorted(line_spectrum.items()))=={1:6,2:3,3:4}
