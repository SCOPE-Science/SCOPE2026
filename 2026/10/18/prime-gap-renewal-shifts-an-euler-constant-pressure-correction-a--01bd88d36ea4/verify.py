"""Independent numerical and finite-word checks for prime-gap shift formulas.

All physical quantities and mathematical constants refer only to the model.
The universal conclusions use the separate analytic proof.
"""
import math
from bisect import bisect_right
from itertools import product

def primes_up_to(n):
    sieve=bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2, math.isqrt(n)+1):
        if sieve[i]:
            sieve[i*i:n+1:i]=b'\x00'*((n-i*i)//i+1)
    return [i for i in range(n+1) if sieve[i]]

PRIMES=primes_up_to(2_000_000)

def partition(s):
    return sum(math.exp(-s*(p+1)) for p in PRIMES)

def root(t):
    z=math.exp(-t)
    lo,hi=0.0,1.0
    for _ in range(75):
        s=(lo+hi)/2
        if z*partition(s)>1:
            lo=s
        else:
            hi=s
    return (lo+hi)/2

checked=0
for t in (4.0,6.0,8.0):
    s=root(t)
    weights=[math.exp(-s*(p+1)-t) for p in PRIMES]
    mass=sum(weights)
    assert abs(mass-1)<1.e-11,(t,mass)
    effective=e_denom=math.exp(-t)/s
    pred=t+math.log(t)-math.euler_gamma if hasattr(math,'euler_gamma') else t+math.log(t)-0.5772156649015329
    assert 0<effective-pred<0.28,(t,effective,pred)
    mean=sum(w*(p+1) for w,p in zip(weights,PRIMES))
    rho=1/mean
    L=math.log(1/s)
    assert abs(rho/s - (1+1/L)) <0.035,(t,rho,s,L)
    checked+=3
    for x in (0.5,1.0,2.0):
        i=bisect_right(PRIMES, x/s-1)
        cdf=sum(weights[:i])
        exp_cdf=-math.expm1(-x)
        # Direct quadrature of the first correction.  At u=0, u log u is integrable.
        N=10000
        h=x/N
        integral=0.0
        for j in range(N):
            u=(j+0.5)*h
            integral+=math.exp(-u)*math.log(u)
        integral*=h
        corrected=exp_cdf-(integral+0.5772156649015329*exp_cdf)/L
        assert abs(cdf-corrected) <0.013,(t,x,cdf,corrected)
        checked+=1

# Independent finite-word encoding of complete marker-to-marker words.
allowed={p+1 for p in PRIMES[:7]}
comps={0:1}
for n in range(1,19):
    comps[n]=sum(comps.get(n-q,0) for q in allowed if q<=n)
    count=0
    # Exhaustively inspect the intervening gap pattern, rather than recurrence.
    for mask in range(1<<(n-1)):
        if n>15: break
        word=[1]+[(mask>>i)&1 for i in range(n-1)]+[1]
        spots=[i for i,c in enumerate(word) if c]
        if all((spots[j+1]-spots[j]) in allowed for j in range(len(spots)-1)):
            count+=1
    if n<=15:
        assert count==comps[n],(n,count,comps[n])
        checked+=1
print('VERIFY_OK:',checked,'root/moment/distribution/composition comparisons; all limits remain analytic')
