"""Reproducible numerical and exact checks for the crosspolytope centroid support theorem.
The universal assertions are proved analytically; the checks verify algebra and samples.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.integrate import quad
from scipy.special import gammaln

# Exact ratio-squared recurrence: (a_{d+1}/a_d)^2 = 1 + 1/(4d(d+1)).
for d in range(1,80):
    lhs=Fraction((2*d+1)**2, 4*d*(d+1))
    rhs=Fraction(1,1)+Fraction(1,4*d*(d+1))
    assert lhs==rhs and lhs>1
print('EXACT_MONOTONE_RADIUS_RATIO_RECURRENCE_PASSED 79')


def support(s):
    d=len(s)
    def f(t):
        if t==0: return 0.0
        z=sum(math.log1p(t*t*x) for x in s)
        return -math.expm1(-z)/(t*t)
    return (2/(math.pi*(d+1)))*quad(f,0,math.inf,epsabs=2e-11,epsrel=2e-11,limit=300)[0]


def balanced(d):
    return (2*math.sqrt(d/math.pi)*math.exp(gammaln(d+0.5)-gammaln(d+1)))/(d+1)


for d in range(2,13):
    axis=[1.]+[0.]*(d-1)
    diag=[1./d]*d
    assert abs(support(axis)-1/(d+1))<5e-11,(d,support(axis))
    assert abs(support(diag)-balanced(d))<5e-11
print('INDEPENDENT_FOURIER_QUADRATURE_ENDPOINTS_PASSED 11')

# A T-transform toward balance must increase h strictly.
rng=np.random.default_rng(160217)
count=0
for d in (2,3,4,5,7,10):
    for _ in range(32):
        s=rng.dirichlet(np.ones(d))
        i,j=rng.choice(d,size=2,replace=False)
        if s[i] < s[j]: i,j=j,i
        if abs(s[i]-s[j])<1e-7: continue
        a=rng.uniform(.05,.45)
        t=s.copy()
        t[i]-=a*(s[i]-s[j]);t[j]+=a*(s[i]-s[j])
        assert support(t)>support(s)+1e-12,(s,t)
        count+=1
print('INDEPENDENT_STRICT_BALANCING_COMPARISONS_PASSED',count)

for a in (0.,.05,.125,.25,.41,1/math.sqrt(2)):
    b=math.sqrt(max(0.,1.-a*a))
    exact=(a*a+a*b+b*b)/(3*(a+b))
    actual=support([a*a,b*b])
    assert abs(actual-exact)<1e-10,(a,b,exact,actual)
print('INDEPENDENT_TWO_DIMENSIONAL_ABSOLUTE_MOMENT_PASSED 6')

# Exact local stability Hessian computed through beta integral.
for d in (2,3,5,9):
    c=d**1.5*math.exp(gammaln(d+.5)-gammaln(d+2))/(4*math.sqrt(math.pi)*(d+1))
    delta=np.zeros(d);delta[0]=1.;delta[1]=-1.
    for eps in (1e-2,1e-3):
        s=np.ones(d)/d+eps*delta
        deficit=balanced(d)-support(s)
        assert abs(deficit/(2*eps*eps)/c-1)<.015,(d,eps,deficit,c)
print('LOCAL_RIGIDITY_HESSIAN_QUADRATURE_PASSED 8')

for d in (2,3,4,5,8):
    for _ in range(20):
        s=rng.dirichlet(np.ones(d))
        deficit=balanced(d)-support(s)
        lower=sum((s-1/d)**2)/(12*math.pi*math.e*(d+1))
        assert deficit+1e-11>=lower,(d,s,deficit,lower)
print('GLOBAL_RIGIDITY_INEQUALITY_DIAGNOSTICS_PASSED 100')

for d in (2,3,5,7):
    signs=rng.choice([-1,1],size=(250000,d))
    exponential=rng.exponential(size=(250000,d+1))
    X=signs*exponential[:,1:]/np.sum(exponential,axis=1)[:,None]
    weights=rng.normal(size=d);weights/=np.linalg.norm(weights)
    estimate=np.mean(np.abs(X@weights))
    target=support(weights**2)
    assert abs(estimate-target)<.007,(d,estimate,target)
print('INDEPENDENT_UNIFORM_CROSSPOLYTOPE_MONTE_CARLO_PASSED 4')
print('ALL_CHECKS_PASSED')
