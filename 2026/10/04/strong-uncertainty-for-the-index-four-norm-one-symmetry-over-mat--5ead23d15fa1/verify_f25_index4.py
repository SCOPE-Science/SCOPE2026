#!/usr/bin/env python3
"""Exact verification for index-4 compressed Fourier matrices over F_25.

All cyclotomic arithmetic is in Z[z]/(Phi_30), Phi_30=z^8+z^7-z^5-z^4-z^3+z+1.
No floating point or external packages are used.
"""
from itertools import combinations, permutations
from math import gcd

P = 5
# F_25 = F_5[a]/(a^2-2). Elements are pairs (u,v)=u+v*a.
def fm(x,y):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % P,
            (x[0]*y[1] + x[1]*y[0]) % P)
def fpow(x,n):
    r=(1,0)
    while n:
        if n & 1: r=fm(r,x)
        x=fm(x,x); n//=2
    return r

def ford(x):
    if x==(0,0): return 0
    for d in (1,2,3,4,6,8,12,24):
        if fpow(x,d)==(1,0): return d
    raise AssertionError

g=(1,2)
assert ford(g)==24
H=[fpow(g,4*t) for t in range(6)]
assert len(set(H))==6
R=[fpow(g,k) for k in range(4)]
# Since a^5=-a, Tr(u+va)=2u.
def tr(x): return (2*x[0]) % 5

# Cyclotomic ring basis 1,z,...,z^7, where z is primitive 30th root.
# Phi_30 coefficients low-to-high.
PHI=(1,1,0,-1,-1,-1,0,1,1)
ZERO=(0,)*8
ONE=(1,0,0,0,0,0,0,0)
Z=(0,1,0,0,0,0,0,0)
def red(c):
    c=list(c)
    while len(c)<9: c.append(0)
    while len(c)>8:
        d=len(c)-1; a=c[d]
        if a:
            sh=d-8
            for i,b in enumerate(PHI): c[sh+i]-=a*b
        while len(c)>8 and c[-1]==0: c.pop()
    return tuple(c+[0]*(8-len(c)))
def add(a,b): return tuple(a[i]+b[i] for i in range(8))
def neg(a): return tuple(-v for v in a)
def mul(a,b):
    c=[0]*15
    for i,aa in enumerate(a):
        if aa:
            for j,bb in enumerate(b):
                if bb: c[i+j]+=aa*bb
    return red(c)
def power(a,n):
    r=ONE
    while n:
        if n & 1: r=mul(r,a)
        a=mul(a,a); n//=2
    return r
assert power(Z,30)==ONE and power(Z,15)==neg(ONE)
z5=power(Z,6)   # exp(2*pi*i/5)
z6=power(Z,5)   # exp(2*pi*i/6)

def det(A):
    n=len(A); out=ZERO
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=ONE
        for i,j in enumerate(p): term=mul(term,A[i][j])
        out=add(out,neg(term) if inv&1 else term)
    return out

def matrix(j):
    # chi_j((g^4)^t)=z6^(j t). j=0 is trivial and includes the zero orbit.
    reps=[(0,0)]+R if j==0 else R
    M=[]
    for s in reps:
        row=[]
        for r in reps:
            sm=ZERO
            for t,h in enumerate(H):
                e=tr(fm(s,fm(h,r)))
                term=power(z5,e)
                if j: term=mul(power(z6,j*t),term)
                sm=add(sm,term)
            row.append(sm)
        M.append(row)
    return M

def minors(M):
    n=len(M)
    for k in range(1,n+1):
        for rs in combinations(range(n),k):
            for cs in combinations(range(n),k):
                yield k,rs,cs,det([[M[i][j] for j in cs] for i in rs])

expected={
    0:(0,{}),
    1:(0,{}),
    2:(10,{2:10}),
    3:(34,{1:8,2:18,3:8}),
    4:(10,{2:10}),
    5:(0,{}),
}
for j in range(6):
    vals=list(minors(matrix(j)))
    zeros=[x for x in vals if x[3]==ZERO]
    by={k:sum(v[0]==k for v in zeros) for k in range(1,len(matrix(j))+1)}
    by={k:v for k,v in by.items() if v}
    assert (len(zeros),by)==expected[j]
    order=1 if j==0 else 6//gcd(j,6)
    print(f"j={j} character_order={order} matrix_size={len(matrix(j))} minors={len(vals)} zero_minors={len(zeros)} by_size={by}")

# Concrete witnesses for both failure types.
z2=[x for x in minors(matrix(2)) if x[3]==ZERO][0]
z3=[x for x in minors(matrix(3)) if x[3]==ZERO][0]
assert z2[:3]==(2,(0,1),(0,3))
assert z3[:3]==(1,(0,),(1,))
print("order3_zero_witness: rows=(0,1) cols=(0,3), size=2")
print("order2_zero_witness: row=(0) col=(1), size=1")
print("NVM iff character order is 1 or 6")
print("VERIFY_OK")
