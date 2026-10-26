#!/usr/bin/env python3
"""Independent exact enumeration of joint coset leaders for extended binary Hamming codes."""
from collections import defaultdict
from itertools import combinations, product
from math import comb, factorial


def rank_binary_rows(rows, width):
    basis = [0] * width
    r = 0
    for y in rows:
        x = y
        while x:
            i = x.bit_length() - 1
            if basis[i]:
                x ^= basis[i]
            else:
                basis[i] = x
                r += 1
                break
    return r


def rank_count(a, t, r):
    if r < 0 or r > min(a,t):
        return 0
    if r == 0:
        return 1
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (2**a - 2**i) * (2**t - 2**i)
        denominator *= 2**r - 2**i
    assert numerator % denominator == 0
    return numerator // denominator


def gl(r):
    v = 1
    for i in range(r):
        v *= 2**r - 2**i
    return v


def expected(m,t):
    d = {}
    d[0] = (0,1,1)
    for r in range(1,min(m+1,t)+1):
        amount = rank_count(m+1,t,r)-rank_count(m,t,r)
        multiplicity = gl(r)//((2**r-1)*factorial(r))
        assert gl(r)%((2**r-1)*factorial(r))==0
        d[('A',r)] = (r,amount,multiplicity)
    for r in range(1,min(m,t)+1):
        amount = rank_count(m,t,r)
        numerator = 2**m*gl(r)
        assert numerator%factorial(r+1)==0
        d[('B',r)] = (r+1,amount,numerator//factorial(r+1))
    assert sum(z[1] for z in d.values())==2**((m+1)*t)
    return d


def syndrome(m,t, assignments):
    # H columns are (1,a), with a=0,...,2^m-1.
    top=0
    bottom=[0]*m
    for a,v in assignments:
        top^=v
        for i in range(m):
            if (a>>i)&1:
                bottom[i]^=v
    return (top,*bottom)


def brute(m,t):
    length=2**m
    radius=min(m,t)+1
    minimum={}
    leaders=defaultdict(int)
    tested=0
    for weight in range(radius+1):
        for positions in combinations(range(length), weight):
            for vals in product(range(1,2**t),repeat=weight):
                key=syndrome(m,t,zip(positions,vals))
                tested+=1
                if key not in minimum:
                    minimum[key]=weight
                    leaders[key]=1
                elif minimum[key]==weight:
                    leaders[key]+=1
        assert len(minimum)<=2**((m+1)*t)
    assert len(minimum)==2**((m+1)*t)
    observed=defaultdict(int)
    for key,weight in minimum.items():
        rows=[x for x in key]
        r=rank_binary_rows(rows,t)
        if r==0:
            cls=0
        elif key[0]==0:
            cls=('B',r)
        else:
            cls=('A',r)
        predicted=expected(m,t)[cls]
        assert (weight,leaders[key])==(predicted[0],predicted[2]), (m,t,key,weight,leaders[key],predicted)
        observed[cls]+=1
    for cls,(_,amount,_) in expected(m,t).items():
        assert observed[cls]==amount, (m,t,cls,amount,observed[cls])
    return tested, len(minimum), {str(k):v for k,v in sorted(observed.items(),key=lambda x:str(x[0]))}


if __name__=='__main__':
    for m,t in [(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)]:
        checks,cosets,hist=brute(m,t)
        print(f'm={m} t={t} checked_errors={checks} cosets={cosets} types={hist}')
    print('EXACT_JOINT_LEADERS_VERIFY_OK')
