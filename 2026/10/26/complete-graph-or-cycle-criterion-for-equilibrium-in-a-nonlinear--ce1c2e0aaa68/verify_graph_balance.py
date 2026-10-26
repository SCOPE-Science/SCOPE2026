"""Independent finite-state checks for a nonlinear spin-flip reversibility theorem.

Python 3, standard library only. Run: python verify_graph_balance.py
"""
from itertools import product, combinations
from math import atanh, exp, log, tanh

S = 0.63
J = 0.47
TOL = 5e-11


def f(x, s=S):
    return x + atanh(s * tanh(x))


def flip(z, i):
    y = list(z)
    y[i] *= -1
    return tuple(y)


def nbrs(n, edges):
    a = [set() for _ in range(n)]
    for i, j in edges:
        a[i].add(j)
        a[j].add(i)
    return a


def rate(z, i, adjacency):
    u = tanh(J * sum(z[j] for j in adjacency[i]))
    return (1 - z[i] * u) * (1 - S * z[i] * u) / 2


def affinity(z, i, j, adjacency):
    zi = flip(z, i)
    zj = flip(z, j)
    zij = flip(zi, j)
    forward = (rate(z, i, adjacency) * rate(zi, j, adjacency)
               * rate(zij, i, adjacency) * rate(zj, j, adjacency))
    reverse = (rate(z, j, adjacency) * rate(zj, i, adjacency)
               * rate(zij, j, adjacency) * rate(zi, i, adjacency))
    return log(forward / reverse)


def criterion(adjacency):
    n = len(adjacency)
    seen = set()
    for root in range(n):
        if root in seen:
            continue
        todo = [root]
        component = set()
        while todo:
            u = todo.pop()
            if u in component:
                continue
            component.add(u)
            todo.extend(adjacency[u] - component)
        seen |= component
        k = len(component)
        clique = all(len(adjacency[u]) == k - 1 for u in component)
        cycle = k >= 3 and all(len(adjacency[u]) == 2 for u in component)
        if not (clique or cycle):
            return False
    return True


def all_4cycles_zero(n, edges):
    a = nbrs(n, edges)
    for z in product((-1, 1), repeat=n):
        for i, j in edges:
            if abs(affinity(z, i, j, a)) > TOL:
                return False
    return True


def db_check(n, edges, log_weight):
    a = nbrs(n, edges)
    total = 0
    for z in product((-1, 1), repeat=n):
        for i in range(n):
            zp = flip(z, i)
            defect = (log_weight(z) - log_weight(zp)
                      - log(rate(zp, i, a) / rate(z, i, a)))
            assert abs(defect) < TOL, (n, z, i, defect)
            total += 1
    return total


def run():
    total_graphs = 0
    for n in range(1, 6):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = [p for k, p in enumerate(possible) if mask & (1 << k)]
            a = nbrs(n, edges)
            expected = criterion(a)
            measured = all_4cycles_zero(n, edges)
            assert measured == expected, (n, edges, measured, expected)
            total_graphs += 1
    k4 = list(combinations(range(4), 2))
    a = (f(3*J) + f(J))/4
    b = (f(3*J) - 3*f(J))/4
    assert b < 0
    checks = db_check(4, k4, lambda z: a*sum(z[i]*z[j] for i,j in k4) + b*z[0]*z[1]*z[2]*z[3])
    c5 = [(k,(k+1)%5) for k in range(5)]
    checks += db_check(5, c5, lambda z: f(2*J)/2 * sum(z[i]*z[j] for i,j in c5))
    p3 = [(0,1),(1,2)]
    z = (1,1,1)
    p3_aff = abs(affinity(z, 0, 1, nbrs(3, p3)))
    assert abs(p3_aff - 2*(2*f(J)-f(2*J))) < TOL
    assert p3_aff > 0
    # Complete-graph general stationary weight for six vertices.
    k6 = list(combinations(range(6), 2))
    def clique_weight(z):
        k = (sum(z) + 6)//2
        return 2*sum(f(J*(-6+2*m+1)) for m in range(k))
    checks += db_check(6, k6, clique_weight)
    print('PASS: %d simple labelled graphs of orders 1 through 5' % total_graphs)
    print('PASS: %d detailed-balance identities on K4, C5, K6' % checks)
    print('PASS: P3 nonzero square-cycle affinity = %.12f' % p3_aff)
    print('PASS: K4 four-spin Gibbs coefficient = %.12f' % b)

if __name__ == '__main__':
    run()
