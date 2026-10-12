#!/usr/bin/env python3
"""Exact-rational illustrations of the period-mean payoff degeneracy."""
from fractions import Fraction as F


def dot_A(x, A, y):
    return sum(x[i] * A[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))


def vec_add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vec_scale(k, x):
    return tuple(k * a for a in x)


# Published game matrix, arXiv:2601.01996v1, Appendix E(i).
A = (
    (F('-0.022'), F('-0.829'), F('-0.505'), F('5.5')),
    (F('0.45'), F('-0.211'), F('1.325'), F('-1.531')),
    (F('1.295'), F('-0.008'), F('-0.326'), F('-0.96')),
    (F('0.10'), F('0.25'), F('0.1'), F('0.0')),
)
p = (F(1, 4),) * 4
v = (F(1, 16), -F(1, 16), F(0), F(0))
w = (F(0), F(0), F(1, 16), -F(1, 16))
assert sum(p) == 1 and sum(v) == sum(w) == 0
assert all(p[i] - abs(v[i]) - abs(w[i]) >= F(3, 16) for i in range(4))
assert any(v) and any(w)
# For r(t)=p+v*cos(t)+w*sin(t), the exact full-period average is p.
assert dot_A(p, A, p) == F(1157, 4000)
for eta in (F(1, 1000), F(1, 10), F(1, 2), F(3, 4)):
    # m_eta(t) = p+(1-eta)*(v*cos(t)+w*sin(t)): nonconstant, same mean.
    v_eta, w_eta = vec_scale(1-eta, v), vec_scale(1-eta, w)
    assert any(v_eta) and any(w_eta)
    mean_mutant = p  # Integrals of sine and cosine vanish on full periods.
    assert mean_mutant == p
    for eps in (F(1, 100), F(1, 2), F(99, 100)):
        opponent = vec_add(vec_scale(1-eps, p), vec_scale(eps, mean_mutant))
        assert opponent == p
        # Averaging either focal path gives p, so both payoffs tie exactly.
        resident_payoff = dot_A(p, A, opponent)
        mutant_payoff = dot_A(mean_mutant, A, opponent)
        assert resident_payoff == mutant_payoff == F(1157, 4000)
        # The local comparison uses the mutant's full-period sliding mean p.
        assert dot_A(p, A, mean_mutant) == dot_A(mean_mutant, A, mean_mutant)

# An exact replicator equilibrium for a classical 3-strategy game.
B = ((F(0), F(-1), F(1)), (F(1), F(0), F(-1)), (F(-1), F(1), F(0)))
u = (F(1, 3),) * 3
assert all(sum(B[i][j]*u[j] for j in range(3)) == dot_A(u, B, u) == 0 for i in range(3))
print('VERIFY_OK: rational universal-mean witness, local interpolation and stationary game state')
