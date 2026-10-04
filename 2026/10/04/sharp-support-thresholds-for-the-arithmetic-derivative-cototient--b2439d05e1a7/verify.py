#!/usr/bin/env python3
LIMIT = 1_000_000

spf = list(range(LIMIT + 1))
for i in range(2, int(LIMIT ** 0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, LIMIT + 1, i):
            if spf[j] == j:
                spf[j] = i

def factor(n):
    out = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[p] = e
    return out

def phi_from_factor(n, f):
    ans = n
    for p in f:
        ans = ans // p * (p - 1)
    return ans

def deriv_from_factor(n, f):
    return sum(e * (n // p) for p, e in f.items())

expected = {
    2: [4],
    3: [9],
    4: [],
    5: [25],
    6: [],
    7: [49],
    8: [8, 12],
    9: [18, 30],
}
seen = {k: [] for k in expected}

for n in range(1, LIMIT + 1):
    f = factor(n)
    ph = phi_from_factor(n, f) if n > 1 else 1
    D = deriv_from_factor(n, f)
    G = D - (n - ph)
    w = len(f)

    if 2 <= G <= 9:
        seen[G].append(n)

    if w == 1:
        p, e = next(iter(f.items()))
        if e >= 2:
            assert G == (e - 1) * p ** (e - 1)
            assert G >= 2
            if G == 2:
                assert n == 4
    elif w == 2:
        items = sorted(f.items())
        (p, a), (q, b) = items
        formula = p ** (a - 1) * q ** (b - 1) * ((a - 1) * q + (b - 1) * p + 1)
        assert G == formula
        if a == b == 1:
            assert G == 1
        else:
            assert G >= 8
            if G == 8:
                assert n == 12
    elif w >= 3:
        assert G >= 9
        if G == 9:
            assert n == 30

assert seen == expected, (seen, expected)
print('VERIFY_OK')
print('checked_n_max=' + str(LIMIT))
print('small_fibers_2_through_9=' + repr(seen))
print('support_thresholds_checked=true')
