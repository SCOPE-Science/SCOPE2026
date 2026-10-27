"""Reproducible exact/finite spectral tests for harmonic sampling on staggered latitudes."""
import math
import numpy as np
import sympy as sp
from scipy.special import lpmv

x=sp.Symbol('x')

def amplitude_exact(l,m,c=sp.Rational(1,2)):
    a=abs(m)
    v=sp.diff(sp.legendre(l,x),x,a).subs(x,c)
    return sp.factorial(l-a)/sp.factorial(l+a)*(1-c*c)**a*v*v

def predictions(N,l,c=sp.Rational(1,2)):
    vals=[sp.Integer(0)]*(2*N)
    if N%2:
        for m in range(-l,l+1):
            r=m%N
            vals[r]+=2*N*amplitude_exact(l,m,c)
    else:
        for m in range(-l,l+1):
            r=m%N
            k=(m-r)//N
            vals[2*r+(k%2)]+=2*N*amplitude_exact(l,m,c)
    return vals

def numerical_matrix(N,l,c):
    j=np.arange(N)
    phi=2*np.pi*j/N
    v=np.zeros((2*N,2*l+1), dtype=complex)
    for idx,m in enumerate(range(-l,l+1)):
        a=abs(m)
        q=math.exp(.5*(math.lgamma(l-a+1)-math.lgamma(l+a+1))) *lpmv(a,l,c)
        v[:N,idx]=q*np.exp(1j*m*phi)
        v[N:,idx]=(-1)**(l+a)*q*np.exp(1j*m*(phi+np.pi/N))
    return v

def main():
    checkcount=0; worst=0.; worst_case=None
    for N in range(3,13):
        for l in range(0,13):
            vals=predictions(N,l)
            rank=sum(v!=0 for v in vals)
            target=min(2*l+1,N if N%2 else 2*N)
            assert rank==target, (N,l,rank,target)
            assert all(v>=0 for v in vals)
            E=numerical_matrix(N,l,.5)
            num=np.linalg.eigvalsh(E@E.conj().T)
            pred=np.array(sorted(map(float,vals)))
            err=np.max(abs(np.sort(num)-pred))
            if err>worst: worst=err; worst_case=(N,l)
            assert err<1e-9, (N,l,err)
            checkcount+=1
    # Exhaust exact arithmetic nonvanishing of all associated Legendre amplitudes.
    rational_tests=0
    for c in [sp.Rational(1,2),sp.Rational(1,4),sp.Rational(-3,8),sp.Rational(5,6)]:
        for l in range(0,35):
            for m in range(0,l+1):
                assert amplitude_exact(l,m,c)>0,(l,m,c)
                rational_tests+=1
    print('rank_and_spectrum_cases:',checkcount)
    print('max_abs_gram_eigenvalue_error:',format(worst,'.6g'),'at',worst_case)
    print('positive_exact_associated_Legendre_tests:',rational_tests)
    print('sharp_odd_threshold_N11:',(11-1)//2,'ranks:',[sum(v!=0 for v in predictions(11,l)) for l in [4,5,6]])
    print('sharp_even_threshold_N10:',10,'ranks:',[sum(v!=0 for v in predictions(10,l)) for l in [9,10,11]])
    print('all_tests_passed')
if __name__=='__main__':main()
