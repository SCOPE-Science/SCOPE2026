"""Independent finite check of the geometric three-point extension lemma.
Enumerates all ordered triples in prime projective planes and verifies that
side/equality/incidence/collinearity data determine exactly the attainable
fourth-vertex equality and adjacency patterns. Finite checking supplements
but does not replace the projective-plane-axiom proof.
"""
from itertools import product
from collections import defaultdict, Counter

def normalized(v, p):
    a = next((x for x in v if x), None)
    return tuple(x * pow(a, -1, p) % p for x in v) if a else None

def plane(p):
    coords = sorted({normalized(v, p) for v in product(range(p), repeat=3)} - {None})
    m = len(coords)
    adj = [[False] * (2*m) for _ in range(2*m)]
    for i, x in enumerate(coords):
        for j, y in enumerate(coords):
            if sum(a*b for a,b in zip(x,y)) % p == 0:
                adj[i][j+m] = adj[j+m][i] = True
    return m, adj

def geom_signature(t, m, adj):
    # side statuses, equalities, and incidences are remembered individually.
    sig = (tuple(int(x>=m) for x in t),
           tuple((t[i] == t[j], adj[t[i]][t[j]])
                 for i in range(3) for j in range(i)))
    if len(set(t))==3 and (all(x<m for x in t) or all(x>=m for x in t)):
        # Concurrency/collinearity, depending on which part the triple lies in.
        sig += (any(all(adj[v][x] for x in t)
                    for v in range(2*m)),)
    return sig

def extension(t, adj):
    # Only the uncolored pure-graph atomic diagram of fourth vertex matters.
    return frozenset((tuple(v==x for x in t), tuple(adj[v][x] for x in t))
                     for v in range(len(adj)))

def test(p):
    m, adj = plane(p)
    profiles = {}
    sizes = Counter()
    for t in product(range(2*m), repeat=3):
        sig=geom_signature(t,m,adj)
        ext=extension(t,adj)
        if sig in profiles:
            assert profiles[sig] == ext, ('nonuniform triple type',p,t,sig)
        else: profiles[sig] = ext
        sizes[sig]+=1
    pair_sets = {}
    for t in product(range(2*m), repeat=2):
        pair_signature=(tuple(int(x>=m) for x in t),
                        t[0] == t[1], adj[t[0]][t[1]])
        possible=frozenset(geom_signature(t+(w,), m, adj) for w in range(2*m))
        if pair_signature in pair_sets:
            assert pair_sets[pair_signature]==possible, ('nonuniform pair',p,t)
        else: pair_sets[pair_signature]=possible
    single_sets = {}
    for u in range(2*m):
        sig=int(u>=m)
        possible=frozenset((int(u>=m),int(v>=m),u==v,adj[u][v]) for v in range(2*m))
        if sig in single_sets:
            assert single_sets[sig]==possible
        else: single_sets[sig]=possible
    print(f'order={p} vertices={2*m} triples={(2*m)**3} geometric_types={len(profiles)} pair_types={len(pair_sets)} single_types={len(single_sets)}')
    return profiles,pair_sets,single_sets

if __name__ == '__main__':
    a=test(2)
    b=test(3)
    assert a==b, ('different geometric or extension profiles')
    print('PASS identical geometric triple extension signatures for orders 2 and 3')
    print('PASS all ordered triples and equality/repetition patterns')
