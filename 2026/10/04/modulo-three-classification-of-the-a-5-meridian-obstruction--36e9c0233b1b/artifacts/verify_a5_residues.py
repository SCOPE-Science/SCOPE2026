#!/usr/bin/env python3
"""Exact finite-group verification of the A5 meridian-count residue theorem.

The program enumerates A5 from first principles, evaluates both relators in the
published presentation, and checks all residues modulo the exponent of A5.
This is exhaustive for the finite-group computation, not a sample.
"""
import itertools, math, json

N=5
ID=tuple(range(N))

def compose(p,q):
    """Function composition p after q."""
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    r=[0]*N
    for i,j in enumerate(p): r[j]=i
    return tuple(r)

def power(p,n):
    if n<0: return power(inverse(p),-n)
    r=ID; a=p
    while n:
        if n&1: r=compose(r,a)
        a=compose(a,a); n//=2
    return r

def parity(p):
    return sum(p[i]>p[j] for i in range(N) for j in range(i+1,N))%2

A5=[p for p in itertools.permutations(range(N)) if parity(p)==0]
assert len(A5)==60

# sigma=(15432) in one-based cycle notation.
sigma=(4,0,1,2,3)
assert sigma in A5

def order(p):
    r=ID
    for k in range(1,61):
        r=compose(r,p)
        if r==ID: return k
    raise AssertionError('order too large')

orders={order(p) for p in A5}
assert orders=={1,2,3,5}
exp=1
for o in orders: exp=math.lcm(exp,o)
assert exp==30

def satisfies(x,y,a,m):
    # r1=(yx)^m y (yx)^(-m) x^(-1)
    yx=compose(y,x)
    r1=compose(compose(compose(power(yx,m),y),power(yx,-m)),inverse(x))
    # r2=(x^(-1) a x) a^(-1) x^(-1) (y a y^(-1))
    t1=compose(compose(inverse(x),a),x)
    t2=inverse(a)
    t3=inverse(x)
    t4=compose(compose(y,a),inverse(y))
    r2=compose(compose(compose(t1,t2),t3),t4)
    return r1==ID and r2==ID

def counts(m):
    nb=sum(satisfies(sigma,y,a,m) for y in A5 for a in A5)
    ng=sum(satisfies(x,y,sigma,m) for x in A5 for y in A5)
    return nb,ng

table=[]
for r in range(exp):
    got=counts(r)
    want=(6,1) if r%3==1 else (1,1)
    assert got==want,(r,got,want)
    table.append({'residue_mod_30':r,'N_B':got[0],'N_G':got[1]})

# Directly verify periodicity over one full shifted period and the published case.
for r in range(exp):
    assert counts(r+exp)==counts(r)
assert counts(1)==(6,1)
assert counts(61)==(6,1)

print('VERIFY_OK A5_size=60 exponent=30 residues=30 distinguished=10 pattern=m_mod_3_eq_1 source_case=true')
