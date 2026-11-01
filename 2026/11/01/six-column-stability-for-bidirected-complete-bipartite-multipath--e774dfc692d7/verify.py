#!/usr/bin/env python3
"""Finite universal-fiber certificate for a bidirected complete-bipartite multipath theorem.

Only Python's standard library is required.  The mathematical proof explains why
checking the 312 patterns on four symbolic exterior columns applies for every q>=6.
"""
from itertools import combinations
from collections import Counter, deque


def arrows(q):
    # The first half points from the two left vertices to the right side;
    # the second half points in the other direction.
    return ([(a, 2+j) for a in range(2) for j in range(q)] +
            [(2+j, a) for a in range(2) for j in range(q)])


def is_multipath(arcs, selected):
    incoming = {}
    outgoing = {}
    for k in selected:
        u,v = arcs[k]
        if u in outgoing or v in incoming:
            return False
        outgoing[u] = v
        incoming[v] = u
    for u in outgoing:
        seen = set()
        while u in outgoing:
            if u in seen:
                return False
            seen.add(u)
            u = outgoing[u]
    return True


def all_faces(q):
    a = arrows(q)
    fs = [[] for _ in range(5)]
    for k in range(1,5):
        for c in combinations(range(4*q), k):
            if is_multipath(a,c):
                fs[k].append(sum(1<<i for i in c))
    return fs


def toggle_matching(simplices, pivot_positions):
    """Match all remaining toggle pairs, in the given fixed pivot order."""
    remaining = set(simplices)
    matching = []
    for i in pivot_positions:
        bit = 1 << i
        pairs = [(s,s|bit) for s in remaining
                 if not s & bit and (s|bit) in remaining]
        for low, high in pairs:
            remaining.remove(low)
            remaining.remove(high)
        matching.extend(pairs)
    return remaining, matching


def check_directed_acyclic(simplices, matching, positions):
    """Independently test the Hasse orientation for a finite fiber."""
    ss = set(simplices)
    mm = set(matching)
    adjacency = {s:[] for s in ss}
    indeg = {s:0 for s in ss}
    for s in ss:
        for i in positions:
            b = 1<<i
            if not s & b and s|b in ss:
                h = s|b
                x,y = (h,s) if (s,h) in mm else (s,h)
                adjacency[x].append(y)
                indeg[y]+=1
    Q = deque(s for s in ss if indeg[s]==0)
    checked=0
    while Q:
        x=Q.popleft();checked+=1
        for y in adjacency[x]:
            indeg[y]-=1
            if indeg[y]==0:Q.append(y)
    assert checked==len(ss), (checked,len(ss))


def boundary_ranks_mod2(faces):
    ranks = [0]*6
    for k in range(2,5):
        smaller = {s:i for i,s in enumerate(faces[k-1])}
        pivots={}
        for s in faces[k]:
            r=0
            t=s
            while t:
                bit=t&-t
                r^=1<<smaller[s^bit]
                t-=bit
            while r:
                j=r.bit_length()-1
                if j in pivots:r^=pivots[j]
                else:pivots[j]=r;break
        ranks[k]=len(pivots)
    return tuple(len(faces[k])-ranks[k]-ranks[k+1]
                 for k in range(1,5))


def main():
    f = all_faces(6)
    assert tuple(map(len,f[1:])) == (24,192,600,600)
    base = [s for dim in f[1:] for s in dim]
    R,M = toggle_matching(base,range(24))
    assert Counter(s.bit_count() for s in R) == Counter({1:1,4:169})
    check_directed_acyclic(base,M,range(24))
    print('BASE_OK:',len(base),'simplices,',len(M),'matching pairs,',
          'one critical vertex and 169 critical tetrahedra')

    a=arrows(10)
    probe = [i for i,(u,v) in enumerate(a) if (2<=u<8 or 2<=v<8)]
    exterior = [i for i,(u,v) in enumerate(a) if (8<=u or 8<=v)]
    assert len(probe)==24 and len(exterior)==16
    checked=Counter()
    critical_profiles=Counter()
    for s in range(1,5):
        for W in combinations(exterior,s):
            if not is_multipath(a,W):
                continue
            checked[s]+=1
            remaining_capacity=4-s
            simplices=[0]
            for k in range(1,remaining_capacity+1):
                for U in combinations(probe,k):
                    if is_multipath(a,(*W,*U)):
                        simplices.append(sum(1<<i for i in U))
            R,M=toggle_matching(simplices,probe)
            check_directed_acyclic(simplices,M,probe)
            profile=tuple(sorted(Counter(t.bit_count() for t in R).items()))
            assert all(t==remaining_capacity for t in map(int,dict(profile))), (W,profile)
            critical_profiles[(s,profile)]+=1
    assert checked == Counter({1:16,2:80,3:144,4:72}),checked
    assert critical_profiles == Counter({
        (1,((3,71),)):16,
        (2,((2,19),)):56,
        (2,((2,25),)):24,
        (3,((1,5),)):144,
        (4,((0,1),)):72,
    }),critical_profiles
    print('UNIVERSAL_FIBERS_OK:',sum(checked.values()),
          'exhaustive external configurations on four symbolic columns')
    for q in range(2,7):
        f=all_faces(q)
        expected=(4*q,6*q*q-4*q,4*q*(q-1)**2,q*(q-1)**2*(q-2))
        assert tuple(map(len,f[1:]))==expected
        b=boundary_ranks_mod2(f)
        expected_b={2:(1,3,2,0),3:(1,1,6,0),
                    4:(1,0,8,1),5:(1,0,1,32),6:(1,0,0,169)}[q]
        assert b==expected_b,(q,b)
        print('LOW_BOUND_OK:',q,'f=',expected,'mod2_betti=',b)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
