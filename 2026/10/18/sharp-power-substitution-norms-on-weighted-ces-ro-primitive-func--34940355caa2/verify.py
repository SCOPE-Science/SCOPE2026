"""Independent-input numerical and exact-algebra checks for power substitution bounds.

Run using Python 3.10+; no third-party packages. The infinite-dimensional
claims are established by the accompanying proof, not these finite checks.
"""
from fractions import Fraction
from math import isfinite


def simpson(fun, a, b, steps=400):
    if b <= a:
        return 0.0
    h = (b-a)/steps
    total = fun(a)+fun(b)
    for k in range(1,steps):
        total += (4 if k%2 else 2)*fun(a+k*h)
    return total*h/3


def interval_norm_p(l, r, p, sigma):
    return (simpson(lambda x: ((x-l)/x**sigma)**p, l, r) +
            simpson(lambda x: ((r-l)/x**sigma)**p, r, 1.0))


def left_norm_p(r, p, sigma):
    first = r**(1+p*(1-sigma))/(1+p*(1-sigma))
    if abs(p*sigma-1)<1e-12:
        from math import log
        second = r**p*log(1/r)
    else:
        second = r**p*(1-r**(1-p*sigma))/(1-p*sigma)
    return first+second


def main():
    checks=0
    for j in range(1,50):
        r=Fraction(j,100)
        # Integral of the primitive of the indicator (0,r), squared.
        assert r*r - Fraction(2,3)*r**3 == r*r*r/Fraction(3)+r*r*(1-r)
        # Integral of the normalized primitive, squared.
        assert 2*r-r*r == r + r*r*(1/r-1)
        checks+=2
    for p in (1,2,3,4):
        for sigma in (0.0,0.5,1.0):
            for alpha in (0.3,0.5,0.8,1.0):
                bound=alpha**(-1-1/p)
                for l,r in ((0.10,0.25),(0.35,0.6),(0.73,0.94)):
                    inp=interval_norm_p(l,r,p,sigma)
                    out=interval_norm_p(l**(1/alpha),r**(1/alpha),p,sigma)
                    actual=(out/inp)**(1/p)
                    assert isfinite(actual) and actual<=bound*(1+1e-8),(p,sigma,alpha,l,r,actual,bound)
                    checks+=1
                if alpha<1.0:
                    eps=0.0001
                    inp=interval_norm_p(1-eps,1.0,p,sigma)
                    out=interval_norm_p((1-eps)**(1/alpha),1.0,p,sigma)
                    actual=(out/inp)**(1/p)
                    assert abs(actual/bound-1)<0.002,(p,sigma,alpha,actual,bound)
                    checks+=1
            for alpha in (1.1,1.5,2.0):
                ratios=[]
                for r in (1e-3,1e-5,1e-7):
                    value=(left_norm_p(r**(1/alpha),p,sigma)/left_norm_p(r,p,sigma))**(1/p)
                    ratios.append(value)
                    checks+=1
                assert ratios[0]<ratios[1]<ratios[2],(p,sigma,alpha,ratios)
                checks+=1
    print(f"PASS: {checks} exact/numerical assertions; no external dependencies")


if __name__=='__main__':
    main()
