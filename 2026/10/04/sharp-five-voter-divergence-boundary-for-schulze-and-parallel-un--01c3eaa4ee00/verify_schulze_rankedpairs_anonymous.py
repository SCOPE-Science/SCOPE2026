#!/usr/bin/env python3
from itertools import permutations, combinations
from collections import Counter, defaultdict
from fractions import Fraction
from math import factorial
from functools import lru_cache

C=range(4)
ORDERS=tuple(permutations(C))
OID={o:i for i,o in enumerate(ORDERS)}
PAIRS=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
CPERMS=ORDERS

CONTRIB=[]
for o in ORDERS:
    pos={x:i for i,x in enumerate(o)}
    CONTRIB.append(tuple(1 if pos[a]<pos[b] else -1 for a,b in PAIRS))

def compositions(n,k):
    for bars in combinations(range(n+k-1),k-1):
        prev=-1; out=[]
        for b in bars+(n+k-1,):
            out.append(b-prev-1); prev=b
        yield tuple(out)

def margin_tuple(counts):
    return tuple(sum(counts[i]*CONTRIB[i][e] for i in range(24)) for e in range(6))

def mat(v):
    d=[[0]*4 for _ in C]
    for x,(a,b) in zip(v,PAIRS): d[a][b]=x; d[b][a]=-x
    return d

def simple_paths(a,b):
    mids=[x for x in C if x not in (a,b)]
    yield (a,b)
    for x in mids: yield (a,x,b)
    for x,y in permutations(mids,2): yield (a,x,y,b)

@lru_cache(None)
def schulze(v):
    d=mat(v)
    p=[[0]*4 for _ in C]
    for a in C:
        for b in C:
            if a==b: continue
            best=0
            for path in simple_paths(a,b):
                strength=min(max(d[path[i]][path[i+1]],0) for i in range(len(path)-1))
                best=max(best,strength)
            p[a][b]=best
    return frozenset(a for a in C if all(p[a][b]>=p[b][a] for b in C if b!=a))

@lru_cache(None)
def ranked_pairs_tideman(v):
    d=mat(v)
    groups=defaultdict(list)
    for a,b in PAIRS:
        if d[a][b]>0: groups[d[a][b]].append((a,b))
        else: groups[-d[a][b]].append((b,a))
    winners=set()
    # Independent implementation of Tideman's original ranking-elimination description.
    def rec(strengths_i, rankings):
        if strengths_i==len(strengths):
            winners.update(r[0] for r in rankings)
            return
        g=groups[strengths[strengths_i]]
        seen=set()
        for order in permutations(g):
            cur=tuple(rankings)
            for a,b in order:
                consistent=tuple(r for r in cur if r.index(a)<r.index(b))
                if consistent:
                    cur=consistent
            if cur not in seen:
                seen.add(cur)
                rec(strengths_i+1,cur)
    strengths=sorted(groups,reverse=True)
    rec(0,ORDERS)
    return frozenset(winners)

def multinomial(c):
    z=factorial(sum(c))
    for x in c: z//=factorial(x)
    return z

def relabel_margin(v,p):
    d=mat(v); z=[[0]*4 for _ in C]
    for a in C:
        for b in C: z[p[a]][p[b]]=d[a][b]
    return tuple(z[a][b] for a,b in PAIRS)

def canon_margin(v):
    return min(relabel_margin(v,p) for p in CPERMS)

hist=Counter(); ahist=Counter(); diff_anonymous=[]; types=Counter(); type_anon=Counter()
for c in compositions(5,24):
    v=margin_tuple(c)
    S=schulze(v); R=ranked_pairs_tideman(v)
    w=multinomial(c)
    hist[(len(S),len(R),S==R)] += w
    ahist[(len(S),len(R),S==R)] += 1
    if S!=R:
        assert R < S
        diff_anonymous.append(c)
        cm=canon_margin(v)
        types[cm] += w
        type_anon[cm] += 1

assert len(diff_anonymous)==576
assert sum(hist.values())==24**5==7962624
assert hist==Counter({
    (1,1,True):6858144,
    (2,2,True):275760,
    (3,3,True):591120,
    (4,4,True):185760,
    (3,2,False):51840,
})
assert Fraction(51840,24**5)==Fraction(5,768)
assert types==Counter({
    (-3,-3,1,-1,-1,-1):11520,
    (-3,-1,1,1,-1,-1):40320,
})
assert type_anon==Counter({
    (-3,-3,1,-1,-1,-1):168,
    (-3,-1,1,1,-1,-1):408,
})
# Each canonical margin type has 24 candidate relabelings; exact fibers are uniform.
exact=Counter(); exactw=Counter()
for c in diff_anonymous:
    v=margin_tuple(c); exact[v]+=1; exactw[v]+=multinomial(c)
assert len(exact)==48
assert Counter(exact.values())==Counter({7:24,17:24})
assert Counter(exactw.values())==Counter({480:24,1680:24})

# Three-candidate structural lower bound tested on all odd margin triples realizable for 1,3,5 voters.
def rule3(v):
    # v=(m01,m02,m12), nonzero odd margins.
    d=[[0]*3 for _ in range(3)]
    for x,(a,b) in zip(v,((0,1),(0,2),(1,2))): d[a][b]=x;d[b][a]=-x
    # Schulze by all simple paths.
    ps=[[0]*3 for _ in range(3)]
    for a in range(3):
        for b in range(3):
            if a==b: continue
            other=3-a-b
            ps[a][b]=max(max(d[a][b],0),min(max(d[a][other],0),max(d[other][b],0)))
    S=frozenset(a for a in range(3) if all(ps[a][b]>=ps[b][a] for b in range(3) if b!=a))
    # Tideman ranking-elimination exact over 6 rankings.
    ranks=tuple(permutations(range(3))); groups=defaultdict(list)
    for a,b in ((0,1),(0,2),(1,2)):
        if d[a][b]>0:groups[d[a][b]].append((a,b))
        else:groups[-d[a][b]].append((b,a))
    W=set()
    def rec3(si,cur):
        if si==len(strengths): W.update(r[0] for r in cur); return
        for ordg in permutations(groups[strengths[si]]):
            cc=cur
            for a,b in ordg:
                nxt=tuple(r for r in cc if r.index(a)<r.index(b))
                if nxt: cc=nxt
            rec3(si+1,cc)
    strengths=sorted(groups,reverse=True); rec3(0,ranks)
    return S,frozenset(W)
for n in (1,3,5):
    orders3=tuple(permutations(range(3)))
    # Anonymous enumeration enough to cover all profiles exactly.
    cont=[]
    for o in orders3:
        p={x:i for i,x in enumerate(o)}
        cont.append(tuple(1 if p[a]<p[b] else -1 for a,b in ((0,1),(0,2),(1,2))))
    for c in compositions(n,6):
        v=tuple(sum(c[i]*cont[i][e] for i in range(6)) for e in range(3))
        assert rule3(v)[0]==rule3(v)[1]

print('VERIFY_OK')
print('anonymous_profiles',98280)
print('anonymous_divergent',576)
print('labeled_profiles',24**5)
print('labeled_divergent',51840,'probability','5/768')
print('histogram',dict(hist))
print('margin_types',dict(types))
print('anonymous_margin_types',dict(type_anon))
print('exact_margin_matrices',len(exact),'fiber_counts',dict(Counter(exact.values())),'fiber_weights',dict(Counter(exactw.values())))
