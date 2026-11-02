#!/usr/bin/env python3
"""Independent finite-field table enumeration and arithmetic count checks."""
from itertools import product
from math import gcd


def prime_order_two(p):
    z=2%p
    m=1
    while z!=1:
        z=z*2%p
        m+=1
    return m


def expected_count(p,q):
    assert p%2==1 and p>=3 and q>=2
    m=prime_order_two(p)
    if m%2==0:
        h=m
        N=2**(m//2)+1
    else:
        h=2*m
        N=2**m-1
    s=(p-1)//h
    H={pow(2,e,p) for e in range(m)}|{-pow(2,e,p)%p for e in range(m)}
    assert len(H)==h
    if q%p==0:
        return 1+q**s, dict(m=m,h=h,N=N,s=s,d=0,sigma=0,e=0,g=0)
    d=1
    while pow(q,d,p) not in H:
        d+=1
        assert d<=s
    residue=pow(q,d,p)
    if m%2==0:
        signs=[1]
    else:
        signs=[1,-1]
    possible=[(sigma,e) for sigma in signs for e in range(m) if sigma*pow(2,e,p)%p==residue]
    assert len(possible)==1
    sigma,e=possible[0]
    g=gcd(N,abs(q**d-sigma*2**e))
    return 2*(1+g)**(s//d),dict(m=m,h=h,N=N,s=s,d=d,sigma=sigma,e=e,g=g)


def add(a,b,q):
    if q in (2,4): return a^b
    if q==9: return (a%3+b%3)%3+3*((a//3+b//3)%3)
    return (a+b)%q


def mul(a,b,q):
    if q==2:
        return a&b
    if q==9:
        c,d=a%3,a//3
        e,f=b%3,b//3
        return (c*e-d*f)%3+3*((c*f+d*e)%3)
    if q==4:
        x=0
        for i in range(2):
            if b & (1<<i):
                x ^= a<<i
        if x&8:
            x^=0b1100  # alpha^3 = alpha^2 + alpha in GF4, reduction
        if x&4:
            x^=0b111   # alpha^2 = alpha + 1
        return x
    return a*b%q


def brute(p,q):
    assert q in (2,3,4,5,7,9)
    lut=[[mul(i,j,q) for j in range(q)] for i in range(q)]
    target=[[(2*y-x)%p for y in range(p)] for x in range(p)]
    count=0
    for a in product(range(q),repeat=p):
        support=[(i,x) for i,x in enumerate(a) if x]
        if not support:
            count+=1
            continue
        b=[0]*p
        for i,x in support:
            row=target[i]
            for j,y in support:
                k=row[j]
                b[k]=add(b[k],lut[x][y],q)
        if all(b[i]==a[i] for i in range(p)):
            count+=1
    return count


def main():
    # Full coefficient-space enumerations; no sampling or Fourier method used.
    cases=[(3,2),(3,3),(3,4),(3,5),(3,9),
           (5,2),(5,3),(5,4),(5,5),
           (7,2),(7,3),(7,4),(7,7),
           (11,2),(11,3),(13,2),(17,2)]
    seen=set()
    for p,q in cases:
        if (p,q) in seen: continue
        seen.add((p,q))
        pred,data=expected_count(p,q)
        got=brute(p,q)
        assert pred==got,(p,q,pred,got)
        print(f'EXHAUSTIVE_OK p={p} q={q} ambient={q**p} idempotents={got} H={data["h"]} d={data["d"]} root_gcd={data["g"]}')
    for p,q in [(11,3),(17,3),(17,5),(31,2),(31,3),(41,2)]:
        print(f'ARITHMETIC p={p} q={q} count={expected_count(p,q)[0]}')
    print('VERIFY_OK all independent coefficient-table checks passed')

if __name__=='__main__': main()
