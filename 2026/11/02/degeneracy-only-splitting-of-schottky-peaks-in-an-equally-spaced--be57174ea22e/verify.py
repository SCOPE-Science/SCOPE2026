"""Independent finite checks for an equispaced three-level heat-capacity theorem.

Run with Python 3.10+ and no third-party packages.
Finite arithmetic corroborates, but does not prove, the uniform theorem.
"""
import math
from fractions import Fraction


def direct(m, x):
    # Rescale all weights to avoid underflow at the two temperature scales.
    logs = [0.0, 2 * math.log(m) - x, 3 * math.log(m) - 2 * x]
    shift = max(logs)
    w = [math.exp(v - shift) for v in logs]
    s = sum(w)
    p = [v / s for v in w]
    mu = sum(j * p[j] for j in range(3))
    var = sum((j - mu) ** 2 * p[j] for j in range(3))
    skew = sum((j - mu) ** 3 * p[j] for j in range(3))
    return x * x * var, x * (2 * var - x * skew)


def algebraic(m, x):
    logs = [0.0, 2 * math.log(m) - x, 3 * math.log(m) - 2 * x]
    # Tests only use moderate exponents, and here the unscaled polynomial is independent.
    b, c = math.exp(logs[1]), math.exp(logs[2])
    z = 1 + b + c
    p = b + 4 * c + b * c
    q = (c - 1) * (b*b - b*c - b - 8*c)
    return x*x*p/z**2, x*(2*p*z-x*q)/z**3


def bisection(m, left, right, n=90):
    fa = direct(m, left)[1]
    fb = direct(m, right)[1]
    assert fa*fb < 0
    for _ in range(n):
        mid = (left + right)/2
        fmid = direct(m, mid)[1]
        if fmid == 0:
            return mid
        if fmid*fa > 0:
            left, fa = mid, fmid
        else:
            right, fb = mid, fmid
    return (left + right)/2


def check():
    tests = 0
    bound1 = Fraction(5, 11)*(1-Fraction(9,256))*(1-Fraction(11,160))/((1+Fraction(21,256))*(1+Fraction(3,256)))
    bound2 = Fraction(5,11)*(1-Fraction(9,16384))/((1+Fraction(117,16384))*(1+Fraction(9,16384)))
    assert bound1 > Fraction(1,3) and bound2 > Fraction(1,3)
    tests += 2
    for m in (256, 512, 1000, 4096, 10000, 100000):
        L = math.log(m)
        checkpoints = (L, L+1, 1.5*L, 2*L+1)
        expected = (1,-1,1,-1)
        for x, sign in zip(checkpoints, expected):
            f = direct(m,x)[1]
            assert sign*f>0, (m,x,f)
            tests+=1
        hot = bisection(m,L,L+1)
        middle = bisection(m,L+1,1.5*L)
        cold = bisection(m,1.5*L,2*L+1)
        assert hot < middle < cold
        assert direct(m,hot)[0]>direct(m,middle)[0]
        assert direct(m,cold)[0]>direct(m,middle)[0]
        tests+=3
        for x in [0.2,0.5,L-0.3,L+0.2,L+1,L+1.7,1.5*L,1.8*L,2*L+0.2,2*L+1,3*L]:
            c1,f1=direct(m,x)
            c2,f2=algebraic(m,x)
            assert abs(c1-c2) < 1e-9*(1+abs(c1))
            assert abs(f1-f2) < 1e-9*(1+abs(f1))
            h=2e-5
            fd=(direct(m,x+h)[0]-direct(m,x-h)[0])/(2*h)
            assert abs(fd-f1) < 1e-6*(1+abs(f1)),(m,x,fd,f1)
            tests+=3
        xmid=1.5*L
        exact=4.5*L*L/(math.sqrt(m)+2)
        assert abs(direct(m,xmid)[0]-exact)<1e-9*(1+exact)
        tests+=1
    for m in (10**4,10**5,10**6,10**8):
        L=math.log(m)
        hot=bisection(m,L,L+1)
        cold=bisection(m,1.5*L,2*L+1)
        assert abs((hot-L)*L-4) < 2
        assert abs((cold-2*L)*L-2) < 0.2
        tests+=2
    print('PASS: {} independent arithmetic, moment, derivative, and branch checks'.format(tests))
    print('rational derivative-ratio lower bounds:',str(bound1),str(bound2))

if __name__=='__main__':
    check()
