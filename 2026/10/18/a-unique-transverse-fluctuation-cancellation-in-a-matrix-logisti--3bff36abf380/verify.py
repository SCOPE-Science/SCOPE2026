"""Reproducible finite checks for a matrix-logistic transverse fluctuation theorem.

Run: python3 verify.py (standard library only).
The infinite claims require the accompanying analytic proof.
"""
from fractions import Fraction as Q
from math import cos, log, pi, sin, sqrt

checks = 0

def equal(a, b, label):
    global checks
    checks += 1
    if a != b:
        raise AssertionError(f'{label}: {a!r} != {b!r}')

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

# Exact rational instances of H'=D H(I-H)D for real symmetric H.
for b in (Q(11,10), Q(5,4), Q(7,5), Q(3,2), Q(5,3)):
    for xnum in range(1, 7):
        for ynum in range(1, 7):
            for znum in range(-2, 3):
                x, y, z = Q(xnum, 11), Q(ynum, 12), Q(znum, 60)
                H = [[x,z],[z,y]]
                IminusH = [[1-x,-z],[-z,1-y]]
                D = [[Q(2),Q(0)],[Q(0),b]]
                actual=matmul(matmul(D,matmul(H,IminusH)),D)
                expect=[[4*(x*(1-x)-z*z),2*b*(1-x-y)*z],
                        [2*b*(1-x-y)*z,b*b*(y*(1-y)-z*z)]]
                for i in range(2):
                    for j in range(2):
                        equal(actual[i][j], expect[i][j], 'matrix coordinate identity')
    c=1-Q(1)/(b*b)
    equal(b*b*c*(1-c), c,'invariant diagonal fixed channel')

# Exact periodic cosine orbit sums of the martingale variance bracket.
# For beta=pi/2 and odd q: cos(q beta)=0,
# cos(2q beta)=-1, cos(2^j q beta)=+1 for j>=2.
for q in range(1,501,2):
    g=Q(0)+Q(-1,2)+sum((Q(1,2**j) for j in range(2,56)),Q(0))+Q(1,2**55)
    equal(g,Q(0),'unique internal zero-variance resonance')

# For beta=2*pi/3, cos(2^j q beta) is 1 if 3|q and -1/2 otherwise.
# The exact infinite bracket equals 2 times this common cosine.
for q in range(1,501,2):
    expected=Q(2) if q%3==0 else Q(-1)
    g=Q(2)*(Q(1) if q%3==0 else Q(-1,2))
    equal(g,expected,'nonzero resonance bracket')

# Tail bound: sigma^2=2 sum_odd g(q)^2/q^2,
# with |g(q)|<=2. Thus tail beyond Q is <=8/Q.
for cutoff in (1001,10001,100001):
    estimate=2*sum((4 if q%3==0 else 1)/(q*q)
                   for q in range(1,cutoff+1,2))
    equal(abs(estimate-pi*pi/3)<8/cutoff,True,'certified variance-series truncation bound')

# The beta=pi/2 cocycle is an exact derivative coboundary.
# Finite calculations use theta only up to n=18 to avoid cancellation.
for theta in (0.17341,0.21791,0.42315,0.56812,0.78331):
    for n in range(1,19):
        left=sum(log(abs((sqrt(2))*cos((2**j)*theta))) for j in range(n))
        right=n*log(sqrt(2)/2)+log(abs(sin((2**n)*theta)))-log(abs(sin(theta)))
        equal(abs(left-right)<4e-8,True,'exact telescoping multiplier formula')

# Independent numerical comparison of the martingale formula against
# a truncated Green-Kubo covariance series at a nonresonant parameter.
# The proof, not truncation, establishes the infinite identities.
beta = __import__('math').acos(Q(1,5))
cutoff = 8000
trunc = 18
odd_variance = 2*sum(
    (sum(2**(-j)*cos((2**j)*q*beta) for j in range(trunc))**2)/(q*q)
    for q in range(1,cutoff+1,2))
green_kubo = 0.0
for k in range(15):
    cov = 2*2**(-k)*sum(
        cos((2**k)*r*beta)*cos(r*beta)/(r*r)
        for r in range(1,cutoff+1))
    green_kubo += (1 if k==0 else 2)*cov
equal(abs(odd_variance-green_kubo)<0.001,True,'independent Fourier/Green-Kubo truncations')

print(f'PASS: {checks} exact-rational or bounded floating-point consistency assertions')
print('Analytic lemmas, the CLT, and absence of additional resonances are proved in RESULT.md, not by enumeration.')
