#!/usr/bin/env python3
"""Independent finite checker for odd/even dihedral R_n filtration statistics."""
from collections import Counter
from itertools import product
from math import gcd

def divisors(n): return [d for d in range(1,n+1) if n%d==0]
def phi(n): return sum(gcd(i,n)==1 for i in range(1,n+1)) if n>1 else 1

def affine(n):
    return [tuple((u*x+v)%n for x in range(n)) for u in range(n) for v in range(n)]

def check_algebra():
    for n in range(2,6):
        maps=[]
        for vals in product(range(n),repeat=n):
            if all(vals[(2*y-x)%n] == (2*vals[y]-vals[x])%n for x in range(n) for y in range(n)):
                maps.append(vals)
        assert set(maps)==set(affine(n)),(n,len(maps))
    for n in range(2,11):
        all_aff=affine(n)
        cosets = {frozenset((a+d*j)%n for j in range(n//d)) for d in divisors(n) for a in range(d)}
        subs=[]
        for mask in range(1,1<<n):
            U={x for x in range(n) if mask>>x&1}
            if all((2*y-x)%n in U for x in U for y in U):
                subs.append(frozenset(U))
        assert set(subs)==cosets,(n,sorted(subs,key=lambda x:(len(x),sorted(x)))[:4])
        for U in subs:
            for x in U:
                num=sum(all(m[y] in U for y in (x,)) for m in all_aff)
                assert num==n*len(U), (n,U,x,num)
            # stronger test using all 2-element subsets of U
            for x in U:
                for y in U:
                    num=sum(m[x] in U and m[y] in U for m in all_aff)
                    assert num==n*len(U),(n,U,x,y,num)
    print('ALGEBRA_OK')

def braid_trace(n,k,a,b):
    # Dihedral coloring under one positive crossing.
    x,y=a,b
    seen={a,b}
    for _ in range(k):
        x,y=y,(2*y-x)%n
        seen.add(x);seen.add(y)
    assert (x,y)==(a,b) or (k*(b-a))%n != 0
    return (x,y),seen

def predicted_monomial(n,r):
    mon=Counter()
    factor=n//r
    mon[(0,1)] += factor
    mon[(1,1)] += factor*(n-1)
    for s in divisors(r):
        if s==1:continue
        mon[(1,s-1)] += factor*phi(s)*s
        mon[(1,s)] += factor*phi(s)*(n-s)
    return tuple(sorted((a,b,e) for (a,b),e in mon.items() if e))

def brute_monomial(n, image):
    cnt=Counter()
    for u in range(n):
        for v in range(n):
            im={(u*x+v)%n for x in image}
            layer=0 if im=={0} else 1
            weight=1 if layer==0 else len(im-{0})
            cnt[(layer,weight)] +=1
    assert sum(cnt.values())==n*n
    return tuple(sorted((a,b,e) for (a,b),e in cnt.items() if e))

def graded_formula(n,k):
    ans=Counter()
    for r in divisors(gcd(n,k)):
        ans[predicted_monomial(n,r)] += n*phi(r)
    return ans

def check_links():
    for n in (2,3,4,5,6,7,8,9,10,12,15):
        for k in (1,3,5,7,9,15):
            if n>10 and k>9:continue
            obs=Counter()
            for a in range(n):
                for b in range(n):
                    endpoint, colors=braid_trace(n,k,a,b)
                    if endpoint!=(a,b):continue
                    delta=(b-a)%n
                    r=n//gcd(n,delta) if delta else 1
                    assert colors=={(a+j*delta)%n for j in range(r)},(n,k,a,b,colors,r)
                    observed=brute_monomial(n,colors)
                    expect=predicted_monomial(n,r)
                    assert observed==expect,(n,k,a,b,observed,expect)
                    obs[observed]+=1
            theory=graded_formula(n,k)
            assert obs==theory,(n,k,obs,theory)
    print('GRADED_OK')

if __name__=='__main__':
    check_algebra()
    check_links()
    for r in divisors(9): print('N9_R',r,predicted_monomial(9,r))
    print('VERIFY_OK')
