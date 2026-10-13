#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# F16 = F2[beta]/(beta^4+beta+1), beta encoded as 2.
MOD16=0b10011
def m16(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a&16:a^=MOD16
    return r&15
def p16(a,n):
    r=1
    while n:
        if n&1:r=m16(r,a)
        a=m16(a,a);n//=2
    return r

beta=2
x=1
order=0
while True:
    order+=1
    x=m16(x,beta)
    if x==1:break
assert order==15

omega=p16(beta,5)
omega2=m16(omega,omega)
assert omega2^omega^1==0
F4set={0,1,omega,omega2}
to4={0:0,1:1,omega:2,omega2:3}

# Abstract F4 = F2[w]/(w^2+w+1).
def m4(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1
        a<<=1
        if a&4:a^=0b111
    return r&3
INV4={1:1,2:3,3:2}

def rank4(M):
    if not M:return 0
    A=[r[:] for r in M]
    m=len(A);n=len(A[0]);rr=0
    for c in range(n):
        p=next((i for i in range(rr,m) if A[i][c]),None)
        if p is None:continue
        A[rr],A[p]=A[p],A[rr]
        iv=INV4[A[rr][c]]
        A[rr]=[m4(iv,z) for z in A[rr]]
        for i in range(m):
            if i!=rr and A[i][c]:
                f=A[i][c]
                A[i]=[A[i][j]^m4(f,A[rr][j]) for j in range(n)]
        rr+=1
        if rr==m:break
    return rr

R=CERT["defining_zero_set"]
poly=[1]
for e in R:
    a=p16(beta,e)
    new=[0]*(len(poly)+1)
    for j,c in enumerate(poly):
        new[j]^=m16(c,a)
        new[j+1]^=c
    poly=new
assert all(c in F4set for c in poly)
g=[to4[c] for c in poly]
assert g==[2,3,1,0,2,3,3,1,0,2,1]

# Polynomial division over F4: x^15+1 by monic g.
f=[1]+[0]*14+[1]
rem=f[:]
for d in range(15,9,-1):
    c=rem[d]
    if c:
        shift=d-10
        for j,a in enumerate(g):
            rem[j+shift]^=m4(c,a)
assert all(z==0 for z in rem[:10])

rows=[]
for s in range(5):
    row=[0]*15
    for j,c in enumerate(g):
        row[j+s]=c
    rows.append(row)
assert rank4(rows)==5

def dot(a,b):
    z=0
    for x,y in zip(a,b):
        z^=m4(x,y)
    return z
assert all(dot(a,b)==0 for a in rows for b in rows)

def word(coeff):
    out=[0]*15
    for a,row in zip(coeff,rows):
        if a:
            out=[x^m4(a,y) for x,y in zip(out,row)]
    return out

words={}
wd=collections.Counter()
for coeff in itertools.product(range(4),repeat=5):
    w=word(coeff)
    words[tuple(coeff)]=w
    wd[sum(x!=0 for x in w)]+=1
assert dict(sorted(wd.items()))=={int(k):v for k,v in CERT["ordinary_weight_distribution"].items()}

def qbinom(n,r,q=4):
    a=b=1
    for i in range(r):
        a*=q**(n-i)-1
        b*=q**(r-i)-1
    return a//b

def subspaces_rref(n,d,q=4):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv) for c in range(p+1,n) if c not in P]
        for vals in itertools.product(range(q),repeat=len(free)):
            B=[[0]*n for _ in range(d)]
            for i,p in enumerate(piv):B[i][p]=1
            for (i,c),v in zip(free,vals):B[i][c]=v
            yield B

expected={int(r):{int(w):n for w,n in sp.items()} for r,sp in CERT["support_spectra"].items()}
gh=[];mins=[];total=0
for r in range(1,6):
    ctr=collections.Counter()
    count=0
    for B in subspaces_rref(5,r):
        supp=[False]*15
        for coeff in B:
            w=words[tuple(coeff)]
            for j,z in enumerate(w):
                if z:supp[j]=True
        ctr[sum(supp)]+=1
        count+=1
    assert count==qbinom(5,r,4)
    assert count==CERT["subspace_counts"][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr))
    mins.append(ctr[min(ctr)])
    total+=count

assert total==CERT["subspaces_checked"]==12277
assert gh==CERT["generalized_hamming_weights"]
assert mins==CERT["minimum_subcode_counts"]

for r in range(1,6):
    B=[[int(x) for x in row] for row in CERT["minimizer_witness_bases"][str(r)]]
    assert rank4(B)==r
    supp=[False]*15
    for coeff in B:
        w=words[tuple(coeff)]
        for j,z in enumerate(w):
            if z:supp[j]=True
    assert sum(supp)==gh[r-1]

print("VERIFY_OK")
