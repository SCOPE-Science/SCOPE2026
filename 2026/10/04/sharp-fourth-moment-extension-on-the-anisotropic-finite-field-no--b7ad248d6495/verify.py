#!/usr/bin/env python3
from collections import Counter

def legendre(a,p):
    a%=p
    if a==0: return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def first_nonsquare(p):
    for d in range(2,p):
        if legendre(d,p)==-1:
            return d
    raise RuntimeError('no nonsquare')

def primes_upto(n):
    out=[]
    for x in range(3,n+1,2):
        if all(x%r for r in range(3,int(x**0.5)+1,2)):
            out.append(x)
    return out

def check(p):
    d=first_nonsquare(p)
    T=[(x,y) for x in range(p) for y in range(p) if (x*x-d*y*y)%p==1]
    assert len(T)==p+1
    reps=Counter(((a[0]+b[0])%p,(a[1]+b[1])%p) for a in T for b in T)
    assert reps[(0,0)]==p+1
    assert max(v for s,v in reps.items() if s!=(0,0))<=2
    energy=sum(v*v for v in reps.values())
    assert energy==3*p*(p+1)
    return len(T),len(reps),energy

def main():
    ps=primes_upto(101)
    total_sums=0
    for p in ps:
        _,nr,_=check(p); total_sums+=nr
    print(f'VERIFY_OK primes={len(ps)} max_prime={max(ps)} represented_sums={total_sums}')

if __name__=='__main__':
    main()
