"""Independent exhaustive tests of minimum Italian-labeling formula on sunlet graphs.

Usage: python3 checks/verify_sunlet.py
No external dependencies.
"""
from itertools import product
from math import ceil

def formula(n):
    q, r = divmod(n, 3)
    if r == 0:
        return n + q, 3 * 2**q
    if r == 1:
        return n + q + 1, n * (q + 3) * 2**q
    return n + q + 1, n * 2**(q + 1)

def cycle_search(n):
    best, count = 10**9, 0
    for a in product((0, 1, 2), repeat=n):
        weight = 0
        for i, t in enumerate(a):
            if t == 0:
                weight += 1 + (a[(i - 1) % n] + a[(i + 1) % n] == 0)
            else:
                weight += 2
        if weight < best:
            best, count = weight, 1
        elif weight == best:
            count += 1
    return best, count

def fully_exhaustive(n):
    # No optimization based on the theorem: examine all 3^(2n) labelings.
    best, count = 10**9, 0
    for pairs in product(range(9), repeat=n):
        a = [v // 3 for v in pairs]
        b = [v % 3 for v in pairs]
        w = sum(a) + sum(b)
        if w > best:
            continue
        if any(b[i] == 0 and a[i] != 2 for i in range(n)):
            continue
        if any(a[i] == 0 and
               (a[(i - 1) % n] + a[(i + 1) % n] + b[i]) < 2
               for i in range(n)):
            continue
        if w < best:
            best, count = w, 1
        elif w == best:
            count += 1
    return best, count

if __name__ == '__main__':
    for n in range(3, 13):
        predicted = formula(n)
        computed = cycle_search(n)
        assert computed == predicted, (n, computed, predicted)
        print(f'cycle-search n={n} minimum={computed[0]} count={computed[1]} PASS', flush=True)
    for n in range(3, 7):
        predicted = formula(n)
        computed = fully_exhaustive(n)
        assert computed == predicted, (n, computed, predicted)
        print(f'all-labelings n={n} minimum={computed[0]} count={computed[1]} PASS', flush=True)
    print('ALL CHECKS PASSED', flush=True)
