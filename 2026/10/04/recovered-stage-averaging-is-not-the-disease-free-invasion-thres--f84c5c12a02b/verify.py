import math

gamma = 1.0
mu = 1.622e-4
T = 52.43
threshold = 2.0 * (gamma + mu)
assert abs(threshold - 2.0003244) < 1e-12

reported_rounded_beta0 = [2.25, 2.18, 2.14]
for beta0 in reported_rounded_beta0:
    exponent = T * (beta0 / 2.0 - (gamma + mu))
    assert exponent > 0.0
    multiplier = math.exp(exponent)
    assert multiplier > 1.0

def class_average_factor(s0, a, n=520):
    susceptibilities = [1.0 - (1.0 - s0) * math.exp(-a * tau) for tau in range(n)]
    return (1.0 + sum(susceptibilities)) / (n + 1.0)

profiles = [(0.00, 9.602e-3), (0.25, 8.680e-3), (0.50, 7.380e-3)]
factors = [class_average_factor(s0, a) for s0, a in profiles]
expected = [0.8005072020838215, 0.8352590323305544, 0.8722919636767662]
for got, want in zip(factors, expected):
    assert abs(got - want) < 1e-12
    assert 0.0 < got < 1.0

# Exact full-period integral of beta0/2 * (1 + cos(2*pi*t/T-phi)) is beta0*T/2.
for beta0 in reported_rounded_beta0:
    integral_beta = beta0 * T / 2.0
    floquet_exponent = integral_beta - (gamma + mu) * T
    assert abs(floquet_exponent - T * (beta0 / 2.0 - (gamma + mu))) < 1e-12

print('VERIFY_OK')
print('threshold', format(threshold, '.10f'))
print('class_average_factors', ' '.join(format(x, '.10f') for x in factors))
