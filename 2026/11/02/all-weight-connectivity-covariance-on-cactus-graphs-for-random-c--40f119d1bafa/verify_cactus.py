"""Exact finite checks for weighted cactus connection correlations.

Only finite checks are made here; the general proof is algebraic and structural.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations


def add(A, B):
    C = Counter(A)
    for k, v in B.items(): C[k] += v
    return {k: v for k, v in C.items() if v}


def multiply(A, B):
    C = Counter()
    for e, a in A.items():
        for f, b in B.items():
            C[tuple(e[i] + f[i] for i in range(4))] += a * b
    return {k: v for k, v in C.items() if v}


def poly_var(i):
    k = [0] * 4
    k[i] = 1
    return {tuple(k): 1}


def poly_sum(*arrays):
    out = {}
    for A in arrays: out = add(out, A)
    return out


def poly_neg(A):
    return {k: -v for k, v in A.items()}


def poly_prod(*arrays):
    out = {(0, 0, 0, 0): 1}
    for A in arrays: out = multiply(out, A)
    return out


one = {(0, 0, 0, 0): 1}
x, y, z, w = [poly_var(i) for i in range(4)]
S = poly_sum(x, y, z, w)
Z = poly_sum(poly_prod(add(one, x), add(one, y), add(one, z), add(one, w)), poly_neg(one))
R = poly_sum(x, y, multiply(x, y), z, w, multiply(z, w))
C = poly_sum(x, z, multiply(x, z), y, w, multiply(y, w))
N = poly_sum(multiply(S, Z), poly_neg(multiply(R, C)))
assert len(N) == 21 and all(v > 0 for v in N.values())
assert N == poly_sum(
    poly_prod(x, w, poly_sum(x,w), poly_sum(one,y,z)),
    poly_prod(y, z, poly_sum(y,z), poly_sum(one,x,w)),
    poly_prod(x,y,z), poly_prod(x,y,w), poly_prod(x,z,w), poly_prod(y,z,w),
    poly_prod(x,y,z,w,poly_sum({(0,0,0,0):4},x,y,z,w)),
)
H = poly_sum(Z, S, poly_neg(R), poly_neg(C))
assert all(v >= 0 for v in H.values())
assert H == poly_sum(
    poly_prod(x, w), poly_prod(y,z),
    poly_prod(x,y,z), poly_prod(x,y,w), poly_prod(x,z,w), poly_prod(y,z,w),
    poly_prod(x,y,z,w),
)
# The last identity enumerates nonempty closed supports spanning both rows/columns.


def connected(n, chosen, a, b):
    parent = list(range(n))
    def root(v):
        while parent[v] != v: v = parent[v]
        return v
    for u,v in chosen:
        ru,rv = root(u),root(v)
        parent[ru] = rv
    return root(a) == root(b)


def is_forest(n, chosen):
    parent = list(range(n))
    def root(v):
        while parent[v] != v: v = parent[v]
        return v
    for u,v in chosen:
        ru,rv = root(u),root(v)
        if ru == rv: return False
        parent[ru] = rv
    return True


def components(n, chosen):
    parent = list(range(n))
    def root(v):
        while parent[v] != v: v = parent[v]
        return v
    for u,v in chosen: parent[root(u)] = root(v)
    return len(set(root(u) for u in range(n)))


def check_graph(n, edges, weights, q=None):
    counts = Counter()
    pairs = list(combinations(range(n), 2))
    Z = F(0)
    sum1 = {p:F(0) for p in pairs}
    sum2 = {(p,r):F(0) for p in pairs for r in pairs}
    for mask in range(1 << len(edges)):
        chosen = [edge for j,edge in enumerate(edges) if (mask >> j) & 1]
        if q is None:
            if not is_forest(n, chosen): continue
            wt = F(1)
        else:
            wt = q ** components(n, chosen)
        for j in range(len(edges)):
            if (mask >> j) & 1: wt *= weights[j]
        Z += wt
        cc = [p for p in pairs if connected(n, chosen, *p)]
        for p in cc: sum1[p] += wt
        for p in cc:
            for r in cc: sum2[p,r] += wt
    assert Z > 0
    for p in pairs:
        for r in pairs:
            assert sum2[p,r] * Z - sum1[p] * sum1[r] >= 0, (n, edges, p, r, q)
            counts['covariance'] += 1
    return counts


def main():
    # Cactus blocks include bridges, isolated and multiply attached cycles.
    graphs = [
        (3, [(0,1),(1,2),(2,0)]),
        (4, [(0,1),(1,2),(2,3),(3,0)]),
        (5, [(0,1),(1,2),(2,0),(2,3),(3,4)]),
        (5, [(0,1),(1,2),(2,0),(0,3),(3,4),(4,0)]),
        (6, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)]),
        (7, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,2),(4,5),(5,6)]),
        (8, [(0,1),(1,2),(2,3),(3,0),(3,4),(4,5),(5,6),(6,3),(6,7)]),
    ]
    assertions = 0
    for n,edges in graphs:
        for shift in (0,1):
            weights = [F(1,2),F(3,2),F(2),F(5,3),F(4,3)]
            ww = [weights[(j+shift)%len(weights)] for j in range(len(edges))]
            for q in (None, F(1,3), F(2,3), F(2)):
                assertions += check_graph(n,edges,ww,q)['covariance']
    print('PASS polynomial coefficients: 21 nonnegative; nonnegative cross-spanning H')
    print('PASS exact rational covariance inequalities:', assertions)
    print('PASS graphs:', len(graphs), '; weight patterns: 2; models: forest, q=1/3,2/3,2')

if __name__ == '__main__': main()
