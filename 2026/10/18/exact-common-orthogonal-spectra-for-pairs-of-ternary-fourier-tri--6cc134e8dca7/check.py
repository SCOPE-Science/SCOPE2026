"""Exact finite-field verification of common orthogonal Fourier spectra of ternary triples."""
from itertools import combinations,product
import random

def add(a,b):return tuple((x+y)%3 for x,y in zip(a,b))
def sub(a,b):return tuple((x-y)%3 for x,y in zip(a,b))
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3

def rank(vectors,d):
    A=[list(v) for v in vectors if any(v)]
    j=0
    for c in range(d):
        k=next((k for k in range(j,len(A)) if A[k][c]),None)
        if k is None:continue
        A[j],A[k]=A[k],A[j]
        q=A[j][c]
        A[j]=[(x*q)%3 if q==2 else x for x in A[j]]
        for i in range(len(A)):
            if i!=j and A[i][c]:
                q=A[i][c]
                A[i]=[(x-q*y)%3 for x,y in zip(A[i],A[j])]
        j+=1
        if j==len(A):break
    return j

def desc(A):
    a,b,c=A
    t=add(add(a,b),c)
    u=sub(b,a)
    return t,u

def predicted(A1,A2,d):
    t,u=desc(A1)
    v,w=desc(A2)
    r=rank((t,v),d)
    r1=rank((t,v,u),d)
    r2=rank((t,v,w),d)
    if r1==r or r2==r:return 0
    s=rank((t,v,u,w),d)-r
    assert s in (1,2)
    if s==1:return 3**(3*d-2*r-3)
    return 6*3**(3*d-2*r-6)

def is_spectrum(A,B):
    for x,y in combinations(B,2):
        h=sub(x,y)
        if sorted(dot(a,h) for a in A)!=[0,1,2]:
            # Orthogonality is the three residues, possibly uniformly translated
            vals={dot(a,h) for a in A}
            if len(vals)!=3:return False
    return True

def brute_common(A1,A2,Bs):
    return sum(is_spectrum(A1,B) and is_spectrum(A2,B) for B in Bs)

def main():
    for d in (1,2):
        G=list(product(range(3),repeat=d))
        triples=list(combinations(G,3))
        B_cache={A:{i for i,B in enumerate(triples) if is_spectrum(A,B)} for A in triples}
        checked=0
        counts={}
        for A in triples:
            for H in triples:
                z=len(B_cache[A]&B_cache[H])
                p=predicted(A,H,d)
                assert z==p,(d,A,H,z,p)
                checked+=1
                counts[p]=counts.get(p,0)+1
        print('exhaustive dimension',d,'triples',len(triples),'ordered pairs',checked,'multiplicity histogram',dict(sorted(counts.items())))
    rng=random.Random(314159)
    for d,samples in ((3,115),(4,17)):
        G=list(product(range(3),repeat=d))
        triples=list(combinations(G,3))
        for idx in range(samples):
            A=triples[rng.randrange(len(triples))]
            H=triples[rng.randrange(len(triples))]
            z=brute_common(A,H,triples)
            p=predicted(A,H,d)
            assert z==p,(d,A,H,z,p)
        print('independent dimension',d,'random ordered pairs',samples,'frequency triples per pair',len(triples),'all exact checks passed')
    # Explicit obstruction: a triangle and the line parallel to its nonzero sum
    A=((0,0),(1,0),(0,1))
    H=((0,0),(1,1),(2,2))
    B=list(combinations(list(product(range(3),repeat=2)),3))
    assert predicted(A,H,2)==brute_common(A,H,B)==0
    print('incompatible triangle-line witness dimension 2 passed')
if __name__=='__main__':main()
