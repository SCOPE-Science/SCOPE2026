"""Exact finite certificate for the least simultaneous phi/sigma jump on sphenic pairs.

The mathematical reduction to this finite search is proved in RESULT.md.
Only Python 3 standard library is used.
"""
from math import isqrt, prod


def is_prime(z):
    if z < 2:
        return False
    for d in range(2, isqrt(z) + 1):
        if z % d == 0:
            return False
    return True


def normalized_shapes_below(bound):
    """Exhaust even-offset triples B=(a,b,c), 0<a<b<c, abc<bound.
    Equating elementary symmetric sums forces A=(0,u,v).
    """
    tried = 0
    shapes = []
    for a in range(2, bound, 2):
        if a * (a + 2) * (a + 4) >= bound:
            break
        for b in range(a + 2, bound, 2):
            if a * b * (b + 2) >= bound:
                break
            for c in range(b + 2, (bound - 1) // (a * b) + 1, 2):
                h = a * b * c
                assert h < bound
                tried += 1
                s = a + b + c
                pair_sum = a * b + a * c + b * c
                delta = s * s - 4 * pair_sum
                if delta <= 0:
                    continue
                root = isqrt(delta)
                if root * root != delta or (s - root) % 2:
                    continue
                u, v = (s - root) // 2, (s + root) // 2
                if not (0 < u < v and u % 2 == v % 2 == 0):
                    continue
                if len({0, u, v, a, b, c}) != 6:
                    continue
                assert u + v == s and u * v == pair_sum
                shapes.append((h, (0, u, v), (a, b, c)))
    return tried, sorted(shapes)


def verify():
    checked, shapes = normalized_shapes_below(320)
    target = [
        (96, (0, 8, 10), (2, 4, 12)),
        (192, (0, 10, 14), (2, 6, 16)),
    ]
    assert checked == 37, checked
    assert shapes == target, shapes
    for h, A, B in shapes:
        residues = {(z % 3) for z in A + B}
        assert residues == {0, 1, 2}
        assert 6 in B or 12 in B
        assert not all(is_prime(3 + z) for z in A + B)
    A = (11, 23, 29)
    B = (13, 19, 31)
    assert all(is_prime(p) for p in A + B)
    assert len(set(A + B)) == 6
    n, N = prod(A), prod(B)
    assert (n, N, N - n) == (7337, 7657, 320)
    phi_A, phi_B = prod(p - 1 for p in A), prod(p - 1 for p in B)
    sigma_A, sigma_B = prod(p + 1 for p in A), prod(p + 1 for p in B)
    assert phi_B - phi_A == sigma_B - sigma_A == N - n == 320
    print('VERIFY_OK tested_normalized_even_offset_triples=37')
    print('subthreshold_shapes=' + repr(shapes))
    print('prime_obstruction=mod3_at_t_ge5_and_composite_at_t_3')
    print('witness=7337_7657 jump=320 phi=(6160,6480) sigma=(8640,8960)')
    print('finite_certificate_exhaustive_under_proved_normalization=YES')


if __name__ == '__main__':
    verify()
