from collections import defaultdict
from math import factorial

def critical_n(d):
    assert d >= 4 and d % 3 != 0
    return 2 + (d + 1) * (d + 2) // 6

def plane_count(d):
    n = critical_n(d)
    target = (n, n - 1, n - 2)
    dp = {(0, 0, 0): 1}
    for i in range(d + 1):
        for j in range(d - i + 1):
            k = d - i - j
            nd = defaultdict(int)
            for e, c in dp.items():
                if i and e[0] + 1 <= target[0]:
                    nd[(e[0] + 1, e[1], e[2])] += c * i
                if j and e[1] + 1 <= target[1]:
                    nd[(e[0], e[1] + 1, e[2])] += c * j
                if k and e[2] + 1 <= target[2]:
                    nd[(e[0], e[1], e[2] + 1)] += c * k
            dp = nd
    vandermonde = [
        ((2, 1, 0), 1),
        ((2, 0, 1), -1),
        ((1, 2, 0), -1),
        ((1, 0, 2), 1),
        ((0, 2, 1), 1),
        ((0, 1, 2), -1),
    ]
    ans = 0
    for shift, sign in vandermonde:
        e = tuple(target[t] - shift[t] for t in range(3))
        if min(e) >= 0:
            ans += sign * dp.get(e, 0)
    return ans

def K(q):
    return 2 * factorial(3 * q) // (factorial(q) * factorial(q + 1) * factorial(q + 2))

def v2_factorial(n):
    v = 0
    while n:
        n //= 2
        v += n
    return v

def v2_K(q):
    return 1 + v2_factorial(3*q) - v2_factorial(q) - v2_factorial(q+1) - v2_factorial(q+2)

expected = {
    4: 3297280,
    5: 420760566875,
    7: 279101475496912988004267637,
    8: 1876914105621812001806757234042994688,
    10: 9212839670339521387053252378983349723754232206532608000000000,
    11: 7937408575884424724019635722350148703822387692677961301359612005526786667486,
}
for d, value in expected.items():
    got = plane_count(d)
    assert got == value, (d, got, value)

odd_degrees = []
parity_checks = 0
for d in range(4, 300):
    if d % 3 == 0:
        continue
    if d % 2 == 0:
        predicted = 0
    else:
        m = (d - 1) // 2
        assert m % 3 in (0, 2)
        q = m * (m + 1) // 6
        predicted = K(q) & 1
    if predicted:
        odd_degrees.append(d)
    parity_checks += 1
assert odd_degrees == [5, 7], odd_degrees

valuation_checks = 0
for q in range(1, 5001):
    v = v2_K(q)
    assert (K(q) & 1) == (v == 0)
    assert (v == 0) == (q in (1, 2))
    valuation_checks += 1

assert K(1) == 1
assert K(2) == 5
assert K(3) == 42
print('VERIFY_OK', len(expected), parity_checks, valuation_checks)
print('ODD_CRITICAL_DEGREES_UNDER_300', odd_degrees)
