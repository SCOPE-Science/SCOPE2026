"""Supplementary numerical checks of two-modulation cyclic Gabor erasure-design theorem.
Run: python CHECK.py (requires numpy). Not a substitute for the analytic proof.
"""
import itertools
import math
import numpy as np


def path_matrix(m,q):
    assert m >= 1
    x=np.diag(np.array([1.]+[2.]*(m-1)+[1.]))
    for i in range(m):
        x[i,i+1]=x[i+1,i]=q
    return x


def spectral_path(m,q):
    w=np.linalg.eigvalsh(path_matrix(m,q))
    return float(w[0]),float(w[-1])


def gabor_operator(n,ell,K):
    g=np.zeros(n,dtype=complex);g[0]=g[1]=1
    s=np.zeros((n,n),dtype=complex)
    for k in K:
        v=np.roll(g,k)
        for l in (0,ell):
            w=v*np.exp(2j*np.pi*l*np.arange(n)/n)
            s+=np.outer(w,np.conjugate(w))
    return s


def gaps(n,E):
    E=sorted(E)
    return tuple((E[(i+1)%len(E)]-E[i]-1)%n for i in range(len(E)))


def check():
    count=0;case_counts=0
    for n in range(3,12):
        for ell in range(1,n):
            q=abs(math.cos(math.pi*ell/n))
            if q<1e-13: continue
            for h in range(1,n//2+1):
                a=(n-h)//h; b=(n-h+h-1)//h
                ala,_=spectral_path(a,q)
                _,ubb=spectral_path(b,q)
                kopt=ubb/ala
                opt=0;actual_opt=1e30
                for e in itertools.combinations(range(n),h):
                    K=sorted(set(range(n))-set(e))
                    L=gaps(n,e)
                    w=np.linalg.eigvalsh(gabor_operator(n,ell,K))
                    minw,maxw=w[0],w[-1]
                    if min(L)==0:
                        assert abs(minw)<1e-8
                        continue
                    assert minw>0
                    aa=min(spectral_path(m,q)[0] for m in L)
                    bb=max(spectral_path(m,q)[1] for m in L)
                    assert abs(minw-2*aa)<1e-8,(n,ell,e,'lower')
                    assert abs(maxw-2*bb)<1e-8,(n,ell,e,'upper')
                    cond=maxw/minw
                    assert cond>=kopt-1e-7,(n,ell,e,cond,kopt)
                    if max(L)-min(L)<=1:
                        assert abs(cond-kopt)<1e-7
                        opt+=1
                    else:
                        assert cond>kopt+1e-8,(n,ell,e,cond,kopt)
                    actual_opt=min(actual_opt,cond)
                    count+=1
                assert abs(actual_opt-kopt)<1e-7
                r=(n-h)-a*h
                assert opt*h==n*math.comb(h,r),(n,ell,h,opt)
                case_counts+=1
    for q in [.04,.2,.5,.9,.99]:
        prevlo=0.;prevhi=0.
        for m in range(1,100):
            lo,hi=spectral_path(m,q)
            assert lo>=prevlo-1e-12 and hi>prevhi+1e-13
            if m<6: assert lo>prevlo+1e-13
            assert lo<1-q*q+1e-10
            h0=math.acosh((2-lo)/(2*q))
            assert abs(q*(math.cosh(h0)+math.sinh(h0)*math.tanh(m*h0/2))-1)<1e-8
            prevlo,prevhi=lo,hi
    print('PASS: %d numerical spectral comparisons across %d parameter families; monotonicity and hyperbolic root tests.' %(count,case_counts))

if __name__=='__main__': check()
