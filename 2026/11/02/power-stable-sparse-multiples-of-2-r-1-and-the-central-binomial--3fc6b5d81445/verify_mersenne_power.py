"""Exact integer tests of Mersenne-power sparse multiples and central binomial valuations.
Finite checks corroborate, but do not prove, unrestricted statements.
"""
from math import comb, gcd


def lift_exponent(r, k):
    assert r >= 2 and k >= 1
    M = (1 << r) - 1
    t = 0
    for s in range(1, k):
        mod = M ** s
        H = (pow(1 + M, t, M * mod) - 1) // M
        target = (-pow(2, -1, mod)) % mod
        step = M ** (s - 1)
        assert (target - H) % step == 0
        digit = ((target - H) // step) % M
        t += digit * step
        H1 = (pow(1 + M, t, M * mod) - 1) // M
        assert (1 + 2 * H1) % mod == 0
    assert 0 <= t < M ** (k - 1)
    return t


def sparse_exponents(r, k):
    t = lift_exponent(r, k)
    return [0, 1 + r * t] + list(range(2, r))


def central_binom_p_valuation(n, p):
    total, power = 0, p
    while power <= 2 * n:
        total += (2 * n // power) - 2 * (n // power)
        power *= p
    return total


def prime_list(stop):
    return [p for p in range(2, stop) if p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))]


def order_mod(p, u):
    assert u > 1 and gcd(p, u) == 1
    v, h = p % u, 1
    while v != 1:
        v = v * p % u
        h += 1
        assert h <= u
    return h


def odd_prime_witness(modulus, p):
    u, e = modulus, 0
    while u % p == 0:
        u //= p
        e += 1
    if u == 1:
        return [e]
    h = order_mod(p, u)
    return [e + j * h for j in range(u)]


def main():
    checks = 0
    for r in range(2, 9):
        for k in range(1, 5 if r <= 5 else 4 if r <= 6 else 3):
            m = (1 << r) - 1
            mod = m ** k
            exps = sparse_exponents(r, k)
            assert len(exps) == len(set(exps)) == r
            assert sum(pow(2, e, mod) for e in exps) % mod == 0
            assert len(set(e % r for e in exps)) == r
            # Materialize for small witnesses and independently check valuation.
            if max(exps) < 100000:
                n = sum(1 << e for e in exps)
                assert n % mod == 0
                assert n.bit_count() == r
                if n.bit_length() < 10000:
                    assert central_binom_p_valuation(n, 2) == r
            checks += 1
    for r in range(2, 6):
        m = (1 << r) - 1
        for k in range(1, 4):
            mod = m**k
            for p in prime_list(29):
                if p == 2:
                    continue
                if mod > 4000:
                    continue
                exps = odd_prime_witness(mod, p)
                assert len(set(exps)) == len(exps)
                assert sum(pow(p, e, mod) for e in exps) % mod == 0
                if max(exps) < 8000:
                    n = sum(p ** e for e in exps)
                    assert n % mod == 0
                    if n < 20000:
                        assert central_binom_p_valuation(n, p) == 0
    for r in range(2, 7):
        m = (1 << r) - 1
        for k in range(1, 5):
            mod = m**k
            bound = 500 if mod > 1000 else 1500
            for a in range(1, bound + 1):
                n = mod * a
                assert n.bit_count() >= r
                if n <= 500:
                    assert central_binom_p_valuation(n, 2) >= r
                    assert central_binom_p_valuation(n, 2) == n.bit_count()
    print('VERIFY_OK lifted_Mersenne_powers=', checks,
          'odd_prime_zero_carry_witnesses=checked',
          'initial_multiple_minimal_weight=checked',
          'central_binomial_carry_identity=checked')

if __name__ == '__main__':
    main()
