import math


def g_source(n, t, x):
    # x=c^2, t=T_{n-1}^2; algebraically equivalent to source eq. (41)
    return math.sqrt(x/(n+x)) * (1.0 + n / (((n+x)*(n-1))/t + x))**(n/2)


def g2_closed(n, t, x):
    a=n-1+t
    return x*(n+x)**(n-1)*a**n/(n*(n-1)+a*x)**n


def log_envelope(n, t):
    if t <= 1.0:
        return 0.0
    return 0.5*(n*math.log1p((t-1.0)/n)-math.log(t))


def barrier(n, alpha):
    target=-math.log(alpha)
    lo, hi=1.0, 2.0
    while log_envelope(n, hi*hi) < target:
        hi *= 2.0
    for _ in range(200):
        mid=(lo+hi)/2.0
        if log_envelope(n, mid*mid) < target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


def barrier_inf(alpha):
    # Solve (b^2-1)/2 - log b = -log(alpha), b>1.
    target=-math.log(alpha)
    lo, hi=1.0, 2.0
    def f(b):
        return 0.5*(b*b-1.0)-math.log(b)
    while f(hi) < target:
        hi *= 2.0
    for _ in range(200):
        mid=(lo+hi)/2.0
        if f(mid) < target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0


def main():
    for n,t,x in [(3,2.0,0.7),(5,8.0,3.0),(10,16.0,2.5),(20,1.2,40.0)]:
        a=g_source(n,t,x)
        b=math.sqrt(g2_closed(n,t,x))
        assert math.isclose(a,b,rel_tol=2e-13,abs_tol=2e-13), (n,t,x,a,b)

    for n,t in [(3,2.0),(5,4.0),(10,16.0),(50,3.0)]:
        xstar=n/(t-1.0)
        center=math.sqrt(g2_closed(n,t,xstar))
        left=math.sqrt(g2_closed(n,t,xstar*0.8))
        right=math.sqrt(g2_closed(n,t,xstar*1.2))
        assert center>left and center>right
        exact=math.exp(log_envelope(n,t))
        assert math.isclose(center,exact,rel_tol=2e-13,abs_tol=2e-13)

    for n,t in [(3,0.2),(10,1.0)]:
        vals=[g_source(n,t,x) for x in (1.0,10.0,100.0,1e5)]
        assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))
        assert vals[-1] < 1.0 and vals[-1] > 0.99

    alpha=0.05
    b10=barrier(10,alpha)
    assert abs(b10-3.852638236307639)<2e-12
    bins=[barrier(n,alpha) for n in (2,3,5,10,20,50,100)]
    assert all(bins[i]>bins[i+1] for i in range(len(bins)-1))
    binf=barrier_inf(alpha)
    assert abs(binf-3.0351224130285503)<2e-12
    assert all(b>binf for b in bins)
    null_limit=math.erfc(binf/math.sqrt(2.0))
    assert abs(null_limit-0.0024043807677837682)<2e-15
    print('VERIFY_OK')


if __name__=='__main__':
    main()
