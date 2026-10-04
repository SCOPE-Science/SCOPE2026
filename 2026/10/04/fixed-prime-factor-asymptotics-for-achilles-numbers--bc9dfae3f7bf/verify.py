#!/usr/bin/env python3
import math
from collections import Counter

BOUND = 100_000_000

def spf_sieve(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    for i in range(2, math.isqrt(n) + 1):
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def factor(n, spf):
    out = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out

def main():
    lim = max(math.isqrt(BOUND), int(round(BOUND ** (1/3))) + 4)
    spf = spf_sieve(lim + 2)
    squarefree = []
    for b in range(1, int(round(BOUND ** (1/3))) + 5):
        fb = factor(b, spf)
        if all(e == 1 for e in fb.values()):
            squarefree.append((b, fb))
    total = 0
    by_omega = Counter()
    principal = Counter()
    seen = set()
    for b, fb in squarefree:
        b3 = b ** 3
        if b3 > BOUND:
            break
        for a in range(1, math.isqrt(BOUND // b3) + 1):
            n = a * a * b3
            if n in seen:
                raise AssertionError('square-cube representation was not unique')
            seen.add(n)
            exps = {}
            for p, e in factor(a, spf).items():
                exps[p] = 2 * e
            for p in fb:
                exps[p] = exps.get(p, 0) + 3
            if not exps:
                continue
            g = 0
            for e in exps.values():
                g = math.gcd(g, e)
            if min(exps.values()) >= 2 and g == 1:
                total += 1
                r = len(exps)
                by_omega[r] += 1
                vals = list(exps.values())
                if sum(e % 2 for e in vals) == 1 and vals.count(2) == r - 1:
                    principal[r] += 1
    if total != 10553:
        raise AssertionError((total, 'expected 10553 from OEIS A052486 below 10^8'))
    expected = {2: 2861, 3: 5785, 4: 1865, 5: 42}
    if dict(by_omega) != expected:
        raise AssertionError((dict(by_omega), expected))
    expected_principal = {2: 2350, 3: 2762, 4: 781, 5: 31}
    if dict(principal) != expected_principal:
        raise AssertionError((dict(principal), expected_principal))
    print('VERIFY_OK bound=%d total=%d omega=%s principal=%s' %
          (BOUND, total, ','.join('%d:%d' % x for x in sorted(by_omega.items())),
           ','.join('%d:%d' % x for x in sorted(principal.items()))))

if __name__ == '__main__':
    main()
