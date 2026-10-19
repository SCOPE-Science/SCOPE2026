#!/usr/bin/env python3
"""Exact rational checks for a two-stage four-pulse Floquet threshold example."""
from fractions import Fraction as F
from itertools import permutations

I = ((F(1), F(0)), (F(0), F(1)))
# The physical flow is E = E0/sqrt(2).  Four gaps contribute 1/4.
E0 = ((F(5, 4), F(3)), (F(3, 16), F(5, 4)))
D = (
    (F(1, 2), F(4, 5)),
    (F(9, 10), F(1, 2)),
    (F(19, 20), F(1, 2)),
    (F(3, 5), F(99, 100)),
)


def matmul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def det(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def mat_trace(a):
    return a[0][0] + a[1][1]


def floquet(chronological):
    """Returns exact monodromy for a chronological list of pulse indices."""
    n = len(chronological)
    m = I
    for pulse_index in reversed(chronological):
        d = D[pulse_index]
        dE0 = tuple(tuple(d[i] * E0[i][j] for j in range(2))
                     for i in range(2))
        m = matmul(m, dE0)
    # For n even, E=(1/sqrt(2))E0 contributes 2^(-n/2).
    assert n % 2 == 0, 'Use floquet only for even numbers of pulses'
    scale = F(1, 2 ** (n // 2))
    return tuple(tuple(scale * x for x in row) for row in m)


def characteristic_at_one(a):
    return F(1) - mat_trace(a) + det(a)


def check():
    # Physical A=[[-1/2,4],[1/4,-1/2]]: (A+I/2)^2=I.
    B = ((F(0), F(4)), (F(1, 4), F(0)))
    assert matmul(B, B) == I
    assert det(E0) == 1
    assert all(F(0) < d < F(1) for pair in D for d in pair)
    # Two schedules use the very same four distinct survival matrices.
    decay_schedule = (0, 2, 3, 1)
    growth_schedule = (2, 1, 3, 0)
    m_decay = floquet(decay_schedule)
    m_growth = floquet(growth_schedule)
    d0, d1 = det(m_decay), det(m_growth)
    t0, t1 = mat_trace(m_decay), mat_trace(m_growth)
    p0, p1 = characteristic_at_one(m_decay), characteristic_at_one(m_growth)
    assert d0 == d1 == F(50787, 16000000)
    assert t0 == F(101759121, 102400000)
    assert t1 == F(4243977, 4096000)
    assert p0 == F(4829579, 512000000) > 0
    assert p1 == -F(16871941, 512000000) < 0
    assert F(0) < d0 < F(1)
    # Positive 2x2 matrix + determinant<1: sign det(I-M) says rho < or >1.
    for schedule, mat, tr, pc in ((decay_schedule, m_decay, t0, p0),
                                  (growth_schedule, m_growth, t1, p1)):
        assert all(v > 0 for row in mat for v in row)
        disc = tr * tr - F(4) * det(mat)
        assert disc > 0
        print('chronological:', schedule,
              'trace:', tr, 'det:', det(mat), 'det(I-M):', pc,
              'Perron radius approximate:', (float(tr) + float(disc)**0.5)/2)
    # Finite reproducibility sample; universal <=3 theorem is analytic,
    # not justified by this enumeration.
    def unscaled_trace_perm(order):
        m = I
        for j in reversed(order):
            ds = D[j]
            m = matmul(m, tuple(tuple(ds[i] * E0[i][k] for k in range(2))
                                       for i in range(2)))
        return mat_trace(m), det(m)
    for n in (1, 2, 3):
        outcomes = {unscaled_trace_perm(p) for p in permutations(range(n))}
        assert len(outcomes) == 1
        print(f'{n} types: checked {len(list(permutations(range(n))))} permutations')
    assert len({unscaled_trace_perm(p) for p in permutations(range(4))}) == 3
    print('Four pulse orders have three distinct trace classes; exact checks PASSED.')


if __name__ == '__main__':
    check()
