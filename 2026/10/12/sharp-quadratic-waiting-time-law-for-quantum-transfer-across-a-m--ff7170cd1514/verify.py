#!/usr/bin/env python3
"""Finite arithmetic and independent matrix checks for a defective-clique quantum walk."""
import cmath
import math


def adjacency(n):
    return [[int(i != j and {i, j} != {0, 1}) for j in range(n)] for i in range(n)]


def mv(a, v):
    return [sum(x*y for x,y in zip(row, v)) for row in a]


def direct_amplitude(n, t, terms=140):
    a = adjacency(n)
    term = [complex(int(i == 0)) for i in range(n)]
    acc = term.copy()
    for k in range(1, terms):
        term = [1j*t*x/k for x in mv(a,term)]
        acc = [v+w for v,w in zip(acc,term)]
    return acc[1]


def closed_amplitude(n,t):
    r=n-2;s=n-3;d=math.sqrt((n+1)**2-8)
    wp=(d-s)/(2*d)
    f=wp*cmath.exp(1j*t*(s+d)/2)+(1-wp)*cmath.exp(1j*t*(s-d)/2)
    return (f-1)/2


block_count=0
matrix_count=0
lower_count=0
witness_count=0
for n in range(4,41):
    a=adjacency(n)
    r=n-2;s=n-3;delta=(n+1)**2-8
    assert n*n < delta < (n+1)**2
    assert delta-s*s == 8*r
    # Use the unnormalized three-dimensional invariant basis a,b,c.
    anti=[1,-1]+[0]*r
    sym=[1,1]+[0]*r
    core=[0,0]+[1]*r
    assert mv(a,anti)==[0]*n
    assert mv(a,sym)==[2*x for x in core]
    assert mv(a,core)==[r*b+s*c for b,c in zip(sym,core)]
    block_count+=1
    if n<=17:
        for t in [0.03,0.14,0.27,0.41]:
            assert abs(direct_amplitude(n,t)-closed_amplitude(n,t))<2e-11
            matrix_count+=1
    d=math.sqrt(delta);alpha=d/s;wp=(d-s)/(2*d)
    for j in range(60):
        t=(1+j*j*0.271)/(3+n*0.25)
        failure=1-abs(closed_amplitude(n,t))**2
        explicit_lower=2*wp/(s*s*(1+alpha*alpha)*(d*s*t/math.pi+d+s)**2)
        assert failure+1e-12>=explicit_lower
        lower_count+=1
    # Concrete finite-wait witnesses at the prescribed arithmetic times.
    beta=(alpha-1)/2
    for N in [100,1000,5000]:
        err,k=min((abs((k*beta)%1-0.5),k) for k in range(1,N+1))
        t=2*math.pi*k/s
        assert t<=2*math.pi*N/s+1e-8
        assert 1-abs(closed_amplitude(n,t))**2<=2*math.pi**2*err*err+1e-10
        witness_count+=1
print('VERIFY_OK exact_block_checks=%s independent_exponential_checks=%s explicit_lower_checks=%s target_phase_witnesses=%s' % (block_count,matrix_count,lower_count,witness_count))
