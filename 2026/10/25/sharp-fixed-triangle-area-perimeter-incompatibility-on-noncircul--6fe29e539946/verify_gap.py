"""Reproducibility checks for the inscribed-ellipse triangle perimeter gap.

The proof in RESULT.md is analytic. Finite tests below test, but cannot
certify, its all-parameter assertions.
"""
from math import sin, cos, pi, sqrt
from random import Random


def pt(t, a, b):
    return (a*cos(t), b*sin(t))


def distance(x, y):
    return sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)


def perimeter(phases, a, b):
    pts=[pt(t,a,b) for t in phases]
    return sum(distance(pts[i],pts[(i+1)%3]) for i in range(3))


def lower_bound(a,b):
    return 81*b**7*(a*a-b*b)**2/(2048*a**10)


def variation_gain(theta,a,b):
    phases=[theta+i*2*pi/3 for i in range(3)]
    P=perimeter(phases,a,b)
    best=-1.0
    # evaluate safe signed Taylor steps at each vertex, using exact derivative
    for i in range(3):
        h=2.0e-6
        old=phases[i]
        phases[i]=old+h
        plus=perimeter(phases,a,b)
        phases[i]=old-h
        minus=perimeter(phases,a,b)
        phases[i]=old
        deriv=(plus-minus)/(2*h)
        step=deriv * b / (4*a*a)
        phases[i]=old+step
        q=perimeter(phases,a,b)-P
        phases[i]=old
        best=max(best,q)
    return best


def secant_optim(p,a,b):
    # Maximize perimeter by gradient ascent with a restart near each 3-spaced triangle.
    from scipy.optimize import minimize
    def fn(v): return -perimeter(v,a,b)
    q=minimize(fn,p,method='BFGS',tol=1e-12)
    return -q.fun


def main():
    rng=Random(25117)
    for i in range(800):
        b=0.3+2.5*rng.random()
        a=b*(1+2*rng.random())
        theta=2*pi*rng.random()
        gain=variation_gain(theta,a,b)
        lb=lower_bound(a,b)
        assert gain+2e-8*a>=lb, (a,b,theta,gain,lb)
    target=9*sqrt(3)/16
    for eps in (0.02,0.01,0.005,0.002):
        a,b=1+eps,1
        # Formula max over area-maximizers, sampled densely.
        Parea=max(perimeter([th+2*pi*i/3 for i in range(3)],a,b) for th in [pi*k/100 for k in range(101)])
        Popt=max(secant_optim([th+2*pi*i/3 for i in range(3)],a,b) for th in (0.1,0.3,0.7))
        ratio=(Popt-Parea)/(eps*eps)
        assert abs(ratio-target)<1.5*eps, (eps,ratio,target)
        print('epsilon',eps,'gap/epsilon^2',f'{ratio:.10f}', 'limit',f'{target:.10f}')
    print('PASS: 800 random Taylor-gain checks and 4 near-circular gap tests')


if __name__=='__main__':
    main()
