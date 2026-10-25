"""Independent numerical checks for squared-position fluctuation control.

Run with: python3 verify_variance.py
Requires NumPy.
This does not claim to certify the analytic proof.
"""
import math
import numpy as np


def stationary_moments(alpha, beta, D, r, ez, ez2):
    m1 = (2 * (alpha + D) + r * ez) / (2 * beta + r)
    m2 = (4 * (alpha + 3 * D) * m1 + r * ez2) / (4 * beta + r)
    return m1, m2


def stationary_variance(alpha, beta, D, r, ez, varz=0.0):
    m1, m2 = stationary_moments(alpha, beta, D, r, ez, ez * ez + varz)
    return m2 - m1*m1


def optimal_square(alpha, beta, D, r):
    return (alpha-D)/beta - D*r/(beta*beta)


def exact_stationary_samples(alpha, beta, D, r, reset_squared, n, rng):
    """Independent sampling via CIR transition at exponential stationary reset age."""
    t = rng.exponential(scale=1.0 / r, size=n)
    q = np.exp(-2 * beta * t)
    reset_sq = reset_squared(n, rng)
    c = D*(1-q)/beta
    df = (alpha + D)/D
    lam = beta*q*reset_sq/(D*(1-q))
    y = c*rng.noncentral_chisquare(df=df, nonc=lam)
    return y


def check():
    rng = np.random.default_rng(20261024)
    scenarios = [
        (3.0, 2.0, 1.0, 1.0, lambda n,rng: np.full(n, 0.75), 'interior optimizer'),
        (3.0, 2.0, 1.0, 1.0, lambda n,rng: np.where(rng.random(n) < 0.5, 0.25, 1.25), 'randomized resets'),
        (3.0, 2.0, 1.0, 1.0, lambda n,rng: np.full(n, 2.0), 'off-optimal'),
        (3.0, 2.0, 1.0, 6.0, lambda n,rng: np.full(n, 0.05), 'boundary regime'),
        (3.0, 2.0, 1.0, 6.0, lambda n,rng: np.full(n, 1.0), 'boundary comparison'),
        (0.5, 2.0, 1.0, 1.0, lambda n,rng: np.full(n, 0.05), 'accessible origin case'),
    ]
    n = 250_000
    for alpha,beta,D,r,draw,label in scenarios:
        reset = draw(n,rng)
        # Compare against a second independent sample from the exact conditional CIR law
        t = rng.exponential(1/r,n)
        q = np.exp(-2*beta*t)
        scale = D*(1-q)/beta
        lam = beta*q*reset/(D*(1-q))
        y = scale*rng.noncentral_chisquare((alpha+D)/D,lam)
        mean_calc, second_calc = stationary_moments(alpha,beta,D,r,float(reset.mean()),float((reset**2).mean()))
        mean_ob = float(y.mean())
        var_ob = float(y.var())
        var_calc = second_calc-mean_calc**2
        rel_m=abs(mean_ob-mean_calc)/mean_calc
        rel_v=abs(var_ob-var_calc)/var_calc
        print(f'{label:24s}: mean={mean_ob:.6f} predicted={mean_calc:.6f}; variance={var_ob:.6f} predicted={var_calc:.6f}; rel={rel_m:.3%},{rel_v:.3%}')
        assert rel_m<0.02 and rel_v<0.04
    for alpha,beta,D,r in [(3,2,1,1),(3,2,1,6),(0.5,2,1,1), (8,0.3,0.1,1)]:
        zc=optimal_square(alpha,beta,D,r)
        z1,z2=0.25,1.25
        k=4*beta**2*r/((2*beta+r)**2*(4*beta+r))
        lhs=stationary_variance(alpha,beta,D,r,z2)-stationary_variance(alpha,beta,D,r,z1)
        rhs=k*((z2-zc)**2-(z1-zc)**2)
        assert abs(lhs-rhs)<1e-11
        mu=0.75
        s2=0.25
        assert abs(stationary_variance(alpha,beta,D,r,mu,s2)-stationary_variance(alpha,beta,D,r,mu)-r*s2/(4*beta+r))<1e-11
    print('All independent CIR transition sampling and quadratic/dispersion-penalty identities passed.')


if __name__ == '__main__':
    check()
