from math import gcd

BOUND = 500_000

def sieve_spf(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf

spf=sieve_spf(BOUND)

def factor(n):
    out=[]
    while n>1:
        p=spf[n]; a=0
        while n%p==0:
            n//=p; a+=1
        out.append((p,a))
    return out

def divisors_of(a):
    return [d for d in range(1,a+1) if a%d==0]

def esigma_from_factor(f):
    z=1
    for p,a in f:
        z *= sum(p**d for d in divisors_of(a))
    return z

def is_eperfect(n):
    return esigma_from_factor(factor(n)) == 2*n

def core_and_squarefree(n):
    c=m=1
    for p,a in factor(n):
        if a==1: m*=p
        else: c*=p**a
    return c,m

eps=[]; omega2=[]; decomposed=0; cores=set()
layer_counts={2:0,3:0,4:0,5:0,6:0}
for n in range(2,BOUND+1):
    if is_eperfect(n):
        eps.append(n)
        f=factor(n); w=len(f)
        if w in layer_counts: layer_counts[w]+=1
        if w==2: omega2.append(n)
        c,m=core_and_squarefree(n)
        assert c>1 and gcd(c,m)==1
        assert all(a>=2 for _,a in factor(c))
        assert is_eperfect(c)
        assert all(a==1 for _,a in factor(m)) if m>1 else True
        assert c*m==n
        cores.add(c); decomposed+=1
assert omega2==[36], omega2
# Exact 36-core contribution to the 3-prime layer: 36*p, p prime, p not 2 or 3.
primes=[p for p in range(2,BOUND//36+1) if spf[p]==p]
base36=sum(1 for p in primes if p not in (2,3) and 36*p<=BOUND)
assert all(is_eperfect(36*p) for p in primes if p not in (2,3) and 36*p<=BOUND)
print('VERIFY_OK', f'bound={BOUND}', f'eperfect={len(eps)}', f'decomposed={decomposed}',
      f'omega2={omega2}', f'cores={len(cores)}', f'base36_omega3={base36}',
      'layers=' + ','.join(f'{k}:{layer_counts[k]}' for k in sorted(layer_counts)))
