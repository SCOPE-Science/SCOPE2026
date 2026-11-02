"""Numerical checks for the saddlepoint factor in a periodic varying-index jump law.
The tests address the deterministic normalization; they are not stochastic-process proofs.
"""
import math
from scipy.special import i0e

def laplace_prefactor(log_n, alpha_min, epsilons):
    d = len(epsilons)
    L = (log_n - 0.5*d*math.log(log_n))/alpha_min
    assert L > 0
    out = log_n ** (d / 2)
    for e in epsilons:
        out *= i0e(e*L)
    return out

def predicted(alpha_min, epsilons):
    # Hessian of sum e_j(1-cos(2*pi*x_j)) is diag(4*pi*pi*e_j).
    d = len(epsilons)
    return (2*math.pi*alpha_min)**(d/2) / math.prod(math.sqrt(4*math.pi**2*e) for e in epsilons)

count = 0
for a, es in [(1.0,(0.25,)), (1.1,(0.20,)), (0.8,(0.10,0.13)),(1.1,(0.10,0.14,0.11))]:
    c = predicted(a, es)
    errors = []
    for t in (60,100,300,1000,3000,10000,100000):
        v = laplace_prefactor(t,a,es)
        e = abs(v/c-1)
        errors.append(e)
        assert math.isfinite(v) and v > 0
        count += 2
    assert errors[-1] < 0.005, (a,es,errors)
    assert errors[-1] < errors[0]
    count += 2
    print(f'alpha0={a:.1f}; dimension={len(es)}; Hessian prefactor={c:.9f}; '
          f'relative error at log(n)=100000: {errors[-1]:.8f}')

# A marked two-regime mixture: the two quadratic minima contribute linearly.
for weights in [(0.25,0.75),(0.6,0.4)]:
    a = 1.0
    coeff = weights[0]*predicted(a,(0.2,)) + weights[1]*predicted(a,(0.35,))
    for t in (3000, 100000):
        approx = (weights[0]*laplace_prefactor(t,a,(0.2,))
                  +weights[1]*laplace_prefactor(t,a,(0.35,)))
        assert abs(approx/coeff-1)<0.015
        count += 1
    print(f'two-regime weights={weights}, limiting coefficient={coeff:.9f}')

# The exact scale identity n*b_n^(-alpha0)=(log n)^(d/2), using logs only.
for d in (1,2,3):
    for a in (0.7,1.1,1.7):
        for t in (20,200,2000):
            log_b=(t-0.5*d*math.log(t))/a
            assert abs((t-a*log_b)-0.5*d*math.log(t))<1e-11
            count += 1
print(f'PASS: {count} deterministic saddlepoint/normalization checks')
