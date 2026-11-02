"""Independent finite enumeration of collision-free quadratic moment fibers."""
from collections import defaultdict


def primes(n):
    out=[]
    p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:
                n//=p
                k+=1
            out.append((p,k))
        p+=1
    if n>1:
        out.append((n,1))
    return out


def character(a,p):
    a%=p
    if a==0:
        return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def field_count(p,s,w):
    if p==2:
        return 0
    if p==3:
        return 6 if s%3==0 and w%3==2 else 0
    d=(3*w-s*s)%p
    chi=character(-3,p)
    if d==0:
        return (p-1)*(1+chi)
    return p-chi-3*(1+character(d*pow(2,-1,p),p))


def formula(n,s,w):
    v=1
    for p,k in primes(n):
        v*=p**(k-1)*field_count(p,s%p,w%p)
    return v


def independent_census(n):
    out=defaultdict(int)
    for x in range(n):
        for y in range(n):
            if any((x-y)%p==0 for p,k in primes(n)):
                continue
            z_candidates=(z for z in range(n)
                 if all((x-z)%p!=0 and (y-z)%p!=0 for p,k in primes(n)))
            for z in z_candidates:
                out[((x+y+z)%n,(x*x+y*y+z*z)%n)]+=1
    assert sum(out.values())==sum(formula(n,s,w) for s in range(n) for w in range(n))
    for s in range(n):
        for w in range(n):
            assert out.get((s,w),0)==formula(n,s,w),(n,s,w,out.get((s,w),0),formula(n,s,w))
    return len(out),sum(out.values())


def run():
    levels=[2,3,4,5,7,8,9,11,13,17,19,25,27,35,45,49,55,63,77,81,121,125,169]
    checks=0
    for n in levels:
        support, triples=independent_census(n)
        checks+=n*n
        print('LEVEL_OK',n,'support',support,'total_trip',triples)
    print('VERIFY_OK full_moduli=',len(levels),'target_fibers=',checks)


if __name__=='__main__':
    run()
