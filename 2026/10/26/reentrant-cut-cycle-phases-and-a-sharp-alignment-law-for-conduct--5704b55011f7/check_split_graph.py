"""Exact-rational check for endpoint projections of conductance-weighted complete split graphs.

Uses an independently inverted grounded Laplacian, not the spectral proof.
Execute with Python 3 and the standard library only.
"""
from fractions import Fraction as F


def inverse(a):
    z = len(a)
    r = [list(row) + [F(i == j) for j in range(z)] for i, row in enumerate(a)]
    for k in range(z):
        pivot = next(i for i in range(k, z) if r[i][k])
        r[k], r[pivot] = r[pivot], r[k]
        v = r[k][k]
        r[k] = [t / v for t in r[k]]
        for i in range(z):
            if i != k and r[i][k]:
                t = r[i][k]
                r[i] = [u - t * v for u, v in zip(r[i], r[k])]
    return [row[z:] for row in r]


def verify(m, n, x):
    N = m + n
    edges = [(i, j, x) for i in range(m) for j in range(i + 1, m)]
    edges.extend((i, j, F(1)) for i in range(m) for j in range(m, N))
    g = [[F(0) for _ in range(N-1)] for _ in range(N-1)]
    for a, b, root in edges:
        w = root * root
        if a < N-1:
            g[a][a] += w
        if b < N-1:
            g[b][b] += w
        if a < N-1 and b < N-1:
            g[a][b] -= w
            g[b][a] -= w
    gi = inverse(g)
    lam = m*x*x + n
    qa = F(2)*((m-1)*x*x + n*x)/lam
    qb = 1+F(m-1,1)*(x + F(2*(n-1),m))/lam
    pa = 1+F(2)*((m-3)*x*x + n*x)/lam
    pb = 2-F(2,m)+F(m-1,1)*(x + F(2*(n-2),m))/lam
    for e,(u,v,root) in enumerate(edges):
        evec = [F(0)]*(N-1)
        if u < N-1: evec[u] += root
        if v < N-1: evec[v] -= root
        pot = [sum(gi[i][j]*evec[j] for j in range(N-1)) for i in range(N-1)] + [F(0)]
        col = [r*(pot[a]-pot[b]) for a,b,r in edges]
        cut = sum(map(abs,col))
        cyc = sum(abs((F(1) if k == e else F(0))-val) for k,val in enumerate(col))
        expected = (qa,pa) if v < m else (qb,pb)
        assert (cut,cyc) == expected, (m,n,x,e,(cut,cyc),expected)
        assert F(0) <= col[e] <= F(1)
    return len(edges)


def main():
    graphs = columns = 0
    for m in range(2,8):
        for n in range(2,7):
            for x in (F(1,3), F(1), F(6,5), F(2)):
                columns += verify(m,n,x)
                graphs += 1
    assert verify(2,2,F(3,2)) == 5
    assert verify(2,3,F(1)) == 7
    print('WEIGHTED_SPLIT_ENDPOINT_EXACT_OK graphs=%d columns=%d boundary_spotchecks=2' % (graphs,columns))

if __name__ == '__main__':
    main()
