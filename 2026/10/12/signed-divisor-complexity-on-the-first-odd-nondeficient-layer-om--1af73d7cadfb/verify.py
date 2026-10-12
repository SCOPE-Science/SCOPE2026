#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import csv, math

ROOT = Path(__file__).resolve().parent


def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True


def primes(a,b):
    return [n for n in range(max(2,a), b+1) if is_prime(n)]


def factor(n):
    out={}
    d=2
    while d*d<=n:
        while n%d==0:
            out[d]=out.get(d,0)+1; n//=d
        d=3 if d==2 else d+2
    if n>1: out[n]=out.get(n,0)+1
    return out


def sigma_from_factor(f):
    z=1
    for p,a in f.items():
        z *= (p**(a+1)-1)//(p-1)
    return z


def all_divisors(f):
    ds=[1]
    for p,a in sorted(f.items()):
        ds=[d*p**e for d in ds for e in range(a+1)]
    return sorted(ds)


def omega(f): return sum(f.values())


def abundancy(n):
    return Fraction(sigma_from_factor(factor(n)),n)


def enumerate_boundary():
    out=[]
    # Support 3. The proof in RESULT.md forces support {3,5,7}.
    for exps in product(range(1,4), repeat=3):
        if sum(exps)!=5: continue
        n=3**exps[0]*5**exps[1]*7**exps[2]
        if sigma_from_factor(factor(n)) >= 2*n:
            out.append(n)
    # Support 4. The proof forces the two smallest primes to be 3,5 and p_max <= 103.
    ps=primes(3,103)
    for comb in combinations(ps,4):
        if comb[0]!=3 or comb[1]!=5: continue
        for j in range(4):
            n=1
            for i,p in enumerate(comb):
                n*=p**(2 if i==j else 1)
            if sigma_from_factor(factor(n)) >= 2*n:
                out.append(n)
    # Support 5. The proof forces the first three primes to be 3,5,7 and p_max <= 383.
    for p,q in combinations([r for r in primes(11,383)],2):
        n=3*5*7*p*q
        if sigma_from_factor(factor(n)) >= 2*n:
            out.append(n)
    return sorted(set(out))


def min_negative(n):
    f=factor(n); sig=sigma_from_factor(f)
    assert n%2==1 and omega(f)==5 and sig>=2*n
    excess=sig-2*n
    assert excess%2==0
    H=excess//2
    ds=[d for d in all_divisors(f) if 1<d<n and d<=H]
    for k in range(1,6):
        for comb in combinations(ds,k):
            if sum(comb)==H:
                return k,tuple(comb),H
    return None,None,H


def read_certificate():
    rows=[]
    with open(ROOT/'spectrum.csv', newline='', encoding='utf-8') as fh:
        for row in csv.DictReader(fh):
            n=int(row['n']); k=int(row['min_negative']); H=int(row['H'])
            w=tuple(int(x) for x in row['witness'].split('+')) if row['witness'] else tuple()
            rows.append((n,k,H,w,row['factorization']))
    return rows


def main():
    # Recheck the analytic finite bounds used before enumeration.
    assert Fraction(5,4)*Fraction(7,6)*Fraction(11,10) < 2
    assert Fraction(3,2)*Fraction(7,6)*Fraction(11,10) < 2
    assert Fraction(31,25)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13) < 2
    assert Fraction(13,9)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13) < 2
    assert Fraction(6,5)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13)*Fraction(18,17) < 2
    assert Fraction(4,3)*Fraction(8,7)*Fraction(12,11)*Fraction(14,13)*Fraction(18,17) < 2
    assert Fraction(4,3)*Fraction(6,5)*Fraction(12,11)*Fraction(14,13)*Fraction(18,17) < 2
    # Largest-prime bounds: q<=104 in support 4, q<=384 in support 5.
    assert Fraction(13,9)*Fraction(6,5)*Fraction(8,7) == Fraction(208,105)
    assert Fraction(4,3)*Fraction(6,5)*Fraction(8,7)*Fraction(12,11) == Fraction(768,385)

    ns=enumerate_boundary()
    assert len(ns)==121 and ns[0]==945 and ns[-1]==442365
    cert=read_certificate()
    assert [r[0] for r in cert]==ns
    hist={}
    extremals=[]
    for n,k,H,w,facstr in cert:
        f=factor(n)
        assert omega(f)==5 and n%2==1 and sigma_from_factor(f)>=2*n
        kk,ww,HH=min_negative(n)
        assert (kk,HH)==(k,H)
        assert sum(w)==H and len(w)==k and len(set(w))==k
        ds=set(all_divisors(f)); assert all(1<d<n and d in ds for d in w)
        # Exact minimality: no subset of fewer than k nontrivial proper divisors sums to H.
        small=[d for d in sorted(ds) if 1<d<n and d<=H]
        for j in range(1,k):
            assert all(sum(c)!=H for c in combinations(small,j))
        hist[k]=hist.get(k,0)+1
        if k==5: extremals.append(n)
    assert hist=={1:17,2:1,3:88,5:15}
    expected=[19635,26565,82005,84315,95865,116655,118965,151305,172095,181335,199815,206745,222915,262185,296835]
    assert extremals==expected
    print('VERIFY_OK boundary=121 spectrum=17,1,88,0,15 max_negative=5 extremals=15')

if __name__=='__main__': main()
