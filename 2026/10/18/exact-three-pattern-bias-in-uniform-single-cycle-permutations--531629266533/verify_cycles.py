"""Independent finite checks of expected length-three patterns in uniform n-cycles.
Run: python verify_cycles.py (standard library only).
Finite tests corroborate the separate general counting proof.
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
from math import factorial

PATTERNS = ('123', '132', '213', '231', '312', '321')
DELTA = {'123': 0, '132': -1, '213': -1, '231': 1, '312': 1, '321': 0}


def pat(vals):
    return ''.join(str(1 + sum(t < v for t in vals)) for v in vals)


def cycles(n):
    for rest in permutations(range(2, n + 1)):
        order = (1,) + rest
        p = [0] * (n + 1)
        for j, x in enumerate(order):
            p[x] = order[(j + 1) % n]
        yield p


def q_formula(n, i, pattern):
    b = (n - 1) * (n - 2) * (n - 3)
    if pattern in ('123', '321'):
        return b // 6
    num = {
        '132': n**3 - 6*n**2 + 5*n + 6 + 6*i,
        '213': n**3 - 6*n**2 + 11*n - 6*i,
        '231': n**3 - 6*n**2 + 17*n - 18 - 6*i,
        '312': n**3 - 6*n**2 + 11*n - 12 + 6*i,
    }[pattern]
    assert num % 6 == 0
    return num // 6


def is_acyclic_on_domain(imgs, domain):
    f = dict(zip(domain, imgs))
    for x in domain:
        seen = set()
        while x in f:
            if x in seen:
                return False
            seen.add(x)
            x = f[x]
    return True


def test_finite():
    cycle_checks = mapping_checks = 0
    for n in range(4, 10):
        sums = Counter()
        count = 0
        for p in cycles(n):
            count += 1
            for i in range(1, n-1):
                sums[pat(p[i:i+3])] += 1
        assert count == factorial(n-1)
        assert sum(sums.values()) == count * (n-2)
        for q in PATTERNS:
            observed = Fraction(sums[q], count)
            predicted = Fraction(n-2,6) + Fraction(DELTA[q], 2*(n-1))
            assert observed == predicted, (n,q,observed,predicted)
            cycle_checks += 1
    for n in range(4, 16):
        for i in range(1, n-1):
            domain = (i,i+1,i+2)
            c = Counter()
            for vals in permutations(range(1,n+1),3):
                if is_acyclic_on_domain(vals,domain):
                    c[pat(vals)] += 1
            for q in PATTERNS:
                assert c[q] == q_formula(n,i,q), (n,i,q,c[q],q_formula(n,i,q))
                mapping_checks += 1
    print('PASS: cycle mean cases',cycle_checks,'and acyclic-triple counts',mapping_checks)

if __name__ == '__main__':
    test_finite()
