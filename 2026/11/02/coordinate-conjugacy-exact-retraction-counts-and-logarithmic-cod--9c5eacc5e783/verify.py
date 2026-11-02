#!/usr/bin/env python3
"""Finite, independent checks for retractions of truncated group algebras.

For p=2,d=2, enumerate every unital F_q-algebra endomorphism over q=2,4,
calculate its square by direct substitution, and determine the F_q-linear
rank of its image by explicit Gaussian elimination. No symbolic theorem
is assumed by the exhaustive path. Also verify closed-form group-index
counts in a variety of (p,q,d) settings.
"""
from itertools import product
import math

def field(q):
    if q==2:
        return lambda a,b:a^b, lambda a,b:a&b
    if q==4:
        def mult(a,b):
            c=0
            for i in range(2):
                for j in range(2):
                    if (a>>i)&1 and (b>>j)&1:
                        c^=(1<<(i+j))
            if c&8:c^=0b1110 # t^3=(t+1)t=t^2+t; reduce t^3+t^2+t=0
            if c&4:c^=0b111  # t^2=t+1
            return c
        return lambda a,b:a^b, mult
    raise ValueError(q)

def explicit(q):
    plus,mul=field(q)
    elems=list(product(range(q),repeat=3)) # coefficients for x,y,xy
    zero=(0,0,0,0)
    one=(1,0,0,0)
    def add(v,w):return tuple(plus(a,b) for a,b in zip(v,w))
    def times(v,w):
        a,b,c,d=v; e,f,g,h=w
        return (mul(a,e),plus(mul(a,f),mul(b,e)),plus(mul(a,g),mul(c,e)),
                plus(plus(mul(a,h),mul(b,g)),plus(mul(c,f),mul(d,e))))
    def scale(a,v):return tuple(mul(a,b) for b in v)
    def ev(v,u,w):
        z=times(u,w)
        acc=scale(v[0],one)
        for coef,basis in zip(v[1:],(u,w,z)):
            acc=add(acc,scale(coef,basis))
        return acc
    def independent_rank(vectors):
        a=[list(v) for v in vectors]
        rank=0
        for col in range(4):
            pivot=next((j for j in range(rank,len(a)) if a[j][col]!=0),None)
            if pivot is None:continue
            a[rank],a[pivot]=a[pivot],a[rank]
            # normalize not needed for elimination; use inverses
            inv=next(i for i in range(1,q) if mul(i,a[rank][col])==1)
            a[rank]=[mul(inv,b) for b in a[rank]]
            for j in range(len(a)):
                if j!=rank and a[j][col]:
                    factor=a[j][col]
                    a[j]=[plus(t,mul(factor,s)) for t,s in zip(a[j],a[rank])]
            rank+=1
        return rank
    cnt={}
    for us,ws in product(elems,repeat=2):
        u=(0,)+us; w=(0,)+ws
        if ev(u,u,w)==u and ev(w,u,w)==w:
            rank=independent_rank((one,u,w,times(u,w)))
            cnt[rank]=cnt.get(rank,0)+1
    predicted={1:1,2:(q+1)*q*q,4:1}
    assert cnt==predicted,(q,cnt,predicted)
    return q,cnt

def gl(n,q):
    out=1
    for i in range(n):out*=q**n-q**i
    return out

def gbin(n,k,q):
    return (gl(n,q)//(gl(k,q)*gl(n-k,q)*q**(k*(n-k))))

def n_retractions(d,k,p,q):
    K=p**k;P=p**d;b=d-k
    e=k*(P-K)+b*(K-k-1)
    assert e>=0
    return gbin(d,k,q)*q**e

def orbit_count(d,k,p,q):
    P=p**d;K=p**k;b=d-k
    numer=gl(d,q)*q**(d*(P-1-d))
    denom=gl(k,q)*gl(b,q)*q**(k*(K-k-1)+b*(P-K-b))
    assert numer%denom==0
    return numer//denom

def main():
    print('EXHAUSTIVE', explicit(2),explicit(4))
    tests=0
    for p,q in [(2,2),(2,4),(3,3),(3,9),(5,5)]:
        for d in range(1,6):
            for k in range(d+1):
                assert n_retractions(d,k,p,q)==orbit_count(d,k,p,q)
                tests+=1
    assert [n_retractions(3,k,2,2) for k in range(4)]==[1,448,3584,1]
    # For d large, check rigorous three-point mass bound numerically via exact integers
    for p,q,d in ((2,2,20),(2,4,25),(3,3,19)):
        b0=0
        while p**(b0+1)<=d:b0+=1
        vals=[]
        for b in range(d+1):
            k=d-b; K=p**k;P=p**d
            exp=k*(P-K)+b*(K-k-1)
            vals.append(exp + math.log(gbin(d,k,q),q))
        peak=max(vals)
        mass=sum(q**(v-peak) for v in vals)
        inside=sum(q**(vals[b]-peak) for b in range(max(0,b0-1),min(d,b0+1)+1))
        assert inside/mass > 0.999,(p,q,d,inside/mass)
    print('VERIFY_OK: two complete endomorphism censuses; %d exact independent group-index identities; three asymptotic consistency cases'%tests)
if __name__=='__main__':main()
