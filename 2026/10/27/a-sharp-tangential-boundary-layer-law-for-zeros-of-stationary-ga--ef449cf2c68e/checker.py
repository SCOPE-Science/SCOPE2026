"""Exact finite-Fourier checks for a spectral-zero tangential crossover.
Only numerical corroboration; the limiting theorem has an analytic proof.
"""
import math


def moments(m, r, theta):
    ck = [(-1)**k * math.comb(2*m, m+k) for k in range(1,m+1)]
    u = math.comb(2*m,m) + 2*sum(c*r**k*math.cos(k*theta) for k,c in enumerate(ck,1))
    ur = 2*sum(k*c*r**(k-1)*math.cos(k*theta) for k,c in enumerate(ck,1))
    ut = -2*sum(k*c*r**k*math.sin(k*theta) for k,c in enumerate(ck,1))
    ratio = 1-(1-r*r)**2*(ur*ur+(ut/r)**2)/(4*u*u)
    return u,ur,ut,ratio


def main():
    count=0
    for m in (1,2,3):
        b=2*math.comb(2*m-2,m-1)
        ur = 2*sum(k*(-1)**k*math.comb(2*m,m+k) for k in range(1,m+1))
        assert math.isclose(-ur,b,rel_tol=1e-12,abs_tol=1e-12)
        count+=1
        for x in (0.5, 1., 2.):
            target=1-(b/(b+x**(2*m)))**2
            errs=[]
            for eps in (1e-3,2e-4,5e-5):
                theta=x*eps**(1/(2*m))
                u,ur,ut,s=moments(m,1-eps,theta)
                assert u>0 and -1e-6<=s<=1+1e-6
                errs.append(abs(s-target))
                count+=2
            assert errs[2]<errs[1]<errs[0]
            count+=1
    print(f"PASS: {count} finite-Fourier assertions; no infinite-proof certification")

if __name__ == '__main__':
    main()
