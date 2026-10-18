#!/usr/bin/env python3
"""Exact finite-field checks for singular Hurwitz--Klein plane curves.

The program checks selected prime characteristics and degrees by directly
computing all projective F_p points and the complete Jacobian system.
Finite-field checks are independent corroboration, not a replacement for
the all-characteristic proof.
"""


def primes_at_most(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** .5) + 1))]


def normalize(point, p):
    leading = next(x for x in point if x % p)
    inv = pow(leading, -1, p)
    return tuple(x * inv % p for x in point)


def singular_points_brute(n, p):
    points = [(1, y, z) for y in range(p) for z in range(p)]
    points += [(0, 1, z) for z in range(p)] + [(0, 0, 1)]
    singular = set()
    for x, y, z in points:
        f = (pow(x, n, p) * y + pow(y, n, p) * z + pow(z, n, p) * x) % p
        fx = (n * pow(x, n - 1, p) * y + pow(z, n, p)) % p
        fy = (pow(x, n, p) + n * pow(y, n - 1, p) * z) % p
        fz = (pow(y, n, p) + n * pow(z, n - 1, p) * x) % p
        if not (f or fx or fy or fz):
            singular.add(normalize((x, y, z), p))
    return singular


def singular_points_predicted(n, p):
    m = n * n - n + 1
    if m % p:
        return set()
    assert n % p and (n - 1) % p and p != 2
    c = (-1 if n % 2 else 1) * pow(n, 2 - n, p)
    result = set()
    for v in range(1, p):
        if pow(v, m, p) == c % p:
            u = -pow(n * pow(v, n - 1, p) % p, -1, p) % p
            assert n * (n - 1) * pow(u, n - 2, p) % p
            result.add(normalize((u, 1, v), p))
    return result


def verify():
    count = 0
    examples = []
    for n in range(2, 17):
        for p in primes_at_most(29):
            brute = singular_points_brute(n, p)
            predicted = singular_points_predicted(n, p)
            assert brute == predicted, (n, p, brute, predicted)
            count += 1
            if n in (2, 3, 4, 5) and p in (3, 7, 13) and brute:
                m = n * n - n + 1
                q, r = 1, m
                while r % p == 0:
                    r //= p
                    q *= p
                examples.append((n, p, len(brute), q, r, (r - 1) // 2,
                                 (q - 1) // 2))
    assert (3, 7, 1, 7, 1, 0, 3) in examples
    assert (4, 13, 1, 13, 1, 0, 6) in examples
    assert (5, 7, 3, 7, 3, 1, 3) in examples
    print('VERIFY_OK; projective finite-field classifications:', count)
    print('EXAMPLES (n,p,Fp_singular_count,q,r,geometric_genus,cusp_delta):')
    for item in examples:
        print(item)


if __name__ == '__main__':
    verify()
