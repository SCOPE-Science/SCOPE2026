import math

BOUND = 500_000
SIEVE_MAX = 2_000_000

def sieve(n):
    isprime = bytearray(b'\x01')*(n+1)
    if n >= 0: isprime[0]=0
    if n >= 1: isprime[1]=0
    for p in range(2, int(n**0.5)+1):
        if isprime[p]:
            start=p*p
            isprime[start:n+1:p]=b'\x00'*(((n-start)//p)+1)
    primes=[i for i in range(2,n+1) if isprime[i]]
    return isprime, primes

ISPRIME, PRIMES = sieve(SIEVE_MAX)

def factor(n):
    out=[]
    x=n
    for p in PRIMES:
        if p*p>x: break
        if x%p==0:
            e=0
            while x%p==0:
                x//=p; e+=1
            out.append((p,e))
        if x==1: break
    if x>1: out.append((x,1))
    return out

def divisors_from_factor(f):
    ds=[1]
    for p,e in f:
        old=ds[:]
        powers=[]
        q=1
        for _ in range(e):
            q*=p; powers.append(q)
        ds=[d*q for d in old for q in [1]+powers]
    return sorted(ds)

def practical_by_definition(n, f=None):
    if f is None: f=factor(n)
    reach=0
    for d in divisors_from_factor(f):
        if d>reach+1:
            return False
        reach += d
        if reach>=n:
            return True
    return reach>=n

def candidate_from_two_prime_factor(f):
    if len(f)!=2 or f[0][0]!=2:
        return False
    (p0,a),(p,b)=f
    return p <= 2**(a+1)

checked=0
truth=0
cand=0
for n in range(2, BOUND+1):
    f=factor(n)
    if len(f)==2:
        checked += 1
        t=practical_by_definition(n,f)
        c=candidate_from_two_prime_factor(f)
        truth += int(t)
        cand += int(c)
        if t!=c:
            raise AssertionError((n,f,t,c))

def count_exact(X):
    total=0
    a=1
    while (1<<a)*3 <= X:
        lim=min(1<<(a+1), X//(1<<a))
        for p in PRIMES:
            if p==2: continue
            if p>lim: break
            q=(1<<a)*p
            while q<=X:
                total+=1
                if q > X//p: break
                q*=p
        a+=1
    return total

def phase_F(s):
    return (8.0+4.0*s)/math.sqrt(2.0*s)

phase=[]
for m in (12,15,18):
    for s in (1.0,2.0,3.5):
        X=int(s*(2**(2*m+1)))
        c=count_exact(X)
        norm=c*math.log(X)/math.sqrt(X)
        target=phase_F(s)
        phase.append((m,s,c,norm,target,abs(norm-target)))
# Crude convergence sanity: by m=18 all tested phases are within 25%.
for m,s,c,norm,target,err in phase:
    if m==18 and err > 0.25*target:
        raise AssertionError(('phase',m,s,norm,target))

print('VERIFY_OK bound=%d support_two_checked=%d practical_support_two=%d phase_samples=%d' % (BOUND, checked, truth, len(phase)))
for row in phase:
    print('PHASE m=%d s=%.1f count=%d normalized=%.9f target=%.9f abs_error=%.9f' % row)
