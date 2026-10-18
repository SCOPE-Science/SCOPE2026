#!/usr/bin/env python3
"""Independent numerical checks of Euclidean perimeter deficits for random convex chains.
Requires Python 3.10+ and SciPy. Run: python CHECK.py
All identities and bounds are proved analytically in RESULT.md; this program tests instances.
"""
import math
import random
from scipy.integrate import quad

C = math.gamma(.75)**2/2
A = math.gamma(.75)**2/(2*math.gamma(1.5))


def baseline(n):
    return C * math.exp(math.lgamma(n+1)-math.lgamma(n+1.5))


def coeff(k):
    # 2 * (3/2)_k * (2k+1)! / [k! (4k+3)]
    return 2 * math.exp(math.lgamma(k+1.5)-math.lgamma(1.5)+math.lgamma(2*k+2)-math.lgamma(k+1)-math.log(4*k+3))


def inverse_factorial_term(n,k):
    return coeff(k) * math.exp(math.lgamma(n+1)-math.lgamma(n+2*k+3))


def sum_bound(n,m):
    return baseline(n)-sum((-1)**k*inverse_factorial_term(n,k) for k in range(m+1))


def exact_delta_by_support(n):
    # Direct Cauchy-support formula, integrating all negative normals and the cap-survival probability.
    def integral_t(theta):
        a,b=math.cos(theta),math.sin(theta)
        if a==0 or b==0:
            return 0.
        s=min(a,b)
        return quad(lambda t:(1-t*t/(a*b))**n,0.,s,epsabs=2e-12)[0]
    return 2*quad(integral_t,0.,math.pi/4,epsabs=3e-11,limit=200)[0]


def hull_perimeter(points):
    p=sorted(set(points))
    if len(p)==2:
        return 2*math.dist(p[0],p[1])
    def cross(o,a,b):
        return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    lo=[]
    for x in p:
        while len(lo)>1 and cross(lo[-2],lo[-1],x)<=0:lo.pop()
        lo.append(x)
    hi=[]
    for x in reversed(p):
        while len(hi)>1 and cross(hi[-2],hi[-1],x)<=0:hi.pop()
        hi.append(x)
    poly=lo[:-1]+hi[:-1]
    return sum(math.dist(poly[i],poly[(i+1)%len(poly)]) for i in range(len(poly)))


def sample_triangle(rng):
    a,b=rng.random(),rng.random()
    if a+b>1: a,b=1-a,1-b
    return a,b


def monte_carlo(n,runs,seed):
    rng=random.Random(seed)
    v=[]
    for i in range(runs):
        points=[(1.,0.),(0.,1.)]+[sample_triangle(rng) for _ in range(n)]
        v.append(hull_perimeter(points))
    mu=sum(v)/runs
    sd=math.sqrt(sum((x-mu)**2 for x in v)/(runs-1))
    return mu,sd/math.sqrt(runs)


def main():
    print('n direct_delta series_bounds[low,high] abs_gap')
    for n in [0,1,2,3,5,10,30,100]:
        value=exact_delta_by_support(n)
        low=sum_bound(n,0)
        high=sum_bound(n,1)
        tight=sum_bound(n,2)
        assert low-2e-12 < value < high+2e-12,(n,value,low,high)
        assert tight-2e-12 < value < high+2e-12
        error=inverse_factorial_term(n,3)
        assert high-value>0 and high-value<inverse_factorial_term(n,2)+1e-12
        assert abs(value-tight)<error+1e-12,(n,value,tight,error)
        print(n, format(value,'.12g'),f'[{low:.12g},{high:.12g}]', f'{abs(value-tight):.3g}')

    exact_zero=2-math.sqrt(2)
    assert abs(exact_delta_by_support(0)-exact_zero)<2e-11
    print('zero-point deterministic check',exact_zero)
    n=1
    # At one point the perimeter is base plus the two random edge lengths; independent 2D area quadrature.
    direct_edge=2 * quad(lambda x: quad(lambda y: math.hypot(1-x,y),0.,1-x,epsabs=2e-12)[0],0.,1.,epsabs=2e-12)[0]
    independent_p=math.sqrt(2)+2*direct_edge
    from_cauchy=2+math.sqrt(2)-exact_delta_by_support(1)
    assert abs(independent_p-from_cauchy)<1e-10,(independent_p,from_cauchy)
    exact_one=(5*math.sqrt(2)+2*math.asinh(1))/3
    assert abs(independent_p-exact_one)<1e-10
    print('one-point independent triangle-edge integral and exact asinh formula',independent_p)

    for n,runs in [(1,8000),(3,6000),(12,4000),(50,4000)]:
        observed,se=monte_carlo(n,runs,52379+n)
        predicted=2+math.sqrt(2)-exact_delta_by_support(n)
        print(f'MC n={n} runs={runs} observed={observed:.8f} predicted={predicted:.8f} SE={se:.6f}')
        assert abs(observed-predicted)<6*se+0.001

    for n in [100,1000,10000,100000]:
        correction=baseline(n)-inverse_factorial_term(n,0)+inverse_factorial_term(n,1)
        asym=(C/math.sqrt(n)-3*C/(8*n**1.5)-2/(3*n*n))
        ratio=abs(correction-asym)*n**2.5
        assert ratio<3,ratio
        print(f'asym n={n} corrected={correction:.11g} error_scaled_n^2.5={ratio:.6g}')
    print('CHECKER PASS: support integrals, signed factorial bounds, independent edge integral, Monte Carlo, and asymptotics')

if __name__=='__main__':main()
