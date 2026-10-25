#!/usr/bin/env python3
"""Direct finite-field orbit enumeration for annihilator-valued Rota-Baxter maps.
Uses only standard Python and direct field arithmetic. """
from itertools import product,combinations
from math import gcd

def field(q):
    modulus={2:0b11,4:0b111,8:0b1011}[q]
    def mul(x,y):
        p=0
        while y:
            if y&1:p^=x
            y>>=1
            x<<=1
            if x&q:x^=modulus
        return p
    def power(x,n):
        t=1
        for _ in range(n):t=mul(t,x)
        return t
    return mul,power

def action(c,a,b,q,mul,powf):
    n=len(c); L=2**(n-1)
    z=[0]*n
    z[n-1]=c[n-1]
    for i in range(1,n-1):
        z[i]=mul(powf(a,L-2**i),c[i])
    z[0]=mul(powf(a,L-1),c[0]) ^ mul(mul(b,powf(a,q-2)),c[n-1])
    return tuple(z)

def expected_orbit_size(c,q):
    n=len(c); t=q-1
    indices=range(n-1) if c[-1]==0 else range(1,n-1)
    support=[i for i in indices if c[i]]
    if not support:return 1 if c[-1]==0 else q
    d=0
    for i in support:d=gcd(d,n-(i+1))
    d=gcd(d,q.bit_length()-1)
    stabilizer=2**d-1
    return t//stabilizer if c[-1]==0 else q*t//stabilizer

def predicted_orbits(q,n):
    t=q-1;e=q.bit_length()-1
    def subset_sum(indices):
        val=1; indices=list(indices)
        for j in range(1,len(indices)+1):
            for J in combinations(indices,j):
                g=e
                for i in J:g=gcd(g,n-(i+1))
                val+=t**(j-1)*(2**g-1)
        return val
    return subset_sum(range(n-1))+t*subset_sum(range(1,n-1))

def predicted_divisor_sum(q,n):
    t=q-1
    def phi(d):
        return sum(gcd(i,d)==1 for i in range(1,d+1))
    def order_two(d):
        if d==1:return 1
        x=2%d;h=1
        while x!=1:
            x=(2*x)%d;h+=1
        return h
    total=0
    for d in range(1,t+1):
        if t%d:continue
        h=order_two(d)
        total+=phi(d)*(q**((n-1)//h)+t*q**((n-2)//h))
    assert total%t==0
    return total//t

def check(q,n):
    mul,powf=field(q)
    cset=set(product(range(q),repeat=n))
    group=list(product(range(1,q),range(q)))
    # Formula is checked against orbit-size classification for EVERY coefficient vector.
    seen=set();sizes={}
    for c in cset:
        if c in seen:continue
        orbit={action(c,a,b,q,mul,powf) for a,b in group}
        assert orbit<=cset
        for x in orbit:
            assert expected_orbit_size(x,q)==len(orbit),(q,n,c,x,len(orbit))
        assert not (orbit & seen)
        seen.update(orbit)
        sizes[len(orbit)]=sizes.get(len(orbit),0)+1
    assert seen==cset
    assert sum(s*cnt for s,cnt in sizes.items())==q**n
    want=predicted_orbits(q,n)
    assert sum(sizes.values())==want==predicted_divisor_sum(q,n),(q,n,want,sizes,predicted_divisor_sum(q,n))
    print('ORBIT_OK',q,n,'operators',q**n,'orbits',want,'orbit_sizes',sorted(sizes.items()))

def check_full_automorphisms(q,n):
    mul,powf=field(q)
    # Directly enumerate all n-by-n linear matrices in small cases.
    def prod(x,y):return tuple(0 if i==0 else mul(x[i-1],y[i-1]) for i in range(n))
    def mapping(cols,v):return tuple(__import__('functools').reduce(lambda acc,z:acc^z,(mul(v[i],cols[i][j]) for i in range(n)),0) for j in range(n))
    es=[tuple(int(i==j) for j in range(n)) for i in range(n)]
    autos=[]
    for flat in product(range(q),repeat=n*n):
        cols=tuple(tuple(flat[i*n:(i+1)*n]) for i in range(n))
        if any(prod(cols[i],cols[j])!=(0,)*n for i in range(n) for j in range(i+1,n)):continue
        if any(prod(cols[i],cols[i])!=cols[i+1] for i in range(n-1)):continue
        if prod(cols[-1],cols[-1])!=(0,)*n:continue
        if len({mapping(cols,v) for v in product(range(q),repeat=n)})!=q**n:continue
        autos.append(cols)
    predicted=[]
    for a,b in product(range(1,q),range(q)):
        cols=[]
        for i in range(n):
            v=[0]*n
            v[i]=powf(a,2**i)
            if i==0:v[-1]=b
            cols.append(tuple(v))
        predicted.append(tuple(cols))
    assert set(autos)==set(predicted),(q,n,len(autos),len(predicted))
    print('AUT_OK',q,n,'linear_maps_checked',q**(n*n),'automorphisms',len(autos))

if __name__=='__main__':
    check_full_automorphisms(2,3)
    check_full_automorphisms(4,2)
    for q,n in [(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4),(8,2),(8,3),(8,4)]:check(q,n)
    print('VERIFY_OK')
