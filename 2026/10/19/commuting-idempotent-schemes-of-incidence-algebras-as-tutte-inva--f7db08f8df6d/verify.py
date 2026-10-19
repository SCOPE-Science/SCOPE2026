"""Reproducible finite-field checks of commuting-idempotent schemes of incidence algebras.
All algorithms below use plain Python and prime fields, without symbolic assumptions.
Run: python3 verify.py
"""
from itertools import product
from collections import Counter
from math import comb

POSETS = {
    'star4': (4, [(0, 3), (1, 3), (2, 3)]),
    'path4': (4, [(0, 1), (2, 1), (2, 3)]),
    'diamond4': (4, [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]),
    'chain3': (3, [(0, 1), (1, 2), (0, 2)]),
}

def multiplication_data(n, edges):
    pairs = [(i, i) for i in range(n)] + sorted(edges)
    lookup = {ij: k for k, ij in enumerate(pairs)}
    triples = [(lookup[(i, k)], ai, bi)
               for ai, (i, j) in enumerate(pairs)
               for bi, (j2, k) in enumerate(pairs)
               if j == j2]
    return pairs, triples

def multiply(a, b, triples, dim, p):
    ans = [0]*dim
    for out, i, j in triples:
        ans[out] += a[i]*b[j]
    return tuple(v % p for v in ans)

def enumerate_idempotents(n, edges, p):
    pairs, triples = multiplication_data(n, edges)
    idem = []
    for a in product(range(p), repeat=len(pairs)):
        if multiply(a, a, triples, len(pairs), p) == a:
            idem.append(a)
    return pairs, triples, idem

def fiber_profile(n, edges, p, r):
    color_count = 2**r
    predicted = Counter()
    for labels in product(range(color_count), repeat=n):
        dim = sum(labels[i] != labels[j] for i, j in edges)
        predicted[labels] = p**dim
    return predicted

def check(n, edges, p, label):
    pairs, triples, idem = enumerate_idempotents(n, edges, p)
    dim = len(pairs)
    r1 = fiber_profile(n, edges, p, 1)
    found1 = Counter(tuple(e[i] for i in range(n)) for e in idem)
    assert all(found1[k] == v for k,v in r1.items())
    assert len(idem) == sum(r1.values())
    # Independently multiply ALL idempotent pairs and impose both commutation equations.
    r2 = fiber_profile(n, edges, p, 2)
    found2 = Counter()
    for a in idem:
        for b in idem:
            if multiply(a,b,triples,dim,p) != multiply(b,a,triples,dim,p):
                continue
            color = tuple(a[i]+2*b[i] for i in range(n))
            found2[color] += 1
    assert all(found2[k] == v for k,v in r2.items())
    assert len(found2) == 4**n
    print(label, 'field', p, 'idempotents', len(idem),
          'commuting_pairs', sum(found2.values()),
          'fibers', len(found2))
    return len(idem),sum(found2.values())

def tree_formula(n, q, r):
    Q=2**r
    return Q*(1+(Q-1)*q)**(n-1)

def main():
    results={}
    for name,(n,edges) in POSETS.items():
        for p in (2,3):
            results[name,p]=check(n,edges,p,name)
    for p in (2,3):
        for name in ('star4','path4'):
            a,b=results[name,p]
            assert a==tree_formula(4,p,1) and b==tree_formula(4,p,2)
        assert results['star4',p]==results['path4',p]
    # Verify the change of variables from the cut-coloring sum to the FK expansion.
    for name,(n,edges) in POSETS.items():
        m=len(edges)
        for Q in (2,4,8):
            for q in (2,3,5):
                direct=sum(q**sum(labels[i]!=labels[j] for i,j in edges)
                           for labels in product(range(Q),repeat=n))
                fk=0
                for mask in range(1<<m):
                    parent=list(range(n))
                    def root(v):
                        while parent[v]!=v:
                            v=parent[v]
                        return v
                    for edge_id,(i,j) in enumerate(edges):
                        if (mask>>edge_id)&1:
                            ri,rj=root(i),root(j)
                            parent[ri]=rj
                    k=len({root(i) for i in range(n)})
                    cnt=mask.bit_count()
                    fk += q**(m-cnt)*(1-q)**cnt * Q**k
                assert direct==fk,(name,Q,q,direct,fk)
    print('VERIFY_OK')
if __name__ == '__main__': main()
