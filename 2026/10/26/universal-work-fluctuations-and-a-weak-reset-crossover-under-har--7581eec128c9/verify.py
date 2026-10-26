"""Numerical checks for stationary harmonic partial-reset work moments.

Run: python verify.py
Requires: Python 3 and numpy.
"""
import numpy as np


def exact_moments(n, a, diffusivity, stiffness, mean_time, var_time):
    q = a*a
    mu = stiffness*diffusivity*mean_time
    reward_var = (stiffness*diffusivity)**2 * (
        2*mean_time**2 + 3*var_time*(1-q)/(1+q)
    )
    bracket = n*(1+q)/(1-q) - 2*q*(1-q**n)/(1-q)**2
    return n*mu, reward_var*bracket


def experiment(n, a, law, sample_count, seed):
    generator = np.random.default_rng(seed)
    diffusion, stiffness = .85, 1.4
    r = 1.2
    if law == 'exponential':
        mean_time, var_time = 1/r, 1/r**2
        def draw(size): return generator.exponential(mean_time, size)
    elif law == 'erlang3':
        mean_time, var_time = 1/r, 1/(3*r**2)
        def draw(size): return generator.gamma(3, mean_time/3, size)
    elif law == 'deterministic':
        mean_time, var_time = 1/r, 0.
        def draw(size): return np.full(size, mean_time)
    else:
        raise ValueError('unknown duration law')
    state = np.zeros(sample_count)
    q = a*a
    burn = max(90, int(np.ceil(np.log(1.e-12)/np.log(q)))) if q else 2
    for _ in range(burn):
        time = draw(sample_count)
        state = a*state + np.sqrt(2*diffusion*time)*generator.normal(size=sample_count)
    total = np.zeros(sample_count)
    for _ in range(n):
        time = draw(sample_count)
        state = a*state + np.sqrt(2*diffusion*time)*generator.normal(size=sample_count)
        total += stiffness*(1-q)*state**2/2
    expected_mean, expected_var = exact_moments(n, a, diffusion, stiffness, mean_time, var_time)
    observed_mean, observed_var = float(total.mean()), float(total.var(ddof=1))
    return observed_mean/expected_mean-1, observed_var/expected_var-1


def main():
    specifications = [(20, 0., 'exponential'), (25,.36,'erlang3'),
        (35,.75,'deterministic'), (55,.90,'exponential'),
        (65,.94,'erlang3'), (70,.975,'exponential')]
    for index, (n, a, law) in enumerate(specifications):
        e_mean,e_var = experiment(n,a,law,70000,90240+index)
        print(f'{law:13s} a={a:.3f} n={n}: mean relerr={e_mean:+.5f}, variance relerr={e_var:+.5f}')
        assert abs(e_mean)<.020 and abs(e_var)<.060
    for eps in [.05,.02,.008]:
        a = np.sqrt(1-eps)
        n = round(2/eps)
        mean, variance = exact_moments(n,a,.85,1.4,1/1.2,1/1.2**2)
        actual_scaled = variance/(mean*mean)
        limit = 4*(2-1+np.exp(-2))/4
        print(f'OU weak-reset crossover eps={eps:.3f}: exact normalized variance={actual_scaled:.8f}, continuum={limit:.8f}')
        assert abs(actual_scaled-limit)<.035
    print('ALL CHECKS PASS')

if __name__=='__main__':
    main()
