"""Exact finite-state checks for joint descent/inversion laws under random-to-top shuffling.
No external dependencies; run with Python 3.9+.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from math import exp, sqrt

checks = 0

def eq(actual, expected, message):
    global checks
    checks += 1
    if actual != expected:
        raise AssertionError(f'{message}: {actual!r} != {expected!r}')

def des(p):
    return sum(p[i] > p[i+1] for i in range(len(p)-1))

def inv(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def moments(sample):
    m=len(sample)
    d=Q(sum(x for x,y in sample),m)
    i=Q(sum(y for x,y in sample),m)
    cov=Q(sum(x*y for x,y in sample),m)-d*i
    return d,i,cov

def mu_d(n,k):
    return Q(k-1,2)+Q(n-k,n-k+1) if k else Q(0)

def mu_i(n,k):
    return Q(k*(2*n-k-1),4)

def cov_di(n,k):
    return Q(k-1,4)+Q(n-k,2*(n-k+1)) if k else Q(0)

# Uniform random k-card prefix followed by the untouched cards in sorted order.
for n in range(2,8):
    for k in range(1,n+1):
        observed=[]
        for p in permutations(range(1,n+1)):
            deck=p[:k]+tuple(sorted(p[k:]))
            observed.append((des(deck),inv(deck)))
        d,i,c=moments(observed)
        eq(d,mu_d(n,k),f'conditional descent mean n={n} k={k}')
        eq(i,mu_i(n,k),f'conditional inversion mean n={n} k={k}')
        eq(c,cov_di(n,k),f'conditional covariance n={n} k={k}')

# Direct shuffled histories versus exact occupancy-mixture covariance.
for n in range(2,7):
    for r in range(1,7):
        samples=[]
        counts={}
        for moves in product(range(1,n+1),repeat=r):
            deck=tuple(range(1,n+1))
            for v in moves:
                deck=(v,)+tuple(x for x in deck if x!=v)
            k=len(set(moves))
            counts[k]=counts.get(k,0)+1
            samples.append((des(deck),inv(deck)))
        d,i,c=moments(samples)
        total=n**r
        e_d=sum((Q(count,total)*mu_d(n,k) for k,count in counts.items()),Q())
        e_i=sum((Q(count,total)*mu_i(n,k) for k,count in counts.items()),Q())
        e_di=sum((Q(count,total)*(mu_d(n,k)*mu_i(n,k)+cov_di(n,k)) for k,count in counts.items()),Q())
        eq(d,e_d,f'full history descent mean n={n} r={r}')
        eq(i,e_i,f'full history inversion mean n={n} r={r}')
        eq(c,e_di-e_d*e_i,f'full history covariance n={n} r={r}')
        assert c>0
        checks+=1

# Numeric, exact recursion for occupancy K at r=floor(c*n) moves.
def occupancy(n,r):
    z=[0.0]*(n+1)
    z[0]=1.
    for _ in range(r):
        y=[0.0]*(n+1)
        for k,p in enumerate(z):
            if p:
                y[k]+=p*k/n
                if k<n:y[k+1]+=p*(n-k)/n
        z=y
    return z

for c in (0.5,1.,2.):
    b=exp(-c)
    tau2=b-(1+c)*b*b
    target=b*tau2/4
    errors=[]
    for n in (80,160,320,640):
        pk=occupancy(n,int(c*n))
        ed=sum(p*float(mu_d(n,k)) for k,p in enumerate(pk))
        ei=sum(p*float(mu_i(n,k)) for k,p in enumerate(pk))
        edi=sum(p*float(mu_d(n,k)*mu_i(n,k)+cov_di(n,k)) for k,p in enumerate(pk))
        observed=(edi-ed*ei)/n**2
        errors.append(abs(observed-target))
        if not observed>0:raise AssertionError('covariance sign')
        checks+=1
    if errors[-1]>0.01:
        raise AssertionError(f'wrong asymptotic covariance for c={c}: {errors}')
    if errors[-1] >= errors[0]:
        raise AssertionError(f'nonconvergent finite covariance for c={c}: {errors}')
    checks+=2
    print(f'c={c:g}: asymptotic covariance={target:.12f}, errors={errors}')

print(f'PASS: {checks} exact rational and deterministic numerical assertions')
