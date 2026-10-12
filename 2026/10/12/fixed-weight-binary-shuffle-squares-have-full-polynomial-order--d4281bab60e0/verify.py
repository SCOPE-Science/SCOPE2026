#!/usr/bin/env python3
import itertools
from itertools import combinations
from math import comb

def compositions(total, parts):
    if parts == 1:
        yield (total,); return
    for x in range(total+1):
        for tail in compositions(total-x, parts-1): yield (x,)+tail

def construct(p,c):
    k=len(c); root='0'*p[0]
    for i in range(k): root += '1'+'0'*p[i+1]
    out=[]; colors=[]
    for i in range(k):
        out += ['0']*p[i]; colors += ['A']*p[i]
        out += ['0']*c[i]; colors += ['B']*c[i]
        out += ['1']; colors += ['A']
        out += ['0']*(p[i]-c[i]); colors += ['B']*(p[i]-c[i])
        out += ['1']; colors += ['B']
    out += ['0']*p[k]; colors += ['A']*p[k]
    out += ['0']*p[k]; colors += ['B']*p[k]
    w=''.join(out)
    assert ''.join(ch for ch,col in zip(w,colors) if col=='A')==root
    assert ''.join(ch for ch,col in zip(w,colors) if col=='B')==root
    return w

def gaps(w):
    r=[]; z=0
    for ch in w:
        if ch=='0': z+=1
        else: r.append(z); z=0
    r.append(z); return tuple(r)

def is_shuffle_square(w):
    n=len(w)//2
    for inds in combinations(range(len(w)),n):
        S=set(inds)
        if ''.join(w[i] for i in range(len(w)) if i in S)==''.join(w[i] for i in range(len(w)) if i not in S): return True
    return False

def brute_B(n,k):
    t=0
    for ones in combinations(range(2*n),2*k):
        w=['0']*(2*n)
        for i in ones:w[i]='1'
        t+=is_shuffle_square(''.join(w))
    return t

cases=0
for k in range(1,5):
    for n in range(k,11):
        seen={}
        for p in compositions(n-k,k+1):
            for c in itertools.product(*[range(x+1) for x in p[:-1]]):
                w=construct(p,c); g=gaps(w)
                pp=[]; cc=[]
                for i in range(k):
                    pp.append((g[2*i]+g[2*i+1])//2); cc.append((g[2*i]-g[2*i+1])//2)
                pp.append(g[-1]//2)
                assert tuple(pp)==p and tuple(cc)==c and g[-1]%2==0
                assert w not in seen
                seen[w]=(p,c); cases+=1
        assert len(seen)==comb(n+k,2*k)
expected={1:[1,1],2:[1,4,1],3:[1,10,10,1],4:[1,19,42,19,1],5:[1,31,128,128,31,1]}
for n,row in expected.items(): assert [brute_B(n,k) for k in range(n+1)]==row
for n in range(1,100):
    exact=3*n*(n-1)//2+1; lower=comb(n+1,2)
    assert lower<=exact<=comb(2*n,2)
print(f'VERIFY_OK constructive_cases={cases} k=1..4_n<=10 brute_fixed_weight_n<=5 source_k1_formula_n<=99 lower_count=binom(n+k,2k)')
