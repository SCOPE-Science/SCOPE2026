#!/usr/bin/env python3
"""Exact symbolic cut-inclusion and small-field checks for rank-one projector generation."""
from itertools import combinations, product


def add(a,b):
    out=[0]*max(len(a),len(b))
    for j,x in enumerate(a):out[j]+=x
    for j,x in enumerate(b):out[j]+=x
    return out


def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out


def scale(a,s):return [s*x for x in a]


def shift(a,k):return [0]*k + a


def evalp(a,q):return sum(c*q**i for i,c in enumerate(a))

I={1:[1],2:[1,-1,1],3:[0,1,-2,3,-1,-1,1]}
subsets=[frozenset(t) for k in (1,2) for t in combinations(range(3),k)]
contributions={i:[0] for i in range(1,7)}

for mask in range(1,64):
    cuts=[subsets[j] for j in range(6) if (mask>>j)&1]
    profiles=[tuple(int(i in s) for s in cuts) for i in range(3)]
    blocks={}
    for i,x in enumerate(profiles):blocks.setdefault(x,[]).append(i)
    free=0
    for i in range(3):
        for j in range(3):
            if profiles[i]!=profiles[j] and all(not (i in s) or j in s for s in cuts):free+=1
    term=shift([1],free)
    for block in blocks.values():term=mul(term,I[len(block)])
    if len(cuts)%2==0:term=scale(term,-1)
    contributions[len(cuts)]=add(contributions[len(cuts)],term)

want_by_size={
    1:[0,0,6,-6,6],
    2:[-3,3,-9,-6],
    3:[2,12,6],
    4:[-9,-6],
    5:[6],
    6:[-1],
}
for k,expected in want_by_size.items():
    actual=contributions[k]
    assert actual+[0]*max(0,len(expected)-len(actual)) == expected+[0]*max(0,len(actual)-len(expected)),(k,actual,expected)
reducible=[0]
for k in range(1,7):reducible=add(reducible,contributions[k])
assert reducible==[-5,9,3,-12,6]
strong=add(I[3],scale(reducible,-1))
assert strong==[5,-8,-5,15,-7,-1,1],strong
assert strong==mul([1,-2,1],[5,2,-6,1,1])


def ff_add(a,b,q):return (a^b) if q==4 else (a+b)%q

def ff_mul(a,b,q):
    if q!=4:return (a*b)%q
    v=0
    while b:
        if b&1:v^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return v


def matrix_rank(rows,q):
    A=[list(r) for r in rows]
    n=len(A);m=len(A[0]);p=0
    for j in range(m):
        lead=next((i for i in range(p,n) if A[i][j]),None)
        if lead is None:continue
        A[p],A[lead]=A[lead],A[p]
        for i in range(p+1,n):
            if not A[i][j]:continue
            # x/y multiplication without division by trying inverse in the finite field
            x=A[i][j];y=A[p][j]
            inv=next(a for a in range(1,q) if ff_mul(a,y,q)==1)
            factor=ff_mul(x,inv,q)
            for k in range(j,m):
                neg=ff_mul(factor,A[p][k],q)
                A[i][k]=ff_add(A[i][k],neg,q) if q==4 else (A[i][k]-neg)%q
        p+=1
        if p==n:break
    return p


def strongly_connected(C):
    n=len(C)
    for i in range(n):
        seen={i}
        for _ in range(n):
            seen|={j for k in tuple(seen) for j in range(n) if C[k][j]}
        if len(seen)!=n:return False
    return True

for q in (2,3,4,5,7):
    total=0;strong_count=0
    for z in product(range(q),repeat=6):
        C=[[1,z[0],z[1]],[z[2],1,z[3]],[z[4],z[5],1]]
        inv=(matrix_rank(C,q)==3)
        total+=inv
        strong_count+=inv and strongly_connected(C)
    assert total==evalp(I[3],q),(q,total,evalp(I[3],q))
    assert strong_count==evalp(strong,q),(q,strong_count,evalp(strong,q))
    print('M3:',q,'all invertible',total,'strong invertible',strong_count)

for q in (2,3,4,5):
    count=0
    for a,b in product(range(q),repeat=2):
        C=[[1,a],[b,1]]
        count+=matrix_rank(C,q)==2 and strongly_connected(C)
    assert count==(q-1)*(q-2)

# A second algebraic check for every normalized binary 3-by-3 matrix:
# multiply actual rank-one idempotents, rather than checking graph connectivity.
def bitsmul(a,b,n=3):
    out=0
    for i in range(n):
        for j in range(n):
            v=0
            for k in range(n):v^=((a>>(i*n+k))&1)&((b>>(k*n+j))&1)
            out|=v<<(i*n+j)
    return out


def dimension(vals):
    basis={}
    for x in vals:
        while x:
            p=x.bit_length()-1
            if p in basis:x^=basis[p]
            else:
                basis[p]=x
                break
    return len(basis)

Ibits=sum(1<<(4*i) for i in range(3))
for z in product(range(2),repeat=6):
    C=[[1,z[0],z[1]],[z[2],1,z[3]],[z[4],z[5],1]]
    P=[sum(C[i][j]<<(i*3+j) for j in range(3)) for i in range(3)]
    seen=set([Ibits]+P);changed=True
    while changed:
        old=len(seen)
        vals=list(seen)
        seen.update(bitsmul(a,b) for a in vals for b in vals)
        changed=len(seen)!=old
    generated=(dimension(seen)==9)
    criterion=matrix_rank(C,2)==3 and strongly_connected(C)
    assert generated==criterion,(C,generated,criterion)

# A separate full tuple census over all 28 rank-one idempotents in M3(F2),
# without requiring a normalized factor matrix or invertibility of image vectors.
projectors=set()
for u in range(1,8):
    for v in range(1,8):
        trace=sum(((u>>i)&1)*((v>>i)&1) for i in range(3))%2
        if trace:
            M=sum((((u>>i)&1)*((v>>j)&1))<<(i*3+j) for i in range(3) for j in range(3))
            projectors.add(M)
assert len(projectors)==28

def spans_full(a,b,c):
    gens=(a,b,c)
    vectors=[Ibits]
    for g in gens:
        if dimension(vectors+[g])>len(vectors):vectors.append(g)
    k=0
    while k<len(vectors):
        x=vectors[k]
        for g in gens:
            y=bitsmul(g,x)
            if dimension(vectors+[y])>len(vectors):vectors.append(y)
        if len(vectors)==9:return True
        k+=1
    return False
full_count=sum(spans_full(a,b,c) for a,b,c in product(projectors,repeat=3))
assert full_count==1512,full_count
print('binary M3 projector tuples',len(projectors)**3,'generators',full_count)
print('VERIFY_OK')
