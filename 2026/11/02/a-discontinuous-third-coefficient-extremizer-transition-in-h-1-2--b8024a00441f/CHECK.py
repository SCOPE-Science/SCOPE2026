"""Reproducible exact-arithmetic checks for the cubic Hardy coefficient phase boundary.

The infinite-dimensional reduction and compactness arguments are in RESULT.md;
finite sampling here is only supplementary. Standard-library Python is sufficient.
"""
from fractions import Fraction as Q
from math import sqrt
from random import Random


def cubic_value(a, b, c, d, t):
    s = a*a + b*b + c*c + d*d
    assert s > 0
    return (a**4 + t * (4*a**3*d + 12*a*a*b*c + 4*a*b**3)) / (s*s)


def binomial_value(x, t):
    return (1 + 4*t*x) / (1 + x*x)**2


def binomial_optimum(t):
    if t == 0:
        return 1.0, 0.0
    x = (sqrt(1+12*t*t)-1)/(6*t)
    return binomial_value(x,t),x


def quartic(x):
    return 33*x**4+66*x*x-47*x+8


def quartic_derivative(x):
    return 132*x**3+132*x-47


def check():
    count = 0
    t = Q(47, 100)
    witness = cubic_value(18,6,5,5,t)
    assert witness == Q(1387044,1050625)
    assert witness-Q(33,25)==Q(219,1050625)>0
    count+=3

    # For Q(x)=33x^4+66x^2-47x+8, Q''(x)>=132 for x>=0.
    # Thus Q(x)>=Q(r)+Q'(r)(x-r)+66(x-r)^2, and the
    # right side has minimum Q(r)-Q'(r)^2/264 > 0.
    r=Q(8,25)
    certificate = quartic(r)-quartic_derivative(r)**2/264
    assert certificate == Q(4106602319,64453125000)>0
    count+=2

    # The elementary exact witness at the local-instability parameter.
    assert binomial_value(Q(1,3),Q(1,2))==Q(27,20)
    assert cubic_value(3,1,1,1,Q(1,2))==Q(65,48)
    assert Q(65,48)-Q(27,20)==Q(1,240)
    count+=3

    # Sign of the exact transverse Taylor coefficient at stationary x:
    # 2(9x^2-1)/((1-3x^2)(1+x^2)^2).
    for x in [Q(1,20),Q(1,5),Q(1,4),Q(1,3),Q(2,5)]:
        t=x/(1-3*x*x)
        c2=2*(9*t*x**3+5*t*x-1)/(1+x*x)**3
        closed=2*(9*x*x-1)/((1-3*x*x)*(1+x*x)**2)
        assert c2==closed
        assert (c2<0) if x<Q(1,3) else ((c2==0) if x==Q(1,3) else (c2>0))
        count+=2

    # Explicitly check all permutations of the 4-root convolution producing z^3.
    from itertools import product
    for A,B,C,D in [(1,2,3,4),(3,1,1,1),(18,6,5,5)]:
        coeff = 0
        seq=[A,B,C,D]
        for i,j,k,l in product(range(4),repeat=4):
            if i+j+k+l==3: coeff+=seq[i]*seq[j]*seq[k]*seq[l]
        assert coeff==4*A**3*D+12*A*A*B*C+4*A*B**3
        count+=1

    # Nonproof numerical sanity checks for the claimed global t<=1/5 branch.
    rng=Random(2602026)
    for t in [0.001,.02,.1,.2]:
        E,x=binomial_optimum(t)
        for _ in range(1500):
            A,B,C,D=[rng.random() for _ in range(4)]
            assert cubic_value(A,B,C,D,t)<E+1e-10
            count+=1
    assert quartic(Q(1,3))>0
    count+=1
    print('CHECK_OK',count)


if __name__=='__main__':
    check()
