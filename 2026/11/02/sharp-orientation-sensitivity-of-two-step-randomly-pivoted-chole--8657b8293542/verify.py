"""Exact rational enumeration of two adaptive RPCholesky pivots."""
from fractions import Fraction as F

def trace(a):
    return sum(a[i][i] for i in range(3))

def principal_minor(a, i, j):
    return a[i][i] * a[j][j] - a[i][j] * a[j][i]

def determinant(a):
    x, y, z = a[0]
    u, v, w = a[1]
    p, q, r = a[2]
    return x * (v * r - w * q) - y * (u * r - w * p) + z * (u * q - v * p)

def eliminate(a, i):
    assert a[i][i] > 0
    return [[a[j][k] - a[j][i] * a[i][k] / a[i][i]
             for k in range(3)] for j in range(3)]

def from_unit_spike(height, v):
    assert sum(x*x for x in v) == 1
    return [[F(int(i == j)) + (height-1) * v[i] * v[j]
             for j in range(3)] for i in range(3)]

def balanced_spike(height):
    return [[F(int(i == j)) + (height-1)/3
             for j in range(3)] for i in range(3)]

def exact_two_step(a):
    total = F(0)
    prob_total = F(0)
    spectral_trace = F(0)
    inv_first_trace_sum = F(0)
    initial_trace = trace(a)
    for i in range(3):
        after_first = eliminate(a, i)
        first_trace = trace(after_first)
        assert first_trace > 0
        prob_first = a[i][i] / initial_trace
        spectral_trace += prob_first * first_trace
        inv_first_trace_sum += 1 / first_trace
        for j in range(3):
            if j == i:
                continue
            prob_second = after_first[j][j] / first_trace
            prob = prob_first * prob_second
            prob_total += prob
            after_second = eliminate(after_first, j)
            total += prob * trace(after_second)
            # Schur complement determinant identity, independent of total.
            assert trace(after_second) == determinant(a) / principal_minor(a, i, j)
    assert prob_total == 1
    tr_square = sum(a[i][j] * a[j][i] for i in range(3) for j in range(3))
    assert spectral_trace == initial_trace - tr_square / initial_trace
    assert total == 2 * determinant(a) / initial_trace * inv_first_trace_sum
    # An independently normalized DPP distribution on all unordered pairs.
    minors = [principal_minor(a, i, j) for i in range(3) for j in range(i+1,3)]
    dpp_norm = sum(minors)
    dpp_error = sum(m / dpp_norm * determinant(a)/m for m in minors)
    assert dpp_error == 3 * determinant(a) / dpp_norm
    return total, spectral_trace, dpp_error

vectors = [
    (F(1), F(0), F(0)),
    (F(1,3), F(2,3), F(2,3)),
    (F(3,5), F(4,5), F(0)),
    (F(2,7), F(3,7), F(6,7)),
]
for L in [F(1), F(3,2), F(2), F(4), F(11), F(100)]:
    minimum = L * (L+5)/((L+1)*(L+2))
    maximum = 3*L/(2*L+1)
    one_pivot = 2*(2*L+1)/(L+2)
    dpp = 3*L/(2*L+1)
    for v in vectors:
        E, E1, D = exact_two_step(from_unit_spike(L, v))
        assert minimum <= E <= maximum
        assert E1 == one_pivot and D == dpp
        if v == vectors[0]:
            assert E == minimum
    E, E1, D = exact_two_step(balanced_spike(L))
    assert E == maximum and E1 == one_pivot and D == dpp
    print('PASS', 'L=', L, 'minimum=', minimum, 'maximum=', maximum, 'DPP=', D)
print('ALL_EXACT_ENUMERATIONS_PASS')
