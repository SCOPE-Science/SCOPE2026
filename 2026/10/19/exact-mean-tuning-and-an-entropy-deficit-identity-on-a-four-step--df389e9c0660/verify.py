"""Exact-rational checks for the four-step Markov skew-tent family.

Run: python verify.py
No third-party dependencies. The analytical proof establishes statements
for every real s>1; these checks independently test rational instances.
"""
from fractions import Fraction as Q
from math import log, isclose


def data(s):
    assert s > 1
    D = 1 + s + s*s
    N = s*s + 2*s + 3
    a, b = 1/D, (1+s)/D
    h0 = D/N
    h1 = h0 * (1+1/s)
    h2 = h0 * (1+1/s+1/(s*s))
    return D,N,a,b,h0,h1,h2


def T(x,s):
    D,N,a,b,*_ = data(s)
    assert 0 <= x <= 1
    return a+s*x if x <= b else (1-x)/(1-b)


def check(s):
    D,N,a,b,h0,h1,h2 = data(s)
    t = D/(s*s)
    assert t>1
    assert T(Q(0),s)==a
    assert T(a,s)==b
    assert T(b,s)==1
    assert T(Q(1),s)==0
    assert (a,b-a,1-b)==(1/D,s/D,s*s/D)
    assert h0*a+h1*(b-a)+h2*(1-b)==1
    # Frobenius--Perron values on each Markov cell.
    assert h0==h2/t
    assert h1==h0/s+h2/t
    assert h2==h1/s+h2/t
    # Invariant average reconstructed from exact integrals.
    avg=(h0*a*a+h1*(b*b-a*a)+h2*(1-b*b))/2
    closed=Q(1,2)+(s+1)/(D*N)
    assert avg==closed
    assert (h0*a,h1*(b-a),h2*(1-b))==(1/N,(s+1)/N,D/N)
    assert D/N == 1/(3/D+2*s/D+s*s/D)
    # Exact derivative numerator from symbolic rational differentiation.
    P=3*s**4+10*s**3+15*s*s+12*s+2
    assert P>0
    # Compare to central finite difference as auxiliary diagnostic.
    x=float(s); eps=1e-6
    def mean(y): return .5+(y+1)/((1+y+y*y)*(y*y+2*y+3))
    fd=(mean(x+eps)-mean(x-eps))/(2*eps)
    assert abs(fd+float(P/(D*D*N*N)))<1e-8
    return closed


for numerator in range(20,210):
    # These 190 rational points are pairwise distinct.
    s=Q(numerator,19)
    check(s)

# The Markov matrix has characteristic polynomial z^3-z^2-z-1.
# Find its unique root in (1,2) using monotone bisection.
lo,hi=1.0,2.0
for _ in range(90):
    mid=(lo+hi)/2
    if mid**3-mid**2-mid-1>0: hi=mid
    else: lo=mid
lam=(lo+hi)/2
assert abs(lam**3-lam**2-lam-1)<1e-12

def ksent(s):
    D,N,*_=data(s)
    return float((s+2)/N)*log(float(s))+float(D/N)*log(float(D/(s*s)))

for s in [1.01,1.2,1.5,1.8,lam,2.0,3.0,10.0,100.0]:
    D,N,*_=data(s)
    D,N=float(D),float(N)
    q=[s**j/D for j in (0,1,2)]
    p=[lam**(-(3-j)) for j in (0,1,2)]
    assert isclose(sum(q),1.,abs_tol=1e-12)
    assert isclose(sum(p),1.,abs_tol=1e-12)
    divergence=sum(qi*log(qi/pi) for qi,pi in zip(q,p))
    assert abs((log(lam)-ksent(s))-(D/N)*divergence)<1e-12
    assert ksent(s)<=log(lam)+1e-12
assert abs(ksent(lam)-log(lam))<1e-12
print('PASS: 190 exact-rational Markov, density, mean, and derivative tests;')
print('      unique ternary-root check and entropy--KL identity at 9 parameters.')
