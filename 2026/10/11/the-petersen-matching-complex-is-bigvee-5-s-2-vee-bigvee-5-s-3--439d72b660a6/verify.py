#!/usr/bin/env python3
"""Exact verifier for the Petersen-graph ordinary matching complex.
Pure Python standard library; no network access or external packages required.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

# Petersen graph: outer 5-cycle, five spokes, inner pentagram.
def petersen_edges():
    E=[]
    for i in range(5): E.append(tuple(sorted((i,(i+1)%5))))
    for i in range(5): E.append((i,5+i))
    for i in range(5): E.append(tuple(sorted((5+i,5+((i+2)%5)))))
    return sorted(set(E))

EDGES=petersen_edges()
M=len(EDGES)
ORDER=[2,3,8,13,11,12,14,6,1,0,10,7,5,4,9]
EXPECTED_FVEC={0:15,1:75,2:145,3:90,4:6}
EXPECTED_CRITICAL={0:1,2:5,3:5}
EXPECTED_GF2_RANKS={1:14,2:61,3:79,4:6}


def is_matching(mask):
    used=0
    for j,(u,v) in enumerate(EDGES):
        if (mask>>j)&1:
            b=(1<<u)|(1<<v)
            if used & b: return False
            used |= b
    return True

FACES={mask for mask in range(1,1<<M) if is_matching(mask)}


def greedy_matching():
    alive=set(FACES)
    pairs=[]
    for e in ORDER:
        lows=sorted(m for m in alive if not ((m>>e)&1) and (m|(1<<e)) in alive)
        for lo in lows:
            hi=lo|(1<<e)
            if lo in alive and hi in alive:
                alive.remove(lo); alive.remove(hi)
                pairs.append((lo,hi))
    return alive,pairs

CRITICAL,PAIRS=greedy_matching()
LOW_TO_HIGH={lo:hi for lo,hi in PAIRS}


def incidence(hi,lo):
    removed=hi^lo
    assert removed and removed&(removed-1)==0 and (lo & ~hi)==0
    j=removed.bit_length()-1
    bits=[x for x in range(M) if (hi>>x)&1]
    return 1 if bits.index(j)%2==0 else -1


def check_acyclic():
    # Hasse graph on nonempty faces. Ordinary cover arrows go high -> low;
    # matched covers are reversed.
    adj={f:[] for f in FACES}; indeg={f:0 for f in FACES}
    covers=0
    for hi in FACES:
        if hi.bit_count()==1: continue
        for j in range(M):
            if (hi>>j)&1:
                lo=hi^(1<<j)
                assert lo in FACES
                covers += 1
                if LOW_TO_HIGH.get(lo)==hi:
                    a,b=lo,hi
                else:
                    a,b=hi,lo
                adj[a].append(b); indeg[b]+=1
    q=deque([x for x,d in indeg.items() if d==0]); seen=0
    while q:
        x=q.popleft(); seen+=1
        for y in adj[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    return covers, seen==len(FACES)


def gf2_rank(columns):
    piv={}; r=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv: x ^= piv[p]
            else:
                piv[p]=x; r+=1; break
    return r


def chain_ranks_gf2():
    bydim=defaultdict(list)
    for f in FACES: bydim[f.bit_count()-1].append(f)
    for k in bydim: bydim[k].sort()
    ranks={}
    for k in sorted(bydim):
        if k==0: continue
        lower={m:i for i,m in enumerate(bydim[k-1])}
        cols=[]
        for hi in bydim[k]:
            col=0
            for j in range(M):
                if (hi>>j)&1:
                    col ^= 1<<lower[hi^(1<<j)]
            cols.append(col)
        ranks[k]=gf2_rank(cols)
    return bydim,ranks

# Exact integral gradient-path substitution. For a matched lower cell a paired
# with b, the chain relation d(b)=0 after cancellation gives
# a = -(1/[b:a]) sum_{d != a} [b:d] d. Acyclicity makes recursion finite.
@lru_cache(None)
def expand_lower(a):
    if a not in LOW_TO_HIGH:
        return {a:1}
    b=LOW_TO_HIGH[a]
    u=incidence(b,a)
    out=defaultdict(int)
    for j in range(M):
        if (b>>j)&1:
            d=b^(1<<j)
            if d==a: continue
            c=incidence(b,d)
            for t,v in expand_lower(d).items():
                out[t] += -(c*v)//u
    return {t:v for t,v in out.items() if v}


def morse_boundary(critical_hi, critical_lows):
    out=defaultdict(int)
    for j in range(M):
        if (critical_hi>>j)&1:
            d=critical_hi^(1<<j)
            c=incidence(critical_hi,d)
            for t,v in expand_lower(d).items(): out[t] += c*v
    return [out.get(t,0) for t in critical_lows]


def main():
    assert len(EDGES)==15 and len(FACES)==331
    fvec=Counter(f.bit_count()-1 for f in FACES)
    assert dict(sorted(fvec.items()))==EXPECTED_FVEC
    assert len(PAIRS)==160 and 2*len(PAIRS)+len(CRITICAL)==len(FACES)
    crit=Counter(f.bit_count()-1 for f in CRITICAL)
    assert dict(sorted(crit.items()))==EXPECTED_CRITICAL
    covers,acyclic=check_acyclic()
    assert covers==975 and acyclic

    bydim,ranks=chain_ranks_gf2()
    assert ranks==EXPECTED_GF2_RANKS
    betti={}
    for k in sorted(bydim):
        b=len(bydim[k])-ranks.get(k,0)-ranks.get(k+1,0)
        if k==0: b-=1
        betti[k]=b
    assert betti=={0:0,1:0,2:5,3:5,4:0}

    c2=sorted(f for f in CRITICAL if f.bit_count()==3)
    c3=sorted(f for f in CRITICAL if f.bit_count()==4)
    matrix=[morse_boundary(x,c2) for x in c3]
    assert matrix==[[0]*5 for _ in range(5)]

    print('VERIFY_OK')
    print('edges=',EDGES)
    print('edge_order=',ORDER)
    print('faces=',len(FACES),'f_vector=',[fvec[i] for i in range(5)])
    print('hasse_covers=',covers,'matching_pairs=',len(PAIRS),'acyclic=',acyclic)
    print('critical_dimensions=',dict(sorted(crit.items())))
    print('critical_2_masks=',c2)
    print('critical_3_masks=',c3)
    print('morse_d3_to_d2=',matrix)
    print('gf2_boundary_ranks=',ranks)
    print('reduced_gf2_betti=',betti)

if __name__=='__main__': main()
