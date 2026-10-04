#!/usr/bin/env python3
from itertools import product

# Exact Gaussian-integer arithmetic. A complex number a+bi is (a,b).
ALPHABET = [(0,0),(1,0),(-1,0),(0,1),(0,-1)]
N = 4

def add(z,w): return (z[0]+w[0], z[1]+w[1])
def sub(z,w): return (z[0]-w[0], z[1]-w[1])
def mul(z,w): return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])
def conj(z): return (z[0],-z[1])
def scale(k,z): return (k*z[0], k*z[1])
def norm2(z): return z[0]*z[0]+z[1]*z[1]
def zero(z): return z == (0,0)

def signature(x):
    # For n=4, sqrt(n)=2.  Multiplying each orbit coefficient
    # x_i-x_j+(1/sqrt(n))*sum_r x_r by 2 gives
    # 2(x_i-x_j)+sum_r x_r, so squared magnitudes remain exact integers.
    s=(0,0)
    for z in x:
        s=add(s,z)
    out=[]
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            t=add(scale(2,sub(x[i],x[j])),s)
            out.append(norm2(t))
    return tuple(out)

def global_phase_equivalent(x,y):
    # Tests y=alpha*x for some |alpha|=1 without division.
    k=next((i for i,z in enumerate(x) if not zero(z)),None)
    if k is None:
        return all(zero(z) for z in y)
    if norm2(x[k]) != norm2(y[k]):
        return False
    for i in range(N):
        if mul(y[i],x[k]) != mul(y[k],x[i]):
            return False
    return True

def allowed_equivalent(x,y):
    if global_phase_equivalent(x,y):
        return True
    return global_phase_equivalent(tuple(conj(z) for z in x),y)

signals=list(product(ALPHABET, repeat=N))
groups={}
for x in signals:
    groups.setdefault(signature(x),[]).append(x)

max_class=0
pairs_checked=0
for grp in groups.values():
    max_class=max(max_class,len(grp))
    for i in range(len(grp)):
        for j in range(i+1,len(grp)):
            pairs_checked += 1
            if not allowed_equivalent(grp[i],grp[j]):
                raise SystemExit(f"FAIL unexpected collision: {grp[i]} vs {grp[j]}")

print(f"VERIFY_OK n4_signals={len(signals)} signatures={len(groups)} max_collision_class={max_class} collision_pairs={pairs_checked}")
