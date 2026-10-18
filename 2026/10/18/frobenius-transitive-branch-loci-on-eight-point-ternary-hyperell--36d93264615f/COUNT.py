#!/usr/bin/env python3
"""Exact enumeration of a natural ternary prime-polynomial class.

No outside libraries are required.  Output is independent finite arithmetic,
not a claim that finite tests prove the all-degree theorem.
"""
from itertools import product
from math import prod

P = 3

def trim(f):
    a = list(f)
    while a and a[-1] % 3 == 0:
        a.pop()
    return tuple(t % 3 for t in a)

def add(f,g):
    return trim([( (f[i] if i < len(f) else 0) + (g[i] if i < len(g) else 0) ) % 3 for i in range(max(len(f),len(g)))])

def neg(f):
    return tuple((-c)%3 for c in f)

def mul(f,g):
    if not f or not g: return ()
    a=[0]*(len(f)+len(g)-1)
    for i,x in enumerate(f):
        if x:
            for j,y in enumerate(g):
                a[i+j]=(a[i+j]+x*y)%3
    return trim(a)

def mod(f,g):
    a=list(trim(f)); b=trim(g)
    assert b
    while len(a)>=len(b):
        t=a[-1]*pow(b[-1],-1,3)%3
        shift=len(a)-len(b)
        for j,v in enumerate(b): a[j+shift]=(a[j+shift]-t*v)%3
        while a and not a[-1]:a.pop()
    return tuple(a)

def gcd(f,g):
    while g:f,g=g,mod(f,g)
    if not f:return ()
    v=pow(f[-1],-1,3)
    return tuple(x*v%3 for x in f)

def powmod(a,e,f):
    b=(1,)
    while e:
        if e&1:b=mod(mul(b,a),f)
        a=mod(mul(a,a),f)
        e>>=1
    return b

def prime_divisors(n):
    ps=[];d=2
    while d*d<=n:
        if n%d==0:
            ps.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:ps.append(n)
    return ps

def irreducible(f):
    n=len(f)-1
    x=(0,1)
    h=x
    ff={0:x}
    for k in range(1,n+1):
        h=powmod(h,3,f)
        ff[k]=h
    if ff[n]!=x:return False
    for ell in prime_divisors(n):
        if gcd(f,add(ff[n//ell],neg(x)))!=(1,):return False
    return True

def candidates(n):
    assert n>=4 and n%2==0
    ev=list(range(2,n-2,2))
    odd=list(range(1,n-1,2))
    for tup in product(range(3),repeat=len(ev)+len(odd)):
        a=[0]*(n+1);a[0]=a[n]=1
        for i,z in zip(ev,tup[:len(ev)]):a[i]=z
        for i,z in zip(odd,tup[len(ev):]):a[i]=z
        a[n-2]=(2-sum(a[i] for i in ev))%3
        a[n-1]=(-sum(a[i] for i in odd))%3
        yield tuple(a)

def mobius(n):
    q=1
    for p in prime_divisors(n):
        if n%(p*p)==0:return 0
        q=-q
    return q

def all_residue_count(n):
    assert n>0 and n%2==0
    return (3**n-15-2*(-3)**(n//2))//8

def arithmetic_count(n):
    assert n%2==0
    z=0
    for d in range(1,n+1):
        if n%d:continue
        k=n//d
        a=3**d-3 if k%2==0 else all_residue_count(d)
        z+=mobius(k)*a
    assert z%n==0
    return z//n

if __name__=='__main__':
    print('n count_by_formula brute_force')
    for n in (4,6,8,10,12):
        fs=[f for f in candidates(n) if irreducible(f)]
        k=arithmetic_count(n)
        print(n,k,len(fs))
        assert len(fs)==k
        if n==6:
            assert (1,0,0,0,2,0,1) in fs
    assert arithmetic_count(2)==0
    for n in range(2,44,2):
        assert arithmetic_count(n)>=0
        if n>=6:assert arithmetic_count(n)>0
    print('checked analytic counts through degree 42; exhaustive through degree 12')
