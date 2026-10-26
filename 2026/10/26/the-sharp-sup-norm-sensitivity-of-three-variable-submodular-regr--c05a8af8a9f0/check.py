"""Exact arithmetic verification for the three-variable submodular cone projector.

No third-party dependencies; run with Python 3.8 or newer.
The global result also uses the polyhedral active-face argument supplied in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations

N=8
PAIRS=list(combinations(range(3),2))
A=[]
for i,j in PAIRS:
    for base in range(N):
        if base & ((1<<i)|(1<<j)):
            continue
        row=[F(0) for _ in range(N)]
        row[base|(1<<i)]+=1
        row[base|(1<<j)]+=1
        row[base]-=1
        row[base|(1<<i)|(1<<j)]-=1
        A.append(row)
assert len(A)==6

def independent(rows):
    pivots=[]; basis=[]
    for row in rows:
        v=row[:]
        for p,b in zip(pivots,basis):
            f=v[p]
            if f:
                v=[x-f*y for x,y in zip(v,b)]
        p=next((j for j,z in enumerate(v) if z),None)
        if p is not None:
            z=v[p]
            v=[x/z for x in v]
            at=sum(k<p for k in pivots)
            pivots.insert(at,p)
            basis.insert(at,v)
    return len(basis)

def inv(M):
    n=len(M)
    X=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for i in range(n):
        p=next(k for k in range(i,n) if X[k][i])
        X[i],X[p]=X[p],X[i]
        v=X[i][i];X[i]=[x/v for x in X[i]]
        for k in range(n):
            if k==i:continue
            t=X[k][i]
            if t:X[k]=[x-t*y for x,y in zip(X[k],X[i])]
    return [row[n:] for row in X]

def orthogonal_projection(mask):
    rows=[]
    for i,a in enumerate(A):
        if mask>>i&1 and independent(rows+[a])>len(rows):rows.append(a)
    P=[[F(i==j) for j in range(N)] for i in range(N)]
    m=len(rows)
    if m:
        G=[[sum(rows[i][k]*rows[j][k] for k in range(N)) for j in range(m)] for i in range(m)]
        Gi=inv(G)
        for i in range(N):
            for j in range(N):
                P[i][j]-=sum(rows[k][i]*Gi[k][l]*rows[l][j] for k in range(m) for l in range(m))
    for i in range(N):
        for j in range(N):
            assert P[i][j]==P[j][i]
            assert sum(P[i][k]*P[k][j] for k in range(N))==P[i][j]
    return P

def admissible(mask):
    if mask==0:return True
    pairs=[(bool(mask>>(2*j)&1),bool(mask>>(2*j+1)&1)) for j in range(3)]
    if any(a and b for a,b in pairs):
        return all(a==b for a,b in pairs)
    return all(not b for a,b in pairs) or all(not a for a,b in pairs)

def witness_slacks(mask):
    pairs=[(bool(mask>>(2*j)&1),bool(mask>>(2*j+1)&1)) for j in range(3)]
    if any(a and b for a,b in pairs):
        return [F(0 if z else 1) for a,b in pairs for z in (a,b)]
    if any(a for a,b in pairs):
        return [F(0 if a else 1) if pos==0 else F(2 if not a else 1) for a,b in pairs for pos in (0,1)]
    if any(b for a,b in pairs):
        return [F(2 if not b else 1) if pos==0 else F(0 if b else 1) for a,b in pairs for pos in (0,1)]
    return [F(1)]*6

assert independent(A)==4
for i in range(2):
    assert all(A[0][j]-A[1][j]==A[2*i+2][j]-A[2*i+3][j] for j in range(N))
class_norm={}
face_count=0
for mask in range(64):
    if not admissible(mask):continue
    face_count+=1
    s=witness_slacks(mask)
    assert all((s[i]==0)==bool(mask>>i&1) for i in range(6))
    assert s[0]-s[1]==s[2]-s[3]==s[4]-s[5]
    P=orthogonal_projection(mask)
    norm=max(sum(abs(x) for x in row) for row in P)
    class_norm[mask]=norm
assert face_count==22
assert set(class_norm.values())=={F(1),F(3,2),F(5,3),F(7,4)}
assert max(class_norm.values())==F(7,4)
assert {m for m,n in class_norm.items() if n==F(7,4)}=={15,21,42,51,60}
# The explicit lower-bound face is realized by the set function supported at the full set.
f=[F(-1 if s==7 else 0) for s in range(8)]
slack=[sum(a[k]*f[k] for k in range(N)) for a in A]
assert slack==[0,1,0,1,0,1]
P=orthogonal_projection(21)
row=P[0]
assert sum(abs(x) for x in row)==F(7,4)
sgn=[1 if v>=0 else -1 for v in row]
assert sum(x*y for x,y in zip(row,sgn))==F(7,4)
# For two coordinates there is one four-sparse inequality and sharp modulus 3/2.
a=[F(-1),F(1),F(1),F(-1)]
Q=[[F(i==j)-a[i]*a[j]/4 for j in range(4)] for i in range(4)]
assert max(sum(abs(x) for x in row) for row in Q)==F(3,2)
print('PASS: 22 of 64 face patterns; exact Gram inversions and orthogonal projections;')
print('PASS: five sharp faces, norm 7/4, explicit lower-bound active face;')
print('PASS: two-variable baseline norm 3/2.')
