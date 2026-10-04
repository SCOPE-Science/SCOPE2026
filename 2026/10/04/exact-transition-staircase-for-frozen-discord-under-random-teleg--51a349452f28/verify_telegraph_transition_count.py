#!/usr/bin/env python3
import math

def lam(nu, mu):
    return math.exp(-nu)*(math.cos(mu*nu)+math.sin(mu*nu)/mu)

def dlam(nu, mu):
    return -(mu+1.0/mu)*math.exp(-nu)*math.sin(mu*nu)

def closed_count(mu, rho):
    A=(mu/math.pi)*math.log(1.0/rho)
    return 2*math.ceil(A)-1

def zero_point(mu, k):
    return (k*math.pi-math.atan(mu))/mu

def bisect_sign_change(mu, rho, lo, hi, rising):
    def f(x):
        return abs(lam(x,mu))-rho
    flo=f(lo)
    fhi=f(hi)
    assert flo*fhi<0, (mu,rho,lo,hi,flo,fhi)
    for _ in range(90):
        mid=(lo+hi)/2.0
        fm=f(mid)
        if flo*fm<=0:
            hi=mid
            fhi=fm
        else:
            lo=mid
            flo=fm
    return (lo+hi)/2.0

def independent_roots(mu, rho):
    roots=[]
    z1=zero_point(mu,1)
    roots.append(bisect_sign_change(mu,rho,0.0,z1,False))
    n=1
    while True:
        peak=n*math.pi/mu
        height=math.exp(-n*math.pi/mu)
        if height<=rho*(1+2e-14):
            break
        zl=zero_point(mu,n)
        zr=zero_point(mu,n+1)
        roots.append(bisect_sign_change(mu,rho,zl,peak,True))
        roots.append(bisect_sign_change(mu,rho,peak,zr,False))
        n+=1
    return roots

def main():
    derivative_checks=0
    peak_checks=0
    count_checks=0
    for mu in (0.7,1.3,3.0,7.5,19.974984355438178):
        for nu in (0.13,0.71,1.9):
            h=1e-6
            num=(lam(nu+h,mu)-lam(nu-h,mu))/(2*h)
            assert abs(num-dlam(nu,mu))<3e-9
            derivative_checks+=1
        for n in range(1,8):
            x=n*math.pi/mu
            assert abs(dlam(x,mu))<2e-13
            assert abs(abs(lam(x,mu))-math.exp(-n*math.pi/mu))<2e-13
            peak_checks+=1

        for rho in (0.15,0.31,0.55,0.77,0.91):
            roots=independent_roots(mu,rho)
            assert len(roots)==closed_count(mu,rho),(mu,rho,len(roots),closed_count(mu,rho))
            for r in roots:
                assert abs(abs(lam(r,mu))-rho)<2e-12
            count_checks+=1

    # Tangencies: the m-th lobe exactly touches the threshold and adds no pair.
    tangency_checks=0
    for mu in (1.3,3.0,7.5):
        for m in (1,2,3):
            rho=math.exp(-m*math.pi/mu)
            expected=2*m-1
            assert closed_count(mu,rho)==expected
            peak=m*math.pi/mu
            assert abs(abs(lam(peak,mu))-rho)<2e-15
            eps=min(1e-4, 0.01/mu)
            assert abs(lam(peak-eps,mu))<rho
            assert abs(lam(peak+eps,mu))<rho
            tangency_checks+=1

    # Source Figure 1 examples.
    a=1.0
    tau=5.0
    mu=math.sqrt((4*a*tau)**2-1)
    examples=[
        (1.0,0.6,3),
        (0.35,0.1,7),
    ]
    source_checks=0
    for M,c3,expected in examples:
        rho=math.sqrt(c3/M)
        roots=independent_roots(mu,rho)
        assert len(roots)==expected
        assert closed_count(mu,rho)==expected
        source_checks+=1

    print("VERIFY_OK")
    print("derivative_checks =",derivative_checks)
    print("revival_peak_checks =",peak_checks)
    print("independent_root_count_cases =",count_checks)
    print("tangency_cases =",tangency_checks)
    print("source_example_cases =",source_checks)
    for M,c3,expected in examples:
        rho=math.sqrt(c3/M)
        roots=independent_roots(mu,rho)
        print("source_count",M,c3,"=",len(roots),"roots =",",".join(f"{x:.12f}" for x in roots))

if __name__=="__main__":
    main()
