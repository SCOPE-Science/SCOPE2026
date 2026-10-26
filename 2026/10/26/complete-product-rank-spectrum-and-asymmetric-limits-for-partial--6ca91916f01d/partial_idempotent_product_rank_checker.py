#!/usr/bin/env python3
"""Direct map enumeration and two distinct formula checks for partial idempotent products.

-1 denotes an undefined value; composition is e after f. No external data.
"""
from collections import Counter
from itertools import product
from math import comb

def idempotents(n):
    # Each map is a tuple in {-1, 0, ..., n-1}^n.
    maps=[]
    for f in product(range(-1,n), repeat=n):
        if all(y==-1 or f[y]==y for y in f): maps.append(f)
    return maps

def rank(f): return len(set(f)-{-1})

def direct_product_rank(e,f):
    return len({e[y] for y in f if y!=-1 and e[y]!=-1})

def occupancy(n,r,s,t):
    if not (0 <= r <= n and 0 <= s <= n and 0 <= t <= min(r,s)):
        return 0
    ans=0
    for h in range(max(0,r+s-n), min(r,s,t)+1):
        m=s-h
        d=t-h
        hit=sum((-1)**(d-j)*comb(d,j)*(h+j+1)**m for j in range(d+1))
        ways=comb(r,h)*comb(n-r,m)*comb(r-h,d)*hit*(r+1)**(n-r-m)
        ans+=ways
    return comb(n,r)*(s+1)**(n-s)*ans

def block_coefficient(n,r,s,t):
    if not (0 <= r <= n and 0 <= s <= n and 0 <= t <= min(r,s)):
        return 0
    tot=0
    for j in range(t+1):
        coeff=sum(comb(j,l)*comb(n-r,s-l)*(r+1)**(n-r-s+l)*(j+1)**(s-l)
                  for l in range(max(0,s-(n-r)), min(j,s)+1))
        tot+=(-1)**(t-j)*comb(t,j)*coeff
    return comb(n,r)*comb(r,t)*(s+1)**(n-s)*tot

def main():
    for n in range(0,6):
        fs=idempotents(n)
        count=Counter()
        for e in fs:
            r=rank(e)
            for f in fs:
                s=rank(f)
                t=direct_product_rank(e,f)
                count[r,s,t]+=1
        for r in range(n+1):
            for s in range(n+1):
                for t in range(n+1):
                    direct=count[r,s,t]
                    a=occupancy(n,r,s,t)
                    b=block_coefficient(n,r,s,t)
                    assert direct == a == b,(n,r,s,t,direct,a,b)
        assert len(fs)==sum(comb(n,r)*(r+1)**(n-r) for r in range(n+1))
        print(f'n={n} idempotents={len(fs)} pairs={len(fs)**2} nonzero_rank_triples={len(count)}')
    checks=0
    for n in range(0,15):
        for r in range(n+1):
            for s in range(n+1):
                for t in range(min(r,s)+1):
                    assert occupancy(n,r,s,t)==block_coefficient(n,r,s,t),(n,r,s,t)
                    checks+=1
    n=5;r=2;s=4
    hist1=[occupancy(n,r,s,t) for t in range(min(r,s)+1)]
    hist2=[occupancy(n,s,r,t) for t in range(min(r,s)+1)]
    print('ORDER_ASYMMETRY n=5 r=2 s=4 product_EafterF='+str(hist1)+' product_FafterE='+str(hist2))
    print('ALL_PARTIAL_IDEMPOTENT_PRODUCT_RANK_CHECKS_PASSED block_formula_checks='+str(checks))

if __name__=='__main__': main()
