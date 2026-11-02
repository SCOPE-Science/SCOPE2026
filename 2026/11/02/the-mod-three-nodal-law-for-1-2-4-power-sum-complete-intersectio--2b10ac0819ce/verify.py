"""Finite exact checks for the degree-(1,2,4) power-sum complete intersections.

The mathematical proof is given separately; these modular and combinatorial
checks test its stated examples and Hessian-rank assertions, not all dimensions.
"""
from itertools import combinations
from math import factorial

Q = 1009


def rref(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    if not a:
        return a, []
    i = 0
    pivots = []
    for j in range(len(a[0])):
        candidate = next((k for k in range(i, len(a)) if a[k][j]), None)
        if candidate is None:
            continue
        a[i], a[candidate] = a[candidate], a[i]
        mult = pow(a[i][j], -1, p)
        a[i] = [(v * mult) % p for v in a[i]]
        for k in range(len(a)):
            if k != i and a[k][j]:
                scale = a[k][j]
                a[k] = [(v - scale * w) % p for v, w in zip(a[k], a[i])]
        pivots.append(j)
        i += 1
        if i == len(a):
            break
    return a, pivots


def rank(matrix, p):
    return len(rref(matrix, p)[1])


def kernel_basis(matrix, p):
    rr, pivot = rref(matrix, p)
    n = len(matrix[0])
    free = [j for j in range(n) if j not in pivot]
    basis = []
    for f in free:
        v = [0] * n
        v[f] = 1
        for row, col in enumerate(pivot):
            v[col] = -rr[row][f] % p
        basis.append(v)
    return basis


def third_root_of_unity(p):
    assert (p - 1) % 3 == 0
    return next(pow(a, (p - 1) // 3, p)
                for a in range(2, p) if pow(a, (p - 1) // 3, p) != 1)


def verify_node(n, p=Q):
    assert n % 3 == 0 and n < p
    omega = third_root_of_unity(p)
    assert omega != 1 and (1 + omega + omega**2) % p == 0
    a = n // 3
    x = [1] * a + [omega] * a + [omega * omega % p] * a
    assert all(sum(pow(z, d, p) for z in x) % p == 0 for d in (1, 2, 4))
    j = [[1] * n, x, [pow(z, 3, p) for z in x]]
    assert rank(j, p) == 2
    tangent = kernel_basis(j[:2], p)
    assert len(tangent) == n - 2
    diagonal = [12 * pow(z, 2, p) % p for z in x]
    h = [[sum(tangent[i][k] * diagonal[k] * tangent[j][k]
              for k in range(n)) % p for j in range(n - 2)]
         for i in range(n - 2)]
    assert rank(h, p) == n - 3, (n, rank(h, p))
    # The radial vector lies in the Hessian radical.
    assert all(sum(tangent[i][k] * diagonal[k] * x[k]
                   for k in range(n)) % p == 0 for i in range(n - 2))
    return True


def count_node_orbits(n):
    a = n // 3
    expected = factorial(n) // (3 * factorial(a)**3)
    if n > 12:
        return expected
    tuples = set()
    positions = range(n)
    for I in combinations(positions, a):
        rem = sorted(set(positions) - set(I))
        for J in combinations(rem, a):
            v = [2] * n
            for i in I:
                v[i] = 0
            for j in J:
                v[j] = 1
            # Scaling by cube roots cyclically permutes the symbols 0,1,2.
            rep = min(tuple((t + shift) % 3 for t in v) for shift in range(3))
            tuples.add(rep)
    assert len(tuples) == expected, (n, len(tuples), expected)
    return expected


def main():
    # The prime-field experiment is independent of the complex proof.
    assert [count_node_orbits(n) for n in (6, 9, 12, 15)] == [30, 560, 11550, 252252]
    assert all(verify_node(n) for n in (6, 9, 12, 15, 18))
    # For any positive multiplicities not all equal, the quadratic obstruction
    # to three distinct roots has a strictly positive integer value.
    for n in range(4, 32):
        for a in range(1, n - 1):
            for b in range(1, n - a):
                c = n - a - b
                obstruction = a*(b-c)**2 + b*(c-a)**2 + c*(a-b)**2
                assert (obstruction == 0) == (a == b == c)
    print('VERIFY_OK: exact projective orbit counts n=6,9,12; modular Hessian rank n=6,9,12,15,18; multiplicity obstruction n<=31')

if __name__ == '__main__':
    main()
