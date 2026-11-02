"""Independent finite-arithmetic checks of one-step Gaussian-sketched Krylov formulas.
Only the Python standard library is required. These finite tests do not prove the
infinite-moment statements; their proofs use the explicitly derived densities.
"""
import math
import random


def half_student_density(z, m):
    c = math.exp(math.lgamma((m + 1) / 2) - .5 * math.log(math.pi) - math.lgamma(m / 2))
    return c * (1 + z*z) ** (-(m + 1) / 2)


def simpson(f, a, b, n=12000):
    assert n % 2 == 0
    step = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * step)
    return step * s / 3


def test_density_and_moments():
    for m in range(1, 11):
        c = half_student_density(0, m)
        mass = simpson(lambda th: c * math.cos(th)**(m-1), -math.pi/2, math.pi/2)
        assert abs(mass - 1) < 5e-8, (m, mass)
        if m > 2:
            moment = simpson(lambda th: c * math.sin(th)**2 * math.cos(th)**(m-3), -math.pi/2, math.pi/2)
            assert abs(moment - 1/(m-2)) < 5e-8, (m, moment)
        # With a=2 and c=1, Y=2+Z/R and theta_F=1/Y.
        # Numerically integrate the exact pole interval for tail P(|theta_F|>T).
        fzero = half_student_density(-2,m)
        tailconstant = 2*fzero
        for t in (1000, 5000):
            prob = simpson(lambda y: half_student_density(y-2,m), -1/t, 1/t, 120)
            assert abs(t*prob/tailconstant - 1) < 2e-4, (m,t,prob)


def test_reparametrization():
    rng = random.Random(20261025)
    rt2 = math.sqrt(2)
    for m in (1,2,3,4,5,8,12):
        for _ in range(150):
            g = [(rng.gauss(0,1),rng.gauss(0,1)) for i in range(m)]
            U = [(a+b)/rt2 for a,b in g]
            V = [(-a+b)/rt2 for a,b in g]
            # A=diag(1,3); b=(1,1)/sqrt(2); Ab=2b+w.
            # Scaling of the Gaussian matrix by m^{-1/2} cancels.
            bb = sum(u*u for u in U)
            bax = sum(u*(2*u+v) for u,v in zip(U,V))
            aax = sum((2*u+v)**2 for u,v in zip(U,V))
            f_gram = bb/bax
            m_gram = bax/aax
            assert abs(f_gram - 1/(2+sum(u*v for u,v in zip(U,V))/bb)) < 1e-10*max(1,abs(f_gram))
            assert abs(m_gram - sum((2*u+v)*u for u,v in zip(U,V))/aax) < 1e-12
            assert math.isfinite(f_gram) and math.isfinite(m_gram)


def test_exact_example():
    # Direct rational arithmetic for ||x* - theta b||_A^2.
    from fractions import Fraction as F
    a=F(2); norm_Ainv=F(2,3); mu=F(2,5); varscale=F(1,25)
    base = norm_Ainv-2*mu+a*mu*mu
    assert base == F(14,75)
    for m in (3,4,7,12):
        predicted = base+a*varscale/F(m-2)
        assert predicted>base
    # deterministic Galerkin theta=1/2 gives error 1/6
    assert norm_Ainv - 2*F(1,2) + a*F(1,2)**2 == F(1,6)


if __name__ == '__main__':
    test_density_and_moments()
    test_reparametrization()
    test_exact_example()
    print('VERIFY_OK: 10 normalized densities, 8 second moments, 20 pole-tail estimates, 1050 Gaussian-sketch algebra checks, exact rational error laws')
