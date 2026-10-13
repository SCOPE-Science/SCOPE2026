"""Standalone numerical and exact-rational checks for two-lag noisy iterations."""
from fractions import Fraction
from math import sqrt, isclose
import random
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def stable(a, p):
    f1, f2 = a*p, a*(1-p)
    return abs(f2)<1 and 1-f1-f2>0 and 1+f1-f2>0


def var(a, p):
    f1,f2 = a*p,a*(1-p)
    return (1-f2)/((1+f2)*((1-f2)**2-f1**2))


def opt(a):
    s=sqrt(1-a)
    return s/(1+s),1/((1-a)*(2-s)**2)


def check():
    num_exact=0
    for n in range(-59,20):
        a=Fraction(n,20)
        for j in range(0,51):
            p=Fraction(j,50)
            f1,f2=a*p,a*(1-p)
            charstable=stable(a,p)
            roots=np.roots([1,-float(f1),-float(f2)])
            rmax=max(abs(roots))
            if abs(rmax-1)>1e-8:
                assert charstable == (rmax<1)
            if charstable:
                v=var(a,p)
                assert v>0
                y0=f1*v/(1-f2)
                # Exact Yule-Walker equations, including the forcing variance.
                assert (v-f1*y0-f2*(f1*y0+f2*v)) == 1
                num_exact+=1
    rng=random.Random(4512)
    count_lyap=0
    for _ in range(1200):
        a=rng.uniform(-2.999,.999)
        p=rng.random()
        if not stable(a,p):continue
        f1,f2=a*p,a*(1-p)
        B=np.array([[f1,f2],[1,0.]])
        P=solve_discrete_lyapunov(B,np.diag([1.,0.]))
        assert isclose(P[0,0],float(var(a,p)),rel_tol=5e-8,abs_tol=1e-7)
        count_lyap+=1
    num_opt=0
    for i in range(1,999):
        a=-3+4*i/1000
        if abs(a)<1e-8:continue
        p,v=opt(a)
        assert stable(a,p)
        assert isclose(var(a,p),v,rel_tol=1e-9)
        for q in np.linspace(0.,1.,101):
            if stable(a,float(q)):
                assert var(a,float(q))>=v-1e-9
        num_opt+=1
    # Known nontrivial example, rational exact comparison.
    a=Fraction(3,4)
    assert var(a,Fraction(1,3)) == Fraction(16,9)
    assert var(a,Fraction(1,2)) > Fraction(16,9)
    for a in [-4.,-3.,1.,2.]:
        assert not any(stable(a,i/5000) for i in range(5001))
    for eps in [0.1,0.01,0.001]:
        a=-3+eps
        _,v=opt(a)
        assert abs(eps**2*v/4-1)<2*eps
    print('VERIFY_OK exact_stationary_cases=%d lyapunov_cases=%d optimality_grids=%d'%(num_exact,count_lyap,num_opt))

if __name__ == '__main__':check()
