"""Exact conditional fixed-row NODF expectation, with independent enumeration checks.

Run with Python 3.9+ and no external dependencies. All calculations are rational.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def count_covered(r, n):
    return sum((-1)**j * choose(n, j) * prod(choose(n-j, a) for a in r)
               for j in range(n+1))


def prod(values):
    p = 1
    for value in values:
        p *= value
    return p


def pair_counts(r, n):
    """Number of covered matrices for each occupancy triple of two marked columns."""
    m = len(r)
    result = defaultdict(int)
    for j in range(n-1):
        cols = n-2-j
        distribution = {(0, 0, 0): 1}
        for a in r:
            coeff = (choose(cols, a), choose(cols, a-1), choose(cols, a-2))
            new = defaultdict(int)
            for (x, y, z), count in distribution.items():
                if coeff[0]:
                    new[x, y, z] += count*coeff[0]
                if coeff[1]:
                    new[x+1, y, z] += count*coeff[1]
                    new[x, y+1, z] += count*coeff[1]
                if coeff[2]:
                    new[x+1, y+1, z+1] += count*coeff[2]
            distribution = new
        scale = (-1)**j*choose(n-2, j)
        for key, count in distribution.items():
            result[key] += scale*count
    return {key:count for key,count in result.items() if count != 0}


def row_joint_covered(r, n, i, k):
    m = len(r)
    return sum((-1)**j*choose(n-1, j) * choose(n-1-j, r[i]-1) *
               choose(n-1-j, r[k]-1) *
               prod(choose(n-j, r[h]) for h in range(m) if h != i and h != k)
               for j in range(n))


def exact_expected_nodf(r, n):
    m = len(r)
    assert m >= 2 and n >= 2 and all(1 <= a <= n for a in r)
    universe = count_covered(r, n)
    if universe <= 0:
        raise ValueError('No covered matrices exist for these row sums')
    sum_rows = Fraction(0)
    for i, k in combinations(range(m), 2):
        if r[i] != r[k]:
            sum_rows += Fraction(n * row_joint_covered(r,n,i,k),min(r[i],r[k]))
    pairs = pair_counts(r,n)
    assert all(count >= 0 for count in pairs.values()), 'negative inclusion-exclusion count'
    assert sum(count for (x,y,z),count in pairs.items() if x > 0 and y > 0) == universe, (sum(count for (x,y,z),count in pairs.items() if x > 0 and y > 0), universe)
    sum_columns = sum((Fraction(count*z, min(x,y)) for (x,y,z),count in pairs.items()
                       if x > 0 and y > 0 and x != y and z > 0), Fraction(0))
    denominator = (choose(m,2)+choose(n,2))*universe
    return (sum_rows+choose(n,2)*sum_columns)/denominator


def nodf(A):
    m = len(A)
    n = len(A[0])
    assert all(len(row) == n for row in A)
    row_degrees = [sum(row) for row in A]
    col_degrees = [sum(A[i][j] for i in range(m)) for j in range(n)]
    assert min(row_degrees)>0 and min(col_degrees)>0
    total = Fraction(0)
    for i,k in combinations(range(m),2):
        if row_degrees[i] != row_degrees[k]:
            overlap = sum(A[i][j]*A[k][j] for j in range(n))
            total += Fraction(overlap, min(row_degrees[i],row_degrees[k]))
    for j,k in combinations(range(n),2):
        if col_degrees[j] != col_degrees[k]:
            overlap = sum(A[i][j]*A[i][k] for i in range(m))
            total += Fraction(overlap, min(col_degrees[j],col_degrees[k]))
    return total/(choose(m,2)+choose(n,2))


def brute_expected_nodf(r, n):
    choices = [list(combinations(range(n), d)) for d in r]
    sum_nodf, total = Fraction(0),0
    for rows in product(*choices):
        A = [[int(j in row) for j in range(n)] for row in rows]
        if all(any(A[i][j] for i in range(len(r))) for j in range(n)):
            sum_nodf += nodf(A)
            total += 1
    if total == 0:
        raise ValueError('No covered matrices')
    return sum_nodf/total, total


def run_tests():
    profiles, matrices = 0, 0
    for m,n in [(2,2),(2,3),(2,4),(2,5),(2,6),(3,2),(3,3),(3,4),
                (3,5),(3,6),(4,2),(4,3),(4,4),(4,5),(5,3)]:
        for r in product(range(1,n+1),repeat=m):
            if sum(r)<n: continue
            # One representant of each row-multiset avoids repeated costly checks.
            if tuple(sorted(r)) != r: continue
            exact=exact_expected_nodf(r,n)
            brute,count=brute_expected_nodf(r,n)
            assert exact==brute, f'mismatch m={m} n={n} row={r} formula={exact} brute={brute}'
            profiles+=1; matrices+=count
    # One pre-specified nontrivial 3x4 comparison.
    r=(1,2,3); n=4
    exact=exact_expected_nodf(r,n)
    brute,count=brute_expected_nodf(r,n)
    assert exact==brute
    print('VERIFY_OK', 'distinct_profiles', profiles, 'covered_matrices', matrices,
          'sample_profile',r,'sample_mean',str(exact), 'sample_count',count)

if __name__ == '__main__':
    run_tests()
