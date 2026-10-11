"""Exact rational checks for a bistable forest disease–fire ODE."""
from fractions import Fraction as Q

r, K, beta, alpha, sigma, omega, mu = (
    Q(130), Q(130), Q(106), Q(20, 53), Q(126), Q(1), Q(106)
)


def system(s, i):
    f = r * s * (1 - s / K) - beta * s * i / (i + alpha) - sigma * s / (1 + omega * s)
    g = beta * s * i / (i + alpha) - mu * i
    return f, g


def jacobian(s, i):
    return (
        (r - 2 * r * s / K - beta * i / (i + alpha) - sigma / (1 + omega * s) ** 2,
         -beta * s * alpha / (i + alpha) ** 2),
        (beta * i / (i + alpha), beta * s * alpha / (i + alpha) ** 2 - mu),
    )


def nullcline(s):
    return beta * s / mu - alpha


def reduced(s):
    return system(s, nullcline(s))[0] / s


def factored(s):
    return -(s - 1) * (s - 2) * (s - 20) / (s * (1 + s))


assert all(z > 0 for z in (r, K, beta, alpha, sigma, omega, mu))
assert r > sigma
assert [nullcline(z) for z in (Q(1), Q(2), Q(20))] == [Q(33, 53), Q(86, 53), Q(1040, 53)]
for z in (Q(1, 2), Q(3, 2), Q(4), Q(25)):
    assert reduced(z) == factored(z)

values = (
    (Q(1), Q(33, 53), ((Q(61, 2), Q(-40)), (Q(66), Q(-66))), Q(-71, 2), Q(627)),
    (Q(2), Q(86, 53), ((Q(26), Q(-20)), (Q(86), Q(-86))), Q(-60), Q(-516)),
    (Q(20), Q(1040, 53), ((Q(-100, 7), Q(-2)), (Q(104), Q(-104))), Q(-828, 7), Q(11856, 7)),
)
for s, i, expected_J, expected_trace, expected_det in values:
    assert system(s, i) == (0, 0)
    J = jacobian(s, i)
    assert J == expected_J
    tr = J[0][0] + J[1][1]
    det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
    assert tr == expected_trace and det == expected_det
assert values[0][4] > 0 and values[1][4] < 0 and values[2][4] > 0
assert values[0][3] < 0 and values[2][3] < 0
# Exactly one positive disease-free equilibrium follows from
# H(S) = (r-r*S/K)*(1+omega*S)-sigma = -S**2+129*S+4.
for z in (Q(0), Q(1), Q(2), Q(20), Q(130)):
    assert (r - r * z / K) * (1 + omega * z) - sigma == -z*z + 129*z + 4
print('CHECK_OK')
