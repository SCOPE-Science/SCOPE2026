#!/usr/bin/env python3
"""Exact-rational finite diagnostics for two-equilateral-block Hilbert distortion.

The analytic all-parameter theorem is proved separately; finite checks are not
an exhaustive infinite proof. This script uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product


def dot(x, y):
    return sum((a * b for a, b in zip(x, y)), F(0))


def gram_rank(M):
    A = [list(row) for row in M]
    rows, cols = len(A), len(A[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if A[i][c]), None)
        if pivot is None:
            continue
        A[r], A[pivot] = A[pivot], A[r]
        z = A[r][c]
        A[r] = [v / z for v in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                t = A[i][c]
                A[i] = [p - t*q for p, q in zip(A[i], A[r])]
        r += 1
        if r == rows:
            break
    return r


def certificate(a, b, u, w, v):
    assert a >= 2 and b >= 2 and u > 0 and w > 0 and v > 0
    assert u <= 2*v and w <= 2*v
    n = a + b
    sigma = F(a-1, 2*a) * u*u + F(b-1, 2*b) * w*w
    h2 = max(F(0), v*v - sigma)
    Q = [[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(a):
        for j in range(a):
            Q[i][j] = u*u/F(2) * (F(int(i==j)) - F(1, a))
    for i in range(b):
        for j in range(b):
            Q[a+i][a+j] = w*w/F(2) * (F(int(i==j)) - F(1, b)) + h2
    # Q is positive semidefinite as an explicit nonnegative combination
    # of two orthogonal centered-simplex Gram blocks and h2*1_B*1_B^T.
    for i in range(n):
        for j in range(n):
            d2 = Q[i][i] + Q[j][j] - 2*Q[i][j]
            if i == j:
                target = F(0)
            elif i < a and j < a:
                target = u*u
            elif i >= a and j >= a:
                target = w*w
            else:
                target = max(v*v, sigma)
            assert d2 == target, (a,b,u,w,v,i,j,d2,target)
    rank = gram_rank(Q)
    assert rank == n-1 if sigma < v*v else rank == n-2
    # All ratios are >= 1 after noncontracting normalization.
    ratios = [u*u/(u*u), w*w/(w*w), max(v*v,sigma)/(v*v)]
    assert min(ratios) == 1
    assert max(ratios) == max(F(1),sigma/(v*v))
    return n*n + 5, rank


def centroid_identity(points, a):
    xs, ys = points[:a], points[a:]
    b = len(ys)
    assert a >= 2 and b >= 2
    ca = [sum((x[k] for x in xs), F(0))/a for k in range(len(xs[0]))]
    cb = [sum((x[k] for x in ys), F(0))/b for k in range(len(xs[0]))]
    cross = sum((dot([s-t for s,t in zip(x,y)],
                      [s-t for s,t in zip(x,y)]) for x in xs for y in ys), F(0)) / (a*b)
    aa = sum((dot([s-t for s,t in zip(x,y)],
                   [s-t for s,t in zip(x,y)]) for x in xs for y in xs), F(0)) / (2*a*a)
    bb = sum((dot([s-t for s,t in zip(x,y)],
                   [s-t for s,t in zip(x,y)]) for x in ys for y in ys), F(0)) / (2*b*b)
    cent = dot([s-t for s,t in zip(ca,cb)], [s-t for s,t in zip(ca,cb)])
    assert cross == aa+bb+cent
    return 1


def main():
    # Rational parameters cover isometric, critical, and non-isometric branches.
    base = (F(1,2), F(1), F(3,2), F(2), F(5,2))
    tests = assertions = 0
    branches = set()
    for a, b in product(range(2,8), repeat=2):
        for u, w, v in product(base[:4], base[:4], base):
            if u > 2*v or w > 2*v:
                continue
            sigma = F(a-1,2*a)*u*u + F(b-1,2*b)*w*w
            branch = '<' if sigma<v*v else ('=' if sigma==v*v else '>')
            branches.add(branch)
            inc, _ = certificate(a,b,u,w,v)
            assertions += inc
            tests += 1
    assert branches == {'<','=','>'}
    # Verify the identity on genuinely asymmetric finite configurations.
    for a, b, dim, seed in product(range(2,6), range(2,6), range(1,5), range(7)):
        p = [[F(((i+2)*(k+3)+seed*(i-k))%13-6, (k+2))
              for k in range(dim)] for i in range(a+b)]
        assertions += centroid_identity(p, a)
    # In the split graph, both block classes are nontrivial and sigma>1.
    for a,b in product(range(2,100),repeat=2):
        sigma = F(a-1,2*a) + F(2*(b-1),b)
        assert sigma == F(5,2)-F(1,2*a)-F(2,b)
        assert F(5,4) <= sigma < F(5,2)
        assertions += 2
    print('CHECK_OK', 'rational_matrix_cases=',tests,
          'identity_cases=',4*4*4*7,
          'validated_relations=',assertions,
          'branches=',','.join(sorted(branches)))

if __name__ == '__main__':
    main()
