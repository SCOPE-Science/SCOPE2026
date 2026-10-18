"""Finite regression checks for the central-Delannoy neighboring-gcd theorem."""
from math import comb


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))


def delannoy_direct(n):
    return sum(comb(n, k) ** 2 * 2 ** k for k in range(n + 1))


def delannoy_mod_digits(n, p, vals):
    out = 1
    while n:
        out = out * vals[n % p] % p
        n //= p
    return out


def h(m, x, p):
    return sum(comb(m, j) ** 2 * pow(x, j, p) for j in range(m + 1)) % p


def main():
    a, b = 1, 3
    for n in range(350):
        assert a == delannoy_direct(n)
        a, b = b, (3 * (2 * n + 3) * b - (n + 1) * a) // (n + 2)

    blocks = 0
    primes = 0
    for p in range(3, 100, 2):
        if not is_prime(p):
            continue
        primes += 1
        vals = [delannoy_direct(j) % p for j in range(p)]
        roots = {j for j, v in enumerate(vals) if v == 0}
        z = len(roots)
        assert vals[0] == vals[-1] == 1
        assert all(not (vals[j] == vals[j + 1] == 0) for j in range(p - 1))
        assert z <= (p - 1) // 2
        m = (p - 1) // 2
        assert all(h(m, 1 - x, p) == (-1) ** m * h(m, x, p) % p for x in range(p))
        if p % 4 == 3:
            assert m in roots
        for n in range(350):
            assert delannoy_mod_digits(n, p, vals) == delannoy_direct(n) % p

        for L in range(1, 8):
            N = p ** L
            if N > 60000:
                break
            found = sum(
                not (delannoy_mod_digits(n, p, vals) == 0
                     and delannoy_mod_digits(n + 1, p, vals) == 0)
                for n in range(N)
            )
            predicted = 1 + (p - 1) * sum((p - z) ** h0 for h0 in range(L))
            assert found == predicted, (p, L, found, predicted)
            blocks += 1
    assert primes >= 24 and blocks >= 35
    print('VERIFY_OK', f'primes={primes}', f'blocks={blocks}')


if __name__ == '__main__':
    main()
