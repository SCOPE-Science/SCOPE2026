#!/usr/bin/env python3
import math


def closed_area(alpha, beta):
    vals = []
    for a in alpha:
        for b in beta:
            q = (a*b)**2
            vals.append((1-q*q+2*q*math.log(q))/(2*(1-q)**2))
    return sum(vals)/len(vals)


def simpson(f, a, b, n=120000):
    if n % 2:
        n += 1
    h = (b-a)/n
    total = f(a) + f(b)
    for k in range(1, n):
        total += (4 if k % 2 else 2) * f(a+k*h)
    return total*h/3


def boundary_area(alpha, beta):
    # Integrate on y=log R; tails beyond +/-18 are bounded well below tolerance
    aa = [a*a for a in alpha]
    bb = [b*b for b in beta]
    def integrand(y):
        R = math.exp(y)
        t = sum((b2*R)/(1+b2*R) for b2 in bb)/len(bb)
        minus_sp = sum(a2/(R+a2)**2 for a2 in aa)/len(aa)
        return t*minus_sp*R
    pure_below_area = simpson(integrand, -18.0, 18.0)
    return 0.5-pure_below_area


def hyperbola_area(r):
    # Source one-cell coexistence boundary:
    # 1-s-t+(1-r^{-2})st=0, so t=(1-s)/(1+(r^{-2}-1)s).
    k = r**-2 - 1.0
    def gap(s):
        t = (1-s)/(1+k*s)
        return 1-s-t
    return simpson(gap, 0.0, 1.0, n=120000)


def main():
    tests = [
        ([0.2,0.9],[0.2,0.9]),
        ([0.3,0.7],[0.4,0.8,0.9]),
        ([0.1,0.2,0.4],[0.5,0.6]),
    ]
    worst = 0.0
    for alpha,beta in tests:
        assert max(a*b for a in alpha for b in beta) < 1.0
        c = closed_area(alpha,beta)
        n = boundary_area(alpha,beta)
        err = abs(c-n)
        worst = max(worst,err)
        assert err < 2.0e-5, (alpha,beta,c,n,err)
    for r in (0.2,0.5,0.8):
        c = closed_area([r],[1.0])
        h = hyperbola_area(r)
        err = abs(c-h)
        worst = max(worst,err)
        assert err < 2.0e-8, (r,c,h,err)
    print('VERIFY_OK worst_abs_error={:.3e} sample_area={:.15f}'.format(
        worst, closed_area([0.2,0.9],[0.2,0.9])))

if __name__ == '__main__':
    main()
