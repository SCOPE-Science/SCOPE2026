"""Rational cross-orbit collision-kernel verification (standard library only)."""
from fractions import Fraction as Q
from math import log


def b2_periodic(t):
    z = t - (t.numerator // t.denominator)
    return z*z-z+Q(1,6)


def kernel_bernoulli(m, r):
    return (b2_periodic((m-1)*r)-b2_periodic((m+1)*r))/m


def intersection(lo, hi, a, b):
    return max(Q(0),min(hi,b)-max(lo,a))


def kernel_geometric(m, r):
    both=Q(0)
    for k in range(m+1):
        a=max(Q(0),(Q(k)-r)/m)
        b=min(Q(1),(Q(k)+r)/m)
        if a<b:
            both += intersection(a,b,Q(0),r)+intersection(a,b,1-r,Q(1))
    return both-4*r*r


def exact_variance(b,N,s):
    r=Q(s,N)
    return kernel_bernoulli(1,r)+sum((Q(2)*(N-h)**2/Q(N*N))*kernel_bernoulli(b**h,r) for h in range(1,N))


def float_variance(b,N,s):
    r=s/N
    def B(t):
        z=t-int(t)
        return z*z-z+1/6
    # modular reduction prior to division avoids loss of precision at large m
    def c(h):
        if h>120: return 0.0  # tail bounded by 4*r*b**(-120)/(b-1)
        m=b**h
        v1=((m-1)*s)%N / N
        v2=((m+1)*s)%N / N
        return (B(v1)-B(v2))/m
    return 2*r*(1-2*r)+2*sum((1-h/N)**2*c(h) for h in range(1,N))


def run():
    tests=0
    for m in range(1,22):
        for den in [5,7,11,13]:
            for numerator in range(1,(den+1)//2):
                r=Q(numerator,den)
                a,b=kernel_geometric(m,r),kernel_bernoulli(m,r)
                assert a==b,(m,r,a,b)
                tests+=1
    for b in [2,3]:
        for N in [3,4,5,6,8]:
            if N<=2:continue
            v=exact_variance(b,N,1)
            assert v>=0,(b,N,v)
            assert abs(float(v)-float_variance(b,N,1))<1e-12,(b,N,v,float_variance(b,N,1))
            tests+=1
    for b in [2,3,4]:
        target=2*(b+1)/(b-1)
        for N in [100,300,1000]:
            val=N*float_variance(b,N,1)
            print('asymptotic',b,N,round(val,10),'target',round(target,10))
            assert abs(val-target)<max(0.13,5*log(N)/N*target)
            tests+=1
    for base in [2, 3, 4]:
        n=1000000
        leading=2*(base+1)/(base-1)
        scaled=(leading-n*float_variance(base,n,1))*n/log(n,base)
        print('logarithmic_correction',base,round(scaled,9),'target',8)
        assert abs(scaled-8)<1.6
        tests+=1
    print('EXACT_RATIONAL_CHECKS_PASS',tests)

if __name__=='__main__':run()
