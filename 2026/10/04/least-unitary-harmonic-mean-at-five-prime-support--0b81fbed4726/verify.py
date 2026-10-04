#!/usr/bin/env python3
from fractions import Fraction
from math import prod

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def prime_power_base(x):
    """Return p iff x=p^a for a prime p and a>=1; otherwise return None."""
    if x < 2:
        return None
    n = x
    d = 2
    while d*d <= n:
        if n % d == 0:
            p = d
            while n % p == 0:
                n //= p
            if n == 1 and is_prime(p):
                return p
            return None
        d = 3 if d == 2 else d + 2
    return x if is_prime(x) else None

def admissible_bound(prefix, target, remaining, start):
    """
    Largest integer x>=start satisfying
        prefix*(x/(x+1))^remaining <= target.
    The predicate is monotone in x.
    """
    def ok(x):
        return prefix * Fraction(x**remaining, (x+1)**remaining) <= target
    if not ok(start):
        return start - 1
    x = start
    while ok(x + 1):
        x += 1
    return x

def enumerate_target(h, k=5):
    target = Fraction(h, 2**k)
    solutions = []
    nodes = 0
    largest_bound = 0

    def rec(chosen, bases, prefix, last):
        nonlocal nodes, largest_bound
        remaining = k - len(chosen)

        if remaining == 1:
            if prefix <= target:
                return
            forced = target / (prefix - target)
            if forced.denominator != 1:
                return
            x = forced.numerator
            if x <= last:
                return
            base = prime_power_base(x)
            if base is None or base in bases:
                return
            values = chosen + [x]
            exact = Fraction(1, 1)
            for z in values:
                exact *= Fraction(z, z + 1)
            assert exact == target
            assert len({prime_power_base(z) for z in values}) == k
            solutions.append(tuple(values))
            return

        assert prefix > target
        bound = admissible_bound(prefix, target, remaining, last + 1)
        largest_bound = max(largest_bound, bound)
        for x in range(last + 1, bound + 1):
            base = prime_power_base(x)
            if base is None or base in bases:
                continue
            nodes += 1
            new_prefix = prefix * Fraction(x, x + 1)
            if new_prefix <= target:
                continue
            rec(chosen + [x], bases | {base}, new_prefix, x)

    rec([], set(), Fraction(1, 1), 1)
    solutions.sort()
    return solutions, nodes, largest_bound

expected = {
    10: [],
    11: [],
    12: [],
    13: [(2, 5, 7, 9, 13), (3, 4, 5, 7, 13)],
}

for h in (10, 11, 12, 13):
    sols, nodes, bound = enumerate_target(h)
    assert sols == expected[h], (h, sols)
    products = [prod(s) for s in sols]
    print(
        f"h={h} solutions={len(sols)} nodes={nodes} "
        f"largest_bound={bound} products={products}"
    )

assert sorted(prod(s) for s in expected[13]) == [5460, 8190]
print("VERIFY_OK")
