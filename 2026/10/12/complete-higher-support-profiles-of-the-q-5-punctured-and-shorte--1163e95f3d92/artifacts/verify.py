#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
p=5;c1=1;c0=2

def add(x,y): return ((x%p+y%p)%p)+p*((x//p+y//p)%p)
def mul(x,y):
    a,b=x%p,x//p; c,d=y%p,y//p
    return ((a*c-b*d*c0)%p)+p*((a*d+b*c-b*d*c1)%p)
def power(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
alpha=p
z=1;order=0
while True:
    z=mul(z,alpha);order+=1
    if z==1:break
assert order==24

def trace(x):
    t=add(x,power(x,5)); assert t//p==0; return t%p
coords=[]
for i in range(24):
    g=power(alpha,i); coords.append((power(g,20),power(g,13)))

def field_lin(c0,c1): return add(c0,mul(c1,alpha))
def evalmsg(v):
    a=field_lin(v[0],v[1]); b=field_lin(v[2],v[3])
    return [trace(add(mul(a,x),mul(b,y))) for x,y in coords]
G=[evalmsg([1 if i==j else 0 for i in range(4)]) for j in range(4)]

def rank(M,q=5):
    if not M:return 0
    A=[list(r) for r in M];m=len(A);n=len(A[0]);r=0
    for c in range(n):
        s=next((i for i in range(r,m) if A[i][c]%q),None)
        if s is None:continue
        A[r],A[s]=A[s],A[r];inv=pow(A[r][c],-1,q);A[r]=[(inv*x)%q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%q:
                f=A[i][c]%q;A[i]=[(A[i][j]-f*A[r][j])%q for j in range(n)]
        r+=1
        if r==m:break
    return r
assert rank(G)==4

def word(v,M): return [sum(v[i]*M[i][j] for i in range(len(M)))%5 for j in range(len(M[0]))]
def wd(M):
    k=len(M);ctr=collections.Counter()
    for v in itertools.product(range(5),repeat=k): ctr[sum(x!=0 for x in word(v,M))]+=1
    return dict(sorted(ctr.items()))
assert wd(G)=={0:1,16:108,19:288,20:24,21:192,24:12}
Gp=[r[1:] for r in G]
assert rank(Gp)==4
assert wd(Gp)=={0:1,15:72,16:36,18:228,19:80,20:172,21:24,23:12}
col0=[G[i][0] for i in range(4)]
ker=[v for v in itertools.product(range(5),repeat=4) if sum(v[i]*col0[i] for i in range(4))%5==0]
B=[]
for v in ker:
    if v!=(0,0,0,0) and rank(B+[v])>len(B):
        B.append(v)
        if len(B)==3:break
Gs=[]
for v in B:
    w=word(v,G);assert w[0]==0;Gs.append(w[1:])
assert rank(Gs)==3
assert wd(Gs)=={0:1,16:36,19:60,20:4,21:24}

def qbinom(n,r,q=5):
    a=b=1
    for i in range(r):a*=q**(n-i)-1;b*=q**(r-i)-1
    return a//b

def subspaces(n,d,q=5):
    for piv in itertools.combinations(range(n),d):
        P=set(piv);free=[]
        for i,pc in enumerate(piv):
            for c in range(pc+1,n):
                if c not in P:free.append((i,c))
        for vals in itertools.product(range(q),repeat=len(free)):
            R=[[0]*n for _ in range(d)]
            for i,pc in enumerate(piv):R[i][pc]=1
            for (i,c),x in zip(free,vals):R[i][c]=x
            yield R

def spectra(M,expected):
    k=len(M);gh=[];mins=[]
    for d in range(1,k+1):
        ctr=collections.Counter();cnt=0
        for R in subspaces(k,d):
            S=set()
            for v in R:
                w=word(v,M);S.update(j for j,x in enumerate(w) if x)
            ctr[len(S)]+=1;cnt+=1
        assert cnt==qbinom(k,d)
        want={int(w):c for w,c in expected[str(d)].items()}
        assert dict(sorted(ctr.items()))==want
        gh.append(min(ctr));mins.append(ctr[min(ctr)])
    return gh,mins
pg,pm=spectra(Gp,CERT['punctured']['support_spectra'])
sg,sm=spectra(Gs,CERT['shortened']['support_spectra'])
assert pg==CERT['punctured']['generalized_hamming_weights']
assert pm==CERT['punctured']['minimum_subcode_counts']
assert sg==CERT['shortened']['generalized_hamming_weights']
assert sm==CERT['shortened']['minimum_subcode_counts']
print('VERIFY_OK')
