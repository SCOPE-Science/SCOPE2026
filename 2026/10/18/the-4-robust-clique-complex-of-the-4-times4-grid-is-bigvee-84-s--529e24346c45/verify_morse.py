#!/usr/bin/env python3
"""Complete finite discrete-Morse proof for the 4-robust clique complex of P4 x P4.

Run with Python 3 and no nonstandard packages.
"""
from collections import Counter, deque
from itertools import combinations

SIDE = 4
V = SIDE * SIDE
FULL = 1 << V


def grid_edges():
    e = set()
    for r in range(SIDE):
        for c in range(SIDE):
            v = SIDE * r + c
            if r + 1 < SIDE:
                e.add((v, v + SIDE))
            if c + 1 < SIDE:
                e.add((v, v + 1))
    return e


def all_faces():
    adj = [0] * V
    edges = grid_edges()
    assert len(edges) == 24
    for a,b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    # Exact independent-set dynamic program: alpha(S) by vertex deletion.
    alpha = [0] * FULL
    for s in range(1,FULL):
        pivot = s & -s
        v = pivot.bit_length() - 1
        remainder = s - pivot
        alpha[s] = max(alpha[remainder], 1 + alpha[remainder & ~adj[v]])
    faces = [s for s in range(FULL) if alpha[s] < 4]
    # Separate characterization: no independent 4-subset.
    forbidden = set()
    for t in combinations(range(V),4):
        if all(not ((adj[a] >> b) & 1) for a,b in combinations(t,2)):
            forbidden.add(sum(1 << u for u in t))
    # Direct 4-subset test (independent from dynamic program) for every face candidate.
    for s in range(FULL):
        flags = any(s & t == t for t in forbidden)
        assert flags == (alpha[s] >= 4)
    return faces,len(forbidden)


def certify():
    faces,forbidden_count = all_faces()
    by_dim = Counter(s.bit_count()-1 for s in faces)
    assert by_dim == {-1:1,0:16,1:120,2:560,3:1415,4:1788,5:912}
    assert len(faces) == 4812
    membership=set(faces)
    unmatched=set(faces)
    pairs=[]
    # Lexicographic staged toggles, with one pair for each eligible lower face.
    for vertex in range(V):
        bit = 1 << vertex
        for lower in faces:
            if (lower & bit) or (lower not in unmatched):
                continue
            upper=lower|bit
            if upper in unmatched:
                assert upper in membership
                unmatched.remove(lower)
                unmatched.remove(upper)
                pairs.append((lower,upper))
    assert len(pairs) == 2364
    assert len(unmatched) == 84
    assert Counter(s.bit_count()-1 for s in unmatched)=={5:84}
    assert 0 not in unmatched
    assert not(any(s == t for s,t in pairs))
    # Full Hasse diagram, each cover oriented up if matched and down otherwise.
    is_pair=set(pairs)
    idx={s:i for i,s in enumerate(faces)}
    arcs=[[] for _ in faces]
    indeg=[0]*len(faces)
    count=0
    for upper in faces:
        rest=upper
        while rest:
            bit = rest & -rest
            rest -= bit
            lower=upper-bit
            assert lower in membership
            if (lower,upper) in is_pair:
                a,b=idx[lower],idx[upper]
            else:
                a,b=idx[upper],idx[lower]
            arcs[a].append(b)
            indeg[b]+=1
            count+=1
    assert count==22008
    queue=deque(i for i,d in enumerate(indeg) if not d)
    processed=0
    while queue:
        a=queue.popleft()
        processed+=1
        for b in arcs[a]:
            indeg[b]-=1
            if indeg[b]==0:
                queue.append(b)
    assert processed==len(faces)==4812, (processed,len(faces))
    # Exactly one matched edge incident to the empty face; remove it
    # to obtain an ordinary (nonaugmented) acyclic matching.
    empty_matches=[p for p in pairs if p[0]==0]
    assert len(empty_matches)==1 and empty_matches[0][1].bit_count()==1
    print('VERIFY_OK', 'forbidden4='+str(forbidden_count),
          'faces='+str(len(faces)),
          'f_vector='+str([by_dim[d] for d in range(6)]),
          'matched_pairs='+str(len(pairs)),
          'critical5='+str(len(unmatched)),
          'hasse_arcs='+str(count),
          'toposort='+str(processed),
          'ordinary_critical0=1', 'ordinary_critical5=84')


if __name__=='__main__':
    certify()
