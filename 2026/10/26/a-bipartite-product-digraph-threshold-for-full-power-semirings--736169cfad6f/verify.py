"""Independent finite checks for a finite-basis dichotomy in short nilpotent semigroups.

Run with: python3 verify.py
This checks finite graph-homomorphism instances; infinite claims require the proof.
"""
from itertools import product


def digraph(n, mask, loops=False):
    possible = [(u,v) for u in range(n) for v in range(n) if loops or u != v]
    return frozenset(e for i,e in enumerate(possible) if mask & (1 << i))


def maps_to(n, edges, target_vertices, target_edges):
    if n == 0:
        return True
    for seq in product(range(target_vertices), repeat=n):
        if all((seq[u], seq[v]) in target_edges for u,v in edges):
            return True
    return False


def is_bipartite(n, edges):
    neighbors = [set() for _ in range(n)]
    for u,v in edges:
        if u == v: return False
        neighbors[u].add(v); neighbors[v].add(u)
    color = {}
    for root in range(n):
        if root in color: continue
        color[root] = 0
        queue = [root]
        for v in queue:
            for w in neighbors[v]:
                if w not in color:
                    color[w] = 1-color[v]; queue.append(w)
                elif color[w] == color[v]: return False
    return True


def has_two_walk(n, edges):
    return any((u,v) in edges and (v,w) in edges
               for u in range(n) for v in range(n) for w in range(n))


def odd_almost_alternating(n):
    assert n >= 3 and n % 2 == 1
    return frozenset([(i,i+1) if i % 2 == 0 else (i+1,i)
                     for i in range(n-1)] + [(n-1,0)])


def induced_without(n, edges, remove):
    verts = [v for v in range(n) if v != remove]
    loc = {v:i for i,v in enumerate(verts)}
    return frozenset((loc[u],loc[v]) for u,v in edges
                     if u != remove and v != remove)


def check():
    # Check the five-element semigroup's associative multiplication directly.
    elements = range(5)             # a,b,c,z,0
    zero = 4
    def mul(x,y):
        return 3 if (x,y) in {(0,1),(1,2)} else zero
    assert all(mul(mul(x,y),z)==mul(x,mul(y,z))
               for x,y,z in product(elements, repeat=3))
    assert mul(0,1)==3 and mul(1,2)==3
    assert all(mul(x,x)==zero for x in elements)
    # Adding the single product a*c=z preserves associativity.
    def mul_plus(x,y):
        return 3 if (x,y) in {(0,1),(1,2),(0,2)} else zero
    assert all(mul_plus(mul_plus(x,y),z)==mul_plus(x,mul_plus(y,z))
               for x,y,z in product(elements, repeat=3))

    path2 = frozenset({(0,1),(1,2)})
    # For finite targets on at most three vertices, enumerate every loopless
    # bipartite nonempty support and classify the directed-two-walk case.
    counted = [0,0]
    for n in range(2,4):
        for mask in range(1,1 << (n*(n-1))):
            D = digraph(n,mask)
            if not is_bipartite(n,D): continue
            walk = has_two_walk(n,D)
            counted[int(walk)] += 1
            if not walk:
                # Universal finite obstruction: one directed two-walk.
                for hn in range(1,4):
                    for hmask in range(1 << (hn*hn)):
                        H = digraph(hn,hmask,loops=True)
                        assert maps_to(hn,H,n,D) == (not has_two_walk(hn,H))
                assert not maps_to(3,path2,n,D)
            else:
                assert maps_to(3,path2,n,D)
                for k in [3,5,7]:
                    H = odd_almost_alternating(k)
                    assert not maps_to(k,H,n,D)
    # Arbitrarily long oriented odd-cycle pattern checked at finite lengths.
    for k in [3,5,7,9]:
        H = odd_almost_alternating(k)
        assert not maps_to(k,H,3,path2)
        for v in range(k):
            assert maps_to(k-1,induced_without(k,H,v),3,path2)
    # The single extra arc a->c makes a transitive tournament. Its CSP is
    # exactly the absence of a directed walk of length three.
    T3 = frozenset({(0,1),(1,2),(0,2)})
    def has_three_walk(n, E):
        return any((a,b) in E and (b,c) in E and (c,d) in E
                   for a,b,c,d in product(range(n),repeat=4))
    for hn in range(1,4):
        for mask in range(1 << (hn*hn)):
            H = digraph(hn,mask,loops=True)
            assert maps_to(hn,H,3,T3) == (not has_three_walk(hn,H))
    walk3 = frozenset({(0,1),(1,2),(2,3)})
    assert not maps_to(4,walk3,3,T3)
    for v in range(4):
        assert maps_to(3,induced_without(4,walk3,v),3,T3)
    assert all(counted)
    print('VERIFY_OK bipartite finite targets:',counted,
          'odd obstructions tested through size 9')

if __name__=='__main__':
    check()
