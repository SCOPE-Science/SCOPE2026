from math import exp, lgamma, log, sqrt

def _betacf(a, b, x):
    max_iter = 500
    eps = 3e-14
    fpmin = 1e-300
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) <= eps:
            return h
    raise RuntimeError("beta continued fraction did not converge")

def betainc(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = exp(lgamma(a+b)-lgamma(a)-lgamma(b)+a*log(x)+b*log(1-x))
    if x < (a+1.0)/(a+b+2.0):
        return bt * _betacf(a,b,x)/a
    return 1.0 - bt * _betacf(b,a,1.0-x)/b

def gammap(a, x):
    if x <= 0.0:
        return 0.0
    eps = 3e-14
    if x < a + 1.0:
        ap = a
        term = 1.0/a
        total = term
        for _ in range(10000):
            ap += 1.0
            term *= x/ap
            total += term
            if abs(term) <= abs(total)*eps:
                return total * exp(-x + a*log(x) - lgamma(a))
        raise RuntimeError("gamma series did not converge")
    b = x + 1.0 - a
    c = 1.0/1e-300
    d = 1.0/b
    h = d
    for i in range(1,10000):
        an = -i*(i-a)
        b += 2.0
        d = an*d + b
        if abs(d) < 1e-300:
            d = 1e-300
        c = b + an/c
        if abs(c) < 1e-300:
            c = 1e-300
        d = 1.0/d
        delta = d*c
        h *= delta
        if abs(delta-1.0) <= eps:
            q = exp(-x + a*log(x) - lgamma(a))*h
            return 1.0-q
    raise RuntimeError("gamma continued fraction did not converge")

def f_cdf(x, d, m):
    if x <= 0:
        return 0.0
    y = d*x/(d*x+m)
    return betainc(d/2.0,m/2.0,y)

def chisq_cdf(x, d):
    return gammap(d/2.0,x/2.0)

def chisq_density(x,d):
    if x <= 0:
        return 0.0
    a=d/2.0
    return exp((a-1)*log(x)-x/2-a*log(2)-lgamma(a))

def f_central(d,m):
    mu=m/(m-2.0)
    var=2*m*m*(d+m-2.0)/(d*(m-2.0)**2*(m-4.0))
    sd=sqrt(var)
    return f_cdf(mu+sd,d,m)-f_cdf(max(0.0,mu-sd),d,m)

def chi_central(d):
    r=sqrt(2.0*d)
    return chisq_cdf(d+r,d)-chisq_cdf(d-r,d)

def coefficient(d):
    r=sqrt(2.0*d)
    return 2*r*(chisq_density(d+r,d)+chisq_density(d-r,d))

if __name__=="__main__":
    maxerr=0.0
    for d in (6,7,10,20,40):
        c0=chi_central(d)
        a=coefficient(d)
        assert a>0
        errs=[]
        for m in (2000,4000,8000):
            scaled=m*(f_central(d,m)-c0)
            err=abs(scaled-a)
            errs.append(err)
            maxerr=max(maxerr,err)
        assert errs[-1] < errs[0]
        assert errs[-1] < 0.01
        r=sqrt(2.0*d)
        for sign in (-1,1):
            t=d+sign*r
            b=2*d+sign*(d+6)*r/2
            bracket=b+(d/2-1)*t-t*t/2
            assert abs(bracket-sign*2*r)<1e-11
    print(f"VERIFY_OK max_scaled_error={maxerr:.12g}")
