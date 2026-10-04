#!/usr/bin/env python3
import math

def simpson(f,a,b,n=12000):
    if n % 2: n += 1
    h=(b-a)/n
    s=f(a)+f(b)
    for i in range(1,n):
        s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3

def V(lam,delta,s):
    tau=1.0-lam
    def f(u):
        z=tau*s+lam*u
        a=lam*(1.0+delta*u)/(1.0+delta*z)
        return 4.0*lam*math.atanh(a)/(1.0-z*z)
    return simpson(f,-1.0,1.0)

def formulas(lam):
    A=math.atanh(lam)
    vss=16*lam*A/(1+lam)**2
    vds=8*(lam-(1+lam)*A)/(1+lam)**2
    vdd=16*(lam-A)/(1+lam)**2
    H=vdd-vds*vds/vss
    N=A*A*(lam*lam+6*lam+1)-2*A*lam*(3*lam+1)+lam*lam
    H2=-4*N/(A*lam*(1+lam)**2)
    rp=lam*(1+(3+2*math.sqrt(2))*lam)/(1+6*lam+lam*lam)
    return A,vss,vds,vdd,H,H2,rp

def fd_hessian(lam,h=2e-4):
    f00=V(lam,0.0,0.0)
    fsp=V(lam,0.0,h); fsm=V(lam,0.0,-h)
    fdp=V(lam,h,0.0); fdm=V(lam,-h,0.0)
    fpp=V(lam,h,h); fpm=V(lam,h,-h); fmp=V(lam,-h,h); fmm=V(lam,-h,-h)
    vss=(fsp-2*f00+fsm)/(h*h)
    vdd=(fdp-2*f00+fdm)/(h*h)
    vds=(fpp-fpm-fmp+fmm)/(4*h*h)
    return vss,vds,vdd

def main():
    samples=[0.05,0.2,0.5,0.8,0.95]
    for lam in samples:
        A,vss,vds,vdd,H,H2,rp=formulas(lam)
        assert abs(H-H2) < 1e-11
        assert rp < lam < A
        assert H < 0 and vss > 0
        nss,nds,ndd=fd_hessian(lam)
        scale=max(1.0,abs(vss),abs(vds),abs(vdd))
        assert abs(nss-vss) < 3e-4*scale, (lam,'ss',nss,vss)
        assert abs(nds-vds) < 3e-4*scale, (lam,'ds',nds,vds)
        assert abs(ndd-vdd) < 3e-4*scale, (lam,'dd',ndd,vdd)
    print('VERIFY_OK finite-radius Funk trapezoid Hessian samples=5')

if __name__=='__main__':
    main()
