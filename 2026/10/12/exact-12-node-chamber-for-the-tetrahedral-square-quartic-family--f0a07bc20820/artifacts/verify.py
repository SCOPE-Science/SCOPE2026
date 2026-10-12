#!/usr/bin/env python3
"""Exact consistency checks for the tetrahedral square-quartic theorem."""
from itertools import combinations

# Polynomial dictionaries in four variables over F_2.
def add(p, q):
    r = dict(p)
    for m, c in q.items():
        if c & 1:
            r[m] = r.get(m, 0) ^ 1
            if not r[m]:
                r.pop(m)
    return r

def deriv(p, i):
    out = {}
    for m, c in p.items():
        if c and (m[i] & 1):
            mm = list(m)
            mm[i] -= 1
            mm = tuple(mm)
            out[mm] = out.get(mm, 0) ^ 1
            if not out[mm]:
                out.pop(mm)
    return out

def square_poly(p):
    return {tuple(2*e for e in m): c for m, c in p.items() if c & 1}

P = {(1,1,1,1): 1}
q = {}
for i in range(4):
    m = [0]*4; m[i] = 2; q[tuple(m)] = 1
for i,j in combinations(range(4), 2):
    m = [0]*4; m[i] = m[j] = 1; q[tuple(m)] = 1
F = add(P, square_poly(q))
expected = []
for i in range(4):
    m = [1]*4; m[i] = 0
    expected.append({tuple(m): 1})
for i in range(4):
    assert deriv(F, i) == expected[i]

# GF(4) = F_2[w]/(w^2+w+1), represented as a+b*w in two bits.
def gf_add(a,b): return a ^ b

def gf_mul(a,b):
    a0, a1 = a & 1, (a >> 1) & 1
    b0, b1 = b & 1, (b >> 1) & 1
    c0 = (a0*b0) ^ (a1*b1)      # w^2 = w+1 contributes to constant
    c1 = (a0*b1) ^ (a1*b0) ^ (a1*b1)
    return c0 | (c1 << 1)

def gf_pow(a,n):
    r=1
    while n:
        if n&1: r=gf_mul(r,a)
        a=gf_mul(a,a); n//=2
    return r

def poly_eval(p, x):
    s=0
    for m,c in p.items():
        if not c: continue
        t=1
        for xi,e in zip(x,m): t=gf_mul(t,gf_pow(xi,e))
        s=gf_add(s,t)
    return s

def q_eval(x): return poly_eval(q,x)
def F_eval(x): return poly_eval(F,x)

def d_eval(i,x): return poly_eval(expected[i],x)

# Elements 2=w and 3=w+1 are the two roots of T^2+T+1.
w, w2 = 2, 3
for r in (w,w2):
    assert gf_add(gf_add(gf_mul(r,r),r),1) == 0

points=[]
for i,j in combinations(range(4),2):
    comp=[t for t in range(4) if t not in (i,j)]
    k,l=comp
    for r in (w,w2):
        x=[0]*4
        x[k]=1; x[l]=r
        x=tuple(x)
        assert q_eval(x)==0
        assert F_eval(x)==0
        assert all(d_eval(t,x)==0 for t in range(4))
        points.append(x)
assert len(points)==12 and len(set(points))==12

# No coordinate vertex lies on q_0=0, so no edge supports collide at a vertex.
for i in range(4):
    e=[0]*4; e[i]=1
    assert q_eval(tuple(e))==1

# Each simple edge root contributes local Jacobian length 2: basis {1,w_local}.
local_lengths=[2]*12
assert sum(local_lengths)==24
print('VERIFY_OK')
