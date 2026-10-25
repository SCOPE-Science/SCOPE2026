#!/usr/bin/env python3
"""Direct finite verification of maximal nilpotent-chain endpoint fibres."""
from itertools import permutations
from collections import Counter
from math import gcd


def parity_of_cyclic_word(vals):
    k=len(vals)
    desc=sum(vals[i]>vals[(i+1)%k] for i in range(k))
    asc=sum(vals[i]<vals[(i+1)%k] for i in range(k))
    return desc==1,asc==1


def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))


def direct_histogram(n):
    plus=Counter()
    for chain in permutations(range(n)):
        a=chain[-1]; b=chain[0]
        f=dict(zip(chain[:-1],chain[1:]))
        word=[f[x] for x in range(n) if x!=a]
        orient, _=parity_of_cyclic_word(word)
        if orient:plus[(a,b)]+=1
    return plus


def explicit_map(n,a,b,offset):
    dom=sorted(set(range(n))-{a})
    im=sorted(set(range(n))-{b})
    return {x:im[(j+offset)%(n-1)] for j,x in enumerate(dom)}


def single_chain(f,n,a,b):
    if len(f)!=n-1 or set(f)!=set(range(n))-{a} or set(f.values())!=set(range(n))-{b}:return False
    path=[];x=b
    while x in f and x not in path:
        path.append(x)
        x=f[x]
    path.append(x)
    return x==a and len(path)==n and len(set(path))==n


def flip(f,n):
    return {n-1-x:n-1-y for x,y in f.items()}


def check(n):
    plus=direct_histogram(n)
    for a in range(n):
        for b in range(n):
            d=(b-a)%n
            predicted=(a!=b) and (n%2==1 or d%2==1)
            assert (plus[(a,b)]>0)==predicted,(n,a,b,plus[(a,b)],predicted)
            if a!=b and d in {1,n-1}:
                assert plus[(a,b)]==phi(n-1),(n,a,b,plus[(a,b)],phi(n-1))
            assert plus[(a,b)]<=n-1
    return sum(plus.values()),len(plus)


def check_constructive(n):
    for a in range(n):
        for b in range(n):
            if a==b:continue
            d=(b-a)%n
            if n%2==0 and d%2==0:continue
            # Rotate endpoints to (n-1, d-1) in cyclic coordinates.
            shift=(n-1-a)%n
            bb=(b+shift)%n
            if (n%2)==(bb%2):
                p=explicit_map(n,n-1,bb,1)
            else:
                # For odd n, reflection changes odd distance to an even one.
                d1=n-d
                p=explicit_map(n,n-1,d1-1,1)
                p=flip(p,n)
                # Following flip, missing domain is 0; rotate it back to n-1.
                p={(x+n-1)%n:(y+n-1)%n for x,y in p.items()}
            p={(x-shift)%n:(y-shift)%n for x,y in p.items()}
            assert single_chain(p,n,a,b),(n,a,b,d,p)
            orient,_=parity_of_cyclic_word([p[x] for x in sorted(p)])
            assert orient,(n,a,b)


def main():
    for n in range(3,10):
        cp,count=check(n)
        print(f'n={n} oriented_chains={cp} attainable_endpoint_pairs={count}')
    for n in range(3,36):check_constructive(n)
    # This pair is forbidden for maximal chains inside any single cyclic rotation:
    # a 6-cycle cannot have step three, yet an oriented partial map exists.
    f=explicit_map(6,5,2,1)
    assert single_chain(f,6,5,2)
    print('VERIFY_OK: exhaustive Hamilton chains n=3..9, constructions n=3..35, arithmetic fibres')

if __name__=='__main__':main()
