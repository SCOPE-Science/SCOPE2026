#!/usr/bin/env python3
"""Exact algebraic verification of a finite-cyclic sixth-moment identity."""
from collections import defaultdict
from itertools import product
from cmath import exp, pi
from random import Random

ZERO = (0, 0, 0, 0, 0, 0)

def mul(p, q):
    out = defaultdict(int)
    for x, a in p.items():
        for y, b in q.items():
            out[tuple(x[i] + y[i] for i in range(6))] += a * b
    return {k:v for k,v in out.items() if v}

def add(*polys):
    out = defaultdict(int)
    for p in polys:
        for k, v in p.items():
            out[k] += v
    return {k:v for k,v in out.items() if v}

def scale(p, m):
    return {k:v*m for k,v in p.items()}

def power(p, n):
    out = {ZERO:1}
    for _ in range(n):
        out = mul(out,p)
    return out

def mon(index):
    x=[0]*6; x[index]=1
    return {tuple(x):1}

a,b,c,A,B,C = [mon(i) for i in range(6)]
S = add(mul(a,A),mul(b,B),mul(c,C))
U = add(mul(mul(a,A),mul(b,B)),mul(mul(a,A),mul(c,C)),mul(mul(b,B),mul(c,C)))
V = mul(mul(a,A),mul(mul(b,B),mul(c,C)))
terms = [mul(power(a,3),mul(B,power(C,2))),mul(mul(a,power(b,2)),power(C,3)),mul(power(b,3),mul(power(A,2),C))]
conj = lambda p:{(k[3],k[4],k[5],k[0],k[1],k[2]):v for k,v in p.items()}
rhs=add(power(S,3),scale(mul(S,U),6),scale(V,12),*(scale(t,3) for t in terms),*(scale(conj(t),3) for t in terms))

# Form P^3 in the group algebra of Z/7Z; variables index 0,1,3.
packet = {0:a,1:b,3:c}
coeff={0:{ZERO:1}}
for _ in range(3):
    new={}
    for freq,p in coeff.items():
        for offset,x in packet.items():
            f=(freq+offset)%7
            new[f]=add(new.get(f,{}),mul(p,x))
    coeff=new
lhs=add(*(mul(p,conj(p)) for p in coeff.values()))
assert lhs == rhs, ('symbolic coefficient mismatch',set(lhs.items())^set(rhs.items()))
assert len(coeff)==7
assert sum(sum(p.values())**2 for p in coeff.values())==111
assert {f:sum(p.values()) for f,p in sorted(coeff.items())}=={0:4,1:3,2:4,3:4,4:6,5:3,6:3}

# Cross-check independent discrete Fourier sampling for generic complex inputs.
rng=Random(20261009)
w=exp(2j*pi/7)
for _ in range(250):
    x=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(3)]
    n=sum(abs(t)**2 for t in x)
    moment=sum(abs(x[0]+x[1]*w**j+x[2]*w**(3*j))**6 for j in range(7))/7
    convol=[0j]*7
    for i,j,k in product(range(3), repeat=3):
        convol[((0,1,3)[i]+(0,1,3)[j]+(0,1,3)[k])%7]+=x[i]*x[j]*x[k]
    identity=sum(abs(z)**2 for z in convol)
    assert abs(moment-identity)<1e-8*max(1,identity)
    assert moment<=(37/9)*n**3+1e-8*max(1,n**3)
for t in range(7):
    x=[w**(t*j) for j in (0,1,3)]
    moment=sum(abs(x[0]+x[1]*w**j+x[2]*w**(3*j))**6 for j in range(7))/7
    assert abs(moment/27-37/9)<1e-10
print('VERIFY_OK exact_complex_polynomial=PASS cubic_fibers=7 energy=111 samples=250 extremizers=7')
