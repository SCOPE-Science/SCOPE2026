from math import comb


def mul(a, b, N):
    c = [0] * (N + 1)
    for i, ai in enumerate(a):
        if not ai:
            continue
        limit = min(len(b) - 1, N - i)
        for j in range(limit + 1):
            bj = b[j]
            if bj:
                c[i + j] += ai * bj
    return c


def euler_power(exponent, N, step=1):
    out = [1] + [0] * N
    for n in range(step, N + 1, step):
        factor = [0] * (N + 1)
        for k in range(N // n + 1):
            factor[n * k] = (-1 if k % 2 else 1) * comb(exponent, k)
        out = mul(out, factor, N)
    return out


def partition_numbers(N):
    out = [0] * (N + 1)
    out[0] = 1
    for n in range(1, N + 1):
        for j in range(n, N + 1):
            out[j] += out[j - n]
    return out


def t_core_series(t, N):
    out = partition_numbers(N)
    for n in range(1, N // t + 1):
        d = t * n
        factor = [0] * (N + 1)
        for k in range(N // d + 1):
            factor[d * k] = (-1 if k % 2 else 1) * comb(t, k)
        out = mul(out, factor, N)
    return out


def valuation(z, p):
    if z == 0:
        return 10**9
    z = abs(z)
    v = 0
    while z % p == 0:
        z //= p
        v += 1
    return v


cases = []
for p in (2, 3, 5, 7):
    for a in (1, 2, 3):
        t = p**a
        sharp_index = p**(a - 1)
        N = max(sharp_index, min(t + 3, 80))
        F = euler_power(t * t - 1, N)
        C = t_core_series(t, N)
        values = [valuation(F[n] - C[n], p) for n in range(N + 1) if F[n] != C[n]]
        assert values and min(values) >= a + 1
        assert valuation(F[sharp_index] - C[sharp_index], p) == a + 1
        cases.append((p, a, sharp_index, min(values)))

print(
    "VERIFY_OK cases=" + str(len(cases))
    + " sharp=" + ",".join(f"{p}^{a}@{n}" for p, a, n, _ in cases)
    + " minimum_order=" + ",".join(str(v) for _, _, _, v in cases)
)
