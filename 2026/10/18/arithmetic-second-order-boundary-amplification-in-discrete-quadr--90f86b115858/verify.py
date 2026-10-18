#!/usr/bin/env python3
"""Reproduce exact endpoint-kernel and Bernoulli identities for quadratic grid least squares.

Uses only the Python standard library. Finite checks complement, but do not replace,
the analytic proof of the general identity and asymptotic limit set.
"""
from fractions import Fraction as F
from decimal import Decimal as D, localcontext


def b2(t):
    return t*t - t + D(1)/D(6)


def b3(t):
    return t*t*t - D(3)*t*t/D(2) + t/D(2)


def frac(t):
    return t - (t // 1)


def exact_endpoint(m):
    h = F(1, m)
    mu2 = (1 + 2*h)/3
    mu4 = F(1, 5) + F(4, 5)*h + F(8, 15)*h*h - F(8, 15)*h*h*h
    variance = mu4-mu2*mu2
    a = (1-mu2)/variance
    b = 1/mu2
    c = 1-a*mu2
    xx = [-1 + F(2*j, m) for j in range(m+1)]
    kernel = [a*x*x+b*x+c for x in xx]
    return a,b,c,mu2,mu4,variance,xx,kernel,sum(abs(x) for x in kernel)/F(m+1)


def bernoulli_endpoint(m):
    with localcontext() as ctx:
        ctx.prec = 85
        h = D(1)/D(m)
        disc = D(6)+D(6)*h-D(11)*h*h
        root = disc.sqrt()
        a = -(D(1)+D(3)*h)
        r_minus = (a-root)/D(5)
        r_plus = (a+root)/D(5)
        phase_minus = frac(D(m)*(D(1)+r_minus)/D(2))
        phase_plus = frac(D(m)*(D(1)+r_plus)/D(2))
        den = (D(1)+h)*(D(1)+D(2)*h)*(D(1)+D(3)*h)
        value = (D(1) + (D(2)*disc*root/D(25)
                 -D(6)*h*h*root*(b2(phase_minus)+b2(phase_plus))
                 +D(20)*h*h*h*(b3(phase_plus)-b3(phase_minus)))/den)
        return +value


def run():
    checks = 0
    for m in range(2,121):
        a,b,c,mu2,mu4,v,x,k,e = exact_endpoint(m)
        h = F(1,m)
        assert mu2 == (1+2*h)/3; checks += 1
        assert v == F(4,45)*(1-h)*(1+2*h)*(1+3*h); checks += 1
        assert a == F(15,2)/((1+2*h)*(1+3*h)); checks += 1
        assert b == 3/(1+2*h); checks += 1
        assert c == (-3+6*h)/(2*(1+3*h)); checks += 1
        assert sum(xj*xj for xj in x)/F(m+1) == mu2; checks += 1
        assert sum(xj**4 for xj in x)/F(m+1) == mu4; checks += 1
        assert sum(k)/F(m+1) == 1; checks += 1
        for xj, kj in zip(x,k):
            independent = 1 + xj/mu2+(1-mu2)*(xj*xj-mu2)/v
            assert kj == independent; checks += 1
        with localcontext() as ctx:
            ctx.prec = 85
            erational = D(e.numerator)/D(e.denominator)
            assert abs(erational-bernoulli_endpoint(m)) < D('1e-73')
            checks += 1
    with localcontext() as ctx:
        ctx.prec = 85
        sq6 = D(6).sqrt()
        C = D(1)+D(12)*sq6/D(25)
        a = -D(54)*sq6/D(25)
        c2 = D(327)*sq6/D(50)
        for m in [1000,2000,4000,8000,16000,32000]:
            h = D(1)/D(m)
            d = D(6)+D(6)*h-D(11)*h*h
            r_minus = (-(D(1)+D(3)*h)-d.sqrt())/D(5)
            r_plus = (-(D(1)+D(3)*h)+d.sqrt())/D(5)
            theta_minus=frac(D(m)*(D(1)+r_minus)/D(2))
            theta_plus=frac(D(m)*(D(1)+r_plus)/D(2))
            S=b2(theta_minus)+b2(theta_plus)
            W=D(m)**2*(bernoulli_endpoint(m)-C-a/D(m))
            assert abs(W-(c2-D(6)*sq6*S)) < D(500)/D(m);checks+=1
            assert D(227)*sq6/D(50)-D(1) < W < D(377)*sq6/D(50)+D(1);checks+=1
    print(f'PASS: {checks} exact-rational and high-precision assertions')


if __name__=='__main__':
    run()
