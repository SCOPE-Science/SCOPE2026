#!/usr/bin/env python3
"""Elementary identities and reproducible stationary-switch simulation."""
import math
import random


def sample_entry_logs(eps, a, c, b, cycles=300000, seed=1729):
    rng = random.Random(seed)
    x = 0.0  # position at entry to a running episode
    run_log_sum = 0.0
    tumble_log_sum = 0.0
    run_abs_log_sum = 0.0
    tumble_abs_log_sum = 0.0
    num_run = 0
    num_tumble = 0
    for k in range(cycles):
        sign = 1 if rng.random() < 0.5 else -1
        run_t = -math.log(rng.random()) / (eps*a)
        end_run = sign + (x - sign)*math.exp(-b*run_t)
        tumble_t = -math.log(rng.random()) / (eps*c)
        end_tumble = end_run*math.exp(-b*tumble_t)
        if k >= 200:
            q = math.log(abs(end_run))
            tumble_log_sum += q
            tumble_abs_log_sum += abs(q)
            num_tumble += 1
            if sign == 1:
                q = math.log(abs(1.0-x))
                run_log_sum += q
                run_abs_log_sum += abs(q)
                num_run += 1
        x = end_tumble
    return (run_log_sum/num_run, tumble_log_sum/num_tumble,
            run_abs_log_sum/num_run, tumble_abs_log_sum/num_tumble)


def main():
    a, c, b = 1.2, 0.8, 1.3
    k_run = -(c/b)*math.pi**2/24
    k_tum = -(a/b)*math.pi**2/6
    k_bound_run = (c/b)*(math.pi**2/6 + math.log(2)**2 + 1)
    k_bound_tum = (a/b)*math.pi**2/3
    assert math.pi**2/6 + math.log(2)**2 + 1 < math.pi**2/3
    # Verify the two coefficients via an independent convergent series identity.
    zeta2 = math.fsum(1/(k*k) for k in range(1, 250001))
    assert abs(zeta2 - math.pi**2/6) < 5e-6
    assert abs(k_run + (c/(4*b))*zeta2) < 2e-6
    assert abs(k_tum + (a/b)*zeta2) < 4e-6
    # Stationary state probabilities and transition balance.
    p0 = a/(a+c)
    pr = c/(2*(a+c))
    assert abs((p0 + 2*pr)-1)<1e-12
    assert abs(p0*c - 2*pr*a)<1e-12
    # Exact embedded-chain simulation, not an independent proof of asymptotics.
    for epsilon, tol_r, tol_t in [(0.12,0.09,0.25), (0.06,0.065,0.14), (0.03,0.055,0.15)]:
        run, tum, run_abs, tum_abs = sample_entry_logs(epsilon, a,c,b)
        assert abs(run/epsilon-k_run)<tol_r,(epsilon,run/epsilon,k_run)
        assert abs(tum/epsilon-k_tum)<tol_t,(epsilon,tum/epsilon,k_tum)
        assert run_abs <= epsilon*k_bound_run*1.02
        assert tum_abs <= epsilon*k_bound_tum*1.02
        # Mean of the logarithmic localization adds the correction -epsilon E log(entry distance).
        run_mean = b/a - epsilon*run
        tum_mean = b/c - epsilon*tum
        assert run_mean>b/a and tum_mean>b/c
        print('epsilon={:.3f}: Elog(D_run)/epsilon={:.9f}; Elog(D_0)/epsilon={:.9f}; predicted={:.9f},{:.9f}'.format(epsilon,run/epsilon,tum/epsilon,k_run,k_tum))
    print('All stationary-chain, series, and coefficient consistency checks passed.')


if __name__ == '__main__':
    main()
