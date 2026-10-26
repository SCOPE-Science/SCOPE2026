"""Standalone finite checks for exact joint busy-period inference.

Analytic proofs of the unbounded sums, asymptotics, and sufficiency
are in RESULT.md; the tests below are finite corroboration only.
"""
import math
import random
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import gammainc, gammaincc
from scipy.stats import gamma

checks = 0

def check(condition, label):
    global checks
    assert condition, label
    checks += 1

def raney(k, s):
    return Fraction(k * math.comb(2 * s + k, s), 2 * s + k)

def weight(k, s, theta, mu):
    q = theta + mu
    return math.exp(math.log(k)-math.log(2*s+k)+math.lgamma(2*s+k+1)
                    -math.lgamma(s+1)-math.lgamma(s+k+1)
                    +(s+k)*math.log(mu/q)+s*math.log(theta/q))

def test_errors(k, theta0, theta1, mu, smax=300):
    a = math.log(theta1/theta0)/(theta1-theta0)
    alpha=beta=0.0
    for s in range(smax):
        gshape=2*s+k
        alpha += weight(k,s,theta0,mu)*gammainc(gshape, (theta0+mu)*a*s)
        beta += weight(k,s,theta1,mu)*gammaincc(gshape, (theta1+mu)*a*s)
    return alpha,beta

# Direct Catalan path counting (independent from generalized ballot formula).
def paths(j):
    out=0
    def rec(height, ups, downs):
        nonlocal out
        if ups==j-1 and downs==j:
            if height==0:out+=1
            return
        if ups<j-1:rec(height+1,ups+1,downs)
        if height>0 and downs<j:
            if height>1 or downs+1==j:rec(height-1,ups,downs+1)
    rec(1,0,0)
    return out

for j in range(1,11):
    check(paths(j)==math.comb(2*j-2,j-1)//j, f'Catalan paths j={j}')
for s in range(0,13):
    c=[math.comb(2*j,j)//(j+1) for j in range(s+1)]
    for k in range(1,8):
        poly=[1]+[0]*s
        for _ in range(k):
            poly=[sum(poly[i]*c[t-i] for i in range(t+1)) for t in range(s+1)]
        check(raney(k,s).denominator==1 and poly[s]==int(raney(k,s)),f'Raney k={k},s={s}')

for theta,mu in [(0.7,2.1),(1.0,3.0),(2.0,2.5)]:
    for k in [1,2,4,6]:
        ps=[weight(k,s,theta,mu) for s in range(2200)]
        # Heavy loading requires longer sum; only verify if tail safely small.
        if theta/mu<0.8:
            check(abs(sum(ps)-1.0)<5e-11,'count normalization')
        if k==1 and theta/mu<0.8:
            m=sum(s*p for s,p in enumerate(ps))
            check(abs(m-theta/(mu-theta))<1e-9,'mean number of arrivals')

for theta0,theta1,mu in [(1,1.25,3),(0.5,0.6,2),(2,2.05,5)]:
    d=(theta1-theta0-theta0*math.log(theta1/theta0))/(mu-theta0)
    dcount=((mu+theta0)*math.log((mu+theta1)/(mu+theta0))
            -theta0*math.log(theta1/theta0))/(mu-theta0)
    gap=(mu+theta0)/(mu-theta0)*(
        (theta1-theta0)/(mu+theta0)-math.log((mu+theta1)/(mu+theta0)))
    check(abs(d-dcount-gap)<5e-14,'finite KL decomposition')
    check(gap>0,'strict info gap')
    ps=[weight(1,s,theta0,mu) for s in range(700)]
    joint_score_sq=sum(p*((s/theta0-(2*s+1)/(mu+theta0))**2
                         +(2*s+1)/(mu+theta0)**2) for s,p in enumerate(ps))
    count_score_sq=sum(p*((s/theta0-(2*s+1)/(mu+theta0))**2)
                       for s,p in enumerate(ps))
    check(abs(joint_score_sq-1/(theta0*(mu-theta0)))<3e-12,'Fisher joint')
    check(abs(count_score_sq-mu/(theta0*(mu**2-theta0**2)))<3e-12,'Fisher count')

# A separate numerical integration of min(joint densities) validates the
# one-sided likelihood threshold and the optimal testing error series.
theta0,theta1,mu,k = 1.0,1.25,3.0,2
alpha,beta=test_errors(k,theta0,theta1,mu)
q=math.log(theta1/theta0)/(theta1-theta0)
overlap=0.0
for s in range(70):
    w0=weight(k,s,theta0,mu)
    w1=weight(k,s,theta1,mu)
    sh=2*s+k
    def minor(t):
        return min(w0*gamma.pdf(t,a=sh,scale=1/(mu+theta0)),
                   w1*gamma.pdf(t,a=sh,scale=1/(mu+theta1)))
    term=quad(minor,0,math.inf,epsabs=5e-14,epsrel=2e-10,limit=150)[0]
    overlap+=term
check(abs(alpha+beta-overlap)<3e-8,'NP error equals integrated minimum')
check(0<alpha+beta<1,'meaningful exact testing risk')
print('exact tests passed:',checks)
print('example (lambda0=1, lambda1=1.25, mu=3, k=2):')
print('  type I, type II, optimal total error:', alpha,beta,alpha+beta)
print('  joint KL per busy period:', (0.25-math.log(1.25))/2)
print('  paired covert constant:', mu*math.sqrt(2/(theta0*(mu-theta0))))
print('  count-only covert constant:', math.sqrt(2*mu*(mu+theta0)/(theta0*(mu-theta0))))
print('finite computational checks cannot establish the asymptotic theorem')
