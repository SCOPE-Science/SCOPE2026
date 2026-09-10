"""Jones polynomial via Kauffman bracket state sum over the braid word.
Direct and correct: rho(s_i) = A*I + A^{-1}*E_i; expand product into 2^w
TL diagrams (w=27 -> 1.3e8 too many!). Instead: dynamic programming over
matching basis (dim 14) accumulating (diagram -> coefficient) — i.e. matrix
multiplication as before — then take the CORRECT categorical trace:
tr(X) = closure of the tangle X: for X = sum_z c_z * z (basis diagrams),
close each basis diagram z directly: loops(z) = closure_loops_single(z)
= number of circles when top_i connected to bottom_i.
So: compute coefficient vector of rho(word)*|cup...><...|? Precisely:
rho(word) applied to identity: v = M @ e_I (column of identity), then
tr = sum_z v_z * D^{close1(z)}, where close1(z) = loops closing single diagram z.
Must double check normalization with trefoil.
"""
import sympy as sp
from jones_tl import all_matchings, op_compose_table, tl_E, closure_loops

A = sp.Symbol('A')
t = sp.Symbol('t')

def close1(n, Z):
    return closure_loops(n, Z, Z)  # placeholder; replaced below

def single_closure_loops(n, Z):
    """Circles in the standard closure of a single (n,n)-tangle diagram Z:
    connect top i to bottom i with parallel arcs."""
    parent = list(range(2 * n))
    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a
    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[a] = b
    for (a, b) in Z:
        union(a, b)
    for i in range(n):
        union(i, n + i)
    comps = set(find(v) for v in range(2 * n))
    return len(comps)

def jones2(n, word):
    basis = all_matchings(n)
    idx = {m: k for k, m in enumerate(basis)}
    D = sp.Symbol('D')
    d = len(basis)
    tables = {i: op_compose_table(n, basis, idx, tl_E(n, i)) for i in range(1, n)}
    # identity diagram:
    I = frozenset([(j, n + j) for j in range(n)])
    assert I in idx
    # vector v = rho(word) @ I, entries sympy in A,D
    v = [sp.Integer(1) if k == idx[I] else sp.Integer(0) for k in range(d)]
    for i in word:
        assert i > 0
        tab = tables[i]
        w = [sp.Integer(0)] * d
        for c in range(d):
            if v[c] == 0:
                continue
            # A*I term: stays at c
            w[c] += A * v[c]
            # A^{-1}*E term: moves to tab[c]
            lp, r = tab[c]
            w[r] += A**(-1) * (D**lp) * v[c]
        v = [sp.expand(x) for x in w]
    tr = sum(v[k] * D**single_closure_loops(n, basis[k]) for k in range(d))
    tr = sp.expand(tr)
    delta = -A**2 - A**(-2)
    tr = sp.expand(tr.subs(D, delta))
    wr = len(word)
    V_A = sp.simplify(((-A**3)**(-wr)) * tr / delta)
    V = sp.simplify(V_A.subs(A, t**(-sp.Rational(1, 4))))
    return V, {'dim': d, 'bracket': tr}

if __name__ == '__main__':
    for (n, w, name) in [(2, [1, 1, 1], 'trefoil'), (2, [1], 'hopf-closure? (s1 in B2->Hopf link)'),
                         (1, [], 'unknot'), (3, [1, -1], 'cancel? (needs inverse: skip)')]:
        if any(i < 0 for i in w):
            continue
        V, info = jones2(n, w)
        print(name, 'V =', V, '; V(1) =', sp.simplify(V.subs(t, 1)))
    print('expected trefoil RH: t + t^3 - t^4')
