"""Exact cyclotomic checks for three-atom positive Fourier uncertainty.

This checker corroborates the analytic theorem; finite enumeration is not
used to infer the theorem for arbitrarily large cyclic orders.
"""
from itertools import combinations
from math import gcd


def reduce_root_sum(order, terms):
    """Return an exact integer vector in Z[X]/(X^(order/2)+1)."""
    half = order // 2
    result = [0] * half
    for weight, exponent in terms:
        exponent %= order
        position = exponent % half
        result[position] += weight if exponent < half else -weight
    return tuple(result)


def integer_fourier_zeros(order, left, right, weights):
    a, b, c = weights
    return tuple(
        t for t in range(order)
        if not any(reduce_root_sum(order, (
            (a, 0), (b, -left*t), (c, -right*t)
        )))
    )


def quadratic_fourier_zeros(order):
    """Exact Fourier test for weights (1,sqrt(2),1) at 0,N/8,N/4.

    sqrt(2) = zeta^(N/8) + zeta^(-N/8), valid for 8|N.
    """
    assert order % 8 == 0
    step = order // 8
    return tuple(
        t for t in range(order)
        if not any(reduce_root_sum(order, (
            (1, 0),
            (1, step-step*t),
            (1, -step-step*t),
            (1, -2*step*t)
        )))
    )


def strictly_encloses_origin(order, left, right, t):
    residues = sorted((0, (left*t) % order, (right*t) % order))
    gaps = (residues[1]-residues[0],
            residues[2]-residues[1],
            order-residues[2]+residues[0])
    return max(gaps) * 2 < order


def check():
    rational_trials = 0
    geometry_cases = 0
    sample_weights = (
        (1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1),
        (1, 2, 2), (2, 2, 1), (2, 2, 2), (1, 3, 1),
        (1, 1, 3), (3, 1, 1), (1, 4, 1), (1, 4, 3),
        (2, 3, 4), (4, 3, 2)
    )
    for exponent in range(2, 7):
        order = 2 ** exponent
        for left, right in combinations(range(1, order), 2):
            g = gcd(order, left, right)
            for weights in sample_weights:
                zeros = integer_fourier_zeros(order, left, right, weights)
                assert len(zeros) in (0, g, 2*g)
                assert len(zeros) <= order // 4
                rational_trials += 1
            reduced_order = order // g
            u, v = left // g, right // g
            strict_indices = [t for t in range(reduced_order)
                if strictly_encloses_origin(reduced_order, u, v, t)]
            for t in strict_indices:
                assert t not in (0, reduced_order//2)
                assert strictly_encloses_origin(reduced_order, u, v,
                                                 (-t) % reduced_order)
                assert sum(1 for s in range(reduced_order)
                    if (s*u - t*u) % reduced_order == 0 and
                       (s*v - t*v) % reduced_order == 0) == 1
                geometry_cases += 1
            if reduced_order == 4:
                assert strict_indices == []
    for exponent in range(2, 9):
        order = 2 ** exponent
        d = order // 4
        zeros = integer_fourier_zeros(order, d, 2*d, (1, 2, 1))
        assert zeros == tuple(t for t in range(order) if t%4 == 2)
        assert len(zeros) == order//4
    for exponent in range(3, 9):
        order = 2 ** exponent
        zeros = quadratic_fourier_zeros(order)
        assert zeros == tuple(t for t in range(order) if t%8 in (3, 5))
        assert len(zeros) == order//4
    print('VERIFY_OK', 'rational_trials='+str(rational_trials),
          'strict_geometry_cases='+str(geometry_cases),
          'integer_and_quadratic_extremizers=13')


if __name__ == '__main__':
    check()
