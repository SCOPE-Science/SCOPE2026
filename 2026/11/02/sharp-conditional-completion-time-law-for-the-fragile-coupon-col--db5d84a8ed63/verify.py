#!/usr/bin/env python3
"""Reproduce exact finite-size checks for conditional fragile coupon collection."""
from fractions import Fraction as F
from math import prod

checks=0

def require(expr, msg):
    global checks
    assert expr, msg
    checks += 1

def model_success(n,s):
    # One-step first-success recursion from the number of unseen types.
    u=F(1)
    for m in range(1,n+1):
        a=F(m,n)*s**(m-1)
        r=(1-F(m,n))*s**m
        u*=a/(1-r)
    return u

def ordinary_path_coeffs(n,s,K):
    # Direct DP on identities of seen types; no stage reduction.
    states={0:F(1)}
    out={}
    for t in range(1,n+K+1):
        next_states={}
        full=(1<<n)-1
        for mask,weight in states.items():
            for i in range(n):
                next_mask=mask | (1<<i)
                survival=s**(n-next_mask.bit_count())
                new_weight=weight*F(1,n)*survival
                if next_mask==full:
                    out[t]=out.get(t,F(0))+new_weight
                else:
                    next_states[next_mask]=next_states.get(next_mask,F(0))+new_weight
        states=next_states
    return out

def conditional_coeffs(n,s,K):
    # Independent-geometric convolution derived by conditioning on survival.
    coeff=[F(0)]*(K+1)
    coeff[0]=F(1)
    for m in range(1,n+1):
        r=(1-F(m,n))*s**m
        new=[F(0)]*(K+1)
        for a in range(K+1):
            if coeff[a]:
                for b in range(K+1-a):
                    new[a+b] += coeff[a]*(1-r)*r**b
        coeff=new
    return coeff

def exact_moments(n,s):
    r=[(1-F(m,n))*s**m for m in range(1,n+1)]
    return sum((v/(1-v) for v in r),F(0)),sum((v/(1-v)**2 for v in r),F(0))

for n in range(2,8):
    for s in [F(1,2),F(2,3),F(4,5)]:
        K=10
        success=model_success(n,s)
        direct=ordinary_path_coeffs(n,s,K)
        coeff=conditional_coeffs(n,s,K)
        for k in range(K+1):
            require(direct.get(n+k,F(0)) == success*coeff[k],f'n={n},s={s},k={k}')
        require(sum(coeff)<=1, 'coefficients do not exceed one')
        mu,v=exact_moments(n,s)
        require(mu>=0 and v>=0, 'moments are nonnegative')
        require(coeff[0]==prod(1-(1-F(m,n))*s**m for m in range(1,n+1)), 'zero repeats')

# Check analytical coupling lower/upper bound using exact rational finite truncations.
for s in [F(1,3),F(1,2),F(2,3)]:
    for n in [2,3,4,6,10,20,40]:
        r=[(1-F(m,n))*s**m for m in range(1,n+1)]
        p0_n=prod(1-v for v in r)
        L=160
        p0_lim=prod(1-s**m for m in range(1,L+1))
        lower=p0_n-p0_lim
        upper=sum((F(m,n)*s**m/(1-s**m) for m in range(1,n+1)),F(0))+s**(n+1)/(1-s)
        require(lower>=0, 'zero-repeat stochastic comparison')
        require(lower<=upper, 'zero-repeat difference bounded by TV coupling')
        if n>=10:
            limit_alpha=sum((m*float(s)**m/(1-float(s)**m) for m in range(1,400)))
            c0=prod(1-float(s)**m for m in range(1,400))
            error=abs(float(n*lower)-c0*limit_alpha)
            require(error < 8/(n), 'sharp lower-bound coefficient')

# First-order difference of conditional mean.
for s in [0.2, 0.5, 0.75]:
    target=sum(m*s**m/(1-s**m)**2 for m in range(1,600))
    mu_limit=sum(s**m/(1-s**m) for m in range(1,600))
    for n in [1000,2000,4000]:
        mu_n=sum(((1-m/n)*s**m)/(1-(1-m/n)*s**m) for m in range(1,n+1))
        scaled=n*(mu_limit-mu_n)
        require(abs(scaled-target)<(target+1)*5/n,'mean correction')

print('PASS: %d exact/controlled numerical assertions' % checks)
print('Finite path-state DP compared with conditional stage factorization.')
print('Stochastic comparison and first-order constants checked.')

# Sharp total-variation coefficient, obtained from the full Boltzmann partition law.
def finite_pmf(n, s, K):
    arr=[0.] * (K+1)
    arr[0]=1.
    for m in range(1,n+1):
        r=(1-m/n)*s**m
        nxt=[0.] * (K+1)
        nxt[0]=(1-r)*arr[0]
        for k in range(1,K+1):
            nxt[k]=(1-r)*arr[k]+r*nxt[k-1]
        arr=nxt
    return arr

def limit_pmf(s,K):
    out=[]
    p0=prod(1-s**m for m in range(1,500))
    p=p0
    for k in range(K+1):
        if k:p=p*s/(1-s**k)
        out.append(p)
    return out

for s in [0.3,0.5,0.75]:
    K=250
    p=limit_pmf(s,K)
    alpha=sum(m*s**m/(1-s**m) for m in range(1,600))
    h=0.
    C=0.
    for k,pk in enumerate(p):
        if k:h+=1+k*s**k/(1-s**k)
        C+=0.5*pk*abs(alpha-h)
    require(C>0,'TV coefficient positive')
    for n in [100,200,500,1000]:
        pn=finite_pmf(n,s,K)
        scaled=n*0.5*sum(abs(a-b) for a,b in zip(pn,p))
        require(abs(scaled-C)<(C+1)*4/n,'sharp TV first-order coefficient')
    for n in [50,150,500]:
        pn=finite_pmf(n,s,K)
        h=0.
        for k in range(15):
            if k:h+=1+k*s**k/(1-s**k)
            lhs=n*(pn[k]-p[k]); rhs=p[k]*(alpha-h)
            require(abs(lhs-rhs)<(1+abs(rhs))*12/n,'fixed-k first-order probability')

print('PASS: %d total exact/controlled numerical assertions' % checks)
print('Sharp partition-law total-variation coefficient checked.')
