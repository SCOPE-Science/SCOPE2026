from math import isqrt

def primes_upto(n):
    sieve = bytearray(b'\x01')*(n+1)
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b'\x00'*(((n-p*p)//p)+1)
    return [i for i in range(2,n+1) if sieve[i]]

def harmonic_mean_p2qr(p,q,r):
    n=p*p*q*r
    sigma=(p*p+p+1)*(q+1)*(r+1)
    num=12*n
    return num//sigma if num%sigma==0 else None

P=primes_upto(300)
sol=[]
for p in P:
    for i,q in enumerate(P):
        if q==p: continue
        for r in P[i+1:]:
            if r==p or r==q: continue
            if 2 not in (p,q,r): continue
            h=harmonic_mean_p2qr(p,q,r)
            if h is not None:
                sol.append((p*p*q*r,p,q,r,h))
sol=sorted(set(sol))
assert {x[0] for x in sol}=={140}, sol
assert harmonic_mean_p2qr(2,5,7)==5
print('VERIFY_OK prime_bound=300 solutions=140 harmonic_mean=5')
