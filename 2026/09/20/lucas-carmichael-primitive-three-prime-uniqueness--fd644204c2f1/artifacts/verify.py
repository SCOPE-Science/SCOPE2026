from math import gcd, isqrt

def isprime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def divisors(n):
    lo=[]; hi=[]
    d=1
    while d*d <= n:
        if n%d==0:
            lo.append(d)
            if d*d != n: hi.append(n//d)
        d+=1
    return lo + hi[::-1]

def lc(p,q,r):
    n=p*q*r
    return all((n+1)%(s+1)==0 for s in (p,q,r))

hits=[]
triples=0
for p in range(3,100,2):
    if not isprime(p): continue
    for q in range(p+2,3*p*p,2):
        if not isprime(q): continue
        for rp1 in divisors(p*q-1):
            r=rp1-1
            if r<=q or not isprime(r): continue
            if lc(p,q,r):
                triples += 1
                if gcd(gcd(p+1,q+1),r+1)==2:
                    hits.append((p,q,r,p*q*r))
print('three-prime Lucas-Carmichael triples tested with p < 100:', triples)
print('gcd-shift-2 hits:', hits)
assert hits == [(5,13,31,2015)]
assert all(2016 % (s+1) == 0 for s in (5,13,31))
