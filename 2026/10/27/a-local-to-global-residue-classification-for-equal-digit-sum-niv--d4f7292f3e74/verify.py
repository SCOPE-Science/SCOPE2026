"""Exact checks of the arithmetic-progression and digit-block construction."""
import math
from itertools import product


def digitsum(n, base):
    value = 0
    while n:
        n, rem = divmod(n, base)
        value += rem
    return value


def base_part(m, b):
    rem, smooth = m, 1
    for p in range(2, b + 1):
        if b % p == 0 and all(p % t for t in range(2, math.isqrt(p) + 1)):
            while rem % p == 0:
                rem //= p
                smooth *= p
    return smooth, rem


def prefix_classes(B, b, v, mod):
    return {sum(d * B**j for j, d in enumerate(ds)) % mod:
            ds for ds in product(range(b), repeat=v)}


def order(a, n):
    if n == 1:
        return 1
    assert math.gcd(a, n) == 1
    t, power = 1, a % n
    while power != 1:
        power = (power * a) % n
        t += 1
    return t


def repunit_change(R, B):
    if R == 0:
        return []
    rep = [1]
    while B * rep[-1] + 1 <= R:
        rep.append(B * rep[-1] + 1)
    answer = []
    for j in reversed(range(len(rep))):
        x, R = divmod(R, rep[j])
        assert x <= B
        answer.extend([j + 1] * x)
    assert R == 0
    return answer


def construct(b, k, m, r):
    B = b**k
    m0, m1 = base_part(m, b)
    v = 0
    while B**v % m0:
        v += 1
    cls = prefix_classes(B, b, v, m0)
    if r % m0 not in cls:
        return None
    ds = cls[r % m0]
    c = sum(d * B**j for j, d in enumerate(ds))
    d = sum(ds)
    T = (c - d) // (B - 1)
    assert c - d == T * (B - 1)
    for s in range(max(2, d + 1), 20000):
        if s % m1 != r % m1 or math.gcd(s, B) != 1:
            continue
        N = math.lcm(s, m1)
        q = N // math.gcd(N, B - 1)
        R = (-T) % q
        adjustments = repunit_change(R, B)
        if len(adjustments) <= s - d:
            break
    else:
        raise AssertionError('No digit-sum parameter found in bounded test')
    period = order(B, N)
    high_residues = adjustments + [0] * (s - d - len(adjustments))
    used = set(range(v))
    exponents = []
    for j in high_residues:
        e = j % period
        while e < v or e in used:
            e += period
        used.add(e)
        exponents.append(e)
    assert len(exponents) == len(set(exponents))
    nmod = (c + sum(pow(B, e, N) for e in exponents)) % N
    assert nmod == s % N
    assert (c + sum(pow(B, e, m) for e in exponents)) % m == r
    assert d + len(exponents) == s
    assert all(0 <= x < b for x in ds)
    return (s, c, tuple(exponents), N, len(adjustments))


def verify():
    tests = 0
    for b in range(2, 6):
        for k in (1, 2, 3):
            B = b**k
            for m in range(1, 31):
                m0, m1 = base_part(m, b)
                v = 0
                while B**v % m0:
                    v += 1
                allowed = set(prefix_classes(B, b, v, m0))
                for r in range(m):
                    expected = r % m0 in allowed
                    result = construct(b, k, m, r)
                    assert (result is not None) == expected
                    if expected:
                        tests += 1
                        s, c, exps, N, changes = result
                        if max(exps, default=0) * math.log2(B) < 15000:
                            n = c + sum(B**e for e in exps)
                            assert n % s == 0 and n % m == r
                            assert digitsum(n, b) == s == digitsum(n, B)
    assert construct(2, 2, 16, 2) is None
    example = construct(2, 2, 16, 5)
    print('VERIFY_OK', 'parameters=', tests, 'low_residue_obstruction=PASS',
          'modular_digit_construction=PASS', 'example_base4_residue5=', example[:2])

if __name__ == '__main__':
    verify()
