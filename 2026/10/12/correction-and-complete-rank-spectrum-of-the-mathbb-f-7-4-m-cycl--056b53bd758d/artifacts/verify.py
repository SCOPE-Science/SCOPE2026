#!/usr/bin/env python3
import itertools, json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
P=7

# Polynomial utilities over F_7, low coefficient first.
F=[6,0,6,0,1]  # X^4-X^2-1

def peval(f,x):
    z=0
    for a in reversed(f):
        z=(z*x+a)%P
    return z

assert all(peval(F,x)!=0 for x in range(P))

def divrem(f,g):
    r=f[:]
    while len(r)>=len(g):
        while r and r[-1]%P==0:
            r.pop()
        if len(r)<len(g): break
        d=len(r)-len(g)
        c=r[-1]*pow(g[-1],-1,P)%P
        for i,a in enumerate(g):
            r[i+d]=(r[i+d]-c*a)%P
    while r and r[-1]%P==0: r.pop()
    return r

for a in range(P):
    for b in range(P):
        assert divrem(F,[b,a,1]) != []

def add(x,y):
    return tuple((a+b)%P for a,b in zip(x,y))

def neg(x):
    return tuple((-a)%P for a in x)

def smul(c,x):
    return tuple(c*a%P for a in x)

def mul(x,y):
    t=[0]*7
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            t[i+j]=(t[i+j]+a*b)%P
    # X^4=X^2+1
    for d in range(6,3,-1):
        c=t[d]%P
        if c:
            t[d]=0
            t[d-2]=(t[d-2]+c)%P
            t[d-4]=(t[d-4]+c)%P
    return tuple(t[:4])

ZERO=(0,0,0,0)
ONE=(1,0,0,0)
OMEGA=(0,1,0,0)

def power(x,n):
    r=ONE
    while n:
        if n&1: r=mul(r,x)
        x=mul(x,x)
        n//=2
    return r

assert power(OMEGA,16)==(6,0,0,0)
assert power(OMEGA,32)==ONE
for d in (1,2,4,8,16):
    assert power(OMEGA,d)!=ONE

ALPHA=add(smul(4,mul(OMEGA,OMEGA)),(5,0,0,0))
assert mul(ALPHA,ALPHA)==(6,0,0,0)

def rank(rows):
    A=[list(r) for r in rows]
    rr=0
    if not A: return 0
    n=len(A[0])
    for c in range(n):
        piv=next((i for i in range(rr,len(A)) if A[i][c]%P),None)
        if piv is None: continue
        A[rr],A[piv]=A[piv],A[rr]
        iv=pow(A[rr][c],-1,P)
        A[rr]=[(iv*x)%P for x in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]%P:
                f=A[i][c]%P
                A[i]=[(A[i][j]-f*A[rr][j])%P for j in range(n)]
        rr+=1
        if rr==len(A): break
    return rr

def codeword(a,b):
    return [
        add(mul(a,ALPHA),b),
        add(neg(mul(a,add(ALPHA,ONE))),mul(b,ALPHA)),
        add(a,neg(mul(b,ALPHA))),
        b
    ]

ELS=list(itertools.product(range(P),repeat=4))
projective=Counter(rank(codeword(t,ONE)) for t in ELS)
projective[rank(codeword(ONE,ZERO))]+=1
assert dict(sorted(projective.items()))=={1:1,2:49,3:2352}
assert sum(projective.values())==2402

enumerator={0:1}
for w,n in projective.items():
    enumerator[w]=n*(P**4-1)
assert enumerator=={0:1,1:2400,2:117600,3:5644800}
assert sum(enumerator.values())==P**8

# Independent relation-incidence count for affine t.
directions=[(1,b) for b in range(P)]+[(0,1)]
inc=0
by_t=Counter()
for t in ELS:
    for A,B in directions:
        z=add(smul(A,mul(t,ALPHA)),smul(B,add(t,neg(ALPHA))))
        if z[1:]==(0,0,0):
            inc+=1
            by_t[t]+=1
assert inc==56
assert by_t[ALPHA]==8
assert sum(1 for t,n in by_t.items() if n==1)==48
assert all(n in (1,8) for n in by_t.values())

assert CERT["projective_rank_spectrum"]=={"1":1,"2":49,"3":2352}
assert CERT["rank_weight_enumerator"]=={"0":1,"1":2400,"2":117600,"3":5644800}
print("VERIFY_OK")
