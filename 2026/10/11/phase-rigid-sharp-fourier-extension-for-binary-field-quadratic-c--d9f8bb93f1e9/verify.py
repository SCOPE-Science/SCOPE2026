"""Reproduce finite-field checks for the sharp conic extension identity.

Only Python 3 standard library is required. The theorem is proved analytically;
these computations test normalizations and arithmetic boundary cases.
"""
from collections import defaultdict
from math import isclose

IRREDUCIBLE = {1: 0b11, 2: 0b111, 3: 0b1011,
               4: 0b10011, 5: 0b100101}


def multiply(a, b, degree):
    modulus = IRREDUCIBLE[degree]
    mask = (1 << degree) - 1
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & (1 << degree):
            a ^= modulus
    return out & mask


def trace(a, degree):
    value = a
    out = a
    for _ in range(1, degree):
        value = multiply(value, value, degree)
        out ^= value
    assert out in (0, 1)
    return out


def conic(degree, kind, level):
    size = 1 << degree
    if kind == "nonsplit":
        parameter = next(a for a in range(size) if trace(a, degree) == 1)
    else:
        parameter = 0

    def quadratic(x, y):
        cross = multiply(x, y, degree)
        if kind == "split":
            return cross
        return (multiply(x, x, degree) ^ cross ^
                multiply(parameter, multiply(y, y, degree), degree))

    return [(x, y) for x in range(size) for y in range(size)
            if quadratic(x, y) == level]


def square_abs(z):
    return round(z.real * z.real + z.imag * z.imag)


def main():
    set_cases = pair_cases = convolution_cases = direct_fourier_cases = 0
    for degree in range(1, 6):
        q = 1 << degree
        for kind in ("split", "nonsplit"):
            required = q - 1 if kind == "split" else q + 1
            for level in range(1, q):
                points = conic(degree, kind, level)
                m = len(points)
                assert m == required, (degree, kind, level, m)
                set_cases += 1
                # Every nonzero sum has either zero or two ordered representations.
                pair_fibers = defaultdict(list)
                for i, a in enumerate(points):
                    for j, b in enumerate(points):
                        pair_fibers[a[0] ^ b[0], a[1] ^ b[1]].append((i, j))
                assert len(pair_fibers[(0, 0)]) == m
                assert len(pair_fibers) == 1 + m * (m - 1) // 2
                for shift, ordered in pair_fibers.items():
                    if shift == (0, 0):
                        assert all(i == j for i, j in ordered)
                    else:
                        assert len(ordered) == 2
                        assert ordered[0] == ordered[1][::-1]
                pair_cases += 1
                for pattern in range(2):
                    coefficients = [complex((i % 4) + 1, (3*i + pattern) % 5 - 2)
                                    for i in range(m)]
                    t = sum(square_abs(c) for c in coefficients)
                    fourth = sum(square_abs(c)**2 for c in coefficients)
                    square_sum = sum(c*c for c in coefficients)
                    raw_energy = sum(square_abs(sum(coefficients[i]*coefficients[j]
                                                    for i, j in pairs))
                                     for pairs in pair_fibers.values())
                    exact = 2*t*t - 2*fourth + square_abs(square_sum)
                    assert raw_energy == exact, (degree, kind, level, pattern)
                    normalized = [square_abs(c)/t for c in coefficients]
                    defect = (2*sum((w-1/m)**2 for w in normalized)
                              + 1 - square_abs(square_sum)/(t*t))
                    assert isclose(exact/(t*t), 3-2/m-defect,
                                   rel_tol=2e-13, abs_tol=2e-13)
                    convolution_cases += 1
                for signs in ([1] * m, [(-1)**i for i in range(m)]):
                    optimum = sum(square_abs(sum(signs[i]*signs[j]
                                                 for i, j in pairs))
                                  for pairs in pair_fibers.values())
                    assert optimum == 3*m*m - 2*m
                if level == 1 and degree <= 4:
                    coefficients = [complex((i % 4) + 1, (3*i) % 5 - 2)
                                    for i in range(m)]
                    raw_energy = sum(square_abs(sum(coefficients[i]*coefficients[j]
                                                    for i, j in pairs))
                                     for pairs in pair_fibers.values())
                    fourier_moment = 0.0
                    for a in range(q):
                        for b in range(q):
                            value = sum(c*(-1)**trace(multiply(a, x, degree)
                                                        ^ multiply(b, y, degree), degree)
                                        for c, (x, y) in zip(coefficients, points))/m
                            fourier_moment += abs(value)**4
                    assert isclose(fourier_moment, q*q*raw_energy/m**4,
                                   rel_tol=1e-11, abs_tol=1e-11)
                    direct_fourier_cases += 1
    print('VERIFY_OK level_sets=%d pair_fibers=%d convolution_patterns=%d '
          'direct_fourier=%d' % (set_cases, pair_cases,
                                 convolution_cases, direct_fourier_cases))


if __name__ == '__main__':
    main()
