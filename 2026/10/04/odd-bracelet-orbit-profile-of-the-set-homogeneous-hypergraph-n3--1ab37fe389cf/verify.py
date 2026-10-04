def phi(n):
    r = n
    p = 2
    x = n
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1
    if x > 1:
        r -= r // x
    return r


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def rot(w, j):
    return w[j:] + w[:j]


def refl(w, j):
    n = len(w)
    return tuple(w[(j - i) % n] for i in range(n))


def canon(w):
    w = tuple(w)
    return min([rot(w, j) for j in range(len(w))] +
               [refl(w, j) for j in range(len(w))])


def brute(k):
    reps = set()
    for mask in range(1 << k):
        if mask.bit_count() % 2 == 0:
            continue
        w = tuple((mask >> i) & 1 for i in range(k))
        reps.add(canon(w))
    return len(reps)


def formula(k):
    if k <= 2:
        return 1
    s = sum(phi(d) * (1 << (k // d)) for d in divisors(k) if d % 2 == 1)
    if k % 2:
        correction = 1 << ((k - 3) // 2)
    else:
        correction = 1 << (k // 2 - 2)
    num = s + 4 * k * correction
    assert num % (4 * k) == 0
    return num // (4 * k)


def local_orders(k):
    s = sum(phi(d) * (1 << (k // d)) for d in divisors(k) if d % 2 == 1)
    assert s % (2 * k) == 0
    return s // (2 * k)


expected = [1,1,2,2,4,5,9,12,23,34,63,102,190,325,612,1088,2056,3771,7155,13364]
local_expected = [1,1,2,2,4,6,10,16,30,52,94,172,316,586,1096,2048,3856,7286,13798,26216]

for k in range(1, 21):
    f = formula(k)
    L = local_orders(k)
    assert f == expected[k - 1], (k, f)
    assert L == local_expected[k - 1], (k, L)
    assert 2 * f - L == 1 << ((k - 1) // 2), (k, 2 * f - L)
    if k <= 14:
        b = brute(k)
        assert b == f, (k, b, f)

print('orbit_profile', expected)
print('local_orders', local_expected)
print('self_converse', [1 << ((k - 1)//2) for k in range(1,21)])
print('VERIFY_OK')
