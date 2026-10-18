#!/usr/bin/env python3
"""Exact finite checks for factorial-square triple representation multiplicity.

This program checks finite examples only; asymptotic assertions require the
analytic arguments and published theorems cited in RESULT.md.
"""
from math import isqrt, factorial


def signatures(limit):
    # Encode parity of each prime exponent in k! as a bitset.
    primes = []
    masks = [0] * (limit + 1)
    for v in range(2, limit + 1):
        t = v
        mask = 0
        p = 2
        while p * p <= t:
            if t % p == 0:
                if p not in primes:
                    primes.append(p)
                while t % p == 0:
                    t //= p
                    mask ^= 1 << primes.index(p)
            p += 1
        if t > 1:
            if t not in primes:
                primes.append(t)
            mask ^= 1 << primes.index(t)
        masks[v] = masks[v - 1] ^ mask
    return masks, primes


def to_squarefree(mask, primes):
    out = 1
    for k, p in enumerate(primes):
        if (mask >> k) & 1:
            out *= p
    return out


def run():
    LIM = 260
    sig, primes = signatures(LIM)
    assert all(sig[c] != sig[d] or d == c + 1 and isqrt(d) ** 2 == d
               for d in range(2, LIM + 1) for c in range(1, d))
    for n in range(3, LIM + 1):
        consecutive = [c for c in range(1, n - 1) if sig[c] == (sig[n] ^ sig[n - 1])]
        all_reps = [(c, b) for b in range(2, n) for c in range(1, b)
                    if sig[c] ^ sig[b] ^ sig[n] == 0]
        assert len(consecutive) <= 2
        assert all((c, n-1) in all_reps for c in consecutive)
        for c in consecutive:
            x = factorial(c) * factorial(n-1) * factorial(n)
            assert isqrt(x)**2 == x
        if len(consecutive) == 2:
            c1, c2 = consecutive
            assert c2 == c1 + 1 and isqrt(c2)**2 == c2
    for t in range(2, 10):
        a = to_squarefree(sig[t*t], primes)
        assert a == to_squarefree(sig[t*t-1], primes)
    expected = [6, 70, 1430, 676039, 90751353, 35830670759,
                4155610296921974, 548506167006817226845]
    got = [to_squarefree(sig[t*t], primes) for t in range(2,10)]
    assert got == expected, (got, expected)
    for bound in (6, 70, 180, 250):
        direct = sum(1 for n in range(3, bound+1)
                     if sum(sig[c] == (sig[n] ^ sig[n - 1]) for c in range(1,n-1)) == 2)
        predicted = sum(max(0, isqrt(bound//to_squarefree(sig[t*t],primes))
                             - (isqrt((t*t+1)//to_squarefree(sig[t*t],primes))))
                        for t in range(2, isqrt(LIM)+1) if t*t < LIM and
                        to_squarefree(sig[t*t],primes) <= bound)
        if bound <= LIM:
            assert direct == predicted, (bound, direct, predicted)
    print('PASS: squarefree-factorial collision test for all 1<=c<d<=260')
    print('PASS: all triangular factorial-square triples with largest index <=260')
    print('PASS: exact square tests and maximal consecutive multiplicity 2')
    print('PASS: first eight duplicate squarefree kernels:', got)
    print('PASS: exact double-representation counts at X=6,70,180,250')
    print('NOTE: asymptotic error and exceptional-solution bounds are proven analytically, not by this finite test.')

if __name__ == '__main__':
    run()
