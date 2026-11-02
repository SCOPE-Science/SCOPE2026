"""Standalone checks for an exact three-mode spectral-scaling theorem.

No external packages required. Exhaustive proof is in RESULT.md; these checks
validate key algebraic identities and independently sample parameter ranges.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose


def model(b, c, d, theta):
    assert b > c > 0 and 0 < d < sqrt(b) and theta > 0
    disc = sqrt((theta - b)**2 + 4*d*d*theta)
    hi = (theta + b + disc) / 2
    lo = (theta + b - disc) / 2
    return hi / min(c, lo)


def optimum(b, c, d):
    threshold = (b-c) / sqrt(b)
    if d <= threshold:
        th = c*(b-c)/(b-c-d*d)
        val = b/c + d*d/(b-c-d*d)
    else:
        th = b
        val = (sqrt(b)+d)/(sqrt(b)-d)
    return th, val


def exact_checks():
    n = 0
    b, c = F(4), F(1)
    for d, th, cond in [(F(1), F(3,2), F(9,2)),
                         (F(3,2), F(4), F(7)),
                         (F(8,5), F(4), F(9))]:
        # Upper block has trace th+b and determinant th*(b-d**2).
        trace, det = th+b, th*(b-d*d)
        if d <= F(3,2):
            lo = c
            hi = trace-c
        else:
            lo = b-d*F(2)  # sqrt(b)=2 for this exact example
            hi = b+d*F(2)
        assert hi+lo == trace
        assert hi*lo == det
        assert hi / min(c, lo) == cond
        assert (th == b or (th-c)*(b-c) == d*d*th)
        n += 5
    for b in range(2, 17):
        for c in range(1, b):
            B,C=F(b),F(c)
            # At d=(b-c)/sqrt(b), theta=b, and low eigenvalue=c.
            dc2=(B-C)**2/B
            assert C*(B-C)/(B-C-dc2) == B
            assert dc2 < B
            n += 2
    return n


def floating_checks():
    n = 0
    for b,c in [(4.,1.),(2.,1.),(9.,8.),(9.,0.01),(13.,3.),(1.3,0.2)]:
        thcrit=(b-c)/sqrt(b)
        samples=[0.01*sqrt(b),0.2*thcrit,0.99*thcrit,
                 thcrit, min(1.01*thcrit,.999*sqrt(b)),
                 .95*sqrt(b)]
        for d in samples:
            if not 0 < d < sqrt(b):
                continue
            opt, target = optimum(b,c,d)
            got=model(b,c,d,opt)
            assert isclose(got,target,rel_tol=3e-10,abs_tol=3e-10),(b,c,d,opt,got,target)
            n += 1
            # Search many scales on both sides and on an independent log grid.
            for shift in [-4,-2,-1,-0.1,-.0001,.0001,.1,1,2,4]:
                test=opt*exp(shift)
                assert model(b,c,d,test) > got*(1-2e-10), (b,c,d,opt,test)
                n += 1
            for j in range(101):
                test=exp(log(opt)-7+j*14/100)
                assert model(b,c,d,test) >= got*(1-2e-10), (b,c,d,opt,test)
                n+=1
    return n


if __name__ == '__main__':
    ne=exact_checks()
    nf=floating_checks()
    print(f'PASS: {ne} exact-fraction identities and {nf} independent numerical comparisons')
