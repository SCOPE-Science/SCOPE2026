#!/usr/bin/env python3
"""Exact certificate for small-graph [0/3] Padé heat positivity.

Requires Python 3.10+ and SymPy 1.12+. No graph-list downloads.
The proof of completeness enumerates every labeled simple graph on 2..6
vertices and reduces it by explicitly computed permutation orbits.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial
from sympy import Matrix, eye, symbols, Poly, Rational
from sympy.polys.matrices import DomainMatrix

h = symbols('h')


def connected(n, edges, mask):
    seen = {0}
    frontier = [0]
    while frontier:
        v = frontier.pop()
        for bit, (i, j) in enumerate(edges):
            if mask & (1 << bit):
                if i == v and j not in seen:
                    seen.add(j); frontier.append(j)
                if j == v and i not in seen:
                    seen.add(i); frontier.append(i)
    return len(seen) == n


def graph_orbit_reps(n):
    edges = list(combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edges)}
    maps = []
    for p in permutations(range(n)):
        maps.append(tuple(1 << idx[tuple(sorted((p[i], p[j])))] for i, j in edges))
    covered = set()
    reps = []
    for mask in range(1 << len(edges)):
        if mask in covered:
            continue
        is_conn = connected(n, edges, mask)
        # All n! relabelings of this unlabeled isomorphism class.
        one_bits = [i for i in range(len(edges)) if mask & (1 << i)]
        for mp in maps:
            permuted = 0
            for bit in one_bits:
                permuted |= mp[bit]
            covered.add(permuted)
        if is_conn:
            reps.append(mask)
    assert len(covered) == 1 << len(edges)
    return edges, reps


def cofactor_poly(A, row, column):
    # The inverse entry (row,column) is the transposed cofactor.
    minor = A.minor_submatrix(column, row)
    cofactor = (-1)**(row+column) * DomainMatrix.from_Matrix(minor).det().as_expr()
    return Poly(cofactor, h)


def certificate_multiplier(poly):
    coeff = [int(a) for a in reversed(poly.all_coeffs())]
    if not any(a > 0 for a in coeff):
        raise AssertionError('Zero-or-negative cofactor polynomial')
    for degree in range(33):
        if all(a >= 0 for a in coeff):
            return degree
        coeff = [coeff[0]] + [coeff[k-1] + coeff[k] for k in range(1,len(coeff))] + [coeff[-1]]
    raise AssertionError('No degree-32 nonnegative coefficient certificate')


def laplacian(n, edges, mask):
    L = Matrix.zeros(n)
    for bit, (i, j) in enumerate(edges):
        if mask & (1 << bit):
            L[i,i] += 1
            L[j,j] += 1
            L[i,j] -= 1
            L[j,i] -= 1
    return L


def main():
    counts = Counter()
    multipliers = Counter()
    total_pairs = 0
    exception = None
    for n in range(2,7):
        edges, reps = graph_orbit_reps(n)
        counts[n] = len(reps)
        for mask in reps:
            L = laplacian(n, edges, mask)
            A = 6*eye(n) + 6*h*L + 3*h**2*L**2 + h**3*L**3
            for i in range(n):
                for j in range(i+1,n):
                    degree = certificate_multiplier(cofactor_poly(A, i, j))
                    multipliers[degree] += 1
                    total_pairs += 1
                    if degree:
                        assert exception is None
                        exception = (n, mask, i, j, degree)
    assert counts == Counter({2:1,3:2,4:6,5:21,6:112}), counts
    assert total_pairs == 1933, total_pairs
    assert multipliers == Counter({0:1932,32:1}), multipliers
    assert exception is not None and exception[0] == 6
    # P_7 at exact rational timestep values. All diagonal elements of an
    # SPD inverse are automatically positive, so check every entry here.
    n = 7
    P7 = Matrix.zeros(n)
    for i in range(n-1):
        P7[i,i] += 1; P7[i+1,i+1] += 1
        P7[i,i+1] -= 1; P7[i+1,i] -= 1
    expected = {
        Rational(1,2):Rational(1036685,130532396219),
        Rational(3,4):Rational(-529900671519,16012967110980391),
        Rational(1):Rational(-16229,1505893633),
        Rational(2):Rational(96462616,19528273141),
    }
    for t, value in expected.items():
        H=eye(n)+t*P7+t**2*P7**2/2+t**3*P7**3/6
        R=H.inv()
        assert R[0,6] == value
        if t in (Rational(1,2),Rational(2)):
            assert all(z>0 for z in R)
        if t in (Rational(3,4),Rational(1)):
            assert R[0,6]<0
        assert all(sum(R[i,j] for j in range(n)) == 1 for i in range(n))
    print('PASS: exhaustive labeled graph permutation-orbit enumeration for n=2..6')
    print('connected nonisomorphic graph counts:',dict(sorted(counts.items())))
    print('total unordered vertex-pair cofactor certificates:',total_pairs)
    print('nonnegative-coefficient multiplier degree distribution:',dict(sorted(multipliers.items())))
    print('unique degree-32 case (n,edge-mask,i,j,degree):',exception)
    print('PASS: all positive step sizes certified for every graph of order <=6')
    print('PASS: exact P7 entries at steps 1/2, 3/4, 1 and 2; sign-loss-and-recovery witness')
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
