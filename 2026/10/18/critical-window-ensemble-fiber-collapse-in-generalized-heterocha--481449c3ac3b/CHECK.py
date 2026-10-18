"""Reproducibility checks for central-fiber excursion and crossover laws.
Uses only Python standard library; finite tests are not proofs of asymptotics.
"""
from fractions import Fraction
from math import comb, exp, lgamma, log, sqrt, erf, pi
from random import Random

def walk_distribution(n,p):
    v=[Fraction(1)]
    for _ in range(n):
        w=[Fraction(0)]*(len(v)+1)
        for j,mass in enumerate(v):
            w[j+1]+=p*mass
            w[max(0,j-1)]+=(1-p)*mass
        v=w
    return v

def walk_end(n,p,k):
    if abs(k)>n or (n+k)%2: return Fraction(0)
    t=(n+k)//2
    return Fraction(comb(n,t))*p**t*(1-p)**(n-t)

def mass_formula(n,p,j):
    q=1-p
    z=q/p
    swapped_tail=sum((walk_end(n,q,k) for k in range(j+2,n+1)))
    return walk_end(n,p,j)+z*walk_end(n,p,j+1)+(z-1)*z**(-j-1)*swapped_tail

for p in [Fraction(1,5),Fraction(2,5),Fraction(1,2),Fraction(3,5),Fraction(4,5)]:
    for n in range(15):
        exact=walk_distribution(n,p)
        assert sum(exact)==1
        assert all(x==mass_formula(n,p,j) for j,x in enumerate(exact)),(n,p)
        if p==Fraction(1,2):
            assert all(x==Fraction(comb(n,(n-j)//2),2**n) for j,x in enumerate(exact))
print('EXACT_RATIONAL_REFLECTION_AND_BINOMIAL_IDENTITIES_PASS')

# Independently track M-adic images of a whole fiber for finite symbol words.
for M in [2,3,5]:
    rng=Random(673+M)
    for repeat in range(80):
        lo=Fraction(0); length=Fraction(1); depth=0
        for _ in range(60):
            if rng.randrange(2):  # one of the M narrow base branches
                i=rng.randrange(M)
                lo=(lo+i)/M
                length/=M
                depth+=1
            else:                  # wide base branch, beta partition
                if depth:
                    i=int(M*lo)
                    lo=M*lo-i
                    length*=M
                    depth-=1
                else:
                    lo=Fraction(0);length=Fraction(1)
            assert length==Fraction(1,M**depth)
            assert 0<=lo<=1-length
print('GEOMETRIC_M_ADIC_FIBER_REDUCTION_PASS')

def normal_cdf(x): return (1+erf(x/sqrt(2)))/2

def transition_constant(eta):
    mu=2*eta
    return 2*exp(-mu*mu/2)/sqrt(2*pi)-4*eta*normal_cdf(-mu)

def binom_pmf(n,k,p):
    if k<0 or k>n: return 0.
    return exp(lgamma(n+1)-lgamma(k+1)-lgamma(n-k+1)+k*log(p)+(n-k)*log(1-p))

def finite_boundary_mass(n,eta):
    p=.5+eta/sqrt(n);q=1-p;z=q/p
    a=binom_pmf(n,n//2,p) if n%2==0 else 0.
    b=binom_pmf(n,(n+1)//2,p) if n%2 else 0.
    tail=sum(binom_pmf(n,k,q) for k in range((n+2+1)//2,n+1))
    return a+z*b+(z-1)/z*tail

for eta in [-.7,-.2,0.,.25,.7]:
    n=12000
    v=sqrt(n)*finite_boundary_mass(n,eta)
    c=transition_constant(eta)
    assert abs(v-c)<.08*max(c,.02),(eta,v,c)
print('CRITICAL_WINDOW_BOUNDARY_LOCAL_LIMIT_NUMERIC_PASS')
for M in [2,3,5]:
    n=16000
    # For j<=75, only one central binomial endpoint matches each parity.
    p=.5
    e=0.
    for j in range(75):
        k=(n+j)//2
        if (n+j)%2: k=(n+j+1)//2
        e+=M**(-j)*binom_pmf(n,k,p)
    target=sqrt(2/pi)/(1-1/M)
    assert abs(sqrt(n)*e-target)<.012*target,(M,e,target)
print('CRITICAL_MEAN_WIDTH_CONSTANT_NUMERIC_PASS')
