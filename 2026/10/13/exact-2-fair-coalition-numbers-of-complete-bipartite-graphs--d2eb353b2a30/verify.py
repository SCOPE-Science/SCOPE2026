#!/usr/bin/env python3
from functools import lru_cache

def formula(s,t):
    assert 1 <= s <= t
    if (s,t)==(2,2): return 4
    if s==3 and t in (3,4): return 3
    if s>=4: return s+t-4
    return 2

def adj_K(s,t):
    n=s+t
    A=[0]*n
    for i in range(s):
        for j in range(t):
            A[i] |= 1 << (s+j)
            A[s+j] |= 1 << i
    return A

def fair(mask,A,k=2):
    n=len(A)
    return all(((mask>>v)&1) or ((A[v]&mask).bit_count()==k) for v in range(n))

def exact_partition_opt(s,t):
    A=adj_K(s,t); n=s+t
    F=[False]*(1<<n)
    for m in range(1,1<<n): F[m]=fair(m,A,2)
    best=0
    def valid(blocks):
        L=len(blocks)
        for i,m in enumerate(blocks):
            if F[m] and m.bit_count()==2:
                continue
            if F[m]:
                return False
            ok=False
            for j in range(L):
                if i!=j and (not F[blocks[j]]) and F[m|blocks[j]]:
                    ok=True; break
            if not ok: return False
        return True
    def rec(v,blocks):
        nonlocal best
        if v==n:
            if len(blocks)>best and valid(blocks): best=len(blocks)
            return
        if len(blocks)+(n-v)<=best: return
        bit=1<<v
        for i in range(len(blocks)):
            blocks[i] |= bit
            rec(v+1,blocks)
            blocks[i] ^= bit
        blocks.append(bit); rec(v+1,blocks); blocks.pop()
    rec(0,[])
    return best

def construction(s,t):
    # for s>=4: P=(x1,x2,y1), Q=(x3,y2,y3), then singleton tails
    P={0,1,s+0}
    Q={2,s+1,s+2}
    blocks=[P,Q]
    blocks += [{i} for i in range(3,s)]
    blocks += [{s+j} for j in range(3,t)]
    return blocks

def mask(B):
    m=0
    for v in B:m|=1<<v
    return m

def check_partition(s,t,blocks):
    A=adj_K(s,t)
    masks=[mask(B) for B in blocks]
    assert set().union(*blocks)==set(range(s+t))
    assert sum(len(B) for B in blocks)==s+t
    for i,m in enumerate(masks):
        if fair(m,A,2) and m.bit_count()==2: continue
        assert not fair(m,A,2)
        assert any(i!=j and not fair(masks[j],A,2) and fair(m|masks[j],A,2) for j in range(len(masks)))

# Direct occupancy characterization for proper sets when both shores exceed 2.
occ_checks=0
for s in range(3,7):
    for t in range(s,7):
        A=adj_K(s,t); n=s+t; full=(1<<n)-1
        for m in range(1,1<<n):
            if m==full: continue
            a=(m & ((1<<s)-1)).bit_count()
            b=(m >> s).bit_count()
            assert fair(m,A,2) == (a==2 and b==2)
            occ_checks += 1

profiles=0
for s in range(1,9):
    for t in range(s,9):
        if s+t<=9:
            got=exact_partition_opt(s,t)
            exp=formula(s,t)
            assert got==exp,(s,t,got,exp)
            profiles+=1

constructions=0
for s in range(4,41):
    for t in range(s,41):
        B=construction(s,t)
        assert len(B)==formula(s,t)==s+t-4
        check_partition(s,t,B)
        constructions += 1

print(f"ALL CHECKS PASSED; exhaustive_profiles={profiles}; occupancy_subsets={occ_checks}; construction_profiles={constructions}; construction_range=4..40")
