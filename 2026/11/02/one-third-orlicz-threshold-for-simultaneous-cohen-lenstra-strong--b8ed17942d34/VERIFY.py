"""Exact small-weight consistency checks for the Cohen--Lenstra partition model.

Run with: python3 VERIFY.py
The mathematical statements for arbitrary primes and weights use the proof, not
this finite regression check.
"""
from collections import defaultdict
from itertools import product
from fractions import Fraction


def partitions(n, smallest=1):
    if n == 0:
        yield ()
        return
    for i in range(smallest, n + 1):
        for tail in partitions(n-i, i):
            yield (i,) + tail


def elementary_aut_count(prime, exponents):
    # All possible images of cyclic generators (respecting their orders).
    elements = list(product(*(range(prime**k) for k in exponents)))
    candidates = [
        [g for g in elements if all((prime**k)*g[j] % (prime**exponents[j]) == 0
                                    for j in range(len(exponents)))]
        for k in exponents
    ]
    count = 0
    for images in product(*candidates):
        attained = set()
        for coefficients in product(*(range(prime**k) for k in exponents)):
            attained.add(tuple(sum(coefficients[i]*images[i][j]
                                  for i in range(len(exponents))) % (prime**exponents[j])
                                for j in range(len(exponents))))
        if len(attained) == len(elements):
            count += 1
    return count


def closed_aut_count(prime, exponents):
    multiplicity = defaultdict(int)
    for k in exponents:
        multiplicity[k] += 1
    maxk = max(exponents, default=0)
    S = sum(sum(k >= j for k in exponents)**2 for j in range(1,maxk+1))
    n = prime**S
    for m in multiplicity.values():
        for j in range(1,m+1):
            n = Fraction(n)*(1-Fraction(1,prime**j))
    assert n.denominator == 1
    return n.numerator, S


def main():
    checks = 0
    for prime in (2,3):
        for n in range(1,5 if prime == 2 else 4):
            for parts in partitions(n):
                auto, S = closed_aut_count(prime, parts)
                brute = elementary_aut_count(prime, parts)
                assert brute == auto, (prime, parts, auto, brute)
                checks += 1
    limit = 90
    by_square_sums = [0]*(limit+1)
    by_square_sums[0]=1
    for k in range(1,int(limit**0.5)+1):
        for S in range(k*k,limit+1):
            by_square_sums[S]+=by_square_sums[S-k*k]
    by_partitions = [0]*(limit+1)
    for n in range(0,24):
        for parts in partitions(n):
            _, S = closed_aut_count(2, parts)
            if S<=limit:
                by_partitions[S]+=1
    # The partition enumeration is complete only for groups of order <=2^23;
    # compare the range S<=23, where all groups automatically have order <=2^23.
    for S in range(0,24):
        assert by_square_sums[S] == by_partitions[S], (S, by_square_sums[S],by_partitions[S])
    print('VERIFY_OK automorphism_formula_exact_cases=%d square_partition_weights=24 primes=2,3' % checks)


if __name__ == '__main__':
    main()
