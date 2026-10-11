"""Numerical reconstruction of the complete-graph fractional matching polytope John certificate.

Runs with the Python standard library. These finite checks support, but do not
replace, the symbolic all-dimensions proof in RESULT.md.
"""
from itertools import combinations
from math import sqrt, isclose


def inverse(A):
    n = len(A)
    X = [list(map(float, r)) + [float(i == j) for j in range(n)]
         for i, r in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda j: abs(X[j][i]))
        X[i], X[p] = X[p], X[i]
        assert abs(X[i][i]) > 1e-12
        z = X[i][i]
        X[i] = [a / z for a in X[i]]
        for j in range(n):
            if j != i:
                v = X[j][i]
                X[j] = [a - v * b for a, b in zip(X[j], X[i])]
    return [r[n:] for r in X]


def run(n):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    B = [[float(int(i in e)) for e in edges] for i in range(n)]
    G = [[sum(B[i][e] * B[i][f] for i in range(n))
          for f in range(m)] for e in range(m)]
    t = (n - 4 + sqrt(n*n + 8*n - 16)) / (4*(n - 2))
    assert t > 0 and abs(2*(n-2)*t*t-(n-4)*t-2) < 1e-11
    a = t / (1+(n-1)*t)
    b = 1 / (1+(n-1)*t)
    U = 1+(n-1)*t
    V = 1 + (n-2)*t/2
    T = n*(n-3)/2+(n-1)/V+1/U
    A = [[float(e == f) + t*G[e][f]/2 for f in range(m)]
         for e in range(m)]
    K = inverse(A)
    scale = m*a*a/T
    S = [[scale*x for x in r] for r in K]
    w0 = T/m
    w1 = T/(2*m*t)
    assert w0 > 0 and w1 > 0
    assert isclose(m*w0+n*w1, m, abs_tol=1e-9)
    # Tangency on each nonnegative coordinate and each vertex-degree facet.
    for e in range(m):
        assert isclose(S[e][e], a*a, rel_tol=2e-10, abs_tol=2e-10)
    for i in range(n):
        var = sum(B[i][e]*S[e][f]*B[i][f]
                  for e in range(m) for f in range(m))
        assert isclose(var, b*b, rel_tol=2e-10, abs_tol=2e-10)
    # John's balancing weights in facet-normal coordinates.
    for e in range(m):
        assert isclose(-w0/a + w1*sum(B[i][e] for i in range(n))/b,
                       0, abs_tol=2e-10)
    # Matrix second-moment identity without requiring a square-root factor.
    for e in range(m):
        for f in range(m):
            val = sum((w0*float(e==k)/(a*a) + w1*G[e][k]/(b*b))
                      * S[k][f] for k in range(m))
            assert isclose(val, float(e == f), rel_tol=2e-10, abs_tol=2e-10)
    # Independent trace and spectral projector test.
    assert isclose(sum(K[e][e] for e in range(m)), T,
                   rel_tol=2e-10, abs_tol=2e-10)
    assert isclose(sum(S[e][f] for e in range(m) for f in range(m)),
                   m*scale/U, rel_tol=2e-10, abs_tol=2e-10)
    return (m, m+n)


if __name__ == '__main__':
    checks = [run(n) for n in range(3, 11)]
    print('PASS: dimension range n=3,...,10')
    print('PASS: checked %d separate facet tangencies' % sum(z for _,z in checks))
    print('PASS: every John balancing and moment matrix entry; trace and spectrum')
    print('PASS: unique positive quadratic root, strictly positive contact weights')
