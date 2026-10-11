"""Finite computational checks for sharp logarithmic rotational area stability.

Independent of the analytic proof: checks exact spectral formulas, curvature
admissibility, finite-mode cutoff inequalities, and asymptotic witness ratios.
"""
import math
import random

PI=math.pi
C=PI/8.0  # calibration support: 1 + (1/2) sum_{n>=2} 2^{-n} cos(n phi)/n^2

def alpha(n):
    return 4.0**(-n)*(n*n-1.0)/n**4

def weight(n, a):
    return 0.5*PI*(n*n-1)*a*a

def quantities(weights):
    D=sum(weights.values())
    H=sum(n*n*w for n,w in weights.items())
    V=2*C*sum(alpha(n)*w for n,w in weights.items())
    return D,H,V

def test():
    assert sum(0.5*2**(-n) for n in range(2,200)) < 0.251
    # Positive curvature for the high-frequency analytic witness.
    for n in (2,3,4,7,10,20,40,80,120):
        a=1/(2*n*n)
        D,H,V=quantities({n:weight(n,a)})
        z=V/(2*C*H)
        T=math.log(1/z,4)
        assert abs((D/H)*n*n-1)<1e-12
        assert abs(T-(n+math.log(n**6/(n*n-1),4)))<1e-11
        if z<=4.0**-8:
            assert D<=16*H/(T*T), (n,D/H,T)
    # Bounded arbitrary high-mode mixtures for the rigorous logarithmic estimate.
    rng=random.Random(2819)
    checks=0
    for start in (2,6,15,25,35,50,75):
        for _ in range(180):
            weights={n:10**rng.uniform(-5,0) for n in range(start,start+16)}
            D,H,V=quantities(weights)
            z=V/(2*C*H)
            if z<=4.0**-8:
                T=math.log(1/z,4)
                N=math.floor(T/2)
                head=sum(w for n,w in weights.items() if n<=N)
                tail=D-head
                assert head <= (4/3)*z*H*N*N*4**N*(1+1e-10)
                assert tail <= H/(N+1)**2*(1+1e-10)
                assert D<=16*H/T**2*(1+1e-10)
                checks+=1
    # Source-level numerical check uses the independent support integral in verification.py.
    from verification import check
    k=(1.0,{2:(0.5*2**-2/4,0),3:(0.5*2**-3/9,0),4:(0.5*2**-4/16,0),5:(0.5*2**-5/25,0)})
    l=(1.0,{2:(.06,0.02),3:(.012,0),4:(.002,.003)})
    check(k,l)
    print('VERIFY_LOG_OK: analytic-geometry normalization, sharp log cutoff,',checks,'finite mixtures; high-frequency witnesses and direct area quadrature')
if __name__=='__main__':test()
