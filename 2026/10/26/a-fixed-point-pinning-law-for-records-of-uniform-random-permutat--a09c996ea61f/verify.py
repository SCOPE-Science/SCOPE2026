"""Independent exhaustive and rational checks for conditional record counts.

The proof for unbounded n is analytic; enumeration here only tests finite cases.
Run with Python >=3.9: python verify.py
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial

checks = 0

def verify(condition, details):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(details)

def mul(a, b):
    result = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result

def add(a, b):
    result = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a): result[i] += x
    for i, x in enumerate(b): result[i] += x
    return result

def scale(a, c):
    return [x * c for x in a]

def record_pgf(k):
    pol = [Fraction(1)]
    for h in range(k):
        pol = scale(mul(pol, [Fraction(h), Fraction(1)]), Fraction(1, h+1))
    return pol

def conditioned_pgf(n, i):
    m, N = i-1, n-1
    correction = scale(mul(record_pgf(m), record_pgf(N-m)), Fraction(1, comb(N,m)))
    return add(record_pgf(N), mul([Fraction(-1),Fraction(1)], correction))

# Independently enumerate full permutation space; no recurrence or decomposition
# is used for the observed probability counts.
for n in range(2, 10):
    tally = [[0] * (n+1) for _ in range(n)]
    count = [0] * n
    for permutation in permutations(range(1, n+1)):
        highest = 0
        records = 0
        for v in permutation:
            if v > highest:
                highest = v
                records += 1
        for ix, v in enumerate(permutation):
            if v == ix+1:
                tally[ix][records] += 1
                count[ix] += 1
    expected_conditioning_count = factorial(n-1)
    for i in range(1,n+1):
        observed = [Fraction(x, expected_conditioning_count) for x in tally[i-1]]
        expected = conditioned_pgf(n,i)
        expected += [Fraction(0)] * (n+1-len(expected))
        verify(count[i-1] == expected_conditioning_count, ('count',n,i,count[i-1]))
        for k in range(n+1):
            verify(observed[k] == expected[k], ('pgf-coefficient',n,i,k,observed[k],expected[k]))
        observed_mean = sum(Fraction(k)*observed[k] for k in range(n+1))
        predicted_mean = sum(Fraction(1,j) for j in range(1,n)) + Fraction(1,comb(n-1,i-1))
        verify(observed_mean == predicted_mean,('mean',n,i,observed_mean,predicted_mean))
        expected_cov = Fraction(1,i*comb(n,i))-Fraction(1,n*n)
        calculated_cov = Fraction(1,n)*(observed_mean-sum(Fraction(1,j) for j in range(1,n+1)))
        verify(expected_cov == calculated_cov,('covariance',n,i))
        verify(conditioned_pgf(n,i) == conditioned_pgf(n,n+1-i),('reflection',n,i))

for n in range(5,401):
    for i in range(1,n+1):
        cov = Fraction(1,i*comb(n,i))-Fraction(1,n*n)
        positive = i in (1,2,n-1,n)
        verify((cov>0)==positive, ('four-boundary',n,i,cov))
        verify(cov != 0, ('no-zeros',n,i))
    aggregate = sum((Fraction(1,i*comb(n,i))-Fraction(1,n*n)) for i in range(1,n+1))
    reciprocal_binomial = Fraction(1,n)*(sum(Fraction(1,comb(n-1,k)) for k in range(n)) - 1)
    verify(aggregate == reciprocal_binomial and aggregate>0,('aggregate',n))

print('PASS:', checks, 'independent enumeration and rational identity assertions')
print('Enumerated uniform permutations at every n=2,...,9 and all fixed-point positions.')
print('Checked finite all-position covariance sign profiles through n=400.')
print('These tests do not replace the analytic proof for unrestricted n.')
