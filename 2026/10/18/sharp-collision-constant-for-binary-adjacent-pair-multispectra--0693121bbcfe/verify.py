"""Direct census and run-composition check for binary 2-gram collisions.

Uses only the Python standard library. This is finite corroboration, not an
infinite proof of the sharp asymptotic.
"""
from collections import Counter
from math import comb, pi


def brute(n):
    classes = Counter()
    for mask in range(1 << n):
        a = d = b = c = 0
        old = mask & 1
        for j in range(1, n):
            cur = (mask >> j) & 1
            if old == 0 and cur == 0:
                a += 1
            elif old == 1 and cur == 1:
                d += 1
            elif old == 0 and cur == 1:
                b += 1
            else:
                c += 1
            old = cur
        classes[(a, b, c, d)] += 1
    return classes


def formulas(n):
    N = n - 1
    classes = {}
    for k in range((N - 1) // 2 + 1):
        for a in range(N - 2*k):
            d = N - 2*k - 1 - a
            h = comb(a+k, k)*comb(d+k, k)
            classes[(a, k+1, k, d)] = h
            classes[(a, k, k+1, d)] = h
    for k in range(1, N//2 + 1):
        for a in range(N - 2*k + 1):
            d = N - 2*k - a
            h = (comb(a+k, k)*comb(d+k-1, k-1)
                 + comb(a+k-1, k-1)*comb(d+k, k))
            classes[(a, k, k, d)] = h
    classes[(N, 0, 0, 0)] = 1
    classes[(0, 0, 0, N)] = 1
    return classes


def collision(n):
    p = formulas(n)
    return sum(v*v for v in p.values()), len(p), sum(p.values())


def main():
    for n in range(2, 18):
        direct = brute(n)
        analytic = formulas(n)
        assert direct == analytic, (n, 'direct spectrum differs')
        s, profiles, total = collision(n)
        assert total == 2**n
        assert s == sum(v*v for v in direct.values())
        if n in (2, 3, 8, 12, 17):
            print(f'exhaustive n={n} profiles={profiles} collisions={s} nP={n*s/4**n:.12f}')
    for n in (25, 50, 100, 200, 400, 800):
        s, profiles, total = collision(n)
        assert total == 2**n
        print(f'profile-sum n={n} profiles={profiles} nP={n*s/4**n:.12f}')
    print(f'ASYMPTOTIC_TARGET_3/(4pi)={3/(4*pi):.12f}')
    print('VERIFY_OK exhaustive_binary_lengths=2..17 class_formula_and_moments_checked')


if __name__ == '__main__':
    main()
