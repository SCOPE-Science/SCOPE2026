from fractions import Fraction as Q

Lam = Q(1)
mu = Q(1)
beta = Q(1)
xi = Q(1)
dB = Q(1)
F = Q(1)
alpha4 = Q(1)
delta = Q(1)
gamma = Q(1)
pf = Q(2)
alpha3 = Q(3)

k = mu + delta + gamma
S0 = Lam / mu
q = pf - alpha4 * F

published_Fu_dot = pf * F
assert published_Fu_dot == 2

Fu = F
Fc = Q(0)
I = Q(0)
B = Q(0)
lambda_l = beta * (B + alpha3 * Fc)
lambda_f = B + alpha4 * Fc
assert Lam + gamma * I - (mu + lambda_l) * S0 == 0
assert lambda_l * S0 - k * I == 0
assert xi * I - dB * B == 0
assert pf * F - (lambda_f + pf) * Fu == 0
assert lambda_f * Fu - pf * Fc == 0

R_published = beta * xi * Lam / (mu * dB * k)
R_corrected = R_published * (Q(1) + alpha3 * F / q)
assert R_published == Q(1, 3)
assert R_corrected == Q(4, 3)

a = beta * S0
A1 = k + dB + q
A2 = k*dB + k*q + dB*q - a*xi
A3 = k*dB*q - a*xi*q - a*alpha3*xi*F
assert (A1, A2, A3) == (Q(5), Q(6), Q(-1))
assert A3 == k*dB*q*(Q(1)-R_corrected)
assert A3 < 0

print("VERIFY_OK")
