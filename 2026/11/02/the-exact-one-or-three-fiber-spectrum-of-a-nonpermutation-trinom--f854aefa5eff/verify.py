#!/usr/bin/env python3
"""Independent finite-field enumeration for the stated trinomial fibers."""
from collections import Counter, defaultdict

def mul(x,y,p):
    a,b=x; c,d=y
    return ((a*c-b*d)%p,(a*d+b*c)%p)

def power(x,n,p):
    z=(1,0)
    while n:
        if n&1: z=mul(z,x,p)
        x=mul(x,x,p)
        n>>=1
    return z

def F(x,p,t):
    z=power(x,p,p)
    z2=power(x,2*p-1,p)
    return ((z2[0]+t*z[0]-x[0])%p,(z2[1]+t*z[1]-x[1])%p)

cases=0
states=0
for p in (11,19,43,59):
    assert p%8==3 and p%3!=0
    ts=[t for t in range(p) if (t*t+2)%p==0]
    assert len(ts)==2
    chi3=1 if pow(3,(p-1)//2,p)==1 else -1
    S=1+(p-1)*(1-chi3)
    predicted={0:2*(p*p-S)//3, 1:S, 3:(p*p-S)//3}
    for t in ts:
        fibers=defaultdict(int)
        for a in range(p):
            for b in range(p):
                fibers[F((a,b),p,t)]+=1
        assert sum(fibers.values())==p*p
        assert fibers[(0,0)]==1
        freq=Counter(fibers.values())
        freq[0]=p*p-len(fibers)
        assert {k:freq[k] for k in (0,1,3)}==predicted,(p,t,freq,predicted)
        assert all(k in (0,1,3) for k in freq)
        special=[]
        for y,cnt in fibers.items():
            if y==(0,0) or cnt!=1: continue
            label=power(y,p-1,p)
            # s=label + label^{-1}; inverse on the norm-one torus is conjugation.
            assert (2*label[0]+5*t)%p==0
            special.append(label)
        assert len(special)==S-1
        if special: assert len(set(special))==2
        cases+=1; states+=p*p
        print(f'p={p} t={t} delta={chi3} fibers={dict(sorted(predicted.items()))}')
print(f'VERIFY_OK cases={cases} states={states}')
