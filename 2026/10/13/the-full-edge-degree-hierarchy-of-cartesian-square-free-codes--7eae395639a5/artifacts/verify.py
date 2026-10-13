#!/usr/bin/env python3
import itertools, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text())

def shadow(sizes, omitted):
    # degree m-1 monomial omitting coordinate `omitted`
    out=set()
    for beta in itertools.product(*[range(n) for n in sizes]):
        if all(beta[j]>=1 for j in range(len(sizes)) if j!=omitted):
            out.add(beta)
    return out

def check_sizes(sizes):
    m=len(sizes)
    P=1
    for n in sizes:P*=n-1
    Ps=[]
    for i in range(m):
        z=1
        for j,n in enumerate(sizes):
            if j!=i:z*=n-1
        Ps.append(z)
    S=[shadow(sizes,i) for i in range(m)]
    mins=[]
    for r in range(1,m+1):
        vals=[]
        for I in itertools.combinations(range(m),r):
            U=set().union(*(S[i] for i in I))
            expected=P+sum(Ps[i] for i in I)
            assert len(U)==expected
            vals.append((len(U),I))
        got=min(x for x,I in vals)
        target=P+sum(Ps[i] for i in range(m-r,m))
        assert got==target
        mins.append(got)
    return mins

assert check_sizes([2,3,4,5]) == [30,38,50,74]
check_sizes([3,3,3,3])
assert check_sizes([2,3,3])==[6,8,12]

# Direct evaluation over F3 for X={0,1} x F3 x F3.
q=3
X=list(itertools.product([0,1],range(3),range(3)))
# M0=x1*x2 (omits x0), M1=x0*x2, M2=x0*x1.
G=[]
for omit in range(3):
    row=[]
    for x in X:
        v=1
        for j in range(3):
            if j!=omit:v=(v*x[j])%q
        row.append(v)
    G.append(tuple(row))

def rref(rows):
    A=[list(r) for r in rows if any(r)]
    rr=0
    for c in range(3):
        p=next((i for i in range(rr,len(A)) if A[i][c]%q),None)
        if p is None: continue
        A[rr],A[p]=A[p],A[rr]
        iv=pow(A[rr][c],-1,q)
        A[rr]=[(iv*z)%q for z in A[rr]]
        for i in range(len(A)):
            if i!=rr and A[i][c]%q:
                z=A[i][c]%q
                A[i]=[(A[i][j]-z*A[rr][j])%q for j in range(3)]
        rr+=1
        if rr==len(A):break
    A=[tuple(r) for r in A if any(r)]
    return tuple(A)

vectors=[v for v in itertools.product(range(q),repeat=3) if any(v)]
subspaces={0:{()}}
# Generate all spans from all tuples of basis candidates; dimension at most 3, tiny space.
allspaces=set([()])
for r in range(1,4):
    for comb in itertools.combinations(vectors,r):
        R=rref(comb)
        if len(R)==r: allspaces.add(R)

mins={1:10**9,2:10**9,3:10**9}
for B in allspaces:
    r=len(B)
    if r==0: continue
    supp=set()
    for msg in B:
        c=[]
        for col in range(len(X)):
            c.append(sum(msg[i]*G[i][col] for i in range(3))%q)
        supp.update(i for i,z in enumerate(c) if z)
    # Support of a basis equals support of its span.
    mins[r]=min(mins[r],len(supp))
assert [mins[i] for i in (1,2,3)]==CERT['direct_check']['ghw']==[6,8,12]
print('VERIFY_OK')
