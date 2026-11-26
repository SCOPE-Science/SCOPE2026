"""Exact residue-class counts for the two Fibonacci-offset screens."""

from math import lcm


def fibonacci_residue_cycle(prime):
    residues = []
    a, b = 0, 1
    while True:
        residues.append(a)
        a, b = b, (a + b) % prime
        if (a, b) == (0, 1):
            return residues


primes = (2, 3, 5, 7)
cycles = {prime: fibonacci_residue_cycle(prime) for prime in primes}
assert tuple(len(cycles[prime]) for prime in primes) == (3, 8, 20, 16)
period = lcm(*(len(cycles[prime]) for prime in primes), *(2 * p for p in primes))
assert period == 1680


def fib(index, prime):
    cycle = cycles[prime]
    return cycle[index % len(cycle)]


def passes(index, offset, cutoff):
    if fib(index, 2) != 1:
        return False
    if offset == 3 and fib(index, 3) != 2:
        return False
    if offset == 5 and index % 2 == 0:
        return False
    r = (index - 3) // 2
    tests = [(r, 3), (r + 1, 1)]
    if offset == 5:
        tests.append((r - 1, 5))
    return all(d % prime != 0 or fib(index, prime) == c % prime
               for prime in primes if prime <= cutoff for d, c in tests)


expected = {3: (140, 280, 140, 280), 5: (112, 224, 112, 224),
            7: (80, 144, 72, 152)}
for cutoff, counts in expected.items():
    left, right = ({g % period for g in range(9, 9 + period)
                    if passes(g, offset, cutoff)} for offset in (3, 5))
    union = left | right
    actual = (len(left), len(right), len(left & right), len(union))
    assert all(g % 2 == 1 for g in union)
    assert actual == counts, (cutoff, actual)
    if cutoff == 3:
        assert left == {g for g in range(period) if g % 24 in {5, 11}}
        assert right == {g for g in range(period) if g % 24 in {1, 5, 7, 11}}
    print(cutoff, *actual)
print('All residue counts verified.')
