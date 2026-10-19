#!/usr/bin/env python3
"""Exact integer/rational reproduction of a cube diffusion Padé positivity result.

Usage: python3 artifacts/verify_hypercube_pade.py
No third-party packages, downloads, or floating-point computations are required.
"""
from fractions import Fraction
from math import comb, factorial


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def hamming_sum(d,r,k):
    return sum((-1)**j * comb(r,j)*comb(d-r,k-j)
               for j in range(max(0,k-(d-r)),min(r,k)+1))


def polynomials(d):
    # q_k=3+3*k*h+k*k*h*h, q_0=3; D=prod(q_1,...,q_d).
    q=[None]+[[3,3*k,k*k] for k in range(1,d+1)]
    D=[1]
    for k in range(1,d+1):
        D=mul(D,q[k])
    numerators=[]
    for r in range(d+1):
        N=[128*x for x in D] if d==7 and r==0 else [2**d*x for x in D] if r==0 else [0]*len(D)
        for k in range(1,d+1):
            T=[1]
            for j in range(1,d+1):
                if j!=k: T=mul(T,q[j])
            H=hamming_sum(d,r,k)
            for j,t in enumerate(T):
                N[j+1]+=-6*k*H*t
        while len(N)>1 and N[-1]==0:
            N.pop()
        numerators.append(N)
    return D,numerators


def evaluate(coefs,h):
    return sum(Fraction(c)*h**i for i,c in enumerate(coefs))


def variations(seq):
    nz=[1 if x>0 else -1 for x in seq if x]
    return sum(a!=b for a,b in zip(nz,nz[1:]))


def test_exact():
    d=7
    D,N=polynomials(d)
    # This is a separate witness of the Fourier reduction, not the proof
    # of its validity. The actual theorem proves that reduction directly.
    p1=[-324,-6804,-64908,-362880,-1282716,-2835756,-3302157,
        525420,8744306,14937006,13035142,6107220,1259580]
    p2=[-324,-6804,-64800,-364770,-1331316,-3255021,-5305620,
        -5491500,-3084234,-301154,620340,251580]
    p7=[-9,0,966,5880,13538,13132,4356]
    assert N[1]==[0]+[-864*x for x in p1]
    assert N[2]==[0,0]+[-864*x for x in p2]
    assert N[7]==[0]*7+[90720*x for x in p7]
    assert all(c>0 for c in N[0])
    for r in range(3,7):
        assert all(c==0 for c in N[r][:r if r<6 else 7])
        assert all(c>0 for c in N[r][r if r<6 else 7:])
    assert variations(p1)==1 and variations(p2)==1 and variations(p7)==1
    assert evaluate(p7,Fraction(1,20))<0
    assert evaluate(p7,Fraction(1,10))>0
    assert evaluate(p1,Fraction(1,2))<0
    assert evaluate(p1,Fraction(1))>0
    assert evaluate(p2,Fraction(1))<0
    # Thus 1/20<alpha<1/10<1/2<beta<1<gamma, by Descartes.
    # Row-sum preservation follows spectrally from R(0)=1.
    # Every nonzero Hamming shell is strictly positive at h=1/5.
    h=Fraction(1,5)
    assert all(evaluate(N[r],h)>0 for r in range(8))
    # At small and large steps there are explicit negative entries.
    assert evaluate(N[7],Fraction(1,20))<0
    assert evaluate(N[1],Fraction(1))<0
    # Direct diagonalization identity: 2^d*K_r=sum_k H_{d,r,k} R(-2kh).
    for hh in [Fraction(1,20),Fraction(1,5),Fraction(1),Fraction(7,2)]:
        for r in range(d+1):
            s=sum(Fraction(hamming_sum(d,r,k)) * Fraction(3-3*k*hh+k*k*hh*hh,3+3*k*hh+k*k*hh*hh) for k in range(d+1))
            assert evaluate(N[r],hh)/evaluate(D,hh)==s
    # The seventh coefficient of the Padé map is negative.
    # Rational formal power-series recurrence from (12-6z+z^2)R=12+6z+z^2.
    c=[Fraction(0)]*8
    for n in range(8):
        rhs=Fraction({0:12,1:6,2:1}.get(n,0))
        c[n]=(rhs+6*(c[n-1] if n>=1 else 0)-(c[n-2] if n>=2 else 0))/12
    assert c==[Fraction(1),Fraction(1),Fraction(1,2),Fraction(1,6),
               Fraction(1,24),Fraction(1,144),Fraction(0),Fraction(-1,1728)]
    # For a d-cube two vertices at distance exactly seven have
    # ((-L)^7)_{uv}=7!, whence leading contribution -(35/12)*h^7.
    assert c[7]*factorial(7)==Fraction(-35,12)
    # For dimension 6 antipodes, the 6th coefficient is zero and
    # ((-L)^7)_{uv}=-7*6*6!, so the first nonzero term is +35/2*h^7.
    assert c[7]*(-7*6*factorial(6))==Fraction(35,2)
    for dd in range(1,7):
        _,nn=polynomials(dd)
        for r in range(1,dd+1):
            first=next(c for c in nn[r] if c)
            assert first>0,(dd,r)
    print('VERIFY_OK: exact Walsh-spectral numerators and rational tests;')
    print('one positive root each; sharp Q7 positivity {0} U [alpha,beta];')
    print('small-step Hamming cube dimension threshold equals seven.')

if __name__=='__main__':
    test_exact()
