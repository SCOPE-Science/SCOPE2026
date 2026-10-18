#!/usr/bin/env python3
"""Independent GF(2) spanning-set/group-action check of flag refinements."""
from itertools import product
from collections import Counter
from math import prod

def subspaces(n):
    seen={1}
    frontier=[1]
    while frontier:
        A=frontier.pop()
        points=[v for v in range(2**n) if A>>v&1]
        for v in range(1,2**n):
            if (A>>v)&1: continue
            B=A
            for x in points: B|=1<<(x^v)
            if B not in seen:seen.add(B);frontier.append(B)
    return sorted(seen)

def dim(A):return (A.bit_count()).bit_length()-1

def gaussian(n,k,q):
    a=b=1
    for i in range(k):a*=q**(n-i)-1;b*=q**(k-i)-1
    return a//b

def gl(n):
    out=[]
    for cols in product(range(1,2**n),repeat=n):
        span={0}; ok=True
        for col in cols:
            if col in span:ok=False;break
            span|={x^col for x in list(span)}
        if not ok:continue
        maps=[]
        for v in range(2**n):
            z=0
            for k,c in enumerate(cols):
                if v>>k&1:z^=c
            maps.append(z)
        out.append(tuple(maps))
    return out

def map_subspace(A,m):
    B=0
    while A:
        bit=A&-A
        v=bit.bit_length()-1
        B|=1<<m[v]
        A-=bit
    return B

def pred_size(ds,aa,q):
    e=sum(aa[j]*sum(ds[i]-aa[i] for i in range(j)) for j in range(len(ds)))
    return q**e*prod(gaussian(d,a,q) for d,a in zip(ds,aa))

def run(n,cuts):
    S=subspaces(n);idx={A:i for i,A in enumerate(S)}
    flag=[]
    for d in cuts:
        vecs=[v for v in range(2**n) if v < (1<<d)]
        A=sum(1<<v for v in vecs)
        flag.append(A)
    dims=(0,)+cuts+(n,)
    ds=tuple(dims[i+1]-dims[i] for i in range(len(dims)-1))
    full=(1<<(2**n))-1
    chain=[1]+flag+[full]
    sig={A:tuple(dim(A&chain[i+1])-dim(A&chain[i]) for i in range(len(ds))) for A in S}
    classes={a:{A for A in S if sig[A]==a} for a in product(*(range(d+1) for d in ds))}
    assert all(len(U)==pred_size(ds,a,2) for a,U in classes.items())
    # Different exhaustive generator from the row-echelon version.
    GL=gl(n)
    stabilizer=[mat for mat in GL if all(map_subspace(U,mat)==U for U in flag)]
    assert stabilizer
    for a,elems in classes.items():
        representative=next(iter(elems))
        orbit={map_subspace(representative,m) for m in stabilizer}
        assert orbit==elems,(n,cuts,a,len(orbit),len(elems))
    # Two rounds of directed refinement; old color is included in key.
    col={A:(flag.index(A)+1 if A in flag else 0) for A in S}
    for t in range(2):
        keys={A:(col[A],tuple(sorted(Counter(col[B] for B in S if B!=A and B&A==B).items())),tuple(sorted(Counter(col[B] for B in S if B!=A and B&A==A).items()))) for A in S}
        canonical={v:i for i,v in enumerate(sorted(set(keys.values())))}
        col={A:canonical[keys[A]] for A in S}
    for A in S:
        for B in S:
            assert (col[A]==col[B])==(sig[A]==sig[B]),(n,cuts,A,B)
    return len(S),len(GL),len(stabilizer),len(classes)

if __name__=='__main__':
    for n,cuts in [(2,(1,)),(3,(1,)),(3,(1,2)),(4,(2,)),(4,(1,3)),(4,(1,2,3))]:
        print('PASS',n,cuts,run(n,cuts),flush=True)
