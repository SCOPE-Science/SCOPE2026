"""Reproduce finite checks for the derivative–totient fixed-prime counting law.

Python 3 standard library only. Finite tests are not proofs of asymptotics.
"""
from math import isqrt, log


def primes_upto(limit):
    prime = bytearray(b'\x01') * (limit + 1)
    prime[0:2] = b'\x00\x00'
    for d in range(2, isqrt(limit) + 1):
        if prime[d]:
            prime[d*d:limit+1:d] = b'\x00' * ((limit - d*d)//d + 1)
    return [x for x in range(limit + 1) if prime[x]]


def factor(n):
    out = {}
    q = n
    for d in range(2, isqrt(q) + 1):
        while q % d == 0:
            out[d] = out.get(d, 0) + 1
            q //= d
        if q == 1:
            break
    if q > 1:
        out[q] = out.get(q, 0) + 1
    return out


def deriv_phi(n):
    fac = factor(n)
    deriv = sum((n // p) * a for p, a in fac.items())
    phi = n
    for p in fac:
        phi = phi // p * (p - 1)
    return deriv, phi


def exponent_pair(p, q):
    if p == 2 or q % p == 1:
        return None
    t = (-pow(q, -1, p)) % p
    assert 1 <= t <= p - 2
    a, b = p - 1 - t, (t*q - (p-1)) // p
    return a, b


def verify():
    ps = primes_upto(1000)
    pair_cases = 0
    for p in ps:
        if p > 31:
            break
        for q in ps:
            if not p < q <= 101:
                continue
            # Independent Diophantine enumeration, without computing t.
            solutions = [(a, b) for a in range(1, p)
                         for b in range(1, q)
                         if a*q + b*p == (p-1)*(q-1)]
            pair = exponent_pair(p, q)
            assert solutions == ([] if pair is None else [pair]), (p, q, solutions, pair)
            if pair is not None:
                a, b = pair
                n = p**a * q**b
                lhs = a * p**(a-1) * q**b + b * p**a * q**(b-1)
                rhs = (p-1) * p**(a-1) * (q-1) * q**(b-1)
                assert lhs == rhs
            pair_cases += 1

    bound = 180000
    records = {}
    direct_count = 0
    for n in range(2, bound + 1):
        f = factor(n)
        if len(f) != 2:
            continue
        p, q = sorted(f)
        if deriv_phi(n)[0] == deriv_phi(n)[1]:
            direct_count += 1
            records.setdefault(p, []).append(n)
    for p in ps:
        if p > isqrt(bound):
            break
        via_parameter = []
        for q in ps:
            if q <= p:
                continue
            ap = exponent_pair(p, q)
            if ap is None:
                continue
            a, b = ap
            n = p**a * q**b
            if n <= bound:
                via_parameter.append(n)
        assert sorted(via_parameter) == sorted(records.get(p, [])), (p, via_parameter, records.get(p, []))

    for p in [3, 5, 7]:
        for power in [8, 16, 32, 64, 128]:
            X = 10**power
            direct = 0
            for q in ps:
                if q <= p:
                    continue
                exponents = exponent_pair(p, q)
                if exponents is not None:
                    a, b = exponents
                    if p**a * q**b <= X:
                        direct += 1
            # Second implementation: enumerate linear Diophantine pairs.
            alternative = 0
            for q in ps:
                if q <= p:
                    continue
                for a in range(1, p):
                    numer = (p - 1) * (q - 1) - a*q
                    if numer > 0 and numer % p == 0:
                        b = numer // p
                        if p**a * q**b <= X:
                            alternative += 1
            assert direct == alternative, (p, power, direct, alternative)

    print(f'VERIFY_OK: {pair_cases} independent two-prime Diophantine enumerations;'
          f' {direct_count} direct semiprime-support equality cases through {bound};'
          ' 15 exact high-cutoff counting comparisons.')
    print('Caution: asymptotic expansion is proved analytically, not by these finite tests.')


if __name__ == '__main__':
    verify()
