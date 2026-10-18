"""Numerical checks for the confined, globally reset Ornstein--Uhlenbeck count edge.
Run: python verify.py
Only the analytic proof establishes the all-size statement.
"""
from math import erf, exp, sqrt, pi, floor, gamma
from scipy.integrate import quad
from scipy.stats import binom, norm

D=mu=a=1.0
b=a*sqrt(mu/(2*D))
p0=erf(b)
c=b*exp(-b*b)/sqrt(pi)
sigma=sqrt(p0*(1-p0))

def conditional_probability(v):
    # v=exp(-2*mu*age), so particle variance = (D/mu)*(1-v).
    if v>=1.0: return 1.0
    return erf(b/sqrt(1-v))

def edge_prob(n, beta, s=0):
    k=floor(n*p0+s*sqrt(n))
    # Substitute v = (w/sqrt(n)), then w=z^2 to handle beta<1.
    def integrand(z):
        w=z*z
        v=w/sqrt(n)
        return 2*beta*z**(2*beta-1)*binom.cdf(k,n,conditional_probability(v))
    # Gaussian concentration makes z above roughly 6 negligible.
    upper=min(n**.25,8.0)
    val=quad(integrand,0,upper,epsabs=1e-10,epsrel=5e-9,limit=200)[0]
    return n**(-beta/2)*val

def predicted(beta,s=0):
    if s==0:
        return (sigma/c)**beta*2**(beta/2-1)*gamma((beta+1)/2)/sqrt(pi)
    return beta*quad(lambda w:w**(beta-1)*norm.cdf((s-c*w)/sigma),0,30,
                    epsabs=1e-11,epsrel=1e-9)[0]

print('b, p*, c, sigma:',b,p0,c,sigma)
for beta in [.5,1.,2.]:
    target=predicted(beta)
    for n in [300,1500,6000]:
        val=edge_prob(n,beta)*n**(beta/2)
        print(f'beta={beta:g} N={n:5} scaled={val:.9g} target={target:.9g} ratio={val/target:.5f}')
for s in [-.3,.3]:
    beta=1.
    target=predicted(beta,s)
    val=edge_prob(6000,beta,s)*6000**(.5)
    print(f's={s:+.2f} beta=1 N=6000 scaled={val:.9g} limit={target:.9g} ratio={val/target:.5f}')
# Independent age-variable quadrature, compared with the beta-mixture quadrature.
from math import isclose
n=300; beta=1.0; r=2*mu*beta
k=floor(n*p0)
def by_age(t):
    v=exp(-2*mu*t)
    return r*exp(-r*t)*binom.cdf(k,n,conditional_probability(v))
check_age=quad(by_age,0,20,epsabs=1e-11,epsrel=1e-9,limit=150)[0]
check_beta=edge_prob(n,beta)
print('Independent age integral vs transformed beta integral:',check_age,check_beta)
assert isclose(check_age,check_beta,rel_tol=1e-8,abs_tol=1e-10)
print('NUMERICAL CHECKS PASSED')
