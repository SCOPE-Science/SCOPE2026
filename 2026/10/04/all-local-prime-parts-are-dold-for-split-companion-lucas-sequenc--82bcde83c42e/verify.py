from math import gcd


def primes(n):
    out = []
    for x in range(2, n + 1):
        if all(x % d for d in range(2, int(x ** 0.5) + 1)):
            out.append(x)
    return out


def vp(n, p):
    if n == 0:
        raise ValueError("zero term")
    n = abs(n)
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def mobius(n):
    if n == 1:
        return 1
    x = n
    count = 0
    d = 2
    while d * d <= x:
        if x % d == 0:
            x //= d
            count += 1
            if x % d == 0:
                return 0
            while x % d == 0:
                x //= d
        d += 1
    if x > 1:
        count += 1
    return -1 if count % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def ordmod(x, p):
    y = 1
    for h in range(1, p):
        y = y * x % p
        if y == 1:
            return h
    raise AssertionError("order not found")


def check(a, b, p, N=120):
    A = []
    for n in range(1, N + 1):
        value = a ** n + b ** n
        if value == 0:
            raise AssertionError("excluded zero term")
        A.append(p ** vp(value, p))

    transforms = []
    for n in range(1, N + 1):
        L = sum(mobius(n // d) * A[d - 1] for d in divisors(n))
        transforms.append(L)
        assert L % n == 0, ("Dold failure", a, b, p, n, L)

    realizable = all(L >= 0 for L in transforms)
    if p == 2:
        predicted = ((a + b) % 2 != 0) or (a % 2 and b % 2 and vp(a + b, 2) == 1)
    elif a % p == 0 or b % p == 0:
        predicted = True
    else:
        predicted = ordmod((a * pow(b, -1, p)) % p, p) % 2 == 1
    assert realizable == predicted, ("realizability failure", a, b, p, realizable, predicted)


count = 0
for a in range(-8, 9):
    for b in range(-8, 9):
        if a == 0 or b == 0 or a == -b or gcd(abs(a), abs(b)) != 1:
            continue
        for p in primes(29):
            check(a, b, p)
            count += 1

print("VERIFY_OK", count)
