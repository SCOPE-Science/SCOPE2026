"""Reproducible finite checks for the sign-split Euclidean norm theorem.

Finite numerical checks supplement (and do not replace) the analytic proof.
Run: python3 checker.py
"""
import math, random


def bnorm2(v):
    return max(sum(x*x for x in v if x>0), sum(x*x for x in v if x<0))


def quadratic(v,t):
    return sum(x*x for x in v)+t*sum(v)**2


def lower(n,t):
    return (1+n*t)/(1+(n-1)*t)


def upper(n,t):
    c=(math.sqrt(n-1)-1)**2
    return max(1+n*t, 2+c*t)


def optimum(n):
    c=(math.sqrt(n-1)-1)**2
    t_cross=1/(2*math.sqrt(n-1))
    if n <= 4:
        t=t_cross
    elif n >= 7:
        t=0.0
    else:
        # Stable quadratic root of (c-2)+2c(n-1)t+n c(n-1)t*t=0.
        t=(2*(2-c))/(2*c*(n-1)+math.sqrt((2*c*(n-1))**2+4*n*c*(n-1)*(2-c)))
        t=2*(2-c)/(2*c*(n-1)+math.sqrt((2*c*(n-1))**2+4*n*c*(n-1)*(2-c)))
    return t, upper(n,t)/lower(n,t)


def main():
    r = random.Random(314159)
    for n in range(2, 11):
        tstar, d2 = optimum(n)
        if n == 5:
            assert abs(tstar-0.1)<1e-12
            assert abs(d2-49/25)<1e-12
        if n >= 7:
            assert tstar == 0.0 and d2 == 2
        for t in [0,0.025,0.1,0.2,0.5,1.0,2.0]:
            l,u = lower(n,t),upper(n,t)
            assert l<=u+1e-11
            # Independent direct evaluation at random signed vectors.
            for _ in range(6000):
                v=[r.gauss(0,1) for _ in range(n)]
                ratio=quadratic(v,t)/bnorm2(v)
                assert l-1e-9<=ratio<=u+1e-9,(n,t,v,l,u,ratio)
            neg=-t/(1+(n-1)*t)
            witness=[1]+[neg]*(n-1)
            assert abs(quadratic(witness,t)/bnorm2(witness)-l)<1e-9,(n,t)
            ones=[1/math.sqrt(n)]*n
            mixed=[1/math.sqrt(n-1)]*(n-1)+[-1]
            assert abs(max(quadratic(ones,t)/bnorm2(ones),quadratic(mixed,t)/bnorm2(mixed))-u)<1e-9
        # Scalar independent brute-grid optimization
        grid_best=min(upper(n,j/10000)/lower(n,j/10000) for j in range(5001))
        assert grid_best>=d2-1e-8, (n,grid_best,d2)
        assert grid_best<=d2+5e-4, (n,grid_best,d2)
        print(f'n={n} optimal_t={tstar:.12g} d_squared={d2:.12g} d={math.sqrt(d2):.12g}')
    print('Finite tests passed; analytically certified statements require the proof.')

if __name__=='__main__':
    main()
