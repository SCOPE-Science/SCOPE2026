#!/usr/bin/env python3
import math
import numpy as np

def spin1():
    s=1/math.sqrt(2)
    sx=np.array([[0,1,0],[1,0,1],[0,1,0]],dtype=complex)*s
    sy=np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]],dtype=complex)*s
    sz=np.diag([1,0,-1]).astype(complex)
    return sx,sy,sz

def hmat(K,B):
    sx,sy,sz=spin1()
    I=np.eye(3)
    dot=np.kron(sx,sx)+np.kron(sy,sy)+np.kron(sz,sz)
    return K*(dot@dot)+B*(np.kron(sz,I)+np.kron(I,sz))

def pt(rho):
    return rho.reshape(3,3,3,3).transpose(2,1,0,3).reshape(9,9)

def direct(K,B,T):
    w,v=np.linalg.eigh(hmat(K,B))
    p=np.exp(-(w-w.min())/T)
    rho=(v*p)@v.conj().T
    rho/=np.trace(rho)
    lam=np.linalg.eigvalsh(pt(rho))
    return float(-lam[lam<0].sum()),w

def formula(K,B,T):
    r=math.exp(-3*K/T)
    if r<=4:
        return 0.0
    b=B/T
    a=(r-1)/3
    Z=(1+2*math.cosh(b))**2+r-1
    def f(d):
        return math.sqrt(math.sinh(d*b)**2+a*a)-math.cosh(d*b)
    return (2*f(1)+f(2))/Z

def expected(K,B):
    return np.array(sorted([4*K,K-2*B,K-B,K-B,K,K,K+B,K+B,K+2*B]),float)

def main():
    spectra=0
    formulas=0
    for K in (-0.7,-1.0,-3.0):
        for B in (0.0,0.2,1.0,2.5,7.0):
            _,w=direct(K,B,0.8)
            assert np.max(np.abs(w-expected(K,B)))<2e-12
            spectra+=1
            Tc=3*abs(K)/math.log(4)
            for T in (0.2*Tc,0.6*Tc,0.99*Tc,1.01*Tc,1.5*Tc):
                nd,_=direct(K,B,T)
                nf=formula(K,B,T)
                assert abs(nd-nf)<2e-11,(K,B,T,nd,nf)
                formulas+=1

    for K in (-0.7,-1.0,-3.0):
        Tc=3*abs(K)/math.log(4)
        for B in (0.0,1.0,5.0):
            n1,_=direct(K,B,0.99*Tc)
            n2,_=direct(K,B,1.01*Tc)
            assert n1>0
            assert n2<2e-12

    for K in (-1.0,-3.0):
        for T in (0.2,0.5,1.0):
            r=math.exp(-3*K/T)
            if r>4:
                nd,_=direct(K,0,T)
                assert abs(nd-(r-4)/(r+8))<2e-12

    K=-3.0
    Tc=3*abs(K)/math.log(4)
    for B in (5.0,10.0,20.0):
        assert formula(K,B,0.5*Tc)>0

    print("VERIFY_OK")
    print("spectrum_checks =",spectra)
    print("formula_checks =",formulas)
    print("K_minus_3_Tc =",3*3/math.log(4))
    print("zero_temperature_field_crossing_K_minus_3 =",4.5)

if __name__=="__main__":
    main()
