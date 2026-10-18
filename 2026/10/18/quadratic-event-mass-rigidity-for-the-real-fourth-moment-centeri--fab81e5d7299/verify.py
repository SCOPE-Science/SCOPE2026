"""Exact polynomial certificate and finite reproducibility checks.

Run with Python 3; all dependencies are from the standard library.
Finite checks corroborate, but do not prove, the probability-space theorem.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt
from random import Random


def add_pair(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul_pair(x, y):
    return (x[0] * y[0] + 3 * x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])


class Alg:
    """Q(s,t), with s*s=3 and t*t=3+2*s, in basis (1,s,t,s*t)."""
    def __init__(self, u=(Q(0), Q(0)), v=(Q(0), Q(0))):
        self.u, self.v = u, v

    @classmethod
    def rational(cls, x):
        return cls((Q(x), Q(0)))

    def __add__(self, other):
        if not isinstance(other, Alg):
            other = Alg.rational(other)
        return Alg(add_pair(self.u, other.u), add_pair(self.v, other.v))

    __radd__ = __add__

    def __neg__(self):
        return Alg((-self.u[0], -self.u[1]), (-self.v[0], -self.v[1]))

    def __sub__(self, other):
        return self + -other if isinstance(other, Alg) else self + Alg.rational(-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if not isinstance(other, Alg):
            other = Alg.rational(other)
        first = add_pair(mul_pair(self.u, other.u),
                         mul_pair(mul_pair(self.v, other.v), (Q(3), Q(2))))
        second = add_pair(mul_pair(self.u, other.v), mul_pair(self.v, other.u))
        return Alg(first, second)

    __rmul__ = __mul__

    def __pow__(self, n):
        y = Alg.rational(1)
        for _ in range(n):
            y = y * self
        return y

    def __eq__(self, other):
        if not isinstance(other, Alg):
            other = Alg.rational(other)
        return self.u == other.u and self.v == other.v


def padd(p, q):
    out = [Alg.rational(0) for _ in range(max(len(p), len(q)))]
    for j, x in enumerate(p):
        out[j] = out[j] + x
    for j, x in enumerate(q):
        out[j] = out[j] + x
    return out


def pmul(p, q):
    out = [Alg.rational(0) for _ in range(len(p) + len(q) - 1)]
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] = out[i + j] + x*y
    return out


def ppower(p, n):
    out = [Alg.rational(1)]
    for _ in range(n):
        out = pmul(out, p)
    return out


def exact_certificate():
    s = Alg((Q(0), Q(1)))
    t = Alg((Q(0), Q(0)), (Q(1), Q(0)))
    a = s * (t - 1) * Q(1, 2)
    b = -s * (t + 1) * Q(1, 2)
    A = s * Q(2, 3)
    K = Alg.rational(1) + A
    x_minus_one = [Alg.rational(-1), Alg.rational(1)]
    x_minus_a = [-a, Alg.rational(1)]
    x_minus_b = [-b, Alg.rational(1)]
    left = padd([K*c for c in [Alg.rational(0)]*4 + [Alg.rational(1)]],
                [-v for v in ppower(x_minus_one, 4)])
    residual = padd(left,
                    [-A*v for v in pmul(ppower(x_minus_a, 2),
                                         ppower(x_minus_b, 2))])
    expected = [(Alg.rational(10) + 6*s)*v for v in x_minus_one]
    assert residual == expected + [Alg.rational(0)]*3
    alpha = (Alg.rational(3) - t) * Q(1, 6)
    assert 54*alpha**4-108*alpha**3+72*alpha**2-18*alpha+1 == 0
    assert a-b == s*t
    assert a-alpha*(a-b) == 1
    return 3


def numeric_checks():
    rng=Random(173401)
    root=sqrt(3+2*sqrt(3))
    a=sqrt(3)*(root-1)/2
    b=-sqrt(3)*(root+1)/2
    d=a-b
    alpha=(3-root)/6
    A=2/sqrt(3)
    K=1+A
    M=max(abs(a),abs(b))
    c=A*min(d**4/(64*M**4), 1/(16*alpha**2))
    C=A*d**4*(1+alpha)**2
    nidentity=0
    nwitness=0
    for n in range(1,11):
        for _ in range(20):
            raw=[rng.expovariate(1) for _ in range(n)]
            total=sum(raw)
            w=[v/total for v in raw]
            f=[rng.uniform(-2,2) for _ in range(n)]
            mean=sum(wi*xi for wi,xi in zip(w,f))
            D=K*sum(wi*xi**4 for wi,xi in zip(w,f))-sum(wi*(xi-mean)**4 for wi,xi in zip(w,f))
            R=A*sum(wi*((xi-a*mean)*(xi-b*mean))**2 for wi,xi in zip(w,f))
            assert abs(D-R)<1e-9*max(1,abs(D),abs(R))
            nidentity+=1
            subsets=[(abs(sum(wi*bi for wi,bi in zip(w,bits))-alpha),bits)
                     for bits in product((0,1),repeat=n)]
            delta,bits=min(subsets)
            shift=d*(sum(wi*bi for wi,bi in zip(w,bits))-alpha)
            g=[b+shift if bit else a+shift for bit in bits]
            mg=sum(wi*gi for wi,gi in zip(w,g))
            assert abs(mg-1)<1e-10
            ratio=sum(wi*(gi-mg)**4 for wi,gi in zip(w,g))/sum(wi*gi**4 for wi,gi in zip(w,g))
            assert K-ratio<=C*delta**2+1e-9
            nwitness+=1
    ntwo=0
    for i in range(1,1001):
        p=i/1001
        delta=min(alpha,abs(p-alpha),abs(1-p-alpha))
        nfourth=(p**3+(1-p)**3)*(p**(1/3)+(1-p)**(1/3))**3
        gap=K-nfourth
        assert c*delta**2<=gap+1e-11<=C*delta**2+1e-11
        ntwo+=1
    return nidentity,nwitness,ntwo,c,C,alpha


if __name__=='__main__':
    n_poly=exact_certificate()
    n_identity,n_witness,n_two,c,C,alpha=numeric_checks()
    print('PASS exact algebraic polynomial identities:',n_poly)
    print('PASS random weighted SOS instances:',n_identity)
    print('PASS finite subset-mass witness instances:',n_witness)
    print('PASS two-atom norm comparisons:',n_two)
    print('alpha, c, C = %.14g, %.14g, %.14g'%(alpha,c,C))
