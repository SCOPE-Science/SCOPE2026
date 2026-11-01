"""Checks for the planar prescribed-support-direction cone theorem.

Run with Python 3: python verify_polygon_cone.py
Only the standard library is required. Tests are finite corroboration, not a proof.
"""
from itertools import combinations, product
from math import cos, sin, pi


def is_interior_triangle(n, ids):
    i, j, k = ids
    gaps = (j-i, k-j, n-k+i)
    return max(gaps)*2 < n


def counts(n):
    triangles = [tr for tr in combinations(range(n), 3) if is_interior_triangle(n, tr)]
    pairs = [(i, i+n//2) for i in range(n//2)] if n % 2 == 0 else []
    expected_triangles = n*(n*n-1)//24 if n%2 else n*(n-2)*(n-4)//24
    expected_rays = n*(n*n-1)//3 if n%2 else n*(n-2)*(n-4)//3+2*n
    assert len(triangles) == expected_triangles, (n, len(triangles), expected_triangles)
    assert 8*len(triangles)+4*len(pairs) == expected_rays
    return triangles, pairs, expected_rays


def verify_witness(n, support, copy_choice, weights):
    a = [(cos(2*pi*i/n), sin(2*pi*i/n)) for i in range(n)]
    tang = [(-y, x) for x,y in a]
    alpha, beta = [0.0]*n, [0.0]*n
    for i, side, w in zip(support, copy_choice, weights):
        if side == 0:
            alpha[i] = w
        else:
            beta[(i-1)%n] = w
    edges = [tuple(alpha[i]*tang[i][k]+beta[i]*tang[(i+1)%n][k] for k in range(2)) for i in range(n)]
    xs = [(0.0,0.0)]
    for e in edges[:-1]:
        xs.append((xs[-1][0]+e[0],xs[-1][1]+e[1]))
    closure = (xs[-1][0]+edges[-1][0],xs[-1][1]+edges[-1][1])
    assert max(map(abs, closure)) < 1e-8
    for i in range(n):
        for j in range(n):
            if i!=j:
                val=sum(a[i][k]*(xs[j][k]-xs[i][k]) for k in range(2))
                assert val < 1e-8, (n,support,copy_choice,i,j,val)


def main():
    checked = 0
    for n in range(3,19):
        tris, pairs, total = counts(n)
        print(f'n={n:2d}: central_triangles={len(tris):4d}, antipodal_pairs={len(pairs):2d}, rays={total:5d}')
        if n > 12:
            continue
        for supp in pairs:
            for choice in product((0,1), repeat=2):
                verify_witness(n,supp,choice,(1.0,1.0))
                checked+=1
        for i,j,k in tris:
            # Each gap is strictly below pi; positive closure coefficients.
            wi=sin(2*pi*(k-j)/n)
            wj=sin(2*pi*(n-k+i)/n)
            wk=sin(2*pi*(j-i)/n)
            assert min(wi,wj,wk)>0
            for choice in product((0,1), repeat=3):
                verify_witness(n,(i,j,k),choice,(wi,wj,wk))
                checked+=1
    print(f'PASS: exact combinatorial counts n=3..18; {checked} geometric ray witnesses n=3..12')

if __name__ == '__main__':
    main()
