"""Independent finite-case calculations for a rank-one killed-memory kernel.

Run with Python 3 standard library: python check.py
The numerical calculations are consistency tests, not proofs of infinite limits.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, isclose
from random import Random

ASSERTIONS = 0

def check(condition, label):
    global ASSERTIONS
    if not condition:
        raise AssertionError(label)
    ASSERTIONS += 1


def optimum_binary(k0=1.0, k1=0.2, p0=0.5):
    weights = (p0, 1.0 - p0)
    lo, hi = min(k0, k1), max(k0, k1)
    for _ in range(120):
        m = (lo + hi) * 0.5
        a, b = weights[0]*exp(k0/m), weights[1]*exp(k1/m)
        implied = (a*k0 + b*k1)/(a+b)
        if implied > m:
            lo = m
        else:
            hi = m
    m = (lo + hi) * 0.5
    a, b = weights[0]*exp(k0/m), weights[1]*exp(k1/m)
    q0, q1 = a/(a+b), b/(a+b)
    divergence = q0*log(q0/weights[0]) + q1*log(q1/weights[1])
    return m*exp(-divergence), (q0,q1), m


def finite_spectral_radius(k, pi, tau):
    # Keep exactly as many historical bits as the longest used lag.
    d = len(tau)
    count = 1 << d
    mask = count - 1
    v = [1.0] * count
    last_scale = 0.0
    for _ in range(2500):
        u = [0.0] * count
        for state in range(count):
            survival = sum(float(w) * float(k[(state >> i) & 1]) for i,w in enumerate(tau))
            lo = (state << 1) & mask
            u[state] = survival * (float(pi[0])*v[lo] + float(pi[1])*v[lo|1])
        last_scale = max(u)
        v = [x/last_scale for x in u]
    return last_scale


def exact_path_and_transfer_test(k, pi, tau, horizon, past):
    d = len(tau)
    assert len(past) == d
    memory = sum(int(past[i]) << i for i in range(d))
    operator = {memory:Fraction(1)}
    for _ in range(horizon):
        new = {}
        for s,w in operator.items():
            a = sum(tau[i]*k[(s >> i)&1] for i in range(d))
            for new_bit in (0,1):
                t = ((s << 1) & ((1 << d)-1)) | new_bit
                new[t] = new.get(t,Fraction(0)) + w*a*pi[new_bit]
        operator = new
    via_transfer = sum(operator.values(),Fraction(0))

    via_paths = Fraction(0)
    for generated in product((0,1),repeat=horizon):
        density = Fraction(1)
        for bit in generated:
            density *= pi[bit]
        states = list(past)
        for bit in generated:
            survival = sum(tau[i]*k[states[i]] for i in range(d))
            density *= survival
            states = [bit]+states[:-1]
        via_paths += density
    check(via_transfer == via_paths, 'exact path versus transfer')
    return via_paths


def main():
    k = (1.0, 0.2)
    pi = (0.5, 0.5)
    benchmark = 0.6
    bound,q,m = optimum_binary()
    check(abs(bound-0.7024504925079701) < 1e-12,'optimum numerical value')
    check(abs(m-0.78736212101005) < 1e-12,'fixed-point mean')
    check(q[0] > pi[0] and q[1] < pi[1],'nonconstant-k tilt')
    check(bound > benchmark,'strict advantage')
    variance = sum(q[s]*(k[s]-m)**2 for s in (0,1))
    check(abs(sum(q[s]*k[s] for s in (0,1))-m) < 1e-13,'tilted mean')

    for L in range(1,9):
        tau = [1.0/L]*L
        r = finite_spectral_radius(k,pi,tau)
        collision = sum(x*x for x in tau)
        lower = bound*exp(-variance*collision/(2*min(k)**2))
        check(r <= bound + 1e-10, f'upper spectral bound L={L}')
        check(r >= lower - 1e-10, f'quantitative lower L={L}')
        check(r >= benchmark - 1e-10, f'benchmark L={L}')
        if L in (1,2,4,8):
            print(f'uniform_tau_{L}: spectral={r:.12f} lower_bound={lower:.12f} upper={bound:.12f}')

    rng = Random(61726)
    for case in range(90):
        a, b = rng.uniform(0.15,0.99), rng.uniform(0.15,0.99)
        p = rng.uniform(0.1,0.9)
        B, tilt, mean = optimum_binary(a,b,p)
        var = sum(tilt[s]*(v-mean)**2 for s,v in enumerate((a,b)))
        L = 1 + case%5
        raw = [0.01 + rng.random() for _ in range(L)]
        tau = [v/sum(raw) for v in raw]
        r = finite_spectral_radius((a,b),(p,1-p),tau)
        lower = B*exp(-var*sum(v*v for v in tau)/(2*min(a,b)**2))
        check(r < B + 2e-10, f'random upper {case}')
        check(r > lower - 2e-10, f'random lower {case}')
        check(r > p*a+(1-p)*b - 2e-10, f'random baseline {case}')
    print('seeded_rank_one_finite_matrix_cases:',90)

    choices = [
       ([Fraction(1,2),Fraction(1,3),Fraction(1,6)], (Fraction(1),Fraction(1,5)), (Fraction(2,3),Fraction(1,3))),
       ([Fraction(1,3),Fraction(2,3)], (Fraction(1),Fraction(1,4)), (Fraction(3,4),Fraction(1,4))),
       ([Fraction(1,4)]*4, (Fraction(1),Fraction(2,5)), (Fraction(1,2),Fraction(1,2))),
    ]
    for tau, survival, base in choices:
        for horizon in range(1,7):
            for past in product((0,1), repeat=len(tau)):
                exact_path_and_transfer_test(survival,base,tau,horizon,past)
    print('exact_path_consistency: all finite enumeration cases passed')
    print('ASSERTIONS:', ASSERTIONS)

if __name__ == '__main__':
    main()
