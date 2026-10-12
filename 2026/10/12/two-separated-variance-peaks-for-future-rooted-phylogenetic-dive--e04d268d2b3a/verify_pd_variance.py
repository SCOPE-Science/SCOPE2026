"""Exact checks for multiple variance peaks of rooted phylogenetic diversity.

Run: python3 verify_pd_variance.py
Python standard library only. All arithmetic is rational.
"""
from fractions import Fraction as Q
from collections import defaultdict

K = 9
TEST_Q = (Q(1, 2), Q(3, 5), Q(3, 4), Q(9, 10))
EXPECTED_SIGNS = (1, -1, 1, -1)


def add_poly(x, e, coefficient):
    x[e] += coefficient


def covariance_variance_polynomial(edges):
    """Var(PD) as a polynomial in common extinction probability q.

    With leaf mask S_e and edge indicator Y_e, Cov(Y_e,Y_f) is
    q^|S_e union S_f| - q^(|S_e|+|S_f|), exactly.
    """
    answer = defaultdict(Q)
    for mask_e, length_e in edges:
        assert length_e > 0
        for mask_f, length_f in edges:
            term = length_e * length_f
            add_poly(answer, (mask_e | mask_f).bit_count(), term)
            add_poly(answer, mask_e.bit_count() + mask_f.bit_count(), -term)
    return {k: v for k, v in answer.items() if v}


def evaluate(poly, q):
    return sum((coef * q**deg for deg, coef in poly.items()), Q(0))


def derivative_at(poly, q):
    return sum((deg * coef * q**(deg-1)
                for deg, coef in poly.items() if deg), Q(0))


def unresolved_tree(stem):
    b = 1 - stem
    return [(1, Q(1)), (((1 << 10) - 1) ^ 1, stem)] + [
        (1 << i, b) for i in range(1, 10)
    ]


def resolved_binary_tree():
    """Ten tips, crown-stem 3/4, caterpillar crown with step 1/1000."""
    step = Q(1, 1000)
    edges = [(1, Q(1)), (((1 << 10) - 1) ^ 1, Q(3, 4))]
    for j in range(8):
        depth = Q(3, 4) + j * step
        edges.append((1 << (j+1), Q(1) - depth))
        if j < 7:
            future = sum(1 << i for i in range(j+2, 10))
            edges.append((future, step))
        else:
            edges.append((1 << 9, Q(1) - depth))
    assert len(edges) == 18
    assert len({m for m, _ in edges}) == 18
    assert all(l > 0 for _, l in edges)
    assert all(sum(l for m, l in edges if m & (1 << i)) == 1
               for i in range(10))
    return edges


def symbolic_unresolved_at_3_4():
    # V(q)=25/16*q(1-q)+9/16*q^9*(1-q^9)
    #       +27/8*(1-q)*q^9.
    return {1: Q(25, 16), 2: Q(-25, 16),
            9: Q(63, 16), 10: Q(-54, 16), 18: Q(-9, 16)}


def derivative_quadratic_coefficients(q):
    """Coefficients c0+c1*a+c2*a*a of d/ dq Var(PD)."""
    h = (1 - 2*q)
    z = K * q**(K-1)
    c0 = (K + 1)*h
    c1 = -2*K*h + 2*z*(K-(K+1)*q)
    c2 = K*h + z*(1-2*q**K) - 2*z*(K-(K+1)*q)
    return c0, c1, c2


def bernstein_coefficients(q, lower=Q(7, 10), upper=Q(4, 5)):
    c0, c1, c2 = derivative_quadratic_coefficients(q)
    step = upper - lower
    d0 = c0 + lower*c1 + lower*lower*c2
    d1 = step*(c1 + 2*lower*c2)
    d2 = step*step*c2
    # Quadratic in t=(a-lower)/(upper-lower):
    # d(t)=beta0*(1-t)^2+2*beta1*t*(1-t)+beta2*t^2.
    return d0, d0 + d1/2, d0 + d1 + d2


def direct_variance(edges, q):
    """Independent check by summing all 1024 survival configurations."""
    mean = Q(0)
    second = Q(0)
    n = 10
    for survivors in range(1 << n):
        k = survivors.bit_count()
        prob = (1-q)**k * q**(n-k)
        pd = sum((length for mask, length in edges if survivors & mask), Q(0))
        mean += prob * pd
        second += prob * pd * pd
    return second - mean*mean


def verify():
    stem = Q(3, 4)
    polytomy = unresolved_tree(stem)
    poly = covariance_variance_polynomial(polytomy)
    assert poly == symbolic_unresolved_at_3_4(), (poly, symbolic_unresolved_at_3_4())
    # Analytic derivative is [25-50q+567q^8-540q^9-162q^17]/16;
    # descending nonzero coefficient signs are (-,-,+,-,+),
    # so Descartes gives at most 3 positive roots.
    analytic_derivative = {0: Q(25,16), 1: Q(-50,16),
                           8: Q(567,16), 9: Q(-540,16),
                           17: Q(-162,16)}
    actual_derivative = {k-1:k*v for k,v in poly.items() if k}
    assert actual_derivative == analytic_derivative
    for q, sign in zip(TEST_Q, EXPECTED_SIGNS):
        assert sign*derivative_at(poly,q) > 0
        bernstein = bernstein_coefficients(q)
        assert all(sign*b > 0 for b in bernstein), (q, bernstein)
    binary = resolved_binary_tree()
    binary_poly = covariance_variance_polynomial(binary)
    # Explicit rational sign margins for the resolved topology:
    bounds = [Q(1, 20), Q(1, 20), Q(1, 10), Q(1, 2)]
    for q, sign, margin in zip(TEST_Q, EXPECTED_SIGNS, bounds):
        d = derivative_at(binary_poly,q)
        assert d*sign > margin, (q, d, margin)
    checked = 0
    for edges in (polytomy, binary):
        p = covariance_variance_polynomial(edges)
        for q in (Q(1,3), Q(1,2), Q(2,3), Q(4,5)):
            assert evaluate(p,q) == direct_variance(edges,q)
            checked += (1 << 10)
    print('VERIFY_OK',
          'tree_profiles=2',
          'binary_edges=18',
          'clade_parameter_interval=[7/10,4/5]',
          'Bernstein_sign_certificates=4',
          'binary_derivative_sign_certificates=4',
          'survival_configurations=', checked,
          'polytomy_derivative=', {str(k):str(v) for k,v in sorted(analytic_derivative.items())})


if __name__ == '__main__':
    verify()
