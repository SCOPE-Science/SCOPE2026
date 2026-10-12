#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

def dec(a): return [a%3,(a//3)%3,(a//9)%3]
def enc(v): return v[0]+3*v[1]+9*v[2]
def add(a,b):
    A=dec(a); B=dec(b)
    return enc([(A[i]+B[i])%3 for i in range(3)])
def mul(a,b):
    A=dec(a); B=dec(b)
    c=[0]*5
    for i,x in enumerate(A):
        for j,y in enumerate(B):
            c[i+j]=(c[i+j]+x*y)%3
    for d in range(4,2,-1):
        t=c[d]%3
        if t:
            c[d]=0
            c[d-3]=(c[d-3]+2*t)%3
            c[d-2]=(c[d-2]+t)%3
    return enc(c[:3])
def power(a,n):
    r=1
    while n:
        if n&1: r=mul(r,a)
        a=mul(a,a); n//=2
    return r
def trace(a):
    s=add(a,add(power(a,3),power(a,9)))
    v=dec(s)
    assert v[1:]==[0,0]
    return v[0]

for x in range(3):
    assert (x**3+2*x+1)%3 != 0

D=[x for x in range(27) if x not in {0,1,2}]
assert len(D)==24
rows=[]
for a in (1,3,9):
    rows.append([trace(mul(a,x)) for x in D])
rows.append([1]*24)

def rank3(M):
    A=[r[:] for r in M]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]%3),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        if A[r][c]%3==2:
            A[r]=[(2*x)%3 for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%3:
                f=A[i][c]%3
                A[i]=[(A[i][j]-f*A[r][j])%3 for j in range(n)]
        r+=1
        if r==m: break
    return r
assert rank3(rows)==4

def word(coeff):
    return tuple(sum(coeff[i]*rows[i][j] for i in range(4))%3 for j in range(24))

wd=collections.Counter()
for c in itertools.product(range(3),repeat=4):
    w=word(c)
    wd[sum(x!=0 for x in w)]+=1
assert dict(sorted(wd.items()))=={0:1,15:16,16:54,18:8,24:2}

def qbinom(n,r,q):
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def subspaces_rref(n,d,q):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[]
        # RREF: nonpivot entries in row i may occur only to the right of its pivot,
        # excluding all pivot columns.
        for i,p in enumerate(piv):
            for c in range(p+1,n):
                if c not in P:
                    free.append((i,c))
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*n for _ in range(d)]
            for i,p in enumerate(piv): B[i][p]=1
            for (i,c),v in zip(free,vals): B[i][c]=v
            yield B

expected={int(r):{int(w):n for w,n in sp.items()} for r,sp in CERT["support_spectra"].items()}
gh=[]; mins=[]; total=0
for r in range(1,5):
    ctr=collections.Counter(); count=0
    for B in subspaces_rref(4,r,3):
        count+=1
        support=set()
        for coeff in B:
            w=word(coeff)
            support.update(j for j,x in enumerate(w) if x)
        ctr[len(support)]+=1
    assert count==qbinom(4,r,3)
    assert count==CERT["subspace_counts"][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr)); mins.append(ctr[min(ctr)]); total+=count

assert total==CERT["subspaces_checked"]==211
assert gh==CERT["source_generalized_hamming_weights"]
assert mins==CERT["minimum_subcode_counts"]
print("VERIFY_OK")
