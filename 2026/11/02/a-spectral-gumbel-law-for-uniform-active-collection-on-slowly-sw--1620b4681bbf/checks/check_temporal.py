#!/usr/bin/env python3
"""Reproducibility checks for Markov-gated contact coupon collection.
Requires Python 3 standard library only. No external packages or data files are required.
"""
import math, random, statistics


def params(a,b,c):
    pi=a/(a+b)
    disc=math.sqrt((a+b+c)**2-4*a*c)
    gamma=(a+b+c-disc)/2
    Gamma=(a+b+c+disc)/2
    A=(Gamma-pi*c)/(Gamma-gamma)
    return gamma,Gamma,A


def survival(a,b,c,x):
    g,G,A=params(a,b,c)
    return A*math.exp(-g*x)+(1-A)*math.exp(-G*x)


def evolve_survival(a,b,c,x,steps=20000):
    # Uniformized two-state substochastic semigroup, used as an independent ODE check.
    p=a/(a+b);u=1-p;v=p
    h=x/steps
    for _ in range(steps):
        du=-a*u+b*v
        dv=a*u-(b+c)*v
        u+=h*du;v+=h*dv
    return u+v


def sample_cover(n,a,b,seed):
    """Exact Gillespie simulation: CTMC edge flips and rate-one hub contacts."""
    rng=random.Random(seed)
    p=a/(a+b)
    present=[rng.random()<p for _ in range(n)]
    on=[i for i,z in enumerate(present) if z]
    off=[i for i,z in enumerate(present) if not z]
    indices=[0]*n
    for k,i in enumerate(on): indices[i]=k
    for k,i in enumerate(off): indices[i]=k
    seen=[False]*n
    unseen=n; t=0.0
    while unseen:
        flip_on=a*len(off)/n
        flip_off=b*len(on)/n
        rate=1.0+flip_on+flip_off
        t+=rng.expovariate(rate)
        z=rng.random()*rate
        if z<1:
            if on:
                i=on[rng.randrange(len(on))]
                if not seen[i]: seen[i]=True; unseen-=1
        elif z<1+flip_on:
            k=rng.randrange(len(off));i=off[k]
            last=off.pop();
            if k<len(off):off[k]=last;indices[last]=k
            indices[i]=len(on);on.append(i)
        else:
            k=rng.randrange(len(on));i=on[k]
            last=on.pop();
            if k<len(on):on[k]=last;indices[last]=k
            indices[i]=len(off);off.append(i)
    return t



def exact_small_expectation(n,a=1,b=1):
    # Independent finite-state continuous-time generator, solved over Q.
    from fractions import Fraction as F
    allbits=(1<<n)-1
    states=[(mask,seen) for mask in range(1<<n) for seen in range(1<<n) if seen!=allbits]
    lookup={s:i for i,s in enumerate(states)}
    mat=[[F(0) for _ in range(len(states)+1)] for _ in states]
    for i,(mask,seen) in enumerate(states):
        for j in range(n):
            rate=F(a if not mask & (1<<j) else b,n)
            target=(mask^(1<<j),seen)
            k=lookup.get(target)
            mat[i][i]+=rate
            if k is not None: mat[i][k]-=rate
        m=mask.bit_count()
        if m:
            for j in range(n):
                if mask&(1<<j) and not seen&(1<<j):
                    rate=F(1,m)
                    target=(mask,seen|(1<<j))
                    k=lookup.get(target)
                    mat[i][i]+=rate
                    if k is not None:mat[i][k]-=rate
        mat[i][-1]=F(1)
    for i in range(len(states)):
        pivot=next(j for j in range(i,len(states)) if mat[j][i])
        mat[i],mat[pivot]=mat[pivot],mat[i]
        z=mat[i][i];mat[i]=[x/z for x in mat[i]]
        for j in range(len(states)):
            if i==j or not mat[j][i]:continue
            z=mat[j][i];mat[j]=[v-z*w for v,w in zip(mat[j],mat[i])]
    pi=F(a,a+b)
    return sum((pi**mask.bit_count()*(1-pi)**(n-mask.bit_count()))*mat[lookup[(mask,0)]][-1] for mask in range(1<<n))

def check():
    assertions=0
    for a,b in [(1,1),(0.5,1),(2,1),(0.05,0.05),(20,20),(1,2),(0.7,0.2)]:
        c=(a+b)/a
        g,G,A=params(a,b,c)
        assert 0<g<1<G and 0<A<1;assertions+=2
        assert abs((g+G)-(a+b+c))<1e-11;assertions+=1
        assert abs(g*G-a*c)<1e-11;assertions+=1
        for x in [0,.01,.1,1,2,5]:
            S=survival(a,b,c,x)
            assert 0<S<=1+1e-12;assertions+=1
            approx=evolve_survival(a,b,c,x,steps=5000)
            assert abs(S-approx)<0.003;assertions+=1
            if x==0:
                assert abs(S-1)<1e-12;assertions+=1
        for n in (100,1000,10000):
            for y in (-1,0,1):
                x=(math.log(n*A)+y)/g
                if x<0:continue
                F=(1-survival(a,b,c,x))**n
                target=math.exp(-math.exp(-y))
                assert abs(F-target)<.075;assertions+=1
    # A finite-n generator computation (not an asymptotic certificate).
    exact2=exact_small_expectation(2)
    assert exact2>0;assertions+=1
    sim2=statistics.mean(sample_cover(2,1,1,800000+i) for i in range(4000))
    assert abs(sim2-float(exact2))<0.12*float(exact2);assertions+=1
    print('finite n=2 exact rational mean:',exact2,'simulation:',round(sim2,4))
    # Independent exact-event simulation checks only broad asymptotic direction.
    a=b=1;g,G,A=params(a,b,2)
    results=[]
    for n,reps in [(100,70),(300,70),(900,40)]:
        z=[g*sample_cover(n,a,b,10000+n*1000+j)/n-math.log(n*A) for j in range(reps)]
        m=statistics.mean(z)
        results.append((n,reps,round(m,4),round(statistics.pvariance(z),4)))
        assert -.5<m<1.9;assertions+=1
    # Speed monotonicity and its limiting laws.
    prev=0
    for s in (.002,.02,.2,1,2,10,100,1000):
        g,_,_=params(.4*s,.6*s,1/.4)
        assert prev<g<1;assertions+=1;prev=g
    print('PASS',assertions,'checks, monte-carlo standardized (n,reps,mean,var):',results)
    print('For a=b=1: pi=1/2, gamma=2-sqrt(2), A=(2+sqrt(2)-1)/(2sqrt(2))')

if __name__=='__main__':check()
