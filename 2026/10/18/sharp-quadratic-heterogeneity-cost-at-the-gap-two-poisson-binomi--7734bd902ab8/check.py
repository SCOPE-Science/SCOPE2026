"""Standalone arithmetic checks for gap-two Bernoulli sensitivity identities.

Run using Python 3.10+ without third-party packages: python check.py
The tests verify finite coefficient identities, not the universal proof.
"""
from decimal import Decimal, getcontext
from math import isqrt

getcontext().prec = 80
D = Decimal
checks = 0

def verify(statement, msg):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(msg)

def parameters(k):
    d = max(2, (9 + isqrt(8*k+33))//8)
    t = (D((k+1)*(k+2))/D(d*(d-1))).sqrt()
    q = t/(1+t)
    B = D((d-2)*(d-3)) + D(4*(k-d+2))/t - D(k*(k-1))/(t*t)
    C = t*B/(4*D(k+d-1))
    return d,t,q,B,C

def distribution(probs):
    masses=[D(1)]
    for p in probs:
        output=[D(0)]*(len(masses)+1)
        for j,x in enumerate(masses):
            output[j] += x*(1-p)
            output[j+1] += x*p
        masses=output
    return masses

def atom(a,j):
    return a[j] if 0 <= j<len(a) else D(0)

for k in range(1,86):
    d,t,q,B,C = parameters(k)
    m=k+d
    b=distribution([q]*(m-2))
    full=distribution([q]*m)
    c=atom(full,k)
    alpha=atom(b,k+2)-2*atom(b,k+1)+2*atom(b,k-1)-atom(b,k-2)
    ratio=(1+t)**2*B/D(m*(m-1))
    verify(abs(c-atom(full,k+2))<D('1e-70'), ('boundary',k))
    verify(alpha>0, ('alpha sign',k))
    verify(abs(alpha/c-ratio)<D('1e-68'),('coefficient ratio',k))
    verify(abs(C-alpha*D(m)*q*(1-q)/(4*c))<D('1e-67'),('mean shift',k))
    z=min(q,1-q)/D(3)
    skew=distribution([q]*(m-2)+[q+z,q-z])
    verify(abs(atom(skew,k)-atom(skew,k+2)-alpha*z*z)<D('1e-68'),('exact pair',k))

for k in (1,2,8,24,50):
    d,t,q,B,C = parameters(k)
    m=k+d
    b=distribution([q]*(m-2))
    alpha=atom(b,k+2)-2*atom(b,k+1)+2*atom(b,k-1)-atom(b,k-2)
    v=[D(1),D(1),D(-2)]+[D(0)]*(m-3)
    epsilon=min(q,1-q)*D('0.000001')
    p=[q+epsilon*u for u in v]
    masses=distribution(p)
    gap=atom(masses,k)-atom(masses,k+2)
    quadratic=alpha*epsilon**2*D(3)
    verify(abs(gap/quadratic-D(1))<D('0.00001'),('isotropic Hessian',k))

for k in (10000,100000,1000000,100000000):
    d,t,q,B,C = parameters(k)
    verify(D('3.9')<B<D('4.1'),('shape limit',k))
    verify(abs(D(k).sqrt()*C-2*D(2).sqrt())<D('0.1'),('curvature limit',k))

print('PASS:',checks,'high-precision arithmetic checks')
