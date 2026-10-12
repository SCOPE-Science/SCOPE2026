#!/usr/bin/env python3
import itertools, collections, math, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def qbinom(n,r,q=3):
    if r<0 or r>n:
        return 0
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def exact_axis_count(m,h,s):
    if s<0 or s>m:
        return 0
    total=0
    for j in range(m-s+1):
        total += ((-1)**j)*math.comb(m-s,j)*qbinom(m-s-j,h-s-j)
    return math.comb(m,s)*total

def rref_subspaces(n,d,q=3):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv)
              for c in range(p+1,n) if c not in P]
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*n for _ in range(d)]
            for i,p in enumerate(piv):
                B[i][p]=1
            for (i,c),v in zip(free,vals):
                B[i][c]=v
            yield B

def span(B,q=3):
    if not B:
        return {()}
    n=len(B[0])
    return {
        tuple(sum(coeff[i]*B[i][j] for i in range(len(B)))%q for j in range(n))
        for coeff in itertools.product(range(q),repeat=len(B))
    }

def defining_set(n):
    zero=(0,)*n
    return {
        x for x in itertools.product(range(3),repeat=n)
        if x!=zero and x[0] in (0,1)
    }

def formula_spectrum(n,r):
    h=n-r
    ctr=collections.Counter()
    base=2*3**(n-1)
    for s in range(h+1):
        a=exact_axis_count(n-1,h,s)
        if a:
            ctr[n+base-3**h-s]+=a
        if h>=1:
            b=exact_axis_count(n,h,s)-a
            if b:
                ctr[n+base-2*3**(h-1)-s]+=b
    return ctr

def direct_spectrum(n,r):
    h=n-r
    D=defining_set(n)
    std=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
    N=n+len(D)
    ctr=collections.Counter()
    for B in rref_subspaces(n,h):
        if h==0:
            W={(0,)*n}
        else:
            W=span(B)
        zeros=sum(x in W for x in D)+sum(e in W for e in std)
        ctr[N-zeros]+=1
    return ctr

for n in CERT["verified_n"]:
    D=defining_set(n)
    assert len(D)==2*3**(n-1)-1
    for r in range(1,n+1):
        got=direct_spectrum(n,r)
        expected=formula_spectrum(n,r)
        assert got==expected
        assert sum(got.values())==qbinom(n,r)
        assert min(got)==r+2*3**(n-1)-3**(n-r)
        assert got[min(got)]==math.comb(n-1,r-1)

n3=formula_spectrum(3,1)
codeword_dist={0:1}
for w,count in n3.items():
    codeword_dist[w]=2*count
assert codeword_dist=={0:1,10:2,13:4,14:12,15:8}
assert {str(w):c for w,c in sorted(n3.items())}==CERT["example_n3"]["subcode_support_spectra"]["1"]
assert {str(w):c for w,c in sorted(formula_spectrum(3,2).items())}==CERT["example_n3"]["subcode_support_spectra"]["2"]
assert {str(w):c for w,c in sorted(formula_spectrum(3,3).items())}==CERT["example_n3"]["subcode_support_spectra"]["3"]

print("VERIFY_OK")
