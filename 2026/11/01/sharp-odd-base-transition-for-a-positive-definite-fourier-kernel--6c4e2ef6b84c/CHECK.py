#!/usr/bin/env python3
"""Exact-integer enclosure for a one-variable Fourier-kernel counterexample.

All interval endpoints represent integral multiples of 10**35. No floating
point arithmetic is used for the positivity certificate.
"""
from fractions import Fraction
from math import comb

S = 10**35
Q = 25  # The first failing odd lacunarity is proved below.


def fl(a, b):
    return a // b


def ce(a, b):
    return -((-a) // b)


class I:
    __slots__ = ("l", "u")

    def __init__(self, l, u=None):
        self.l = int(l)
        self.u = int(l if u is None else u)
        assert self.l <= self.u

    @classmethod
    def rational(cls, a, b=1):
        return cls(fl(a * S, b), ce(a * S, b))

    def __add__(self, b):
        if not isinstance(b, I):
            b = I.rational(b)
        return I(self.l+b.l, self.u+b.u)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.u, -self.l)

    def __sub__(self, b):
        return self + -b

    def __mul__(self, b):
        if not isinstance(b, I):
            b = I.rational(b)
        p = [a*c for a in (self.l, self.u) for c in (b.l,b.u)]
        return I(fl(min(p), S), ce(max(p), S))

    __rmul__ = __mul__

    def divint(self, n):
        assert n > 0
        return I(fl(self.l,n),ce(self.u,n))

    def mulfrac(self, f):
        assert isinstance(f, Fraction)
        if f < 0:
            return -self.mulfrac(-f)
        return I(fl(self.l*f.numerator,f.denominator),
                 ce(self.u*f.numerator,f.denominator))


def atan_bounds(x, terms=12):
    assert x > 0 and x < 1 and terms % 2 == 0
    a = sum(((-1)**k * x**(2*k+1)/Fraction(2*k+1)) for k in range(terms))
    b = a + x**(2*terms+1)/Fraction(2*terms+1)
    return (a,b)


def pi_interval():
    a1,a2=atan_bounds(Fraction(1,5))
    b1,b2=atan_bounds(Fraction(1,239))
    lo,hi = 16*a1-4*b2, 16*a2-4*b1
    return I(fl(lo.numerator*S,lo.denominator),
             ce(hi.numerator*S,hi.denominator))

PI = pi_interval()
assert 3*S < PI.l < PI.u < 4*S


def cos_bound_pi_fraction(r):
    assert isinstance(r, Fraction)
    # The nearest integer reduces the cosine angle to [-pi/2,pi/2].
    k = fl(r.numerator*2+r.denominator,2*r.denominator)
    v = abs(r-k)
    assert v <= Fraction(1,2)
    z=PI.mulfrac(v)
    y=z*z
    total=I.rational(1)
    term=I.rational(1)
    for j in range(1,13):
        term = (term*y).divint((2*j-1)*(2*j))
        if j < 12:
            total = total + (term if j%2==0 else -term)
    # Twelve retained terms k=0,...,11; the first omitted term is positive.
    # For |z| <= pi/2 its subsequent terms decrease, so 0 <= remainder <= term.
    out=I(total.l,total.u+term.u)
    return (-out if k%2 else out)


def P(ys):
    e=[I.rational(1),I.rational(0),I.rational(0),I.rational(0),I.rational(0)]
    for y in ys:
        for k in range(4,0,-1):
            e[k]=e[k]+e[k-1]*y
    return (I.rational(21)+4*e[2]+4*e[3]+e[4]).divint(280)


def point(j):
    return Fraction(Q-1,Q**j) if j else Fraction(0)


def f_of_difference(j,k):
    r=point(j)-point(k)
    return P([cos_bound_pi_fraction(r * Q**(i-1)) for i in range(1,8)])


def finite_defect(q):
    global Q
    Q=q
    c=[-1]+[1]*7
    d=I.rational(Fraction(7,2).numerator,2)
    for j in range(8):
        for k in range(j+1,8):
            d=d+ f_of_difference(j,k)*I.rational(2*c[j]*c[k])
    return d


def leading_minors(q):
    from functools import lru_cache
    global Q
    Q=q
    A=[[f_of_difference(i,j)-I.rational(1,8)
        for j in range(8)] for i in range(8)]
    out=[]
    for n in range(1,9):
        @lru_cache(None)
        def det(mask):
            k=mask.bit_count()
            if not k:
                return I.rational(1)
            row=n-k
            val=I.rational(0)
            pos=0
            for col in range(n):
                if mask & (1<<col):
                    summand=A[row][col]*det(mask^(1<<col))
                    val=val+(summand if pos%2==0 else -summand)
                    pos+=1
            return val
        out.append(det((1<<n)-1))
    return out


def verify():
    # The source multiaffine polynomial is nonnegative on the cube.
    v=[Fraction((r-2)*(r-3)*(r-7)*(r-10),420) for r in range(8)]
    assert v==[Fraction(1),Fraction(9,35),Fraction(0),Fraction(0),
               Fraction(3,35),Fraction(1,7),Fraction(4,35),Fraction(0)]
    assert all(x>=0 for x in v)
    # Every monomial E_k(cos(q**i*t)) has nonnegative Fourier coefficients.
    assert 21+4*comb(7,2)+4*comb(7,3)+comb(7,4)==280
    assert PI.u*PI.u < 10*S*S  # pi**2 < 10, used in the infinite tail.

    minimum_positive_minor=None
    for q in range(3,25,2):
        for minor in leading_minors(q):
            assert minor.l>0, (q,minor.l,minor.u)
            if minimum_positive_minor is None or minor.l<minimum_positive_minor:
                minimum_positive_minor=minor.l

    maximum_negative_defect=None
    for q in range(25,103,2):
        d=finite_defect(q)
        assert d.u<0, (q,d.l,d.u)
        if maximum_negative_defect is None or d.u>maximum_negative_defect:
            maximum_negative_defect=d.u
        if q==25:
            assert d.u< -9*S//1000

    # Analytic tail: for q odd and >= 103, each seven-coordinate cosine
    # vector at a pairwise node difference is <= 5*pi*pi/q**2 away from
    # its limiting {+1,-1}^7 vertex in l1.  The coordinate derivative of
    # P is bounded by 13/35, so the 56 off-diagonal ordered terms change
    # by at most 56*(13/35)*5*pi*pi/q**2 < 1040/q**2 < 1/10.
    assert Fraction(1040,103**2) < Fraction(1,10)
    assert 56*Fraction(13,35)*5*10 == 1040

    delta=Fraction(1,100000)
    assert (1-delta)*Fraction(maximum_negative_defect,S) + delta*Fraction(63,2) < 0
    assert ((1-delta)*(-Fraction(1,10)+Fraction(1040,103**2))
           +delta*Fraction(63,2)) == -Fraction(4389489,2652250000)

    print('RIGOROUS_ODD_BASE_DICHOTOMY')
    print('positive_definite_matrices_checked',list(range(3,25,2)))
    print('min_certified_principal_minor_lower_bound',Fraction(minimum_positive_minor,S))
    print('negative_sign_witness_checked',list(range(25,103,2)))
    print('max_certified_negative_defect_upper_bound',Fraction(maximum_negative_defect,S))
    print('infinite_tail', 'all odd q>=103 by 1040/q**2<1/10')
    print('q25_bounds',Fraction(finite_defect(25).l,S),Fraction(finite_defect(25).u,S))
    print('PI_bounds',Fraction(PI.l,S),Fraction(PI.u,S))

if __name__=='__main__':
    verify()
