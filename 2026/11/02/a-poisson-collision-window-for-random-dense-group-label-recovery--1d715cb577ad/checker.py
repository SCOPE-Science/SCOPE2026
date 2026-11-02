"""Finite exact and numerical cross-checks for random fixed-size separating matrices.
Uses only the Python standard library and optional NumPy for sampling.
No finite calculation certifies the limiting theorem.
"""
from fractions import Fraction
from collections import Counter
from itertools import combinations, product
from math import comb, factorial, log, exp
import random

def partitions(n, lo=1):
    if n == 0:
        yield ()
    else:
        for a in range(lo, n+1):
            for tail in partitions(n-a, a):
                yield (a,) + tail

def coefficient(parts, k):
    c = [0] * (k+1)
    c[0] = 1
    for s in parts:
        for j in range(k, s-1, -1):
            c[j] += c[j-s]
    return c[k]

def exact_recovery_probability(n,k,t):
    tot = Fraction(0)
    for parts in partitions(n):
        counts = Counter(parts)
        # Calculate each set-partition multiplicity as one exact quotient.
        denom = 1
        for s,m in counts.items():
            denom *= factorial(s)**m * factorial(m)
        orbit = factorial(n)//denom
        mu = 1
        for s in parts:
            mu *= (-1)**(s-1)*factorial(s-1)
        allowed = coefficient(parts,k)
        tot += orbit*mu*Fraction(allowed, comb(n,k))**t
    return tot

def exhaustive_recovery_probability(n,k,t,require_cover=False):
    choices=[tuple(c) for c in combinations(range(n),k)]
    hit=0
    for draw_ix in product(range(len(choices)),repeat=t):
        sig=[0]*n
        for j,ix in enumerate(draw_ix):
            for v in choices[ix]:
                sig[v] |= (1<<j)
        if len(set(sig))==n and (not require_cover or all(sig)):
            hit+=1
    return Fraction(hit, len(choices)**t)

def qn(n,k):
    return Fraction(k*(k-1)+(n-k)*(n-k-1),n*(n-1))

def r3n(n,k):
    return Fraction(k*(k-1)*(k-2)+(n-k)*(n-k-1)*(n-k-2),n*(n-1)*(n-2))

def d4n(n,k):
    return Fraction(k*(k-1)*(k-2)*(k-3)+(n-k)*(n-k-1)*(n-k-2)*(n-k-3)+2*k*(k-1)*(n-k)*(n-k-1),n*(n-1)*(n-2)*(n-3))

def exact_moments(n,k,t):
    q,r,d = qn(n,k),r3n(n,k),d4n(n,k)
    M=comb(n,2)
    mean=M*q**t
    # unordered overlap pairs: 3 per unordered triple
    overlap=3*comb(n,3)
    disjoint=3*comb(n,4)
    var=mean*(1-q**t) +2*overlap*(r**t-q**(2*t)) +2*disjoint*(d**t-q**(2*t))
    return mean,var

def exact_enumerated_moments(n,k,t):
    choices=list(combinations(range(n),k))
    xs=[]
    for draws in product(choices,repeat=t):
        sig=[0]*n
        for j,subset in enumerate(draws):
            for i in subset:
                sig[i]|=1<<j
        count=Counter(sig)
        xs.append(sum(v*(v-1)//2 for v in count.values()))
    mean=Fraction(sum(xs),len(xs))
    var=Fraction(sum(x*x for x in xs),len(xs))-mean**2
    return mean,var

def monte_carlo(n,k,t,reps,seed):
    rng=random.Random(seed)
    zero=0; uncovered=0; total=0
    for _ in range(reps):
        signatures=[0]*n
        for j in range(t):
            for i in rng.sample(range(n), k):
                signatures[i] |= 1<<j
        c=Counter(signatures)
        pairs=sum(v*(v-1)//2 for v in c.values())
        total+=pairs
        zero += pairs==0
        uncovered += c.get(0,0)>0
    return zero/reps,total/reps,uncovered/reps

def main():
    checks=0
    for n,k,t in [(3,1,2),(4,2,2),(4,2,3),(5,2,3),(5,2,4),(6,3,3)]:
        f=exact_recovery_probability(n,k,t)
        g=exhaustive_recovery_probability(n,k,t)
        assert f==g,(n,k,t,f,g)
        assert Fraction(0)<=f<=Fraction(1)
        checks+=2
        print('exact_CDF',n,k,t,str(f))
    for n,k,t in [(4,2,2),(5,2,3),(6,3,3)]:
        f=exact_moments(n,k,t)
        g=exact_enumerated_moments(n,k,t)
        assert f==g,(n,k,t,f,g)
        assert f[1]>=0
        checks+=3
        print('exact_moments',n,k,t,str(f[0]),str(f[1]))
    for n in (80,200,600):
        for p in (.25,.5,.75):
            k=round(p*n)
            q=float(qn(n,k)); a=-log(q); M=comb(n,2)
            t=round(log(M)/a)
            lam=M*q**t
            zero,mean,uncovered=monte_carlo(n,k,t,1000,seed=n*1000+k*13)
            target=exp(-lam)
            # Sampling tolerance wider than 4-5 sigma for probability; mean tolerance is finite-n and sampling.
            assert abs(zero-target)<0.115,(n,k,t,zero,target)
            assert abs(mean-lam)<0.33,(n,k,t,mean,lam)
            checks+=2
            print('simulation',n,k,t,'lambda',round(lam,5),'Pzero',round(zero,5),'Poisson',round(target,5),'mean',round(mean,5),'uncovered',round(uncovered,5))
    print('PASS',checks,'independent exact identity and numerical comparison assertions')
if __name__=='__main__': main()
