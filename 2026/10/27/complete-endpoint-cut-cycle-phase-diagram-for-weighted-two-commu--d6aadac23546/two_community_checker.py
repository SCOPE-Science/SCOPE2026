"""Exact rational verification of weighted two-community transfer-current formulas.

Run with Python 3: python two_community_checker.py
Dependencies: Python standard library only.
"""
from fractions import Fraction as F


def inverse(matrix):
    n = len(matrix)
    a = [list(row) + [F(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next((k for k in range(j, n) if a[k][j]), None)
        assert pivot is not None
        a[j], a[pivot] = a[pivot], a[j]
        coeff = a[j][j]
        a[j] = [v / coeff for v in a[j]]
        for k in range(n):
            if k != j and a[k][j]:
                coeff = a[k][j]
                a[k] = [a[k][h] - coeff * a[j][h] for h in range(2 * n)]
    return [row[n:] for row in a]


def formulas(n, x):
    d = n * (1 + x*x)
    qi = 2 * (n - 1 + n*x) / d
    pi = (n*x*x + 2*n*x + 3*n - 6) / d
    if x <= 1:
        qx = (n*x*x + 2*n*x + n - 2*x) / d
        px = 2*(n-1)*((n-1)*x*x + n*x + n + 1) / (n*n*(1+x*x))
    else:
        qx = ((3*n*n - 4*n + 2)*x*x + 2*n*(n-1)*x - n*n + 4*n - 2)/(n*n*(1+x*x))
        px = 2*(n-1)*((2*n-2)*x*x+n*x+2)/(n*n*(1+x*x))
    return qi, qx, pi, px


def check(n, x):
    N = 2*n
    edges = [(i, j, x if (i < n) != (j < n) else F(1))
             for i in range(N) for j in range(i+1, N)]
    lap = [[F(0) for _ in range(N-1)] for __ in range(N-1)]
    for u,v,w in edges:
        c = w*w
        if u < N-1: lap[u][u] += c
        if v < N-1: lap[v][v] += c
        if u < N-1 and v < N-1:
            lap[u][v] -= c
            lap[v][u] -= c
    inv = inverse(lap)
    vals = {"within":[], "cross":[]}
    for e,(u,v,w) in enumerate(edges):
        src = [F(int(i == u)-int(i == v))*w for i in range(N-1)]
        h = [sum(inv[i][j]*src[j] for j in range(N-1)) for i in range(N-1)] + [F(0)]
        qcol = [ww*(h[uu]-h[vv]) for uu,vv,ww in edges]
        normq = sum(map(abs,qcol))
        normp = sum(abs(F(e == f)-qcol[f]) for f in range(len(edges)))
        vals["cross" if u < n <= v else "within"].append((normq,normp))
    assert vals["within"] and vals["cross"]
    assert len(set(vals["within"])) == 1
    assert len(set(vals["cross"])) == 1
    qi,qx,pi,px = formulas(n,x)
    assert vals["within"][0] == (qi,pi),(n,x,"within",vals["within"][0],(qi,pi))
    assert vals["cross"][0] == (qx,px),(n,x,"cross",vals["cross"][0],(qx,px))
    # Check phase classification independent of the explicit norm formulas.
    if x < 1:
        assert qi > qx
        if n <= 4: assert px > pi
        elif n == 5:
            if x < F(3,7): assert px > pi
            elif x == F(3,7): assert px == pi
            else: assert px < pi
        else: assert pi > px
    elif x == 1:
        assert qi == qx and pi == px
    else:
        assert qx > qi and px > pi
    return len(edges)


def main():
    cases=0
    cols=0
    for n in range(3,9):
        for x in [F(1,5),F(3,7),F(2,3),F(4,5),F(1),F(6,5),F(2),F(3),F(5)]:
            cols += check(n,x)
            cases+=1
    print(f'TWO_COMMUNITY_HODGE_EXACT_OK graphs={cases} verified_full_columns={cols}')

if __name__ == '__main__':
    main()
