#!/usr/bin/env python3
"""Finite exact checks for sharp compatibility-witness size in binary lazy CA."""
from itertools import combinations

def compatible(S, p, U):
    U = set(U)
    S1 = {s for s in S if p[s] == 1}
    if not U or not U.issubset(S1):
        return False
    copies = {}
    for t in U:
        for s in S:
            z=s+t
            if z in copies and copies[z]!=p[s]:
                return False
            copies[z]=p[s]
    for z in S-U:
        if z in copies and copies[z]!=p[z]:
            return False
    return True

def test_family(k):
    S0={-2,0,2}
    T={5+2*j for j in range(k)}
    S=S0|T
    p={s:int(s in T) for s in S}
    assert len(S)==k+3
    assert compatible(S,p,T)
    count=0
    for mask in range(1,1<<k):
        U={5+2*j for j in range(k) if mask>>j&1}
        got=compatible(S,p,U)
        assert got==(U==T), (k,mask,U)
        count+=1
    # An explicit finite local witness: target output p at each site of S.
    SS={u+v for u in S for v in S}
    prescribed={}
    for t in T:
        for s in S:
            z=t+s
            val=p[s]
            assert z not in prescribed or prescribed[z]==val
            prescribed[z]=val
    q={z:prescribed.get(z,0) for z in SS}
    # Compare each translated pattern to p and all zero sites.
    for t in T:
        assert all(q[t+s]==p[s] for s in S)
    for s in S0:
        assert q[s]==0
        assert any(q[s+u]!=p[u] for u in S)
    # The one-step evolution on S equals p; the second step flips origin.
    def phi(x,s):
        return 1 if all(x[s+u]==p[u] for u in S) else x[s]
    out={s:phi(q,s) for s in S}
    assert out==p and out[0]==0 and all(out[u]==p[u] for u in S)
    return count

def test_small_ambient():
    # Enumerate supports in [-4,4] with |S|<=4, p(0)=0,
    # and independently check that no minimum compatible cardinal > 1 occurs.
    coords=[s for s in range(-4,5) if s]
    cases=0
    for m in range(1,5):
        for others in combinations(coords,m-1):
            S={0,*others}
            coords1=sorted(others)
            for mask in range(1<<len(coords1)):
                T={coords1[j] for j in range(len(coords1)) if mask>>j&1}
                p={s:int(s in T) for s in S}
                all_compatible=any(compatible(S,p,{t}) for t in T)
                # Search all subsets without relying on graph closure theorem.
                for mask2 in range(1,1<<len(T)):
                    U={t for j,t in enumerate(sorted(T)) if mask2>>j&1}
                    assert not compatible(S,p,U) or all_compatible, (S,p,U)
                cases+=1
    return cases

def test_graph_lemma():
    # For all small supports, compare graph-closure criterion to compatibility
    # for every subset of an already compatible full active fiber.
    coords=[-4,-3,-2,-1,1,2,3,4]
    cases=0
    for size in (2,3,4,5,6):
        for others in combinations(coords,size-1):
            S={0,*others}
            for bits in range(1<<len(others)):
                T={others[j] for j in range(len(others)) if bits>>j&1}
                p={s:int(s in T) for s in S}
                if not T or not compatible(S,p,T):continue
                S0=S-T
                for submask in range(1,1<<len(T)):
                    U={t for j,t in enumerate(sorted(T)) if submask>>j&1}
                    is_closed=not any((s-t in S0) for t in U for s in T-U)
                    assert compatible(S,p,U)==is_closed, (S,T,U)
                    cases+=1
    return cases

if __name__=='__main__':
    full=sum(test_family(k) for k in range(2,11))
    amb=test_small_ambient()
    graph=test_graph_lemma()
    print('PASS family-subsets:',full)
    print('PASS small-ambient patterns:',amb)
    print('PASS graph-closure equivalences:',graph)
    print('PASS total assertions tested:',full+amb+graph)
