from fractions import Fraction as F


def f(x, eta):
    return x / (1 + eta*x)


def check_holling(x, xs, eta):
    # Exact identity: f(x)-f(xs)=(x-xs)/((1+eta*x)(1+eta*xs)).
    lhs = f(x, eta) - f(xs, eta)
    rhs = (x-xs) / ((1+eta*x)*(1+eta*xs))
    assert lhs == rhs


def check_quadratic(alpha, m1, m2):
    # E[(1-X)(X-alpha)] in terms of first two raw moments.
    raw = -m2 + (1+alpha)*m1 - alpha
    var = m2 - m1*m1
    shell_side = (1-m1)*(m1-alpha) - var
    assert raw == shell_side


for x in [F(1,7), F(2,5), F(9,10), F(7,3)]:
    check_holling(x, F(3,5), F(2,3))

for alpha, m1, m2 in [
    (F(1,5), F(3,5), F(2,5)),
    (F(1,4), F(1,2), F(3,10)),
    (F(2,7), F(4,7), F(5,14)),
]:
    check_quadratic(alpha, m1, m2)

sigma = F(22053, 50000)  # 0.44106
omega = F(1,1)
eta = F(3,5)
xs = sigma / (omega - sigma*eta)
assert xs == F(110265, 183841)
assert f(xs, eta) == sigma/omega
print('VERIFY_OK')
print('x_star =', xs, '=', float(xs))
