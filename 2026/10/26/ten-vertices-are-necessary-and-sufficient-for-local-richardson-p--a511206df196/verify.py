"""Exact, standalone reproducibility checks for a local Richardson-positivity cutoff."""
from fractions import Fraction as Q
from random import Random


def mm(X, Y):
    n = len(X)
    return [[sum(X[i][k] * Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def inv(X):
    n = len(X)
    Z = [[Q(X[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if Z[i][j])
        Z[j], Z[p] = Z[p], Z[j]
        d = Z[j][j]
        Z[j] = [x / d for x in Z[j]]
        for i in range(n):
            if i != j:
                d = Z[i][j]
                if d:
                    Z[i] = [a - d * b for a, b in zip(Z[i], Z[j])]
    return [r[n:] for r in Z]


def lap(A):
    return [[(sum(A[i]) if i == j else 0) - A[i][j] for j in range(len(A))] for i in range(len(A))]


def dists(A, s):
    q = [s]
    d = [-1] * len(A)
    d[s] = 0
    for v in q:
        for j, flag in enumerate(A[v]):
            if flag and d[j] < 0:
                d[j] = d[v] + 1
                q.append(j)
    return d


def graph(n, edges):
    A = [[0] * n for _ in range(n)]
    for i, j in edges:
        assert i != j
        A[i][j] = A[j][i] = 1
    return A


def witness():
    # u=0, v=1, A={2,3,4}, B={5,6,7}, C={8,9}, distinguished bridge (2,5)
    ed = [(0, a) for a in (2, 3, 4)] + [(1, b) for b in (5, 6, 7)] + [(2, 5)]
    ed += [(c, a) for c in (8, 9) for a in (2, 3, 4, 5, 6, 7)]
    return graph(10, ed)


def nine_vertex_bound_witness():
    # u=0, v=1, A={2,3}, B={4,5,6}, C={7,8}; distinguished bridge (2,4)
    ed = [(0, a) for a in (2, 3)] + [(1, b) for b in (4, 5, 6)] + [(2, 4)]
    ed += [(c, a) for c in (7, 8) for a in (2, 3, 4, 5, 6)]
    return graph(9, ed)


def formula(A, u, v):
    assert dists(A, u)[v] == 3
    nu = {i for i, b in enumerate(A[u]) if b}
    nv = {i for i, b in enumerate(A[v]) if b}
    assert not nu & nv
    C = set(range(len(A))) - {u, v} - nu - nv
    p = {i: sum(A[i][j] for j in nv) for i in nu}
    q = {j: sum(A[j][i] for i in nu) for j in nv}
    t = sum(p.values())
    assert t >= 1
    result = -(len(nu) + len(nv) + 2) * t - sum(x*x for x in p.values()) - sum(x*x for x in q.values())
    for w in C:
        x = sum(A[w][i] for i in nu)
        y = sum(A[w][j] for j in nv)
        result += x*y - sum(A[w][i]*p[i] for i in nu) - sum(A[w][j]*q[j] for j in nv)
    return result


def upper(k):
    return [(s, (k-s)*max(0, s*s//4-2)-(s+4)) for s in range(2,k+1)]


def main():
    assert upper(7) == [(2,-6), (3,-7), (4,-2), (5,-1), (6,-3), (7,-11)]
    assert upper(8) == [(2,-6), (3,-7), (4,0), (5,3), (6,4), (7,-1), (8,-12)]
    Z = nine_vertex_bound_witness()
    assert max(max(dists(Z, i)) for i in range(9)) == 3
    ZL = lap(Z)
    assert mm(mm(ZL, ZL), mm(ZL, ZL))[0][1] == formula(Z, 0, 1) == -1
    W = witness()
    assert max(max(dists(W, i)) for i in range(10)) == 3
    L4 = mm(mm(lap(W), lap(W)), mm(lap(W), lap(W)))
    assert L4[0][1] == formula(W, 0, 1) == 4
    for h in [Q(1,75), Q(1,100), Q(1,200), Q(1,1000)]:
        n = len(W)
        L = lap(W)
        half = inv([[(Q(i==j) + h*L[i][j]/2) for j in range(n)] for i in range(n)])
        coarse = inv([[(Q(i==j) + h*L[i][j]) for j in range(n)] for i in range(n)])
        fine2 = mm(half, half)
        val = 2*fine2[0][1]-coarse[0][1]
        assert val < 0, (h,val)
    rng = Random(1449)
    tested = 0
    for n in range(4,13):
        for _ in range(75):
            edges = [(i, j) for i in range(n) for j in range(i+1,n) if rng.randrange(100)<38]
            A = graph(n,edges)
            L = lap(A)
            L2=mm(L,L)
            L4=mm(L2,L2)
            for u in range(n):
                D=dists(A,u)
                for v in range(u+1,n):
                    if D[v] == 3:
                        assert formula(A,u,v) == L4[u][v]
                        if n<=9: assert L4[u][v] <= -1
                        elif n==10: assert L4[u][v] <=4
                        tested += 1
    assert tested > 1000
    print('PASS: exact matrices, sharp 9- and 10-vertex witnesses and bound tables, 4 rational resolvent-sign tests,',tested,'random graph distance-three comparisons')


if __name__ == '__main__':
    main()
