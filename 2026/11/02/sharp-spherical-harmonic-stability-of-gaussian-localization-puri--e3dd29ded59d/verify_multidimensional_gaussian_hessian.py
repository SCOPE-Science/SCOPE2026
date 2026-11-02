"""Independent finite numerical checks of the spherical Fourier multipliers and asymptotic constants.
Requires scipy, numpy. Run from its containing directory with python verify_multidimensional_gaussian_hessian.py.
"""
import math
from scipy.integrate import quad
from scipy.special import iv, ive, eval_gegenbauer, gamma


def sphere_area(k):
    return 2 * math.pi**((k+1)/2) / gamma((k+1)/2)


def multiplier_integral(N, m, t):
    alpha=(N-2)/2
    c0=eval_gegenbauer(m,alpha,1)
    fun=lambda s: math.exp(t*s)*eval_gegenbauer(m,alpha,s)*(1-s*s)**((N-3)/2)
    return sphere_area(N-2)*quad(fun,-1,1,epsabs=1e-11,epsrel=1e-11)[0]/c0


def multiplier_bessel(N,m,t):
    return (2*math.pi)**(N/2)*t**(1-N/2)*iv(m+N/2-1,t)


def gap(N,R):
    t=2*math.pi*R*R
    return R**(2*N-2)*(2*math.pi)**(N/2)*t**(1-N/2)*(ive(N/2,t)-ive(N/2+1,t))


def main():
    cnt=0
    for N in (4,6,8):
        for t in (0.2,1.3,4.0):
            for m in range(5):
                q=multiplier_integral(N,m,t)
                b=multiplier_bessel(N,m,t)
                assert abs(q-b)<3e-9*max(1,b),(N,t,m,q,b)
                cnt+=1
            assert all(multiplier_bessel(N,m,t)>multiplier_bessel(N,m+1,t) for m in range(7))
            cnt+=1
        for R in (0.025,0.05,0.10):
            v=math.pi**(N/2)/gamma(N/2+1)
            ans=2*math.pi*v*R**(2*N)
            assert abs(gap(N,R)/ans-1)<0.12
            cnt+=1
        for R in (30,60):
            expected=(N+1)/(4*math.pi)*R**(N-3)
            assert abs(gap(N,R)/expected-1)<0.003
            cnt+=1
    print(f'PASSED {cnt} finite multiplier, ordering, and asymptotic checks')

if __name__=='__main__': main()
