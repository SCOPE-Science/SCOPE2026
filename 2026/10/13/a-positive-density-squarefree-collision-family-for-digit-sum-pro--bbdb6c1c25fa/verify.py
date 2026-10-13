#!/usr/bin/env python3
LIMIT = 200000

def squarefree_sieve(n):
    good = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        good[0] = 0
    p = 2
    while p * p <= n:
        pp = p * p
        for k in range(pp, n + 1, pp):
            good[k] = 0
        p += 1
    return good

def digit_sum(n, b):
    s = 0
    while n:
        s += n % b
        n //= b
    return s

def main():
    sf = squarefree_sieve(2 * LIMIT + 10)
    qualifying = 0
    progression = 0
    for b in range(8, LIMIT + 1):
        cond = (b % 3 != 0 and sf[b] and sf[b - 2] and sf[2 * b - 3])
        if cond:
            x = b * (2 * b - 3)
            y = (b - 2) * (2 * b - 3)
            assert x != y
            assert digit_sum(x, b) == b - 2
            assert digit_sum(y, b) == b
            assert x * digit_sum(x, b) == y * digit_sum(y, b)

            # Product squarefreeness follows from the theorem's gcd conditions;
            # verify directly here from factor divisibility using the squarefree factors.
            import math
            assert math.gcd(b, 2 * b - 3) == 1
            assert math.gcd(b - 2, 2 * b - 3) == 1
            qualifying += 1
            if b % 36 == 5:
                progression += 1

    print("VERIFY_OK")
    print("base_limit=" + str(LIMIT))
    print("qualifying_bases=" + str(qualifying))
    print("qualifying_bases_b_eq_5_mod_36=" + str(progression))

if __name__ == "__main__":
    main()
