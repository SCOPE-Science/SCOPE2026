#!/usr/bin/env python3
"""Independent finite checks for the stationary batch-reset cloud theorem.
Requires Python 3 standard library only; not a proof of infinite limits.
"""
import math
import random

rng=random.Random(20261020)
D,r=1.0,1.3
checks=0

def ck(condition, message):
    global checks
    assert condition, message
    checks += 1

def finite_cov(N,m,D=D,r=r):
    p=m/N
    c=m*(m-1)/(N*(N-1))
    v=2*D/(r*p)
    joint=4*D*v/(r*(2*p-c))
    return joint-v*v

def source_cov(N,m,D=D,r=r):
    return 4*D*D/(r*r)*N*N*(m-1)/(m*m*(2*N-m-1))

for N in [8, 30, 100, 1000, 3000]:
    for m in sorted(set([1, 2, N//4, N//2, N-1,N])):
        p=m/N
        if not 1<=m<=N:continue
        v1=finite_cov(N,m)
        v2=source_cov(N,m)
        ck(abs(v1-v2)<2e-9*(1+abs(v2)),f'cov {N} {m}')
        if N>=100 and m>=N//4 and m<=N-1:
            v_inf=4*D*D/(r*r*p*(2-p))
            ck(abs(v1/v_inf-1)<max(.15,10/N),f'asymptotic cov {N} {m}')

for alpha in [.2,.5,.8]:
    q=1-alpha
    for k in range(1,6):
        cumulant=math.factorial(k-1)*(2*D/r)**k/(1-q**k)
        terms=sum(q**(k*j) for j in range(500))
        ck(abs(cumulant-math.factorial(k-1)*(2*D/r)**k*terms)<1e-10*(1+cumulant),'cumulant geometric series')
    for z in [.02,.2,2.0]:
        phi=math.prod(1/(1+(2*D*z/r)*q**j) for j in range(300))
        # Stationary fixed-point law: M = 2D E + q M' with E~Exp(r).
        phiq=math.prod(1/(1+(2*D*q*z/r)*q**j) for j in range(300))
        ck(abs(phi-(r/(r+2*D*z))*phiq)<1e-12,'Laplace renewal')
    C=2*D/r
    mean=C/alpha
    var=C*C/(alpha*(2-alpha))
    values=[]
    for _ in range(13000):
        x=0.0
        power=1.0
        for j in range(100):
            x+=power*rng.expovariate(r)
            power*=q
        values.append(2*D*x)
    mu=sum(values)/len(values)
    vv=sum((x-mu)**2 for x in values)/len(values)
    ck(abs(mu-mean)<.065*mean, 'sample mean')
    ck(abs(vv-var)<.16*var, 'sample variance')

# High-L Laplace asymptotic; this checks numerical consequences, not the probability bound.
for q in [.3,.6]:
    a=-math.log(q)
    for L in [35,70,120]:
        z=L
        jmax=math.ceil((z+30)/a)
        # log (1+exp(z-a*j)) evaluated without overflow
        logs=sum(math.log1p(math.exp(z-a*j)) if z-a*j<650 else z-a*j for j in range(jmax))
        rat=logs/(L*L)
        target=1/(2*a)
        ck(abs(rat/target-1)<.075, f'Laplace log-square at {q}, {L}')

for alpha in [.01,.003,.001]:
    q=1-alpha
    second=alpha/(2-alpha)
    third=2*alpha**3/(1-q**3)
    ck(abs(second/alpha-.5)<.01, 'CLT variance normalization')
    ck(third/alpha**1.5 < 0.1, 'CLT vanishing cubic cumulant')

print('PASS',checks,'deterministic/check groups and reproducible Monte Carlo comparisons')
