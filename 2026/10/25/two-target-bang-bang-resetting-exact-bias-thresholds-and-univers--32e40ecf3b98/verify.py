"""Reproducibility checks for binary-target Brownian reset design."""
import math
import numpy as np
from scipy.optimize import minimize_scalar


def clip(x):
    return min(1., max(0., float(x)))


def endpoint_data(diffusion, rate, target, radius, probability, discount):
    lam = math.sqrt((rate + discount) / diffusion)
    c = math.exp(-lam * target)
    lo, hi = math.exp(-lam * radius), math.exp(lam * radius)
    gap = hi - lo
    weight = math.sqrt(probability)
    anti = math.sqrt(1 - probability)
    if discount > 0:
        total = 2 * discount + rate * c * (lo + hi)
        optimum = clip(((total * weight / (weight + anti) - discount) /
                        (rate * c) - lo) / gap)
    else:
        optimum = clip(((hi + lo) * weight / (weight + anti) - lo) / gap)
    return lam, c, lo, hi, gap, optimum


def success_transform(discount, probability, mu_x, mu_p, diffusion=1., rate=1., target=3.):
    lam = math.sqrt((rate + discount) / diffusion)
    def transformed(b):
        f = np.sum(mu_p * np.exp(-lam * np.abs(b - mu_x)))
        return (rate + discount) * f / (discount + rate * f)
    return probability * transformed(target) + (1 - probability) * transformed(-target)


def mean_time(probability, mu_x, mu_p, diffusion=1., rate=1., target=3.):
    lam = math.sqrt(rate / diffusion)
    fplus = np.sum(mu_p * np.exp(-lam * np.abs(target - mu_x)))
    fminus = np.sum(mu_p * np.exp(-lam * np.abs(-target - mu_x)))
    return (probability / fplus + (1 - probability) / fminus - 1) / rate


def simulate(rng, repetitions, probability=.5, diffusion=1., rate=1., target=3., radius=1.):
    selected_target = np.where(rng.random(repetitions) < probability, target, -target)
    position = np.where(rng.random(repetitions) < 0.5, radius, -radius)
    total = np.zeros(repetitions)
    active = np.arange(repetitions)
    while len(active):
        distance = np.abs(selected_target[active] - position[active])
        gaussian = rng.standard_normal(len(active))
        while np.any(gaussian == 0):
            gaussian[gaussian == 0] = rng.standard_normal(np.sum(gaussian == 0))
        first_hit = distance ** 2 / (2 * diffusion * gaussian ** 2)
        reset_wait = rng.exponential(1 / rate, len(active))
        successful = first_hit <= reset_wait
        total[active] += np.minimum(first_hit, reset_wait)
        active = active[~successful]
        position[active] = np.where(rng.random(len(active)) < .5, radius, -radius)
    return total


def test():
    rng = np.random.default_rng(260712)
    count = 0
    for _ in range(160):
        D = rng.uniform(.3, 3.)
        r = rng.uniform(.3, 3.)
        L = rng.uniform(1.5, 5.)
        a = rng.uniform(.1, .9 * L)
        p = rng.uniform(.001, .999)
        s = 0. if count % 2 == 0 else rng.uniform(.01, 4.)
        lam, c, lo, hi, gap, w = endpoint_data(D, r, L, a, p, s)
        def objective(wt):
            xs = np.array([-a, a]); probs = np.array([1-wt, wt])
            return mean_time(p, xs, probs, D, r, L) if s == 0 else -success_transform(s, p, xs, probs, D, r, L)
        calc = minimize_scalar(objective, bounds=(0, 1), method='bounded', options={'xatol':1e-11})
        assert objective(w) <= calc.fun + 1e-9 * max(1,abs(calc.fun)), (w,calc.x)
        assert objective(w) <= objective(0) + 1e-8 and objective(w) <= objective(1) + 1e-8
        # Random interior laws are never better than the analytic endpoint optimizer.
        xs = rng.uniform(-a, a, 12)
        probs = rng.dirichlet(np.ones(len(xs)))
        val = mean_time(p, xs, probs, D, r, L) if s == 0 else -success_transform(s, p, xs, probs, D, r, L)
        assert val > objective(w) - 1e-8
        count += 1
    # Critical prior from the analytic endpoint-derivative sign.
    D,r,L,a=1.,1.,3.,1.
    v=math.exp(a*math.sqrt(r/D)); z=1/v
    critical = v*v/(v*v+z*z)
    for p in [1-critical, .5, critical, .99]:
        w=endpoint_data(D,r,L,a,p,0.)[-1]
        assert 0 <= w <= 1
        if p == critical: assert abs(w-1) < 1e-12
        if p == 1-critical: assert abs(w) < 1e-12
    # The unbiased endpoint law is optimal at every discount (Laplace order).
    for s in [.001,.01,.1,.5,2,10,40]:
        law=np.array([-a,a]); weights=np.array([.5,.5])
        optimum=success_transform(s,.5,law,weights)
        for _ in range(150):
            xs=rng.uniform(-a,a,7); ps=rng.dirichlet(np.ones(7))
            assert success_transform(s,.5,xs,ps) < optimum + 1e-13
    samples=simulate(rng,40000)
    target_mean=mean_time(.5,np.array([-a,a]),np.array([.5,.5]))
    target_transform=success_transform(.08,.5,np.array([-a,a]),np.array([.5,.5]))
    empirical_mean=float(np.mean(samples)); empirical_transform=float(np.mean(np.exp(-.08*samples)))
    assert abs(empirical_mean/target_mean-1) < .035
    assert abs(empirical_transform/target_transform-1) < .025
    print('PASS: 160 parameter settings, endpoint uniqueness, continuous-law domination, exact prior thresholds')
    print('PASS: universal unbiased Laplace-order checks at seven discounts')
    print(f'PASS: 40000 exact-cycle simulations: mean {empirical_mean:.6f} vs {target_mean:.6f}; discounted {empirical_transform:.6f} vs {target_transform:.6f}')
    print(f'pcrit={critical:.12f}; symmetric mean improvement vs centre={(math.exp(L)/r)*(1-1/math.cosh(a)):.9f}')

if __name__ == '__main__':
    test()
