from fractions import Fraction
from math import isqrt

def factor(n):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0: n//=d; e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

def mu_from_fac(f):
    if any(e>1 for _,e in f): return 0
    return -1 if len(f)%2 else 1

def phi_from_fac(f):
    z=1
    for p,e in f: z*=p**(e-1)*(p-1)
    return z

def sinv_sigma_from_fac(f):
    z=1
    for p,e in f:
        if e==1: z*=-(p+1)
        elif e==2: z*=p
        else: return 0
    return z

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

params=[Fraction(-199,100),Fraction(-3,2),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(99,100)]
limit=20000
for t in params:
    zeros=[]
    for n in range(1,limit+1):
        f=factor(n); mu=mu_from_fac(f); ph=phi_from_fac(f); si=sinv_sigma_from_fac(f)
        val=Fraction(si+ph+2)+t*(mu+1)
        if val==0: zeros.append(n)
    assert zeros==[n for n in range(2,limit+1) if isprime(n)], (t, zeros[:20])
# exact endpoint witnesses
for n,t in [(1,Fraction(-2)),(18,Fraction(1))]:
    f=factor(n); val=Fraction(sinv_sigma_from_fac(f)+phi_from_fac(f)+2)+t*(mu_from_fac(f)+1)
    assert val==0,(n,t,val)
# local formula spot-check by convolution for n<=500
# sigma^{-1} * sigma = epsilon
def sigma(n): return sum(d for d in range(1,n+1) if n%d==0)
for n in range(1,501):
    total=0
    for d in range(1,n+1):
        if n%d==0: total += sinv_sigma_from_fac(factor(d))*sigma(n//d)
    assert total==(1 if n==1 else 0),(n,total)
print(f'VERIFY_OK exact_params={len(params)} n_max={limit} endpoint_witnesses=2 convolution_cases=500')
