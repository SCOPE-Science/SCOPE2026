#!/usr/bin/env python3
import math

# Check the two algebraic optimizations on a deterministic grid.
for a in [0.0, 0.1, 1.0, 7.5]:
    for c in [0.0, 0.2, 2.0, 11.0]:
        # Coherent-information substitution: s=sqrt(L/n), with s<=1/2.
        for s in [1e-6, 0.01, 0.1, 0.25, 0.5]:
            lhs = a*s + c*s*s + (1.0+s)/s * (s*s)
            rhs = (a+1.0)*s + (c+1.0)*s*s
            if abs(lhs-rhs) > 1e-12 * max(1.0, abs(rhs)):
                raise SystemExit('coherent substitution failed')

        K = a+c+1.0
        for frac in [1e-8, 1e-5, 1e-3, 0.05, 0.2, 0.5, 1.0]:
            Delta = frac*K
            t = Delta/(2.0*K)
            if not (0.0 < t <= 0.5 + 1e-15):
                raise SystemExit('inadmissible t')
            cost = a*t + c*t*t
            if cost > Delta/2.0 + 1e-12*max(1.0, Delta):
                raise SystemExit('Taylor-cost inequality failed')
            if t/(1.0+t) + 1e-15 < Delta/(3.0*K):
                raise SystemExit('fraction inequality failed')
            lower = t/(1.0+t) * (Delta-cost)
            if lower + 1e-15 < Delta*Delta/(6.0*K):
                raise SystemExit('fidelity exponent inequality failed')

print('VERIFY_OK')
