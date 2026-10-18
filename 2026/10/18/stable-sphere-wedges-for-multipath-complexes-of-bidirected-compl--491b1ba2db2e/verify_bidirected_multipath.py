"""Exact finite consistency checks for directed path complexes of bidirected K_{2,n}.
Run with Python 3 standard library; all combinatorial enumerations are complete for
specified small instances, not a proof for unrestricted n.
"""
from itertools import combinations

def complete_faces(n):
    # Hub vertices are 0,1; leaf i is i+2.  Four directed arcs per leaf.
    arcs = [(u,v) for i in range(n) for (u,v) in
            ((0,i+2),(i+2,1),(1,i+2),(i+2,0))]
    by_dim={k:[] for k in range(4)}
    # A multipath has at most one outgoing and incoming arc at each hub,
    # so at most four arcs in total.
    for k in range(1,5):
        for ids in combinations(range(4*n),k):
            edges=[arcs[i] for i in ids]
            if len({u for u,v in edges})!=k or len({v for u,v in edges})!=k:
                continue
            next_vertex={u:v for u,v in edges}
            if any((lambda start: has_cycle(start,next_vertex))(v)
                   for v in next_vertex):
                continue
            by_dim[k-1].append(sum(1<<i for i in ids))
    return by_dim

def has_cycle(start,next_vertex):
    curr=start;seen=set()
    while curr in next_vertex:
        if curr in seen:return True
        seen.add(curr);curr=next_vertex[curr]
    return False

def betti_mod2(by_dim):
    ranks={}
    for k in range(1,4):
        rows={face:i for i,face in enumerate(by_dim[k-1])}
        pivots={}
        for face in by_dim[k]:
            column=0
            for j in range(face.bit_length()):
                if face & (1<<j): column ^= 1<<rows[face^(1<<j)]
            while column:
                p=column.bit_length()-1
                if p not in pivots:
                    pivots[p]=column;break
                column ^= pivots[p]
        ranks[k]=len(pivots)
    return [len(by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0) for k in range(4)]

def formula(n):
    return n**4-8*n**3+19*n*n-14*n+1

for n in range(4,10):
    fs=complete_faces(n)
    counts=[len(fs[k]) for k in range(4)]
    expected=[4*n, 6*n*n-4*n, 4*n*(n-1)**2, n*(n-1)**2*(n-2)]
    assert counts==expected,(n,counts,expected)
    betti=betti_mod2(fs)
    if n>=7:
        assert betti==[1,0,0,formula(n)],(n,betti)
    print('n=%d f=%s mod2_betti=%s predicted_top=%d PASS' %
          (n,counts,betti,formula(n)))
print('FINITE_CHECKS_PASS')
