from math import isqrt

def isprime(n):
    if n<2:return False
    if n%2==0:return n==2
    d=3
    while d*d<=n:
        if n%d==0:return False
        d+=2
    return True

def predicted(q,A,b,sgn):
    # sgn=+1 means q^b=2^A+1, n=2^A; sgn=-1 means q^b=2^A-1, n=q^b
    if sgn==1:
        return (b==1 and q==(1<<A)+1 and isprime(q)) or (q==3 and b==2 and A==3)
    else:
        return b==1 and q==(1<<A)-1 and isprime(q)

structural=0
for q in range(3,5000,2):
    if not isprime(q): continue
    for A in range(2,25):
        two=1<<A
        for b in range(1,9):
            qb=q**b
            for sgn in (1,-1):
                eq=(qb==two+sgn)
                pr=predicted(q,A,b,sgn)
                if eq!=pr:
                    raise SystemExit((q,A,b,sgn,eq,pr,qb,two))
                structural+=1

# direct triangular scan through 200000: if T_n has exactly primes 2 and q with both positive,
# compare to classification.
def odd_prime_power(m):
    # return (q,b) if m=q^b for an odd prime q, else None
    if m<=1 or m%2==0: return None
    q=None
    x=m
    d=3
    while d*d<=x:
        if x%d==0:
            q=d; break
        d+=2
    if q is None:
        return (m,1) if isprime(m) else None
    if not isprime(q): return None
    b=0
    while x%q==0:
        x//=q;b+=1
    return (q,b) if x==1 else None

direct=0
seen=[]
for n in range(2,200001):
    T=n*(n+1)//2
    a=0
    while T%2==0:
        T//=2;a+=1
    if a==0: continue
    pp=odd_prime_power(T)
    if not pp: continue
    q,b=pp
    direct+=1
    # classification predicted solution tuples
    ok=False
    # Mersenne n=q, q+1 power of 2 with A>=2, beta1
    if b==1 and n==q and (q+1)&q==0 and q+1>=4:
        ok=True
    # Fermat n=q-1, q-1 power of2 with A>=2, beta1
    if b==1 and n==q-1 and q-1>=4 and ((q-1)&(q-2)==0):
        ok=True
    # exceptional
    if (q,b,n,a)==(3,2,8,2):
        ok=True
    if not ok:
        raise SystemExit(('direct mismatch',n,a,q,b))
    seen.append((n,a,q,b))

# Explicit q=3 solutions under n bound should be exactly n=3,8
q3=[x for x in seen if x[2]==3]
if q3 != [(3,1,3,1),(8,2,3,2)]:
    raise SystemExit(('q3',q3))
print(f'VERIFY_OK structural={structural} direct={direct} q3={len(q3)}')
