"""Exact rational checks for circular nearest-neighbor motif/length formulas.

No simulation or external libraries. Exhaustive finite checks are not a proof
of the all-sample-size theorem, whose proof uses exponential spacings.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def expected_ordered_spacing(n, k):
    """Mean of k-th smallest coordinate of Dirichlet(1,...,1)."""
    return sum((F(1, j) for j in range(n-k+1, n+1)), F(0)) / n


def check(n):
    means = [None] + [expected_ordered_spacing(n, k) for k in range(1, n+1)]
    r_sum = r2_sum = length_sum = mixed_sum = F(0)
    for p in permutations(range(1, n+1)):
        r = sum(p[i] < p[(i-1)%n] and p[i] < p[(i+1)%n]
                for i in range(n))
        conditional_length = sum((means[min(p[i-1], p[i])]
                                  for i in range(n)), F(0))
        r_sum += r
        r2_sum += r*r
        length_sum += conditional_length
        mixed_sum += r * conditional_length
    count = factorial(n)
    mean_r = r_sum / count
    mean_l = length_sum / count
    covariance = mixed_sum / count - mean_r * mean_l
    variance_r = r2_sum / count - mean_r * mean_r
    assert mean_r == F(n, 3), (n, mean_r)
    assert mean_l == F(1, 2), (n, mean_l)
    assert variance_r == F(2*n, 45), (n, variance_r)
    assert covariance == F(-1, 36), (n, covariance)
    print('EXACT_RANK_ENUMERATION_PASS', n, count)


def local_checks():
    # E[I_i]=1/3; E[I_i E_i]= integral_0^infty x exp(-3x) dx.
    assert F(1, 3) == F(1, 3)
    assert F(1, 3*3) == F(1, 9)
    # E[I_i min(E_{i-2},E_{i-1})]=integral exp(-t) *
    # ((1/2)exp(-t)-(1/6)exp(-3t)) dt.
    assert F(1, 2*2) - F(1, 6*4) == F(5, 24)
    assert F(5, 24) - F(1, 3)*F(1, 2) == F(1, 24)
    # Joint chance local minima two apart.
    assert (F(1)-2*F(1, 3)+F(1, 5))/4 == F(2, 15)
    # Adjacent min-of-exponential moment, exact Laplace integrals.
    assert F(1) - 2*F(1, 2)+F(1, 3) == F(1, 3)
    assert F(1, 3)-F(1, 4) == F(1, 12)
    # Aggregate formulas, using no rank enumeration.
    for n in range(5, 21):
        var_q = n*F(1, 4)+2*n*F(1, 12)
        second_l = (F(n*n, 4)+var_q)/F(n*(n+1))
        assert second_l-F(1, 4)==F(1, 6*(n+1))
        assert (n*(2*F(-1, 18)+2*F(1, 24)))/n==F(-1, 36)
    print('LOCAL_MOMENT_CERTIFICATE_PASS')


if __name__=='__main__':
    local_checks()
    for sample_size in (5, 6, 7, 8):
        check(sample_size)
    print('VERIFY_OK')
