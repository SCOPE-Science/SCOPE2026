"""Exact finite-state checks for stationary weak-contact response tomography.

Requires only Python 3 standard library. All arithmetic is rational.
Run with: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def moments(n, alpha, delta, beta):
    p = [F(a, a + d) for a, d in zip(alpha, delta)]
    s = [a + d for a, d in zip(alpha, delta)]
    A = [sum((p[j] * beta[j][i] for j in range(n) if j != i), F(0))
         for i in range(n)]
    m = [(1 - p[i]) * A[i] / s[i] for i in range(n)]
    c = {(i, j): (1 - p[i]) * (1 - p[j]) *
         (p[j] * beta[j][i] + p[i] * beta[i][j]) / (s[i] + s[j])
         for i in range(n) for j in range(i + 1, n)}
    return p, s, m, c


def verify_generator(n, alpha, delta, beta):
    p, s, m, c = moments(n, alpha, delta, beta)
    pi0 = {}
    pi1 = {}
    for state in product((0, 1), repeat=n):
        base = F(1)
        for i, bit in enumerate(state):
            base *= p[i] if bit else 1 - p[i]
        h = [F(bit - p[i], p[i] * (1 - p[i])) for i, bit in enumerate(state)]
        score = sum((m[i] * h[i] for i in range(n)), F(0))
        score += sum((v * h[i] * h[j] for (i, j), v in c.items()), F(0))
        pi0[state] = base
        pi1[state] = base * score
    assert sum(pi1.values(), F(0)) == 0
    for i in range(n):
        assert sum((pi1[x] * x[i] for x in pi1), F(0)) == m[i]
    for (i, j), val in c.items():
        assert sum((pi1[x] * (x[i] - p[i]) * (x[j] - p[j]) for x in pi1), F(0)) == val

    # Evaluate row-vector balance pi1 Q0 + pi0 Q1 = 0, state by state.
    residual = dict.fromkeys(pi0, F(0))
    for x in pi0:
        for i in range(n):
            if x[i]:
                q0, q1 = F(delta[i]), F(0)
            else:
                q0 = F(alpha[i])
                q1 = sum((beta[j][i] * x[j] for j in range(n) if j != i), F(0))
            y = list(x)
            y[i] = 1 - y[i]
            y = tuple(y)
            flux = pi1[x] * q0 + pi0[x] * q1
            residual[x] -= flux
            residual[y] += flux
    assert all(r == 0 for r in residual.values())
    for (i, j), value in c.items():
        if beta[i][j] == beta[j][i] == 0:
            assert value == 0
        else:
            assert value > 0
    return 1 + n + len(c) + len(residual)


def rank(matrix):
    a = [[F(v) for v in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for j in range(cols):
        pivot = next((k for k in range(r, rows) if a[k][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][j]
        a[r] = [v / d for v in a[r]]
        for k in range(rows):
            if k != r and a[k][j]:
                d = a[k][j]
                a[k] = [a[k][l] - d*a[r][l] for l in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def components(n, edges):
    par = list(range(n))
    def root(x):
        while par[x] != x:
            x = par[x]
        return x
    for a, b in edges:
        par[root(a)] = root(b)
    return len({root(i) for i in range(n)})


def check_rank(n, edges):
    m = len(edges)
    rows = [[0]*(2*m) for _ in range(n+m)]
    for k, (i, j) in enumerate(edges):
        # Variables are A_{i<-j}, A_{j<-i}.
        rows[i][2*k] = 1
        rows[j][2*k+1] = 1
        rows[n+k][2*k] = rows[n+k][2*k+1] = 1
    nulldim = 2*m-rank(rows)
    assert nulldim == m-n+components(n, edges)
    return 1


def verify_tree_reconstruction(n, alpha, delta, beta):
    p, s, means, covs = moments(n, alpha, delta, beta)
    edges = [(i, j) for i in range(n) for j in range(i+1,n)
             if beta[i][j] or beta[j][i]]
    assert len(edges) == n-components(n, edges)
    u = [s[i]*means[i]/(1-p[i]) for i in range(n)]
    t = {(i,j): (s[i]+s[j])*covs[i,j]/((1-p[i])*(1-p[j])) for i,j in edges}
    adj = [set() for _ in range(n)]
    for i,j in edges:
        adj[i].add(j); adj[j].add(i)
    est = [[F(0) for _ in range(n)] for _ in range(n)]
    while any(adj):
        leaf = next(i for i in range(n) if len(adj[i]) == 1)
        parent = next(iter(adj[leaf]))
        key = (min(leaf,parent),max(leaf,parent))
        incoming = u[leaf]
        outgoing = t[key]-incoming
        est[parent][leaf] = incoming/p[parent]
        est[leaf][parent] = outgoing/p[leaf]
        u[parent] -= outgoing
        u[leaf] = F(0)
        adj[parent].remove(leaf)
        adj[leaf].clear()
    assert all(v == 0 for v in u)
    assert est == beta
    return 1


def triangle_alias():
    n=3
    alpha=delta=[1,1,1]
    symmetric = [[F(0) if i==j else F(2) for j in range(n)] for i in range(n)]
    chiral = [[F(0) if i==j else F(1) for j in range(n)] for i in range(n)]
    # Rows are sources, columns targets; oriented cycle 0 -> 1 -> 2 -> 0.
    for i,j in [(0,1),(1,2),(2,0)]:
        chiral[i][j]=F(3)
    assert symmetric != chiral
    _, _, m0,c0=moments(n,alpha,delta,symmetric)
    _, _, m1,c1=moments(n,alpha,delta,chiral)
    assert m0==m1==[F(1,2)]*3
    assert c0==c1=={(0,1):F(1,8),(0,2):F(1,8),(1,2):F(1,8)}
    return 1


def main():
    rng = Random(20261028)
    checks=0
    for n in range(2,6):
        all_edges=list(combinations(range(n),2))
        masks=range(1 << len(all_edges)) if n<=4 else range(180)
        for mask in masks:
            if n==5:
                selected=[e for e in all_edges if rng.randrange(2)]
            else:
                selected=[e for k,e in enumerate(all_edges) if mask & (1<<k)]
            checks += check_rank(n,selected)
            if n>4 or (n==4 and mask%3):
                continue
            for _ in range(3):
                alpha=[rng.randrange(1,5) for _ in range(n)]
                delta=[rng.randrange(1,5) for _ in range(n)]
                beta=[[F(0) for _ in range(n)] for _ in range(n)]
                for i,j in selected:
                    beta[i][j]=F(rng.randrange(1,6),rng.randrange(1,4))
                    beta[j][i]=F(rng.randrange(1,6),rng.randrange(1,4))
                checks += verify_generator(n,alpha,delta,beta)
                if len(selected)==n-components(n,selected):
                    checks += verify_tree_reconstruction(n,alpha,delta,beta)
    checks+=triangle_alias()
    print('EXACT_CHECKS_OK',checks)


if __name__=='__main__':
    main()
