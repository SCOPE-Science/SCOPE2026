"""Exact and independent checks for weighted diffraction on the Grigorchuk Toeplitz word.

Uses only the Python standard library. Analytic Fourier and homometry arguments
remain necessary for the all-frequency assertions.
"""
from fractions import Fraction as F
from itertools import product
from math import cos, sin, pi, isclose


def coords(w):
    a, b, c, d = map(F, w)
    M = (7*a + 2*b + 4*c + d) / 14
    V = -a + (2*b + 4*c + d) / 7
    P = (4*b - 6*c + 2*d) / 7
    Q = (-6*b + 2*c + 4*d) / 7
    R = (2*b + 4*c - 6*d) / 7
    assert P + Q + R == 0
    return M,V,P,Q,R


def inverse(M,V,P,Q):
    return (M-V/2, M+V/2+(P-Q)/2,
            M+V/2-P/2, M+V/2+P+Q)


def intensity(w, r):
    M,V,P,Q,R = coords(w)
    if r == 0:
        return M*M
    if r == 1:
        return V*V/4
    return [P,Q,R][(r-2)%3]**2 / (4**r)


def ksymbol(w,k):
    a,b,c,d=w
    if k==0:
        return a
    return [c,b,d][(k-1)%3]


def valuation(n):
    assert n>0
    return (n & -n).bit_length()-1


def sequence(w,N):
    return [ksymbol(w,valuation(n+1)) for n in range(N)]


def check():
    # Compare the actual substitution fixed point to the two-adic coding.
    s='a'
    t={'a':'aca','b':'d','c':'b','d':'c'}
    for _ in range(9):
        s=''.join(t[c] for c in s)
    code=tuple('a' if valuation(n+1)==0 else
               'cbd'[(valuation(n+1)-1)%3] for n in range(len(s)))
    assert ''.join(code)==s

    # The rational inverse holds on all 625 small integer weight vectors.
    for w in product(range(-2,3), repeat=4):
        M,V,P,Q,R=coords(w)
        assert inverse(M,V,P,Q)==tuple(map(F,w))
        assert R==-P-Q
        a,b,c,d=map(F,w)
        assert (M*M+V*V/4+P*P/7+Q*Q/14+R*R/28 ==
                a*a/2+b*b/7+2*c*c/7+d*d/14)
        for r in range(2,11):
            assert intensity(w,r+3)==intensity(w,r)/64

    initial=(F(10),F(11),F(13),F(14))
    M,V,P,Q,R=coords(initial)
    assert (M,V,P,Q,R)==(F(79,7),F(18,7),F(-6,7),F(16,7),F(-10,7))
    four=[inverse(M,e*V,z*P,z*Q) for e,z in product((-1,1),repeat=2)]
    assert len(set(four))==4
    assert all(len(set(w))==4 and min(w)>0 for w in four)
    assert all(all(intensity(w,r)==intensity(initial,r) for r in range(25)) for w in four)

    eight=[]
    for sm,sv,sp in product((-1,1),repeat=3):
        w=inverse(sm*M,sv*V,sp*P,sp*Q)
        eight.append(w)
    assert len(set(eight))==8
    assert all(all(intensity(w,r)==intensity(initial,r) for r in range(25)) for w in eight)

    # Compare directly computed long finite Fourier sums at nonzero dyadic
    # frequencies with the shell-integral formula (asymptotic error O(2^-L)).
    N=1<<15
    seq=sequence(initial,N)
    for r in range(1,9):
        q=1/(1<<r)
        computed=sum(float(seq[n])*complex(cos(-2*pi*q*n),sin(-2*pi*q*n))
                     for n in range(N))/N
        D=V if r==1 else [P,Q,R][(r-2)%3]
        pred=float(D)/(1<<r)*complex(cos(2*pi*q),sin(2*pi*q))
        assert abs(computed-pred)<0.00035,(r,computed,pred)

    # Independent finite cyclic autocorrelations: the four positive codings
    # have the same limiting coefficients, up to the single exceptional site.
    L=13
    NN=1<<L
    sw=[]
    for w in four:
        scaled=tuple(int(7*x) for x in w)
        sw.append(sequence(scaled,NN))
    max_error=0
    for h in range(0,33):
        sums=[sum(v[n]*v[(n+h)%NN] for n in range(NN)) for v in sw]
        max_error=max(max_error,max(abs(a-sums[0]) for a in sums[1:])/(49*NN))
    assert max_error < 0.04,max_error
    print('VERIFY_OK: substitution prefixes; 625 exact four-coordinate inversions and Parseval identities;'
          ' 4 distinct positive and 8 distinct real homometric weightings;'
          ' 25 exact Bragg intensities per weighting; 8 independently sampled'
          ' dyadic Fourier modes; 33 finite autocorrelation lags; max_error=',
          round(max_error,8))

if __name__=='__main__':
    check()
