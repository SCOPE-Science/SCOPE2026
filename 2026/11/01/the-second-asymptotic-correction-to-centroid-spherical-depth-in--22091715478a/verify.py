"""Reproducible independent algebra and randomized consistency checks for the geometric asymptotic.
Run: python verify.py. Requires numpy; random checks use a fixed seed.
"""
from fractions import Fraction as Q
from math import log, sqrt, pi
import numpy as np

# Reconstruct exact coefficient from independently stated cumulant contractions.
mu2,mu3,mu4,mu5 = 1,2,9,44
b2, b3 = -1, -3*mu3
var2 = mu4-mu2*mu2
cov23 = mu5-4*mu2*mu3
# f(A,B)=A B^{-3/2}, expanded around (mu3,mu2).
fB=-Q(3,2)*mu3
fBB=Q(15,4)*mu3
fAB=-Q(3,2)
bias = b3 + fB*b2 + Q(1,2)*fBB*var2 + fAB*cov23
assert bias == -27, bias
coeff = bias/3 - Q(3,5)*mu5 + Q(5,4)*mu3*mu4 - Q(35,54)*mu3**3
assert coeff == -Q(4883,270), coeff
print('EXACT contraction: first 2/3, second', coeff)

rng=np.random.default_rng(20261030)
checks=0
# Direct simplicial dot product vs sample centered exponential product, for both signs.
for m in [3,4,7,11,23]:
    A=rng.exponential(size=(600,m));B=rng.exponential(size=(600,m))
    P=A/A.sum(axis=1,keepdims=True);Qp=B/B.sum(axis=1,keepdims=True)
    dot=np.sum((P-1/m)*(Qp-1/m),axis=1)
    cov=np.sum((A-A.mean(axis=1,keepdims=True))*(B-B.mean(axis=1,keepdims=True)),axis=1)
    assert np.array_equal(dot<=0,cov<=0)
    checks+=600
print('EXACT-EVENT simulation equivalences:',checks)

# The known regular triangle (m=3) exact answer supplies a distinct low-d check.
n=120000
A=rng.exponential(size=(n,3));B=rng.exponential(size=(n,3))
z=np.sum((A-A.mean(1,keepdims=True))*(B-B.mean(1,keepdims=True)),axis=1)
p=(z<=0).mean()
truth=1/3+log(3)/6
stderr=sqrt(.25/n)
assert abs(p-truth)<5*stderr, (p,truth,stderr)
print('TRIANGLE:', p, 'exact:',truth, 'difference in SE:', (p-truth)/stderr)

# Larger dimensions show the scale and sign. Monte Carlo tolerance is not used as a proof.
for m,n in [(100,30000),(300,25000),(1000,20000)]:
    negative=0
    for start in range(0,n,1000):
        s=min(1000,n-start)
        A=rng.exponential(size=(s,m)); B=rng.exponential(size=(s,m))
        cov=np.sum((A-A.mean(1,keepdims=True))*(B-B.mean(1,keepdims=True)),axis=1)
        negative+=np.count_nonzero(cov<0)
    p=negative/n
    approx=.5+(2/(3*sqrt(m))+float(coeff)/m**1.5)/sqrt(2*pi)
    stderr=sqrt(.25/n)
    assert abs(p-approx) < 5*stderr, (m,p,approx,stderr)
    print('DIM',m-1,'MC',round(p,7),'two-term',round(approx,7),'MC_stderr',round(stderr,7))
print('verification checks complete')
