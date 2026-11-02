#!/usr/bin/env python3
"""Reproduce exact opposite-side capture tests for a transparent blinking Brownian target.

NumPy is required. The analytic proof is in RESULT.md; simulations and
finite parameter grids are supplementary checks, not universal certificates.
"""
import math
import numpy as np


def formula(x0, diffusivity, reset_rate, gate_rate):
    a = math.sqrt(reset_rate / diffusivity)
    b = math.sqrt((reset_rate + 2 * gate_rate) / diffusivity)
    z = a / b
    v = math.exp(-b*x0)
    fa = (1-z)*(1-v)/4
    fi = fa+v/(2*(1+z))
    return fa, fi


def renewal(x0, d, r, gamma):
    a = math.sqrt(r/d)
    b = math.sqrt((r+2*gamma)/d)
    u = math.exp(-a*x0)
    v = math.exp(-b*x0)
    t = (b-a)/(a+b)
    g = np.array([(b*u+a*v)/(a+b), (b*u-a*v)/(a+b)])
    l = np.array([t*(u-v)/4, t*(u+v)/4])
    c, h = (r+gamma)/(r+2*gamma), gamma/(r+2*gamma)
    R = np.array([[c,h],[h,c]])
    K = R - g[:,None] * R[[0],:]
    return np.linalg.solve(np.eye(2)-K, l)


def backward_boundary_problem(x0, d, r, gamma):
    # Solve D f''+Q f-r(f-f(x0))=0 on each open half-line.
    # Unknowns: f_A(x0),f_I(x0), right decaying amplitudes, left growing amplitudes.
    a = math.sqrt(r/d)
    b = math.sqrt((r+2*gamma)/d)
    c, h = (r+gamma)/(r+2*gamma), gamma/(r+2*gamma)

    def basis(x, sign):
        ea = math.exp((-a if sign == '+' else a)*x)
        eb = math.exp((-b if sign == '+' else b)*x)
        if sign == '+':
            return np.array([[c,h,ea,eb,0,0],
                             [h,c,ea,-eb,0,0]])
        return np.array([[c,h,0,0,ea,eb],
                         [h,c,0,0,ea,-eb]])

    p = basis(0, '+')
    n = basis(0, '-')
    at_reset = basis(x0, '+')
    derivative_i = np.array([0,0,-a,b,-a,b])
    rows = np.array([p[0], n[0], p[1]-n[1], derivative_i,
                     at_reset[0]-np.array([1,0,0,0,0,0]),
                     at_reset[1]-np.array([0,1,0,0,0,0])])
    rhs = np.array([0,1,0,0,0,0])
    return np.linalg.solve(rows, rhs)[:2]


def exact_event_simulation(x0, d, r, gamma, n=25000, seed=1009):
    # Between event times Exp(r+gamma), sample the exact Brownian endpoint.
    # A Brownian bridge crossing 0 has conditional probability
    # exp(-X*Y/(d*dt)) when endpoints have the same sign.
    rng = np.random.default_rng(seed)
    x = np.full(n, x0, dtype=float)
    active = rng.random(n)<0.5
    live = np.ones(n, dtype=bool)
    was_left = np.zeros(n, dtype=bool)
    total_events = 0
    while np.any(live):
        idx = np.flatnonzero(live)
        num = len(idx)
        total_events += num
        if total_events>n*200000:
            raise RuntimeError('Unexpectedly large event count')
        dt = rng.exponential(1/(r+gamma), size=num)
        is_reset = rng.random(num)<r/(r+gamma)
        endpoint = x[idx] + rng.normal(size=num)*np.sqrt(2*d*dt)
        absorption = np.zeros(num, dtype=bool)
        mask = active[idx]
        if np.any(mask):
            product = x[idx[mask]]*endpoint[mask]
            crossing_prob = np.exp(-np.maximum(product, 0)/(d*dt[mask]))
            absorption[mask] = (product<=0) | (rng.random(np.sum(mask))<crossing_prob)
        if np.any(absorption):
            hit_idx = idx[absorption]
            was_left[hit_idx] = x[hit_idx]<0
            live[hit_idx] = False
        survivor = ~absorption
        if np.any(survivor):
            keep = idx[survivor]
            reset = is_reset[survivor]
            x[keep] = endpoint[survivor]
            x[keep[reset]] = x0
            active[keep[~reset]] = ~active[keep[~reset]]
    phat = float(np.mean(was_left))
    return phat, math.sqrt(phat*(1-phat)/n), total_events


def main():
    checked = 0
    for d in (0.4, 1.0, 3.7):
        for x0 in (0.3, 1.0, 2.1):
            for r in (0.05, 0.7, 4.0):
                for g in (0.07, 1.4, 12.0):
                    expected = np.array(formula(x0,d,r,g))
                    from_renewal = renewal(x0,d,r,g)
                    from_boundary = backward_boundary_problem(x0,d,r,g)
                    assert np.allclose(from_renewal, expected, atol=1e-10, rtol=1e-10), (d,x0,r,g,'renewal')
                    assert np.allclose(from_boundary, expected, atol=1e-10, rtol=1e-10), (d,x0,r,g,'BVP')
                    checked += 1
    for r in (0.05,0.2,1,4,20):
        for gamma in (0.05,0.2,1,4,20):
            def equilibrium(r0,g0,x0=1):
                f=formula(x0,1,r0,g0)
                return sum(f)/2
            assert equilibrium(r*1.00001,gamma)<equilibrium(r,gamma)
            assert equilibrium(r,gamma*1.00001)>equilibrium(r,gamma)
            assert equilibrium(r,gamma,1.00001)<equilibrium(r,gamma,1)
            checked += 1
    for ratio in (0.05,0.5,2,20,200):
        for epsilon in (1e-6,1e-8):
            r, g = ratio*epsilon, epsilon
            z = math.sqrt(ratio/(ratio+2))
            p = sum(formula(1,1,r,g))/2
            assert abs(p-1/(4*(1+z))) <= math.sqrt(r+2*g)/8+1e-12
            checked += 1
    print('PASS: finite exact-formula/renewal/backward-BVP/trend/limit tests:',checked)
    for i, gamma in enumerate((0.1,1.0,10.0)):
        sample, se, events = exact_event_simulation(1,1,1,gamma,seed=20260903+i)
        exact = sum(formula(1,1,1,gamma))/2
        # Five normal standard errors plus a small systematic cushion.
        assert abs(sample-exact)<5*math.sqrt(exact*(1-exact)/25000)+0.002, (gamma,sample,exact)
        print('PASS: exact-event simulation gamma=',gamma,'estimate=',round(sample,6),
              'exact=',round(exact,6),'events=',events,'SE=',round(se,6))
    print('All finite consistency checks completed; universal conclusions use the proof.')


if __name__ == '__main__':
    main()
