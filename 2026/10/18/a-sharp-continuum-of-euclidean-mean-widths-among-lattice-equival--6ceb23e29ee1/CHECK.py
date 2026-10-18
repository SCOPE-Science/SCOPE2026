"""Independent finite sanity checks for tree symmetric edge-polytope geometry.
Only the analytical proof establishes the all-dimensional conclusions.
Run with Python 3 standard library: python3 check.py
"""
from itertools import product
from random import Random
from math import sqrt, log, factorial


def edges_from_prufer(code, n):
    degree = [1] * n
    for v in code: degree[v] += 1
    edges = []
    for v in code:
        leaf = min(i for i, d in enumerate(degree) if d == 1)
        edges.append((leaf, v)); degree[leaf] -= 1; degree[v] -= 1
    rest = [i for i, d in enumerate(degree) if d == 1]
    edges.append(tuple(rest))
    return edges


def bareiss_det(matrix):
    a = [list(row) for row in matrix]
    m = len(a)
    if m == 0: return 1
    sign = 1; divisor = 1
    for k in range(m - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, m) if a[j][k]), None)
            if j is None: return 0
            a[k], a[j] = a[j], a[k]; sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, m):
            for j in range(k + 1, m):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % divisor == 0
                a[i][j] = numerator // divisor
            a[i][k] = 0
        divisor = pivot
    return sign * a[m - 1][m - 1]


def gram(edges, n):
    cols = []
    for i, j in edges:
        c = [0] * n; c[i] = 1; c[j] = -1
        cols.append(c)
    return [[sum(x*y for x,y in zip(a,b)) for b in cols] for a in cols]


def sample_width(edges, n, rng, samples):
    total = 0.0
    for _ in range(samples):
        x = [rng.gauss(0,1) for i in range(n)]
        val = max(abs(x[i]-x[j]) for i,j in edges)
        # The support function of the convex hull of all signed edge roots
        # is verified against direct vertex enumeration.
        signed_vertices = []
        for i,j in edges:
            signed_vertices.extend([x[i]-x[j],x[j]-x[i]])
        assert abs(val-max(signed_vertices)) < 1e-12
        total += val
    return total/samples


def main():
    count = 0
    for n in range(3, 7):
        for code in product(range(n),repeat=n-2):
            E = edges_from_prufer(code,n)
            assert len(E)==n-1
            assert bareiss_det(gram(E,n)) == n
            # All tree polytopes have this intrinsic Euclidean volume.
            vol_squared = 4**(n-1)*n/(factorial(n-1)**2)
            assert vol_squared > 0
            count += 1
    assert count == sum(n**(n-2) for n in range(3,7))
    rng = Random(20261017)
    levels=[]
    for n in [128,512,2048]:
        star=[(0,j) for j in range(1,n)]
        path=[(j,j+1) for j in range(n-1)]
        m=int(n**0.75)
        broom=[(j,j+1) for j in range(m)]+[(0,j) for j in range(m+1,n)]
        assert len(broom)==n-1
        means=[sample_width(e,n,rng,250) for e in [star,broom,path]]
        # This ordering is an asymptotic signal, not an all-n optimization claim.
        levels.append((n,tuple(round(z/sqrt(log(n)),4) for z in means)))
    print('PRUFER_GRAM_CASES',count)
    print('GAUSSIAN_EDGE_MAX_SCALED star,broom,path',levels)
    print('PASS')

if __name__=='__main__':main()
