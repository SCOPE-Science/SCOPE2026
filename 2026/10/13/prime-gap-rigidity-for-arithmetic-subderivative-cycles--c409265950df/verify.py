"""Finite regression checks for the two-prime subderivative rigidity theorem.

Uses only the Python standard library. The theorem requires the symbolic proof;
these checks do not certify infinitely many prime pairs or starting integers.
"""
from math import gcd


def primes_upto(bound):
    out = []
    for n in range(2, bound + 1):
        if all(n % d for d in range(2, int(n**0.5) + 1)):
            out.append(n)
    return out


def valuation(n, prime):
    e = 0
    while n and n % prime == 0:
        e += 1
        n //= prime
    return e


def direct_derivative(n, p, q):
    a, b = valuation(n, p), valuation(n, q)
    return n // (p*q) * (a*q+b*p) if n % (p*q) == 0 else n*a//p + n*b//q


def symbolic_step(p, q, a, b):
    if a + b == 0:
        return None
    value = a*q + b*p
    r, s = 0, 0
    while value % p == 0:
        value //= p
        r += 1
    while value % q == 0:
        value //= q
        s += 1
    return (a - 1 + r, b - 1 + s, value)


def regression():
    primes = primes_upto(149)
    pair_count, max_states, direct_count, pending = 0, 0, 0, 0
    for i, p in enumerate(primes):
        if p > 29:
            break
        for q in primes[i + 1:]:
            if q > p**p:
                continue
            pair_count += 1
            for a in range(p + 1):
                for b in range(q + 1):
                    if a + b == 0 or a*q + b*p > p*q:
                        continue
                    max_states += 1
                    n = p**a * q**b
                    if a <= 8 and b <= 8:
                        v = direct_derivative(n, p, q)
                        z = symbolic_step(p, q, a, b)
                        assert v == p**z[0] * q**z[1] * z[2]
                        direct_count += 1
                    if (a, b) in ((p, 0), (0, q)):
                        assert direct_derivative(n, p, q) == n
                        continue
                    z = symbolic_step(p, q, a, b)
                    if z[2] > 1 or z[:2] == (0, 0):
                        continue
                    z2 = symbolic_step(p, q, *z[:2])
                    assert z2 is None or z2[2] > 1 or z2[:2] == (0, 0), (
                        p, q, a, b, z, z2
                    )
                    pending += 1
    # Direct checks with nontrivial support-free multipliers.
    for p, q in ((2, 3), (3, 5), (3, 7), (5, 11), (7, 19)):
        for m in range(1, 90):
            if gcd(m, p*q) != 1:
                continue
            for k in range(1, p+1):
                assert direct_derivative(m*p**k, p, q) == m*k*p**(k-1)
            assert direct_derivative(m*p**p, p, q) == m*p**p
            assert direct_derivative(m*q**q, p, q) == m*q**q
    print('VERIFY_OK')
    print('sampled_prime_pairs=', pair_count)
    print('possible_maximum_exponent_states=', max_states)
    print('direct_symbolic_step_comparisons=', direct_count)
    print('two_step_candidates_checked=', pending)
    print('finite_checks_are_not_a_proof=True')


if __name__ == '__main__':
    regression()
