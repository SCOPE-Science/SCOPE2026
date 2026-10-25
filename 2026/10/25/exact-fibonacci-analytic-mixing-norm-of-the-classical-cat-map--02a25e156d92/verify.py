#!/usr/bin/env python3
"""Exact integer verification for a Fibonacci analytic-correlation formula."""

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a


def power(n):
    if n==0: return (1,0,0,1)
    return (fib(2*n+1),fib(2*n),fib(2*n),fib(2*n-1))


def apply(p,x,y):
    a,b,c,d=p
    return a*x+b*y,c*x+d*y


def norm(z): return abs(z[0])+abs(z[1])


def minimal_modes(n):
    r=n//2
    q=power(r)
    qi=(q[3],-q[1],-q[2],q[0])
    if n%2==0:
        w=((1,0),(-1,0),(0,1),(0,-1))
    else:
        w=((0,1),(0,-1),(1,-1),(-1,1))
    return {apply(qi,*v) for v in w}


def verify():
    count=0
    for n in range(13):
        p=power(n)
        f=fib(n+3)
        expected=minimal_modes(n)
        observed=set()
        best=10**10
        for x in range(-f,f+1):
            for y in range(-(f-abs(x)),f-abs(x)+1):
                if not (x or y): continue
                v=abs(x)+abs(y)+norm(apply(p,x,y))
                count+=1
                if v<best:best=v;observed={(x,y)}
                elif v==best:observed.add((x,y))
        assert best==f,(n,best,f)
        assert observed==expected,(n,observed,expected)
    # Identity check on arbitrary, much larger iterates (no infinite proof claim).
    for n in range(121):
        assert len(minimal_modes(n))==4
        p=power(n)
        for k in minimal_modes(n):
            assert norm(k)+norm(apply(p,*k))==fib(n+3)
    print('VERIFY_OK exhaustive_n=0..12 exact_integer_pairs=',count,'minimizers_per_n=4 candidate_iterations=0..120')

if __name__=='__main__':verify()
