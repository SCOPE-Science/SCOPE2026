"""Independent numerical and finite-rational tests for product-cap spherical concentration.
Dependencies: Python >=3.10, numpy, scipy. Analytical proof is in RESULT.md.
"""
import math
from fractions import Fraction
from scipy.integrate import quad
from scipy.special import beta, betainc
from scipy.stats import chi2

NTESTS=0

def check(cond,msg):
    global NTESTS
    NTESTS+=1
    if not cond: raise AssertionError(msg)

def concentration_su(n,d,a,b,t):
    s=a+b; gamma=n+d-s-2
    assert n>=3 and d>=s and gamma>=1 and 0<t<0.25
    low=2*math.sqrt(t)
    def integrand(S):
        u=(1-math.sqrt(max(0,1-4*t/S**2)))/2
        center=betainc(a+1,b+1,1-u)-betainc(a+1,b+1,u)
        return S**(s+1)*(1-S)**(gamma-1)*center/beta(s+2,gamma)
    return quad(integrand,low,1,epsabs=3e-11,epsrel=5e-11,limit=150)[0]

def concentration_x(n,d,a,b,t):
    gamma=n+d-a-b-2
    lo=(1-math.sqrt(1-4*t))/2
    hi=(1+math.sqrt(1-4*t))/2
    def integrand(x):
        z=min(1.0,t/(x*(1-x)))
        conditional=betainc(gamma,b+1,1-z) # 1-I_z(beta,gamma)
        return x**a*(1-x)**(b+gamma)*conditional/beta(a+1,b+gamma+1)
    return quad(integrand,lo,hi,epsabs=3e-11,epsrel=5e-11,limit=150)[0]

def frac_beta_center(s,a,u):
    N=s+1
    def cdf(z):
        return sum(Fraction(math.comb(N,k))*z**k*(1-z)**(N-k) for k in range(a+1,N+1))
    return cdf(1-u)-cdf(u)

for s in range(1,13):
    for a in range(s):
        u=Fraction(1,5)
        diff=frac_beta_center(s,a+1,u)-frac_beta_center(s,a,u)
        check((diff>0)==(2*(a+1)<s+1) if 2*(a+1)!=s+1 else diff==0,
              f'beta transfer wrong s={s} a={a}')

for n in (3,4,6):
    for d in (2,3,4,5,7):
        r=d//2
        for t in (0.007,0.045,0.13,0.21):
            v={(a,b):concentration_su(n,d,a,b,t) for a in range(d+1) for b in range(d-a+1)}
            for (a,b),value in v.items():
                check(abs(value-concentration_x(n,d,a,b,t))<3e-8, f'independent integration mismatch n,d,a,b,t={n,d,a,b,t}')
                check(-1e-12<=value<=1+1e-12,f'out of range {n,d,a,b,t}')
                check(abs(value-v[(b,a)])<2e-10,f'asymmetry {n,d,a,b,t}')
            top=v[(r,d-r)]
            top_set={(r,d-r),(d-r,r)}
            for k,value in v.items():
                if k not in top_set:check(top>value+1e-12,f'not unique top n,d,k,t={n,d,k,t}')
            if d%2==0:
                runner=v[(r-1,r+1)]
                for k,value in v.items():
                    if k not in top_set:check(runner>=value-2e-10,f'even runner fails {n,d,k,t}')
            else:
                A=v[(r-1,r+2)];B=v[(r,r)]
                runner=max(A,B)
                for k,value in v.items():
                    if k not in top_set:check(runner>=value-2e-10,f'odd runner fails {n,d,k,t}')

for n in (3,4,8):
    for d in (3,5,7):
        r=d//2
        small=0.0001;large=0.2
        A0=concentration_su(n,d,r-1,r+2,small)
        B0=concentration_su(n,d,r,r,small)
        A1=concentration_su(n,d,r-1,r+2,large)
        B1=concentration_su(n,d,r,r,large)
        check(B0>A0,f'odd small cap branch failure n={n},d={d}')
        check(A1>B1,f'odd edge branch failure n={n},d={d}')

for n in (3,4,6):
    c=1.0
    target=chi2.cdf(4*c,2*n-3)
    errors=[]
    for d in (200,700):
        r=d//2
        l=concentration_su(n,d,r,d-r,0.25-c/d)
        errors.append(abs(l-target))
    check(errors[1]<errors[0]+0.0005,f'edge convergence n={n} err={errors}')
    check(errors[1]<0.012,f'edge agreement n={n} err={errors}')

print(f'PASS {NTESTS} independently checked assertions')
print('checked independent x and (S,U) integration, eigenvalue ordering, parity-dependent runner-up, small/edge branch crossover and chi-square scaling')
