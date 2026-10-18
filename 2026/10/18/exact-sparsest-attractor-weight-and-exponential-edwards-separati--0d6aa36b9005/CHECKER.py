"""Standalone finite checks for the exact sparsest Riviera-attractor probability.

Run: python3 CHECKER.py
Requires only the Python 3 standard library.
Finite tests corroborate, but do not replace, the all-length proof.
"""
from collections import Counter
from itertools import permutations
from math import factorial, isclose, log

CHECKS = 0

def check(condition, description):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)


def legal(mask, n):
    return all((mask >> i) & 7 != 7 for i in range(n - 2))


def jammed(mask, n):
    return legal(mask, n) and all(
        (mask >> i) & 1 or not legal(mask | (1 << i), n)
        for i in range(n)
    )


def target(n):
    return sum(1 << i for i in range(n) if i % 4 in (1, 2))


def simulate_order(order):
    n = len(order)
    mask = 0
    for i in order:
        candidate = mask | (1 << i)
        if legal(candidate, n):
            mask = candidate
    return mask


def polynomial_add(dest, poly, shift, mult=1):
    for m, coeff in poly.items():
        dest[m + shift] += coeff * mult


def partitions(max_n):
    """Coefficient recursion for the exact published bivariate generating series."""
    numer = {0:{0:1}, 1:{1:1}, 2:{2:1, 1:-1}, 3:{2:1}, 5:{3:-1}}
    z = []
    for n in range(max_n + 1):
        p = Counter(numer.get(n, {}))
        if n >= 2:
            polynomial_add(p, z[n - 2], 1)
        if n >= 3:
            polynomial_add(p, z[n - 3], 2)
        if n >= 4:
            polynomial_add(p, z[n - 4], 2)
        if n >= 6:
            polynomial_add(p, z[n - 6], 3, -1)
        p = Counter({k: v for k, v in p.items() if v})
        z.append(p)
    return z


def main():
    z = partitions(80)
    check(z[4] == {2:1,3:2}, 'published Z4')
    check(z[8] == {4:1,5:10,6:1}, 'published Z8')
    check(z[12] == {6:1,7:30,8:15}, 'published Z12')
    check(z[14] == {8:50,9:40,10:1}, 'published Z14')
    for n in range(1, 81):
        for m, coeff in z[n].items():
            check(coeff > 0, ('nonpositive GF coefficient', n,m))
            check(2*m >= n, ('density violation', n,m))
        if n % 4 == 0:
            check(z[n].get(n // 2, 0) == 1, ('sparsest uniqueness', n))
        else:
            check(z[n].get(n // 2, 0) == 0 or 2*(n//2) != n, ('unexpected equality', n))
    for n in (4,8,12,16):
        arr=[b for b in range(1 << n) if jammed(b,n)]
        check(len(arr)==sum(z[n].values()), ('static census',n))
        minimal=[b for b in arr if 2*b.bit_count()==n]
        check(minimal==[target(n)], ('minimal unique pattern',n, minimal))
        check(jammed(target(n), n), ('block pattern is jammed',n))
        for b in arr:
            check(2*b.bit_count() >= n, ('static lower bound',n,b))
    for n in (4,8):
        counts=Counter(simulate_order(p) for p in permutations(range(n)))
        check(sum(counts.values()) == factorial(n), ('total permutation count',n))
        check(all(jammed(b,n) for b in counts), ('all outcomes jammed',n))
        check(counts[target(n)] == factorial(n)//(6**(n//4)), ('exact basin weight',n))
        check(sum(v for b,v in counts.items() if b.bit_count()==n//2) == counts[target(n)], ('edge event',n))
    check(factorial(4)//6==4, 'published N4 basin')
    check(factorial(8)//36==1120, 'published N8 basin')
    check(isclose(log(6)/4, 0.44793986730701374,rel_tol=1e-12), 'endpoint exponent')
    check(log(6)/4 > 0.337377, 'a priori entropy comparison')
    print(f'PASS: {CHECKS} exact finite assertions; permutation weights N=4 and N=8 are 4 and 1120.')

if __name__ == '__main__':
    main()
