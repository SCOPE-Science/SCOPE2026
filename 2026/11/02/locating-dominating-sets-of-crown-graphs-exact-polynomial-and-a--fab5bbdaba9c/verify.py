"""Reproduce the locating-dominating enumeration of crown graphs.

No external packages. All tests use integer arithmetic. Run: python verify.py.
The finite checks corroborate, but do not establish, the infinite proof.
"""
from collections import Counter
from math import comb


def graph_neighborhood_masks(n):
    """a_i has neighbors b_j for j != i, and conversely."""
    return [sum(1 << (n+j) for j in range(n) if j != i) for i in range(n)] + [
        sum(1 << i for i in range(n) if i != j) for j in range(n)
    ]


def brute_counts(n):
    neighborhoods = graph_neighborhood_masks(n)
    counts = Counter()
    for selected in range(1 << (2*n)):
        seen = set()
        valid = True
        for v in range(2*n):
            if selected & (1 << v):
                continue
            identifying_set = neighborhoods[v] & selected
            if not identifying_set or identifying_set in seen:
                valid = False
                break
            seen.add(identifying_set)
        if valid:
            counts[selected.bit_count()] += 1
    return counts


def algebraic_counts(n):
    if n == 2:
        return Counter({2: 4, 3: 4, 4: 1})
    coeffs = Counter()
    for j in range(n+1):
        coeffs[n+j] += comb(n, j) * 2**(n-j)
    for j in range(n):
        coeffs[n-1+j] += n * comb(n-1, j) * 2**(n-1-j)
    coeffs[n-1] -= 2*n*n
    coeffs[n] -= 2*n
    if n == 3:
        coeffs[2] += 6
    return Counter({k: v for k, v in coeffs.items() if v})


def criterion_count(n):
    # Independent bit-profile test, not using the algebraic coefficient formula.
    counts = Counter()
    for umask in range(1 << n):
        for vmask in range(1 << n):
            x = n - (umask | vmask).bit_count()
            u, v = umask.bit_count(), vmask.bit_count()
            valid = False
            if u >= 2 and v >= 2:
                valid = x <= 1
            elif u == 0:
                valid = vmask == (1 << n)-1
            elif v == 0:
                valid = umask == (1 << n)-1
            elif u == 1:
                i = (umask & -umask).bit_length()-1
                valid = (vmask & (1 << i)) != 0 and x <= 1
            elif v == 1:
                i = (vmask & -vmask).bit_length()-1
                valid = (umask & (1 << i)) != 0 and x <= 1
            if valid:
                counts[u+v] += 1
    return counts


def run():
    print('Exhaustive original-neighborhood checks:')
    for n in range(2, 10):
        brute = brute_counts(n)
        algebra = algebraic_counts(n)
        criterion = criterion_count(n)
        assert brute == algebra == criterion, (n, brute, algebra, criterion)
        print(n, 'LD sets:', sum(brute.values()), 'minimum:', min(brute),
              'minimum count:', brute[min(brute)])
    print('Exact coefficient and minimum-count checks:')
    for n in range(5, 201):
        counts = algebraic_counts(n)
        assert min(counts) == n-1
        assert counts[n-1] == n*(2**(n-1)-2*n)
        assert all(value > 0 for value in counts.values())
        assert max(counts) == 2*n and counts[2*n] == 1
        assert sum(counts.values()) == 3**n + n*3**(n-1) - 2*n*n - 2*n
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
