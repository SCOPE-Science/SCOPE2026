"""Reproducibility checks for finite projective-cap Toeplitz spectra.

Run with Python 3.10+: python verify.py
No optional dependencies. Finite checks supplement, but do not replace,
the analytic binomial large-deviation proof in RESULT.md.
"""
import math
from fractions import Fraction


def beta_tail(a, b, t):
    """Exact rational beta(a,b) upper-tail integral, for integer a,b."""
    numerator = sum(((-1)**j) * math.comb(b-1, j) *
                    (Fraction(1) - t**(a+j)) / (a+j)
                    for j in range(b))
    denominator = Fraction(math.factorial(a-1)*math.factorial(b-1),
                           math.factorial(a+b-1))
    return numerator / denominator


def binomial_cdf(n, t, cutoff):
    return sum((math.comb(n,j)*t**j*(1-t)**(n-j)
                for j in range(cutoff+1)), Fraction(0))


def multiplicity(d, ell, m, k):
    return math.comb(k+ell-1,ell-1)*math.comb(m-k+d-ell-1,d-ell-1)


def rate_integrand(x, d, ell, t):
    if x <= 0:
        div = -math.log1p(-t)
    elif x >= 1:
        div = -math.log(t)
    else:
        div = x*math.log(x/t)+(1-x)*math.log((1-x)/(1-t))
    return x**(ell-1)*(1-x)**(d-ell-1)*div / (
        math.factorial(ell-1)*math.factorial(d-ell-1))


def predicted_rate(d, ell, t, steps=30000):
    # Composite midpoint rule; finite validation only.
    h=t/steps
    return h*sum(rate_integrand((j+.5)*h,d,ell,t)
                 for j in range(steps))


def log_cdf_prefixes(n,t):
    # Stable finite log-sum-exp of binomial masses.
    a=[math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)
       +j*math.log(t)+(n-j)*math.log1p(-t) for j in range(n+1)]
    out=[];v=-math.inf
    for z in a:
        v=max(v,z)+math.log1p(math.exp(-abs(v-z))) if v!=-math.inf else z
        out.append(min(v,0.0))
    return out


def scaled_negative_logdet(d,ell,t,m):
    values=log_cdf_prefixes(m+d-1,t)
    logdet=sum(multiplicity(d,ell,m,k)*values[k+ell-1]
               for k in range(m+1))
    return -logdet / m**d


def run():
    count=0
    for d in range(3,7):
        for ell in range(1,d):
            for t in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
                for m in range(0,7):
                    assert sum(multiplicity(d,ell,m,k)
                               for k in range(m+1)) == math.comb(m+d-1,d-1)
                    for k in range(m+1):
                        a=k+ell; b=m-k+d-ell
                        assert beta_tail(a,b,t) == binomial_cdf(m+d-1,t,a-1)
                        count+=1
    # An exact three-dimensional example: dimension of H_1 is three.
    d=3;ell=2;t=Fraction(1,2);m=1
    vals=[binomial_cdf(m+d-1,t,k+ell-1) for k in range(m+1)]
    product=Fraction(1)
    for k,v in enumerate(vals): product*=v**multiplicity(d,ell,m,k)
    assert product == Fraction(49,128)
    count+=1
    exact_rate=math.log(2)/6 - 5/48
    quadrature=predicted_rate(3,2,.5)
    assert abs(quadrature-exact_rate)<3e-10
    count+=1
    for d,ell,t in ((3,2,.5),(3,1,.5),(4,2,.3),(5,3,.6)):
        target=predicted_rate(d,ell,t)
        assert target>0
        e200=abs(scaled_negative_logdet(d,ell,t,200)-target)
        e700=abs(scaled_negative_logdet(d,ell,t,700)-target)
        assert e700 < e200
        assert e700/target < .10
        count+=3
    print('PASS:',count,'exact identities and supplementary asymptotic checks')

if __name__=='__main__': run()
