#!/usr/bin/env python3
import math
from itertools import product

# A Pauli channel has probabilities q=(q_I,q_X,q_Y,q_Z).
# Its signed Bloch contractions are the three linear combinations below.
def lambdas(q):
    q0,qx,qy,qz=q
    return (
        q0+qx-qy-qz,
        q0-qx+qy-qz,
        q0-qx-qy+qz,
    )

def concurrence(q):
    return max(0.0, 2.0*max(q)-1.0)

def predicted_from_singular_values(q):
    s=sorted((abs(x) for x in lambdas(q)), reverse=True)
    return max(0.0, (sum(s)-1.0)/2.0), s

# Exhaust a rational simplex grid. This is a finite consistency check, not a proof.
N=30
checked=0
for a in range(N+1):
    for b in range(N+1-a):
        for c in range(N+1-a-b):
            d=N-a-b-c
            q=(a/N,b/N,c/N,d/N)
            c_exact=concurrence(q)
            c_s,s=predicted_from_singular_values(q)
            assert abs(c_exact-c_s) < 2e-12, (q,c_exact,c_s,s)
            s1=s[0]
            upper=max(0.0,(3.0*s1-1.0)/2.0)
            assert c_exact <= upper+2e-12, (q,c_exact,upper)
            # Entanglement-breaking octahedron is equivalent to zero Bell concurrence.
            assert (sum(s) <= 1.0+2e-12) == (c_exact <= 2e-12), (q,s,c_exact)
            checked += 1

# Depolarizing channels attain the privacy-concurrence bound.
for eps in (0.0, math.log(2.0), 1.0, 2.0, 4.0):
    t=math.tanh(eps/2.0)
    p=1.0-t
    q=(1.0-3.0*p/4.0,p/4.0,p/4.0,p/4.0)
    c=concurrence(q)
    bound=max(0.0,(3.0*t-1.0)/2.0)
    assert abs(c-bound) < 2e-12, (eps,q,c,bound)
    if t < 1.0:
        eps_star=math.log((1.0+t)/(1.0-t))
        assert abs(eps_star-eps) < 2e-12, (eps,eps_star)

print('VERIFY_OK', checked)
