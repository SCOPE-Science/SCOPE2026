"""Reproducibility checks for two-dimensional one-node log-determinant quadrature.
Runs on Python 3.10+ with no external dependencies.
The finite checks complement, rather than replace, the proof in RESULT.md.
"""
import math
from fractions import Fraction


def interval_h(x, n=170):
    """Enclose H(x) rigorously using finite rational Taylor sums.

    For 0<x<1: -log(1-x)=sum x^k/k, Li2(x)=sum x^k/k^2,
    log(1+x)=sum (-1)^(k+1)x^k/k.
    Tail bounds are geometric with k-denominators, respectively, and the
    alternating-series bound for the final series.
    """
    assert 0 < x < 1 and n % 2 == 0
    a = b = l = Fraction(0)
    p = Fraction(1)
    for k in range(1,n+1):
        p *= x
        a += p / k
        l += p / (k*k)
        b += (p/k if k%2 else -p/k)
    p *= x
    aa = p / ((n+1)*(1-x))
    ll = p / ((n+1)*(n+1)*(1-x))
    bb = p / (n+1)
    # even truncation of log(1+x) undershoots the exact sum.
    alo,ahi=a,a+aa
    blo,bhi=b,b+bb
    llo,lhi=l,l+ll
    return alo*blo + blo*blo/2 - lhi, ahi*bhi + bhi*bhi/2 - llo


def h_float(x):
    # Independent scalar series evaluation and closed-form elementary logs.
    term=x
    li=0.
    for k in range(1,4000):
        if k>1:term*=x
        li+=term/(k*k)
        if abs(term)<1e-17:break
    return -math.log1p(-x)*math.log1p(x)+.5*math.log1p(x)**2-li


def logcosh(t):
    return abs(t) + math.log1p(math.exp(-2*abs(t))) - math.log(2.)


def mse_sign(kappa):
    u=.5*math.log(kappa)
    return 4*logcosh(u)**2


def mse_sphere(kappa):
    u=.5*math.log(kappa)
    x=math.tanh(u/2)**2
    return mse_sign(kappa)-8*h_float(x)


def angular_moments(kappa,m=8192):
    target=math.log(kappa)
    s0=s1=s2=0.
    for j in range(m):
        theta=2*math.pi*(j+.5)/m
        v=2*math.log(kappa*math.cos(theta)**2+math.sin(theta)**2)
        s0+=1
        s1+=v
        s2+=(v-target)**2
    return s1/s0,s2/s0


def main():
    assert interval_h(Fraction(7778,10000))[1]<0
    assert interval_h(Fraction(7779,10000))[0]>0
    assertions=2
    for kappa in (1.001,2,16,64,128,256,512,1024,65536):
        u=.5*math.log(kappa)
        r=(math.sqrt(kappa)-1)/(math.sqrt(kappa)+1)
        c=((math.sqrt(kappa)+1)/2)**2
        mean=2*math.log(c)
        angular_mean,angular_risk=angular_moments(kappa)
        formula=mse_sphere(kappa)
        assert abs(angular_mean-mean)<1e-10*max(1,abs(mean))
        assert abs(angular_risk-formula)<1e-10*max(1,abs(formula))
        assert abs(mse_sign(kappa)-(2*math.log((kappa+1)/2)-math.log(kappa))**2)<1e-10*max(1,mse_sign(kappa))
        assert abs(8*h_float(r*r)-(mse_sign(kappa)-formula))<1e-10
        assertions+=4
    assert mse_sign(128)<mse_sphere(128)
    assert mse_sphere(256)<mse_sign(256)
    assertions+=2
    print('VERIFY_OK rational one-root bracket, 9 angular moment and risk comparisons,',assertions,'passed assertions')

if __name__=='__main__':main()
