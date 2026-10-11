#!/usr/bin/env python3
import itertools
import math

SQ2=math.sqrt(2.0)

def solve(A,b,eps=1e-11):
    n=len(A)
    M=[list(map(float,A[i]))+[float(b[i])] for i in range(n)]
    for c in range(n):
        p=max(range(c,n),key=lambda r:abs(M[r][c]))
        if abs(M[p][c])<eps:
            return None
        M[c],M[p]=M[p],M[c]
        q=M[c][c]
        M[c]=[z/q for z in M[c]]
        for r in range(n):
            if r==c:
                continue
            q=M[r][c]
            if abs(q)>eps:
                M[r]=[M[r][j]-q*M[c][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

def barrier(a,l):
    s=len(a)
    vals=[]
    for m in range(1,s+1):
        for i in range(s):
            total=sum(a[(i+q)%s] for q in range(m))
            vals.append((total-(m-1)*l)/(2+(m-1)*SQ2))
        if m==s:
            break
    vals.append((sum(a)-s*l)/(s*SQ2))
    return min(vals)

def brute(a,l):
    s=len(a)
    # Variables x_0,...,x_{s-1},r. Rows encode lhs >= rhs.
    rows=[]
    for i in range(s):
        row=[0.0]*(s+1)
        row[i]=1.0; row[-1]=-1.0
        rows.append((row,0.0))

        row=[0.0]*(s+1)
        row[i]=-1.0; row[-1]=-1.0
        rows.append((row,-a[i]))

        row=[0.0]*(s+1)
        row[i]=-1.0
        row[(i+1)%s]=1.0
        row[-1]=-SQ2
        rows.append((row,-(a[i]-l)))

    row=[0.0]*(s+1); row[-1]=1.0
    rows.append((row,0.0))

    best=-1.0
    for active in itertools.combinations(range(len(rows)),s+1):
        A=[rows[j][0] for j in active]
        b=[rows[j][1] for j in active]
        z=solve(A,b)
        if z is None:
            continue
        if all(sum(c*v for c,v in zip(row,z)) >= rhs-2e-9
               for row,rhs in rows):
            best=max(best,z[-1])
    return best

cases=[
    ((2,2),0),((2,2),1),((3,5),1),((4,7),2),
    ((2,2,2),1),((3,4,5),1),((4,6,7),2),((5,5,8),2),
    ((2,3,4),1),((6,4,5),2),
    ((2,2,2,2),1),((3,4,5,6),1),((4,5,7,8),2),
    ((6,6,6,6),3),((5,7,6,8),2),((3,8,5,7),1),
]
for a,l in cases:
    assert 2*l<=min(a)
    want=barrier(a,l)
    got=brute(a,l)
    assert abs(want-got)<=3e-8*max(1.0,abs(want)),(a,l,want,got)

for s in range(2,13):
    for a in (2,4,6,10):
        for l in range(0,a//2+1):
            general=barrier((a,)*s,l)
            closed=min(a/2,(a-l)/SQ2)
            assert abs(general-closed)<2e-12,(s,a,l,general,closed)

print(f"VERIFY_OK chainlink-inradius active_lp_cases={len(cases)} homogeneous_s=2..12")
