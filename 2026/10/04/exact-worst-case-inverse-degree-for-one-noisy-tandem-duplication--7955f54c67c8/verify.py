#!/usr/bin/env python3
from itertools import product


def inv_parents(y,k):
    y=tuple(y)
    n=len(y)-k
    out=set()
    for i in range(n-k+1):
        a=y[i:i+k]
        b=y[i+k:i+2*k]
        if sum(x!=z for x,z in zip(a,b))==1:
            out.add(y[:i+k]+y[i+2*k:])
    return out


def mismatch(y,k):
    return tuple(int(y[t]!=y[t+k]) for t in range(len(y)-k))


def formula(n,k):
    m=n-k+1
    return 2*(m//(k+1))+min(2,m%(k+1))


def witness(n,k):
    m=n-k+1
    z=[]
    B=[1]+[0]*(k-1)+[1]
    while len(z)<n:
        z.extend(B)
    z=z[:n]
    y=[0]*k
    for t,b in enumerate(z):
        y.append(y[t] ^ b)
    return tuple(y),tuple(z)


def legal_starts(y,k):
    z=mismatch(y,k)
    n=len(y)-k
    return [i for i in range(n-k+1) if sum(z[i:i+k])==1]


def collision_criterion(y,k):
    y=tuple(y)
    z=mismatch(y,k)
    starts=legal_starts(y,k)
    parents={i:y[:i+k]+y[i+2*k:] for i in starts}
    for aa,i in enumerate(starts):
        for j in starts[aa+1:]:
            lhs=(parents[i]==parents[j])
            rhs=all(z[t]==0 for t in range(i+k,j+k))
            if lhs!=rhs:
                raise AssertionError((y,k,i,j,z,lhs,rhs))


def exhaustive(q,k,n):
    L=n+k
    best=-1
    for y in product(range(q), repeat=L):
        collision_criterion(y,k)
        best=max(best,len(inv_parents(y,k)))
    assert best==formula(n,k),(q,k,n,best,formula(n,k))
    return q**L

cases=0
words=0
for q,k,nmax in [(2,1,7),(2,2,7),(2,3,7),(3,1,5),(3,2,5)]:
    for n in range(k,nmax+1):
        if q**(n+k)>800000:
            continue
        words += exhaustive(q,k,n)
        cases += 1

witness_cases=0
for k in range(1,13):
    for n in range(k,101):
        y,z=witness(n,k)
        assert mismatch(y,k)==z
        assert len(inv_parents(y,k))==formula(n,k),(n,k,len(inv_parents(y,k)),formula(n,k))
        witness_cases+=1

print(f"VERIFY_OK exhaustive_cases={cases} received_words={words} witness_cases={witness_cases} k<=12_n<=100")
