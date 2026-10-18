"""Finite reproducibility checks for an age-structured predator-prey absorbing estimate.

Run with Python 3; only standard-library modules are used. Numerical checks do
not establish the all-parameter theorem, which follows from the analytic proof.
"""
from fractions import Fraction
from math import exp, isfinite, log, tanh
from random import Random


def rational_checks():
    # Test the algebraic mixed-term cancellation and the dissipative inequality.
    C, a, L, b, c, K, m = map(Fraction, (2, 1, 4, 2, 1, 4, 2))
    c = Fraction(1, 4)
    K = Fraction(2)
    m = Fraction(1, 2)
    q = b*c/(2*K)
    count = 0
    for ix in range(49):
        x = L*Fraction(ix, 48)
        for ip in range(51):
            p = Fraction(ip, 2)
            v = x+q*p
            differential_bound = C*x-a*x*x-b*c*x*p+q*(K*x-m)*p
            assert differential_bound <= (C+m)*L-m*v
            assert b*c-q*K == b*c/2
            count += 1
    return count


def parameter_checks():
    rng = Random(19830319)
    count = 0
    for _ in range(120):
        r, a, s, h, b = [10**rng.uniform(-0.6, 0.6) for _ in range(5)]
        g, mu_B, mu_M, rho, maturation, k, zeta, btilde = [10**rng.uniform(-0.6, 0.6) for _ in range(8)]
        C = r+s*h
        L = 2*C/a
        m = mu_M*exp(-rho*L)
        M = g*L+mu_B+mu_M
        K = k+zeta*btilde
        c = exp(-(M+K*L)*maturation)
        q = b*c/(2*K)
        assert c > 0 and m > 0 and q > 0
        for _ in range(20):
            x = rng.random()*L
            p = rng.random()*50
            y1 = rng.random()*p
            y2 = p-y1
            # At time t>=t0+T, valid states additionally satisfy y2>=c*P.
            y2 = max(y2,c*p)
            if y2 > p: y2=p
            xdot = x*(r-a*x+s*h*tanh(y1/h)-b*y2)
            # Births no larger than K*x*P; mortality no smaller than m*P.
            pdot_upper = (K*x-m)*p
            lhs = xdot+q*pdot_upper
            rhs = (C+m)*L-m*(x+q*p)
            assert lhs <= rhs+2e-10*max(1,abs(rhs),abs(lhs)), (lhs,rhs)
            count += 1
    return count

if __name__ == '__main__':
    r = rational_checks()
    f = parameter_checks()
    print(f'VERIFY_OK: {r} exact rational Lyapunov cases; {f} parameterized birth/death and dissipativity inequalities; analytic proof required for global result')
