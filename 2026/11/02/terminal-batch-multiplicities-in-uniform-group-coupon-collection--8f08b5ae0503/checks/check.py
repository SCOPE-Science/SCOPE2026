"""Standalone scientific checks for bulk uniform-group coupon collection.
Uses exact rational dynamic programming, independent small-model enumeration,
and factorial-moment diagnostics; standard library only.
"""
from fractions import Fraction
from math import comb, factorial, exp, log, floor
from itertools import combinations, product

checks = 0

def ck(condition, label):
    global checks
    assert condition, label
    checks += 1

def raw_prob(n, s, r, t):
    """P(T=t and B=r) via independent inclusion-exclusion identity."""
    if not (1 <= s < n and t >= 2 and 1 <= r <= min(n,s)):
        return Fraction(0)
    total = Fraction(0)
    denominator = comb(n,s)
    for j in range(n-r+1):
        z = n-r-j
        ratio = Fraction(comb(z,s),denominator) if z >= s else Fraction(0)
        total += (-1)**j * comb(n-r,j) * ratio**(t-1)
    return Fraction(comb(n,r)*factorial(s)*factorial(n-r),factorial(s-r)*factorial(n))*total

def markov(n,s,tmax):
    """Independent hypergeometric missing-count transition."""
    d={n:Fraction(1)}
    finished={}
    for t in range(1,tmax+1):
        new={}
        for m,v in d.items():
            for hit in range(max(0,s-(n-m)),min(s,m)+1):
                prob=Fraction(comb(m,hit)*comb(n-m,s-hit),comb(n,s))
                if m-hit==0 and m>0:
                    finished[t,m]=finished.get((t,m),Fraction(0))+v*prob
                else:
                    new[m-hit]=new.get(m-hit,Fraction(0))+v*prob
        d=new
    return finished,d

# Check against exact independent Markov occupancy transitions.
for n in range(2,10):
    for s in range(1,n):
        fm, surv = markov(n,s,5)
        for t in range(2,6):
            for r in range(1,min(n,s)+1):
                ck(raw_prob(n,s,r,t)==fm.get((t,r),Fraction(0)),(n,s,t,r))
        ck(sum(fm.values())+sum(surv.values())==1,(n,s,'mass'))

# Brute enumeration of ordered packages, independent of formula and Markov count DP.
for n in range(2,7):
    for s in range(1,n):
        subsets=[sum(1<<i for i in a) for a in combinations(range(n),s)]
        for t in range(2,4):
            tally={}
            for seq in product(subsets, repeat=t):
                seen=0
                covered=False
                for step,mask in enumerate(seq,1):
                    missing=((1<<n)-1)^seen
                    add=(mask & missing).bit_count()
                    seen |= mask
                    if seen==(1<<n)-1:
                        if step==t: tally[add]=tally.get(add,0)+1
                        covered=True
                        break
                # Non-completing sequences contribute no probability.
            den=len(subsets)**t
            for b in range(1,s+1):
                ck(Fraction(tally.get(b,0),den)==raw_prob(n,s,b,t),(n,s,t,b,'enum'))

# Factorial moments and hypergeometric-to-binomial transition diagnostics.
def fall(n,k):
    v=1
    for j in range(k): v*=n-j
    return v

def survival_fixed(n,s,k):
    if k>n-s:return 0.
    z=1.
    for j in range(k):z*=(n-s-j)/(n-j)
    return z

for c in (0.25,0.5,0.75):
    for n in (2000,10000,40000):
        s=round(c*n)
        q=1-s/n
        a=floor(log(n)/(-log(q)))
        theta=n*q**a
        for j in (-1,0,1):
            t=a+j
            lam=theta*q**j
            for k in range(1,5):
                observed=fall(n,k)*survival_fixed(n,s,k)**t
                target=lam**k
                ck(abs(observed/target-1)<0.13,(c,n,j,k,observed,target))
            for b in range(1,4):
                true=1.
                for h in range(b):true*=(s-h)/(n-h)
                ck(abs(true-c**b)<.01,(c,n,b,'hypergeom'))

# Limiting law: telescoping mass and simultaneous-final-discovery probability.
for c in (.25,.5,.75):
    q=1-c
    for theta in (1, 1/(q**.6)):
        mass=0.; p1=0.; expected=0.
        for j in range(-110,200):
            lam=theta*c*q**(j-1)
            if lam>700:
                continue
            for b in range(1,100):
                v=exp(-theta*q**(j-1)+b*log(lam)-__import__('math').lgamma(b+1)) if lam>0 else 0.
                mass+=v
                expected+=b*v
                if b==1:p1+=v
        ck(abs(mass-1)<1e-7,(c,theta,'mass',mass))
        ck(.0 < 1-p1 < 1,(c,theta,'multiple',p1))
        ck(expected>1,(c,theta,'expected'))

print('PASS',checks,'independent exact, enumerative, and limiting diagnostic assertions')

# Exact embedded jump-chain recursion, independently checking the sparse-collision lemma.
def terminal_distribution(n,s):
    """Exact final-batch distribution using the count process embedded at strict decreases."""
    d={0:{},1:{1:Fraction(1)}}
    for m in range(2,n+1):
        denom=comb(n,s)
        probs={}
        for h in range(max(0,s-(n-m)),min(m,s)+1):
            probs[h]=Fraction(comb(m,h)*comb(n-m,s-h),denom)
        exit_prob=1-probs.get(0,0)
        out={}
        for h,p in probs.items():
            if h==0:continue
            p/=exit_prob
            if h==m:
                out[m]=out.get(m,0)+p
            else:
                for b,v in d[m-h].items():out[b]=out.get(b,0)+p*v
        d[m]=out
    return d[n]

for n in range(3,16):
    for s in range(2,n):
        dist=terminal_distribution(n,s)
        ck(sum(dist.values())==1,(n,s,'terminal mass'))
        c=s/n
        h2=Fraction(s-1,2*n-s-1)
        mult=sum(v for b,v in dist.items() if b>=2)
        eta=c*(3-2*c)/(1-c)**2
        upper=h2+c*c/(1-c)
        lower=h2*max(0,1-eta)
        ck(float(mult)>=lower-1e-12,(n,s,'lower'))
        ck(float(mult)<=upper+1e-12,(n,s,'upper'))
        if 2 in dist:ck(dist[2]<=h2,(n,s,'exact two'))

for n,s in ((300,2),(300,5),(1000,2),(1000,7),(3000,3),(3000,31)):
    # Embedded chain probability of visiting state two.
    prob=[0.]*(n+1);prob[2]=1.
    for m in range(3,n+1):
        hi=min(s,m)
        low=max(0,s-(n-m))
        values=[(h,comb(m,h)*comb(n-m,s-h)/comb(n,s)) for h in range(low,hi+1)]
        leave=sum(p for h,p in values if h>0)
        prob[m]=sum(p*prob[m-h] for h,p in values if h>0)/leave
    ck(0<prob[n]<=1,(n,s,'hit2'))
    ck(1-prob[n]<5*s/n,(n,s,'hit2 sharp'))
    h2=(s-1)/(2*n-s-1)
    ck(abs(prob[n]*h2/((s-1)/(2*n))-1) < 5*s/n,(n,s,'pair coefficient'))

print('PASS',checks,'total assertions including sparse-regime exact terminal distributions')
