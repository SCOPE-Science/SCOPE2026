"""Reproducibility checks for the sharp odd-cycle negative-type asymptotic.

Uses only Python's standard library. Numerical tests support, but do not
replace, the analytic proof in RESULT.md.
"""
import math

PI=math.pi

def J2_series():
    # Integral int_0^(2*pi) (1-cos u)/u du, via entire power series.
    x=2*PI
    return math.fsum(((-1)**(j+1))*x**(2*j)/(2*j*math.factorial(2*j)) for j in range(1,27))

J2=J2_series()
C=2*PI**2/J2

def d(n,r):
    return min(r,n-r)

def fourier_multiplier(n,k,p):
    return 2*math.fsum((r**p)*math.cos(2*PI*k*r/n) for r in range(1,(n-1)//2+1))

def root_mode2(n):
    lo,hi=1.,1.6
    assert fourier_multiplier(n,2,lo)<0 and fourier_multiplier(n,2,hi)>0
    for _ in range(85):
        mid=(lo+hi)/2
        if fourier_multiplier(n,2,mid)>0:
            hi=mid
        else:
            lo=mid
    return (hi+lo)/2

def check_laplacian_identity(n,k,p):
    m=(n-1)//2
    a=m**p-(m-1)**p
    b=[(r+1)**p-2*r**p+(r-1)**p for r in range(1,m)]
    lhs=2+2*sum(b[r-1]*math.cos(2*PI*k*r/n) for r in range(1,m))-2*a*math.cos(2*PI*k*m/n)
    rhs=-4*math.sin(PI*k/n)**2*fourier_multiplier(n,k,p)
    return abs(lhs-rhs)

def main():
    print('J2=%.15f C=%.15f'%(J2,C))
    assert abs(C-8.097627356866537)<2e-11
    count=0
    for n in [5,7,9,11,15,31,51,101,201]:
        r=root_mode2(n)
        print('N=%d mode2_root=%.12f scaled=%.10f'%(n,r,n*n*(r-1)))
        for p in [1,1.001,1.1,1.4]:
            for k in range(1,(n-1)//2+1):
                err=check_laplacian_identity(n,k,p)
                assert err < 2e-8*max(1,n**p)
                count+=1
    for n in [101,201,401,801]:
        p_lo=1+(C-0.5)/n**2
        p_hi=1+(C+0.5)/n**2
        vals=[fourier_multiplier(n,k,p_lo) for k in range(1,(n-1)//2+1)]
        assert max(vals)<3e-6, (n,max(vals))
        assert fourier_multiplier(n,2,p_hi)>0, (n,fourier_multiplier(n,2,p_hi))
        print('N=%d lower_max=%.8g upper_mode2=%.8g'%(n,max(vals),fourier_multiplier(n,2,p_hi)))
        count+=len(vals)+1
    print('PASS %d finite checks (analytic argument establishes the infinite theorem)'%count)

if __name__=='__main__':main()
