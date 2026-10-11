"""Exact rational finite-instance check for two-level Lipschitz polytopes.

This enumerates intersections of independent active constraints.  The proof
for arbitrary cardinalities is analytic; these examples test its formulas.
"""
from fractions import Fraction
from itertools import combinations


def linear_solve(rows, rhs):
    n = len(rhs)
    a = [[Fraction(y) for y in row] + [Fraction(r)]
         for row, r in zip(rows, rhs)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return None
        a[k], a[pivot] = a[pivot], a[k]
        d = a[k][k]
        a[k] = [z/d for z in a[k]]
        for j in range(n):
            if j != k and a[j][k]:
                factor = a[j][k]
                a[j] = [u-factor*v for u, v in zip(a[j], a[k])]
    return tuple(row[-1] for row in a)


def constraints(m, n, t):
    count = m+n
    rows = []
    for i, j in combinations(range(count), 2):
        bound = t if (i < m) == (j < m) else Fraction(1)
        row = tuple((int(i == k)-int(j == k)) for k in range(1, count))
        rows.append((row, bound))
        rows.append((tuple(-a for a in row), bound))
    return rows


def vertices(m, n, t):
    cons = constraints(m, n, t)
    dim = m+n-1
    result = set()
    for subset in combinations(cons, dim):
        solution = linear_solve([row for row, _ in subset],
                                [bound for _, bound in subset])
        if solution is not None and all(
            sum(a*b for a,b in zip(row, solution)) <= bound
            for row, bound in cons
        ):
            result.add(solution)
    return result


def predicted(m, n, t):
    if t == 1:
        return 2**(m+n)-2
    if t == 2:
        return 2**m+2**n-2
    return 2*(2**m-1)*(2**n-1)


if __name__ == '__main__':
    cases = [(2,2,1),(2,2,Fraction(3,2)),(2,2,2),
             (2,3,1),(2,3,Fraction(3,2)),(2,3,2)]
    for m,n,t in cases:
        actual = len(vertices(m,n,t))
        expected = predicted(m,n,t)
        assert actual == expected, (m,n,t,actual,expected)
        print(f'm={m}, n={n}, t={t}: vertices={actual} expected={expected} PASS')
