#!/usr/bin/env python3
"""Independent finite checks for three-marker circular-palindrome distribution.
Science-only checker: no external files or packages required.
"""
from collections import Counter
from itertools import product


def direct_palindromes(gaps):
    a,b,c = gaps
    word = '1' + '0'*a + '1' + '0'*b + '1' + '0'*c
    n = len(word)
    doubled = word + word
    return {doubled[i:i+j] for i in range(n) for j in range(1,n+1)
            if doubled[i:i+j] == doubled[i:i+j][::-1]}


def gap_inventory(gaps):
    vals = sorted(gaps)
    a,b,c = vals
    zeros = {'0'*j for j in range(1,c+1)}
    one = {'0'*j+'1'+'0'*j for j in range(b+1)}
    two = set()
    for index, g in enumerate(gaps):
        rem = [v for ii,v in enumerate(gaps) if ii != index]
        for j in range(min(rem)+1):
            two.add('0'*j+'1'+'0'*g+'1'+'0'*j)
    three = set()
    for i in range(3):
        if gaps[i] == gaps[(i+1)%3]:
            g = gaps[i]
            outer = gaps[(i+2)%3]
            for j in range(outer//2+1):
                three.add('0'*j+'1'+'0'*g+'1'+'0'*g+'1'+'0'*j)
    return zeros | one | two | three


def exact_palcount(gaps):
    a,b,c = sorted(gaps)
    if a==b==c:
        two = a+1
        three = a//2+1
    elif a==b:
        two = 2*a+2
        three = c//2+1
    elif b==c:
        two = a+b+2
        three = a//2+1
    else:
        two = 2*a+b+3
        three = 0
    return c + (b+1) + two + three


def gf_counts(max_m):
    """Extract the exact claimed rational generating function coefficientwise.

    Terms: D + BC + A. Each geometric series is expanded independently.
    Returns multiset counts indexed by (zero_count, number_of_palindromes).
    """
    out=Counter()
    for u in range(max_m//6+1):
        for v,p in ((0,3),(3,6)):
            m=6*u+v
            if m<=max_m:out[(m,7*u+p)]+=1
    for im,ip in ((1,5),(2,7),(4,10),(5,11)):
        for u in range(max_m//6+1):
            for v in range(max_m//2+1):
                m=im+6*u+2*v
                if m<=max_m:out[(m,ip+9*u+3*v)]+=1
    # numerator x*y5+2*x^2*y7+x^4*y10+2*x^5*y11
    for im,ip in ((2,7),(5,11)):
        for u in range(max_m//6+1):
            for v in range(max_m//2+1):
                m=im+6*u+2*v
                if m<=max_m:out[(m,ip+9*u+3*v)]+=1
    for i in range(max_m//3+1):
        for j in range(max_m//2+1):
            for k in range(max_m+1):
                m=3+3*i+2*j+k
                if m<=max_m:out[(m,8+5*i+3*j+k)]+=2
    return out


def test():
    count = 0
    for a,b,c in product(range(20),repeat=3):
        inventory=gap_inventory((a,b,c))
        direct=direct_palindromes((a,b,c))
        assert inventory==direct,(a,b,c,inventory.symmetric_difference(direct))
        assert len(direct)==exact_palcount((a,b,c)),(a,b,c)
        count+=1
    assert count==8000
    cap=50
    gf=gf_counts(cap)
    actual=Counter()
    for a in range(cap+1):
        for b in range(a,cap+1):
            for c in range(b,cap+1):
                if a+b+c>cap:break
                m=a+b+c
                weight=2 if a<b<c else 1
                actual[(m,exact_palcount((a,b,c)))]+=weight
    assert gf==actual,[(key,gf[key],actual[key]) for key in gf.keys()|actual.keys() if gf[key]!=actual[key]][:10]
    # Independent necklace enumeration (all binary necklaces with exactly three 1s).
    checked_necklaces=0
    for n in range(3,18):
        classes={}
        for p in range(n):
            for q in range(p+1,n):
                for r in range(q+1,n):
                    w=['0']*n
                    for i in (p,q,r):w[i]='1'
                    w=''.join(w)
                    key=min(w[i:]+w[:i] for i in range(n))
                    classes[key]=w
        counts=Counter()
        for key,w in classes.items():
            n0=len(w)
            direct={w2[i:i+j] for w2 in [w+w] for i in range(n0) for j in range(1,n0+1) if w2[i:i+j]==w2[i:i+j][::-1]}
            counts[(n0-3,len(direct))]+=1
        assert counts==Counter({k:v for k,v in gf.items() if k[0]==n-3}),(n,counts)
        checked_necklaces+=len(classes)
    print(f'PASS direct gap-inventory and exact count: {count} labeled gap triples')
    print(f'PASS bivariate generating function: all zero counts 0..{cap}')
    print(f'PASS independent rotation-orbit enumeration: {checked_necklaces} necklaces at lengths 3..17')
    print('First distributions:',{n:dict(sorted((k[1],v) for k,v in gf.items() if k[0]==n-3)) for n in range(3,12)})

if __name__=='__main__':test()
