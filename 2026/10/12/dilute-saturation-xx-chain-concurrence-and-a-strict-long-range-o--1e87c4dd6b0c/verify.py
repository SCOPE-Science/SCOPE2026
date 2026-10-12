"""Reproducible finite-covariance and rigorous scalar-bound checks for a sine-kernel concurrence limit."""
import itertools, math
from fractions import Fraction
import numpy as np


def cov(j, nu):
    return nu * float(np.sinc(nu * j))


def wick_expansion(r, nu):
    total = 0.
    for m in range(r):
        for inds in itertools.combinations(range(1, r), m):
            x = [0, *inds]
            y = [r, *inds]
            a = np.array([[cov(i-j, nu) for j in y] for i in x])
            total += (-2)**m * np.linalg.det(a)
    return total


def block_determinant(r, nu):
    g = np.array([[cov(i-j, nu) for j in range(1, r)] for i in range(1, r)])
    a = np.eye(r-1)-2*g
    u = np.array([cov(i,nu) for i in range(1,r)])
    v = np.array([cov(r-i,nu) for i in range(1,r)])
    return np.linalg.det(a)*(cov(r,nu)+2*u @ np.linalg.solve(a,v))


def scaled_concurrence(r,nu):
    z = block_determinant(r,nu)
    b = cov(r,nu)
    p11=nu*nu-b*b
    p00=(1-nu)**2-b*b
    return max(0.,(abs(z)-math.sqrt(p00*p11))/nu)


def limiting_minor(s, n):
    h=s/n
    x=np.arange(1,n)*h
    g=h*np.sinc(x[:,None]-x[None,:])
    a=np.eye(n-1)-2*g
    u=h*np.sinc(x)
    v=h*np.sinc(s-x)
    return np.linalg.det(a)*(float(np.sinc(s))+2*u@np.linalg.solve(a,v)/h)


def check():
    for nu in (0.07,0.19,0.35):
        for r in range(2,7):
            a=wick_expansion(r,nu)
            b=block_determinant(r,nu)
            assert abs(a-b)<1e-12,(nu,r,a,b)
    # Explicit rational interval bounds; elementary elementary sin alternating series
    pi_lo=Fraction(314159,100000); pi_hi=Fraction(314160,100000)
    sqrt2_lo=Fraction(14142,10000)
    k_lo=Fraction(6984,10000)
    # sin(sqrt(2))/sqrt(2)=sum_{n>=0}(-1)^n 2^n/(2n+1)!; lower at odd truncation
    k_partial=sum((Fraction((-2)**j,math.factorial(2*j+1)) for j in range(8)),Fraction(0))
    assert k_partial>k_lo
    I_lo=k_lo*56*sqrt2_lo/(225*pi_hi)
    tail_hi=Fraction(800,1485)/pi_lo**2
    # upper bound threshold sqrt(1-k^2)< 716/1000 by a strict rational square comparison
    thresh_hi=Fraction(716,1000)
    assert 1-k_lo*k_lo < thresh_hi*thresh_hi
    assert k_lo+I_lo-tail_hi>thresh_hi
    s=math.sqrt(2)/math.pi
    val=limiting_minor(s,120)
    threshold=math.sqrt(1-math.sin(math.sqrt(2))**2/2)
    assert val>threshold
    for r in (80,140,240):
        h=(r-1)**2/((r-1)**2+1)
        nu=math.acos(h)/math.pi
        assert scaled_concurrence(r,nu)>0.03,(r,scaled_concurrence(r,nu))
    print('VERIFY_OK Wick_expansions=15 scalar_rational_certificate=passed finite_distance_counterchecks=3')
    print('certificate_lower_gap_min=',float(k_lo+I_lo-tail_hi-thresh_hi))
    print('s0=',s,'Fredholm_minor_N120=',val,'threshold=',threshold)

if __name__=='__main__':check()
