from math import comb, gcd


def primes_upto(n):
    out=[]
    for x in range(2,n+1):
        if all(x%d for d in range(2,int(x**0.5)+1)):
            out.append(x)
    return out


def borrow_count(n,k,p):
    c=0
    b=0
    while n or k or b:
        nd=n%p
        kd=k%p
        if nd-b < kd:
            c += 1
            b = 1
        else:
            b = 0
        n//=p
        k//=p
    return c


def vp(n,p):
    e=0
    while n%p==0:
        e+=1
        n//=p
    return e

structural=0
exhaustive=0
direct=0
for m in range(3,13):
    for p in primes_upto(47):
        if p<=m:
            continue
        for s in range(0,5):
            for t in range(s+1,7):
                N=p**s+p**t
                if N%m:
                    continue
                k=m*p**(t-1)
                assert 0 < k < N and k % m == 0
                assert borrow_count(N,k,p) == 1
                assert p**s % m != 0 and p**t % m != 0
                structural += 1
                if N <= 20000:
                    vals=[borrow_count(N,j,p) for j in range(m,N,m)]
                    assert vals and min(vals)==1
                    exhaustive += 1
                if N <= 500:
                    g=0
                    for j in range(m,N,m):
                        g=gcd(g,comb(N,j))
                    assert vp(g,p)==1
                    direct += 1

# Explicitly test the non-+-1 residue classes modulo 5.
for p in primes_upto(200):
    if p<=5 or p%5 not in (2,3):
        continue
    for s in range(0,4):
        for d in (2,6):
            t=s+d
            N=p**s+p**t
            assert N%5==0
            assert borrow_count(N,5*p**(t-1),p)==1

print(f"VERIFY_OK structural={structural} exhaustive={exhaustive} direct_gcd={direct}")
