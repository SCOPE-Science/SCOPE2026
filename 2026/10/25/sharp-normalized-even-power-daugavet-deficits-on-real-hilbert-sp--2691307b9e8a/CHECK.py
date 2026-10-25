"""Numerical sanity checks for the normalized even-power Hilbert rank-one Daugavet deficit.

Finite arithmetic checks only; all quantified assertions are proved analytically.
"""
import math


def deficit(a, m):
    if not 0.0 <= a <= 1.0 or m < 2 or m % 2:
        raise ValueError("a in [0,1] and an even m>=2 are required")
    b = a ** (m - 1)
    return 0.5 * (2.0 + b - math.sqrt(4.0 + 4.0 * a**m + b*b))


def matrix_singular_norm(a, m):
    # Gram invariants of [[1+a^m, a^(m-1)*sqrt(1-a^2)], [0,1]].
    p = 1.0 + a**m
    q = a ** (m - 1) * math.sqrt(max(0.0, 1.0 - a*a))
    # Stable 2-by-2 singular value identity (avoids subtracting close Gram eigenvalues).
    return 0.5 * (math.hypot(p+1.0, q) + math.hypot(p-1.0, q))


def golden_maximize(f, lo, hi, loops=140):
    ratio=(math.sqrt(5)-1)/2
    x=hi-ratio*(hi-lo)
    y=lo+ratio*(hi-lo)
    for _ in range(loops):
        if f(x) < f(y):
            lo=x
            x=y
            y=lo+ratio*(hi-lo)
        else:
            hi=y
            y=x
            x=hi-ratio*(hi-lo)
    a=(lo+hi)/2
    return a,f(a)


def lambert_positive(z):
    lo,hi=0.0,1.0
    for _ in range(200):
        mi=(lo+hi)/2
        if mi*math.exp(mi)<z:lo=mi
        else:hi=mi
    return (lo+hi)/2


def main():
    for m in (2,4,6,10,20,100,400):
        for a in (0.0,0.01,0.1,1/math.sqrt(5),0.63,0.9,0.995,1.0):
            norm=matrix_singular_norm(a,m)
            direct=1.0+a**(m-1)-norm
            assert abs(direct-deficit(a,m)) < 5e-13,(m,a,direct,deficit(a,m))
    exact=1-2/math.sqrt(5)
    a,f=golden_maximize(lambda x:deficit(x,2),0.0,1.0)
    assert abs(a-1/math.sqrt(5))<1e-7
    assert abs(f-exact)<1e-12
    gamma=lambert_positive(1/(2*math.e))
    assert abs(gamma-0.157184951483814)<1e-10
    print('square overlap, exact gap:', a, exact)
    print('Lambert limiting m * maximum:',gamma)
    for m in (10,100,1000):
        a,f=golden_maximize(lambda c:deficit(1-c/m,m),0.0,min(m,8.0))
        print('even degree, m*maxgap, m*(1-a):',m,m*f,a)
        if m==1000:
            assert abs(m*f-gamma)<0.003 and abs(a-(1+gamma))<0.02
    print('PASS: finite arithmetic and limiting-trend checks')


if __name__=='__main__':
    main()
