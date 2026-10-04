from fractions import Fraction
from itertools import combinations


def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * (((n - i*i) // i) + 1)
    return [i for i, ok in enumerate(sieve) if ok]


def pair_criterion(p, q, r):
    return len({p, q, r}) == 3 and (q - 1) * (r - 1) == p + 1

small_primes = primes_upto(29)
edges = [(a, b) for a, b in combinations(small_primes, 2)]
short_checked = 0
triple_hits = 0

for k in (1, 2, 3):
    for es in combinations(edges, k):
        denoms = [a * b for a, b in es]
        value = sum((Fraction(1, d) for d in denoms), Fraction(0, 1))
        for p in small_primes:
            if value == Fraction(1, p):
                if k < 3:
                    raise AssertionError((p, es, 'forbidden short representation'))
                vertices = set()
                for a, b in es:
                    vertices.add(a)
                    vertices.add(b)
                if len(vertices) != 3 or p not in vertices:
                    raise AssertionError((p, es, 'three edges not a triangle'))
                q, r = sorted(vertices - {p})
                if not pair_criterion(p, q, r):
                    raise AssertionError((p, es, 'factor criterion failed'))
                triple_hits += 1
        short_checked += 1

P = primes_upto(5000)
Pset = set(primes_upto(5002))
factor_cases = []
for p in P:
    found = []
    n = p + 1
    for d in range(1, int(n ** 0.5) + 1):
        if n % d:
            continue
        e = n // d
        q, r = d + 1, e + 1
        if q in Pset and r in Pset and len({p, q, r}) == 3:
            if Fraction(1, p) != Fraction(1, p*q) + Fraction(1, p*r) + Fraction(1, q*r):
                raise AssertionError((p, q, r, 'identity failed'))
            found.append((q, r))
    if found:
        factor_cases.append((p, found))
    if p % 4 == 1:
        lhs = bool(found)
        rhs = (p + 2) in Pset
        if lhs != rhs:
            raise AssertionError((p, found, rhs, 'twin-prime corollary failed'))

print('VERIFY_OK',
      f'edge_subsets={short_checked}',
      f'triple_hits={triple_hits}',
      f'primes_to_5000={len(P)}',
      f'factor_cases={len(factor_cases)}',
      'first_cases=' + repr(factor_cases[:8]))
