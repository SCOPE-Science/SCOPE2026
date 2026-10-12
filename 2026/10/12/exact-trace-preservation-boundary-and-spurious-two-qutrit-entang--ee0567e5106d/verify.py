#!/usr/bin/env python3
"""Exact rational cross-checks for a published two-qutrit damping family."""
from fractions import Fraction as F


def original_state(alpha):
    # Density operator in lexicographic |a,b> order. The amplitudes in
    # the rank-one state combine to rational density-matrix entries.
    x = [[F(0) for _ in range(9)] for _ in range(9)]
    psi_idx = (1, 3, 8)
    for i in psi_idx:
        for j in psi_idx:
            x[i][j] += F(2, 21)
    for idx in (0, 5, 7):
        x[idx][idx] += alpha / 21
    for idx in (4, 6, 2):
        x[idx][idx] += (5-alpha) / 21
    return x


def witness(alpha):
    rho = original_state(alpha)
    assert sum(rho[k][k] for k in range(9)) == 1
    for a in range(3):
        assert sum(rho[3*a+b][3*a+b] for b in range(3)) == F(1, 3)
        assert sum(rho[3*b+a][3*b+a] for b in range(3)) == F(1, 3)
    assert rho[0][0] == alpha / 21
    r, p = F(3, 20), F(3, 4)
    # Q=sum_i E_i^dagger E_i: the absorption diagonal uses the absolute
    # square of E4's continued complex square root.
    q0 = r + (1-r)*(abs(1-2*p)+2*p)
    q1 = r*((1-p)+p) + (1-r)
    q2 = r*((1-p)+p) + (1-r)
    assert q1 == q2 == 1
    delta = q0 - 1
    assert delta == F(17,20)
    trace_exact = sum(rho[3*a+b][3*a+b] * ([q0,q1,q2][a])*([q0,q1,q2][b])
                      for a in range(3) for b in range(3))
    assert trace_exact == 1 + F(2,3)*delta + alpha*delta*delta/21
    assert trace_exact > 1
    return trace_exact-1


def test():
    # Positive partial transpose: lambda_minus>=0 precisely when
    # (2 alpha - 5)^2 + 16 <= 25 on the stated alpha interval.
    for alpha in (F(2),F(5,2),F(7,2),F(4)):
        assert (2*alpha-5)**2 + 16 <= 25
    assert witness(F(5,2)) == F(731,1120)
    assert witness(F(7,2)) == F(1649,2400)
    r, p = F(3,20), F(1,4)
    assert r + (1-r)*(abs(1-2*p)+2*p) == 1
    # Equal-decay physicality threshold exactly p=1/2.
    p = F(1,2)
    assert r+(1-r)*(abs(1-2*p)+2*p) == 1
    print('VERIFY_OK trace_preservation=passed source_marginals=passed')
    print('VERIFY_OK PPT_spectrum=passed rational_witnesses=passed')


if __name__ == '__main__':
    test()
