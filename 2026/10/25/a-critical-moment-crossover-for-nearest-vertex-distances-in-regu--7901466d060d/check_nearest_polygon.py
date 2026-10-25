#!/usr/bin/env python3
"""Reproducibility checks for moments of polygon-vertex proximity.

Only Python's standard library is needed. Numerical tests corroborate,
but do not replace, the exact Voronoi decomposition and limiting proofs.
"""
import math


def integrate(f, low, high, panels=12000):
    assert panels % 2 == 0
    step = (high-low)/panels
    value = f(low)+f(high)
    for i in range(1, panels):
        value += (4 if i % 2 else 2)*f(low+i*step)
    return value*step/3


def moment_formula(n, p):
    a = math.pi/n
    J = integrate(lambda x: math.sin(x)**(-p), a, math.pi/2)
    return (2/((p+1)*(p+2)))*(1+p*math.sin(a)**(p+1)/math.cos(a)*J)


def halton(index, base):
    v, factor = 0.0, 1.0/base
    while index:
        index, r = divmod(index, base)
        v += r*factor
        factor /= base
    return v


def projected_triangle_moments(n, powers=(0.5,1.0,2.0,3.0), samples=42000):
    """Independent 2D equal-area sampling, all nearest sites tested."""
    vertices = [(math.cos(2*k*math.pi/n), math.sin(2*k*math.pi/n)) for k in range(n)]
    x0,y0=vertices[0]
    x1,y1=vertices[1]
    sums=[0.0]*len(powers)
    for i in range(1,samples+1):
        u=math.sqrt(halton(i,2));v=halton(i,3)
        x=u*((1-v)*x0+v*x1)
        y=u*((1-v)*y0+v*y1)
        d=min(math.hypot(x-qx,y-qy) for qx,qy in vertices)
        for j,p in enumerate(powers): sums[j]+=d**p
    return [s/samples for s in sums]


def finite_checks():
    powers=(0.5,1.0,2.0,3.0)
    for n in (3,4,6,10,31):
        observed=projected_triangle_moments(n,powers)
        predicted=[moment_formula(n,p) for p in powers]
        for p,x,y in zip(powers,observed,predicted):
            assert abs(x-y)<0.00032, (n,p,x,y)
    print('INDEPENDENT_POLYGON_VORONOI_GEOMETRY_210000_SAMPLES_OK')
    for n in (3,4,6,10,31):
        a=math.pi/n
        target=1/6+math.sin(a)**2/3
        assert abs(moment_formula(n,2)-target)<2e-10
        mean=1/3+math.sin(a)**2/(3*math.cos(a))*math.log(1/math.tan(a/2))
        assert abs(moment_formula(n,1)-mean)<2e-10
    print('EXACT_FIRST_AND_SECOND_MOMENT_BENCHMARKS_OK')


def asymptotic_checks():
    for p in (0.25,0.5,0.8,1.0,1.5,2.0,3.0):
        n=6000
        a=math.pi/n
        # Finite-n checks of the first asymptotic terms. The convergence
        # rate is slow for exponents close to one from below.
        M=moment_formula(n,p)
        delta=M-2/((p+1)*(p+2))
        assert delta>0
        if p==1:
            expected=a*a*math.log(1/a)/3
            assert abs(delta/expected-1)<0.11
        elif p>1:
            expected=2*p*a*a/((p+2)*(p*p-1))
            assert abs(delta/expected-1)<0.10
        else:
            c=(p*math.sqrt(math.pi)*math.gamma((1-p)/2)/
               ((p+1)*(p+2)*math.gamma(1-p/2)))
            expected=c*a**(p+1)
            # The next term is O(a^2), not negligible near p=1.
            assert abs(delta/expected-1)<0.23
            J0=(math.sqrt(math.pi)*math.gamma((1-p)/2)/
                (2*math.gamma(1-p/2)))
            corrected_J=J0-a**(1-p)/(1-p)-p*a**(3-p)/(6*(3-p))
            corrected=(2*p/((p+1)*(p+2))*
                math.sin(a)**(p+1)/math.cos(a)*corrected_J)
            assert abs(delta/corrected-1)<0.0003
    print('THREE_REGIME_SCALING_EXPONENTS_AND_CONSTANTS_OK')

    for lam in (-1.5,0,1.5):
        # compact-lambda critical-window check at n=5000
        n=5000
        a=math.pi/n
        L=math.log(1/a)
        p=1+lam/L
        delta=moment_formula(n,p)-2/((p+1)*(p+2))
        scaling=(1-math.exp(-lam))/lam if lam else 1.0
        # The proven critical-window convergence has O(1/L) error.
        assert abs(delta/(a*a*L)-scaling/3)<0.12, (lam,delta)
    print('CRITICAL_WINDOW_CROSSOVER_FUNCTION_OK')


if __name__=='__main__':
    finite_checks()
    asymptotic_checks()
    print('ALL_NEAREST_VERTEX_MOMENT_CHECKS_OK')
