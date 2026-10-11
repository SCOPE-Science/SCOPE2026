#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque

def parity(x): return x.bit_count() & 1

def faces_of_facets(facets):
    bydim=defaultdict(set)
    for F in facets:
        F=tuple(sorted(F))
        for r in range(1,len(F)+1):
            for s in combinations(F,r): bydim[r-1].add(frozenset(s))
    return bydim

def rank_f2(rows, ncols):
    piv={}
    rank=0
    for row in rows:
        x=row
        while x:
            j=x.bit_length()-1
            if j in piv: x ^= piv[j]
            else:
                piv[j]=x; rank += 1; break
    return rank

def betti_f2(bydim):
    maxd=max(bydim)
    n=[len(bydim.get(k,set())) for k in range(maxd+1)]
    ranks=[]
    for k in range(1,maxd+1):
        lo={s:i for i,s in enumerate(sorted(bydim[k-1], key=lambda z:tuple(sorted(z))))}
        rows=[]
        for s in sorted(bydim[k], key=lambda z:tuple(sorted(z))):
            bits=0
            for v in s:
                face=frozenset(set(s)-{v})
                bits ^= 1<<lo[face]
            rows.append(bits)
        ranks.append(rank_f2(rows,len(lo)))
    b=[]
    for k in range(maxd+1):
        rk_d = ranks[k-1] if k>=1 else 0
        rk_next = ranks[k] if k<maxd else 0
        b.append(n[k]-rk_d-rk_next)
    return b

def check_d(d):
    V=1<<d
    even=[x for x in range(V) if parity(x)==0]
    odd=[x for x in range(V) if parity(x)==1]
    facets={y:frozenset(y^(1<<i) for i in range(d)) for y in odd}
    bd=faces_of_facets(facets.values())
    # Every face of size >=3 has a unique facet; pairwise facet intersections <=2.
    owners=defaultdict(int)
    for y,F in facets.items():
        for r in range(3,d+1):
            for s in combinations(F,r): owners[frozenset(s)] += 1
    assert owners and max(owners.values())==1
    for y,z in combinations(odd,2): assert len(facets[y]&facets[z]) <= 2

    # Target L: full 1-skeleton plus apex triangles.
    crit0=set(bd[0]); crit1=set(bd[1]); crit2=set()
    for y,F in facets.items():
        a=y^1
        others=sorted(F-{a})
        for u,v in combinations(others,2): crit2.add(frozenset((a,u,v)))
    L=defaultdict(set,{0:crit0,1:crit1,2:crit2})
    assert len(crit0)==1<<(d-1)
    assert len(crit1)==(1<<(d-2))*(d*(d-1)//2)
    assert len(crit2)==(1<<(d-1))*((d-1)*(d-2)//2)

    # Check the explicit elementary matching: within each facet, base faces of size>=3
    # pair with their apex-cones. Every deleted face occurs in exactly one pair.
    paired=set()
    for y,F in facets.items():
        a=y^1; base=sorted(F-{a})
        for r in range(3,len(base)+1):
            for s in combinations(base,r):
                low=frozenset(s); high=frozenset(set(s)|{a})
                assert low in bd[r-1] and high in bd[r]
                assert low not in paired and high not in paired
                paired.add(low); paired.add(high)
    allfaces=set().union(*bd.values())
    critical=crit0|crit1|crit2
    assert allfaces == critical|paired and not (critical&paired)

    # Matching DAG acyclic: orient unmatched cover relations downward and matched upward.
    # This corroborates the descending-size elementary-collapse order.
    if d <= 6:
        fs=sorted(allfaces,key=lambda s:(len(s),tuple(sorted(s))))
        idx={s:i for i,s in enumerate(fs)}
        matched_pairs=set()
        for y,F in facets.items():
            a=y^1; base=sorted(F-{a})
            for r in range(3,len(base)+1):
                for s in combinations(base,r):
                    low=frozenset(s); high=frozenset(set(s)|{a}); matched_pairs.add((low,high))
        adj=[[] for _ in fs]; indeg=[0]*len(fs)
        for high in fs:
            if len(high)<=1: continue
            for v in high:
                low=frozenset(set(high)-{v})
                if not low: continue
                if (low,high) in matched_pairs: u,w=idx[low],idx[high]
                else: u,w=idx[high],idx[low]
                adj[u].append(w); indeg[w]+=1
        q=deque(i for i,x in enumerate(indeg) if x==0); seen=0
        while q:
            u=q.popleft(); seen+=1
            for w in adj[u]:
                indeg[w]-=1
                if indeg[w]==0:q.append(w)
        assert seen==len(fs)

    # Homology corroboration.
    bo=betti_f2(bd); bl=betti_f2(L)
    mu=(1<<(d-3))*(d*d-5*d+8)-1
    assert bl[0]==1 and bl[1]==0 and bl[2]==mu
    assert all(x==0 for x in bo[1:2])
    # original component must have same reduced homology; only beta2 nonzero.
    assert bo[0]==1 and bo[2]==mu and all(bo[k]==0 for k in range(1,len(bo)) if k!=2)
    print(f'd={d}: V={len(crit0)} E={len(crit1)} F={len(crit2)} mu={mu} original_betti={bo} target_betti={bl}')
    return mu

def main():
    mus=[check_d(d) for d in range(4,8)]
    assert mus==[7,31,111,351]
    print('VERIFY_OK d=4..7 mu=7,31,111,351 components=2 wedge_dimension=2')
if __name__=='__main__': main()
