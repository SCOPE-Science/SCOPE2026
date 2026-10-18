#!/usr/bin/env python3
"""Exact rational Taylor enclosures for a weighted log-spline counterexample.
No external packages, no floating-point comparisons, no numerical root solving.
"""
from fractions import Fraction as F
from math import factorial

FINE_NODES = (0, 1, 2, 3, 4)
FINE_HEIGHTS = (F(0), F(3), F(3), F(11, 4), F(9, 4))
COARSE_NODES = (0, 2, 3, 4)
TRIAL_HEIGHTS = (F(0), F(17027588, 10000000),
                 F(11063547, 10000000), F(7452502, 10000000))
DEGREE = 24
EPSILON = F(27 * (3 ** (DEGREE + 1)), factorial(DEGREE + 1))


def hat(j, x, nodes):
    """Value of piecewise-linear Lagrange basis at an integer node."""
    if j == 0:
        return max(F(0), F(nodes[1] - x, nodes[1] - nodes[0])) if nodes[0] <= x <= nodes[1] else F(0)
    if j == len(nodes) - 1:
        return F(x - nodes[-2], nodes[-1] - nodes[-2]) if nodes[-2] <= x <= nodes[-1] else F(0)
    if nodes[j - 1] <= x <= nodes[j]:
        return F(x - nodes[j - 1], nodes[j] - nodes[j - 1])
    if nodes[j] <= x <= nodes[j + 1]:
        return F(nodes[j + 1] - x, nodes[j + 1] - nodes[j])
    return F(0)


def taylor_integral(nodes, heights, basis):
    """Exact integral of truncation of exp(piecewise-affine h)*basis.

    The basis is piecewise affine on all input segments and specified by
    endpoint values in [0,1]. The true integral is between T and
    T + 4*EPSILON (because h in [0,3] and support length is 4).
    """
    answer = F(0)
    for s in range(len(nodes) - 1):
        a, b = nodes[s], nodes[s + 1]
        l = F(b - a)
        u, d = heights[s], heights[s + 1] - heights[s]
        va, vb = F(basis(a)), F(basis(b))
        assert F(0) <= va <= 1 and F(0) <= vb <= 1
        assert F(0) <= heights[s] <= 3 and F(0) <= heights[s + 1] <= 3
        power = [F(1)]
        fact = 1
        for k in range(DEGREE + 1):
            integrated = sum((coeff * (va / (j + 1) + (vb - va) / (j + 2))
                              for j, coeff in enumerate(power)), F(0))
            answer += l * integrated / fact
            if k < DEGREE:
                nxt = [F(0)] * (k + 2)
                for j, coeff in enumerate(power):
                    nxt[j] += u * coeff
                    nxt[j + 1] += d * coeff
                power = nxt
                fact *= k + 1
    return answer


def ratio_bounds(num, den):
    assert 0 <= num and den > 0
    error = 4 * EPSILON
    return (num / (den + error), (num + error) / den)


def mean_bounds(nodes, heights, basis):
    den = taylor_integral(nodes, heights, lambda _: F(1))
    num = taylor_integral(nodes, heights, basis)
    return ratio_bounds(num, den)


def determinant_2(a, b, c, d):
    return a * d - b * c


def determinant_3(h):
    return (h[0][0] * (h[1][1] * h[2][2] - h[1][2] * h[2][1])
            - h[0][1] * (h[1][0] * h[2][2] - h[1][2] * h[2][0])
            + h[0][2] * (h[1][0] * h[2][1] - h[1][1] * h[2][0]))


def verify():
    assert all(FINE_HEIGHTS[j + 1] - FINE_HEIGHTS[j] >
               FINE_HEIGHTS[j + 2] - FINE_HEIGHTS[j + 1]
               for j in range(3))
    w_bounds = [mean_bounds(FINE_NODES, FINE_HEIGHTS,
                           lambda x, j=j: hat(j, x, FINE_NODES))
                for j in range(5)]
    assert all(lo > 0 for lo, hi in w_bounds)
    print('Five probability weights lie in certified rational intervals:')
    for j, (lo, hi) in enumerate(w_bounds):
        print(j, '(%0.12f, %0.12f)' % (float(lo), float(hi)))
    max_gradient_bound = F(0)
    for j in (1, 2, 3):
        basis = lambda x, j=j: hat(j, x, COARSE_NODES)
        fine_lo, fine_hi = mean_bounds(FINE_NODES, FINE_HEIGHTS, basis)
        coarse_lo, coarse_hi = mean_bounds(COARSE_NODES, TRIAL_HEIGHTS, basis)
        grad_lo, grad_hi = coarse_lo - fine_hi, coarse_hi - fine_lo
        assert -F(1, 1000000) < grad_lo <= grad_hi < F(1, 1000000)
        max_gradient_bound = max(max_gradient_bound, abs(grad_lo), abs(grad_hi))
        print('coarse gradient %d lies in (%0.13f, %0.13f)' %
              (j, float(grad_lo), float(grad_hi)))
    # Centered Lebesgue Gram matrix of the three nonconstant coarse hats.
    # H_jk = int(psi_j psi_k)dx - (int psi_j dx)(int psi_k dx)/4.
    H = [[F(7, 16), F(-5, 24), F(-3, 16)],
         [F(-5, 24), F(5, 12), F(1, 24)],
         [F(-3, 16), F(1, 24), F(13, 48)]]
    B = [[H[i][j] - (F(1, 10) if i == j else 0) for j in range(3)] for i in range(3)]
    assert B[0][0] == F(27, 80) > 0
    assert determinant_2(B[0][0], B[0][1], B[1][0], B[1][1]) == F(457, 7200) > 0
    assert determinant_3(B) == F(257, 108000) > 0
    # For ||v-u||_2 <= 1/100, exp(h_v)/int exp(h_v) > 1/40,
    # because -1/100 <= h_v <= 2, e^2<9 and e^(-1/100)>99/100.
    # Thus Hessian(logZ) = Cov_{f_v}(psi) >= (1/40)H > I/400.
    radius = F(1, 100)
    # ||gradient||_2 < sqrt(3)/10^6 < 2/10^6.
    assert max_gradient_bound < F(1, 1000000)
    assert F(1, 8000000) - F(2, 1000000) * radius > 0
    jump = TRIAL_HEIGHTS[3] - 2 * TRIAL_HEIGHTS[2] + TRIAL_HEIGHTS[1]
    assert jump > 4 * radius
    print('trial slope jump at 3:', jump, '=', float(jump))
    print('CERTIFIED: unique coarse critical point lies within radius 1/100;'
          ' its final slope jump is positive.')
    return True


if __name__ == '__main__':
    verify()
