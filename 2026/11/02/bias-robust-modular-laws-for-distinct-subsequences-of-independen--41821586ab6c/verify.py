"""Independent finite checks for modular distinct-subsequence counts.

Run: python verify.py
Requires Python standard library only. All enumerations have finite scope.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from math import gcd, prod


def primitive_states(m):
    return {(x, y) for x in range(m) for y in range(m) if gcd(x, y, m) == 1}


def maps(m, pair):
    x, y = pair
    return (((x + y) % m, y), (x, (x + y) % m))


def predicted(m, a):
    primes = [p for p in range(2, m + 1)
              if m % p == 0 and all(p % d for d in range(2, int(p**0.5) + 1))]
    den = Fraction(1, m)
    for p in primes:
        if (a + 2) % p == 0:
            den *= Fraction(p, p + 1)
        else:
            den *= Fraction(p*p, p*p - 1)
    return den


def subseq_count_literal(bits):
    subs = {()}
    for b in bits:
        subs |= {s + (b,) for s in tuple(subs)}
    return len(subs) - 1


def count_pair_exact(bits):
    x = y = 1
    for b in bits:
        if b == 0:
            x += y
        else:
            y += x
    return x, y


# Independent set-based subsequence enumeration, all words through length 12.
num_words = 0
for n in range(13):
    for bits in product((0, 1), repeat=n):
        x, y = count_pair_exact(bits)
        assert subseq_count_literal(bits) == x + y - 2, (bits, x, y)
        assert gcd(x, y) == 1
        num_words += 1

# Every primitive pair is in the finite orbit; stationary fibers match formula.
num_moduli = 0
for m in range(2, 25):
    v = primitive_states(m)
    reached = {(1 % m, 1 % m)}
    queue = deque(reached)
    while queue:
        for target in maps(m, queue.popleft()):
            if target not in reached:
                reached.add(target)
                queue.append(target)
    assert reached == v, (m, len(reached), len(v))
    if m <= 8:
        # Independently test the fixed-length positivity lemma for all starts/ends.
        exactly = {start: {start} for start in v}
        for _ in range(2*(len(v)-1)):
            exactly = {start: {target for current in ends for target in maps(m, current)}
                       for start, ends in exactly.items()}
        assert all(ends == v for ends in exactly.values()), (m, len(v))
    assert (1 % m, 0) in maps(m, (1 % m, 0))
    assert len(v) == m*m*prod(Fraction(1, 1) - Fraction(1, p*p)
      for p in range(2, m + 1) if m % p == 0 and all(p % d for d in range(2, int(p**0.5) + 1)))
    for a in range(m):
        got = Fraction(sum((x + y - 2) % m == a for x, y in v), len(v))
        assert got == predicted(m, a), (m, a, got, predicted(m, a))
    num_moduli += 1

# Independently enumerate probability mass over words and compare exact state recursions.
num_weight_cases = 0
for m in (2, 3, 4, 5, 7):
    for n in range(9):
        ps = (Fraction(1, 4), Fraction(2, 3), Fraction(3, 5), Fraction(1, 3))
        masses = [Fraction(0) for _ in range(m)]
        for bits in product((0, 1), repeat=n):
            prob = prod(ps[i % len(ps)] if bits[i] else 1-ps[i % len(ps)] for i in range(n))
            val = subseq_count_literal(bits)
            masses[val % m] += prob
        dp = {(1 % m, 1 % m): Fraction(1)}
        for i in range(n):
            nxt = defaultdict(Fraction)
            p = ps[i % len(ps)]
            for v, mass in dp.items():
                a, b = maps(m, v)
                nxt[a] += (1-p)*mass
                nxt[b] += p*mass
            dp = dict(nxt)
        derived = [sum((val for (x, y), val in dp.items() if (x+y-2) % m == a), Fraction(0)) for a in range(m)]
        assert masses == derived, (m, n, masses, derived)
        num_weight_cases += 1

# Bias robustness: a nonstationary independent sequence approaches the arithmetic law.
max_tv = 0
for m in range(2, 11):
    dp = {(1 % m, 1 % m): 1.0}
    biases = (0.11, 0.89, 0.22, 0.76, 0.4)
    prev_tv = 1.0
    target = {v: 1.0 / len(primitive_states(m)) for v in primitive_states(m)}
    for i in range(800):
        p = biases[i % len(biases)]
        nxt = defaultdict(float)
        for v, mass in dp.items():
            a, b = maps(m, v)
            nxt[a] += (1-p) * mass
            nxt[b] += p * mass
        dp = dict(nxt)
        tv = .5 * sum(abs(dp.get(v, 0) - weight) for v, weight in target.items())
        assert tv <= prev_tv + 1e-11, (m, i, tv, prev_tv)
        prev_tv = tv
    assert prev_tv < 0.00005, (m, prev_tv)
    max_tv = max(max_tv, prev_tv)

print('VERIFY_OK literal_words=%d moduli=%d independent_probability_cases=%d max_nonstationary_tv=%.9g' %
      (num_words, num_moduli, num_weight_cases, max_tv))
