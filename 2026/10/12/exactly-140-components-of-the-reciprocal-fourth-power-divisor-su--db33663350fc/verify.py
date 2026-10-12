#!/usr/bin/env python3
"""Exact stand-alone certificate for reciprocal-fourth-power divisor-sum range.
All comparisons use Python integer and rational arithmetic; no external packages.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

P = (2, 3, 5, 7, 11, 13)
A = (3, 2, 1, 1, 1, 1)

def atan_bounds(inv, n=20):
    terms = [Q((-1)**k, (2*k+1)*inv**(2*k+1)) for k in range(n+1)]
    return sum(terms[:n], Q()), sum(terms[:n+1], Q())

# Alternating Taylor remainders and Machin's identity for pi.
l5, h5 = atan_bounds(5)
l239, h239 = atan_bounds(239)
PI_L, PI_H = 16*l5 - 4*h239, 16*h5 - 4*l239
assert PI_L < PI_H
assert Q(3141592653589793,10**15) < PI_L
assert PI_H < Q(3141592653589794,10**15)
C = Q(1,90)
for p in P:
    C *= 1 - Q(1,p**4)
T_L, T_H = C*PI_L**4, C*PI_H**4
assert 1 < T_L < T_H < Q(1001,1000)

def geom(p,a):
    return sum((Q(1,p**(4*k)) for k in range(a+1)),Q())

def lim(p):
    return Q(p**4,p**4-1)

# The exponent cutoff is checked on BOTH sides of each boundary.
for p,a in zip(P,A):
    assert geom(p,a)/geom(p,a-1) > T_H
    assert geom(p,a+1)/geom(p,a) < T_L
    assert lim(p) > geom(p,a)

opts=[]
for p,a in zip(P,A):
    opts.append([(geom(p,i),geom(p,i)) for i in range(a)]
               + [(geom(p,a),lim(p))])

blocks=[]
for choices in product(*opts):
    low=Q(1); high=Q(1)
    for x,y in choices:
        low *= x;high *= y
    blocks.append((low, high))
blocks.sort()
assert len(blocks)==192
components=[]
for l,u in blocks:
    if not components or l > components[-1][1]*T_H:
        components.append([l,u])
    else:
        assert l <= components[-1][1]*T_L
        if u>components[-1][1]:components[-1][1]=u
assert len(components)==140
assert sum(components[i][0]>components[i-1][1]*T_H for i in range(1,140))==139
assert components[0][0]==1
assert components[-1][1]*T_H > Q(108,100)
assert components[-1][1] == __import__('functools').reduce(
    lambda x,p:x*lim(p), P, Q(1))

# Second endpoint construction: Sanna's backward interval recurrence, using
# a cutoff chosen separately for each current interval, not Cartesian tiers.
recursive=[(Q(1),Q(1))]
layer_counts=[]
for p in reversed(P):
    candidate=[]
    for l,u in recursive:
        a=0
        while geom(p,a+1)*l > geom(p,a)*u*T_H:
            candidate.append((l*geom(p,a),u*geom(p,a)))
            a+=1
            assert a<12
        assert geom(p,a+1)*l <= geom(p,a)*u*T_L
        candidate.append((l*geom(p,a),u*lim(p)))
    candidate.sort()
    recursive=[]
    for l,u in candidate:
        if recursive and l <= recursive[-1][1]*T_L:
            recursive[-1]=(recursive[-1][0],max(recursive[-1][1],u))
        else:
            if recursive:assert l>recursive[-1][1]*T_H
            recursive.append((l,u))
    layer_counts.append((p,len(recursive)))
assert layer_counts==[(13,2),(11,4),(7,8),(5,16),(3,48),(2,140)]
assert recursive == [tuple(c) for c in components]

# An independent graph connected-components check, not using sorted sweeping:
parent=list(range(len(blocks)))
def root(i):
    while parent[i]!=i:
        parent[i]=parent[parent[i]]
        i=parent[i]
    return i
for i,(a,b) in enumerate(blocks):
    for j,(c,d) in enumerate(blocks[:i]):
        if a <= d*T_L and c <= b*T_L:
            parent[root(i)]=root(j)
assert len({root(i) for i in range(len(blocks))})==140

# Finite effective tail certificate. For every prime p between 17 and
# 396737, sum of reciprocal fourth powers over next <=10 primes > 1/p^4.
N=430000
prime=bytearray(b'\x01')*(N+1)
prime[0]=prime[1]=0
for k in range(2,int(N**.5)+1):
    if prime[k]:
        prime[k*k::k]=b'\x00'*((N-k*k)//k+1)
primes=[k for k in range(17,N+1) if prime[k]]
checked=0;max_count=0
for i,p in enumerate(primes):
    if p>=396738:break
    assert i+10<len(primes)
    s=Q();first=0
    for j in range(1,11):
        s+=Q(p**4,primes[i+j]**4)
        if s>1:
            first=j
            break
    assert first>0,(p,s)
    checked+=1
    max_count=max(max_count,first)
assert checked>33000 and max_count==10
# Dusart: for x>=396738, a prime exists in (x,x(1+1/(25 log(x)^2))].
# Since log(x)>7, the two successive primes q1,q2 obey
# q2/p < (1001/1000)^2 < 101/100.
assert Q(1001,1000)**2 < Q(101,100)
assert 2*Q(100,101)**4 > 1

# Companion endpoint file: every interval is [low, T*high].
rows=['index\tlower_num\tlower_den\tupper_coefficient_num\tupper_coefficient_den']
for i,(l,u) in enumerate(components,1):
    rows.append(f'{i}\t{l.numerator}\t{l.denominator}\t{u.numerator}\t{u.denominator}')
expected='\n'.join(rows)+'\n'
companion=Path(__file__).with_name('COMPONENTS.tsv')
if companion.exists():
    assert companion.read_text(encoding='utf-8')==expected
else:
    companion.write_text(expected,encoding='utf-8')
print('EXACT_CERTIFICATE_OK',f'blocks={len(blocks)}',f'components={len(components)}',
      'gaps=139',f'finite_primes={checked}',f'worst_next_prime_count={max_count}',
      'machin_terms=20','graph_components=140')
