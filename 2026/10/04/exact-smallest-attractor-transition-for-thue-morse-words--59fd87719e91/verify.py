from itertools import combinations
from pathlib import Path
import math

def thue(m):
    s='0'
    for _ in range(m):
        s=s+''.join('1' if c=='0' else '0' for c in s)
    return s

def factor_cover_edges(s):
    n=len(s); covers={}
    for L in range(1,n+1):
        window=(1<<L)-1
        for i in range(n-L+1):
            f=s[i:i+L]
            covers[f]=covers.get(f,0)|(window<<i)
    edges=sorted(set(covers.values()), key=lambda x:(x.bit_count(),x))
    mins=[]
    for e in edges:
        if not any((m & e)==m for m in mins): mins.append(e)
    assert all(any((m&e)==m for m in mins) for e in edges)
    return covers,mins

def enumerate_attractors(s,k):
    covers,mins=factor_cover_edges(s); sols=[]
    for c in combinations(range(len(s)),k):
        M=sum(1<<i for i in c)
        if all(M&e for e in mins): sols.append(c)
    return covers,mins,sols

def direct_is_attractor(s,c):
    G=set(c); seen={}
    for L in range(1,len(s)+1):
        for i in range(len(s)-L+1):
            f=s[i:i+L]
            if f not in seen: seen[f]=False
            if any(i<=g<i+L for g in G): seen[f]=True
    return all(seen.values())

expected={4:87,5:40,6:32}; total=0; got=[]
for m in (4,5,6):
    s=thue(m)
    for k in (1,2,3):
        _,_,sol=enumerate_attractors(s,k); total+=math.comb(len(s),k); assert not sol
    covers,mins,sol=enumerate_attractors(s,4); total+=math.comb(len(s),4)
    assert len(sol)==expected[m]
    assert all(direct_is_attractor(s,c) for c in sol)
    got += [(m,)+tuple(x+1 for x in c) for c in sol]
    print(f't_{m}: length={len(s)} factors={len(covers)} minimal_edges={len(mins)} min_attractors={len(sol)}')
A=(16,17); B=(24,25); C=(32,33); E=(40,41); D=(48,49)
pred={tuple(sorted((a,b,c,d))) for mid in (B,E) for a in A for b in mid for c in C for d in D}
actual={r[1:] for r in got if r[0]==6}; assert actual==pred and len(actual)==32
lines=Path(__file__).with_name('ATTRACTORS.tsv').read_text(encoding='utf-8').splitlines()
stored=[tuple(map(int,x.split('\t'))) for x in lines[1:]]
assert stored==got
print(f'VERIFY_OK transition_counts=87,40,32 t6_classification=32 total_subsets_checked={total}')
