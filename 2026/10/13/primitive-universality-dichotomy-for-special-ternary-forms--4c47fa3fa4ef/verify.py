#!/usr/bin/env python3
from math import gcd, isqrt

M_MIN = -200
M_MAX = 200
PARAM_LIMIT = 400
BRUTE_BOX = 18
DS = [1, 2, 5, 10, 13, 17, 25, 26, 34, 50]

def egcd(a, b):
    if b == 0:
        return 1, 0, a
    x, y, g = egcd(b, a % b)
    return y, x - (a // b) * y, g

def coprime_sumsq(d):
    for A in range(1, isqrt(d) + 1):
        r = d - A * A
        B = isqrt(r)
        if B > 0 and B * B == r and gcd(A, B) == 1:
            return A, B
    raise AssertionError(('no coprime sum of squares', d))

def primitive(a, b, c):
    return a != 0 and b != 0 and c != 0 and gcd(gcd(abs(a), abs(b)), abs(c)) == 1

def witness(d, m):
    if d == 1:
        for v in range(-PARAM_LIMIT, PARAM_LIMIT + 1):
            if v == 0:
                continue
            num = m - 1 - v * v
            if num % 2:
                continue
            c = num // 2
            a, b = c + 1, v
            if primitive(a, b, c) and a * a + b * b - c * c == m:
                return a, b, c
        return None

    A, B = coprime_sumsq(d)
    x, y, g = egcd(A, B)
    assert g == 1

    if d % 2:
        for t in range(-PARAM_LIMIT, PARAM_LIMIT + 1):
            u, v = x + B * t, y - A * t
            num = m - u * u - v * v
            if num % 2:
                continue
            c = num // 2
            a, b = A * c + u, B * c + v
            if primitive(a, b, c) and a * a + b * b - d * c * c == m:
                return a, b, c
        return None

    C, D = A, B
    if m % 2:
        rhs, denom, parity = 1, 2, None
    elif m % 4 == 2:
        rhs, denom, parity = 2, 4, 1
    elif m % 8 == 0:
        rhs, denom, parity = 2, 4, 0
    else:
        return None

    ux, vy = rhs * x, rhs * y
    step = 1 if rhs == 1 else 1
    for t in range(-PARAM_LIMIT, PARAM_LIMIT + 1, step):
        u, v = ux + D * t, vy - C * t
        if parity is not None and (u & 1) != parity:
            continue
        if parity is not None and (v & 1) != parity:
            continue
        num = m - u * u - v * v
        if num % denom:
            continue
        c = num // denom
        a, b = C * c + u, D * c + v
        if primitive(a, b, c) and a * a + b * b - d * c * c == m:
            return a, b, c
    return None

def brute_forbidden(d, m):
    for a in range(-BRUTE_BOX, BRUTE_BOX + 1):
        if a == 0:
            continue
        for b in range(-BRUTE_BOX, BRUTE_BOX + 1):
            if b == 0:
                continue
            for c in range(-BRUTE_BOX, BRUTE_BOX + 1):
                if c == 0:
                    continue
                if primitive(a, b, c) and a * a + b * b - d * c * c == m:
                    return a, b, c
    return None

def main():
    constructive = 0
    forbidden = 0
    for d in DS:
        if d > 1:
            A, B = coprime_sumsq(d)
            assert A * A + B * B == d and gcd(A, B) == 1
        for m in range(M_MIN, M_MAX + 1):
            allowed = not (d % 2 == 0 and m % 8 == 4)
            w = witness(d, m)
            assert (w is not None) == allowed, (d, m, w)
            if w is not None:
                a, b, c = w
                assert primitive(a, b, c)
                assert a * a + b * b - d * c * c == m
                constructive += 1
            elif d % 2 == 0:
                assert brute_forbidden(d, m) is None, (d, m)
                forbidden += 1
    print('VERIFY_OK')
    print('parameters=' + str(len(DS)))
    print('integer_range=' + str(M_MIN) + '..' + str(M_MAX))
    print('constructive_cases=' + str(constructive))
    print('forbidden_cases=' + str(forbidden))
    print('brute_coordinate_box=' + str(BRUTE_BOX))

if __name__ == '__main__':
    main()
