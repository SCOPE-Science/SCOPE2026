"""Independent exact-arithmetic checks for budgeted discounted first-hitting support.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def solve(A,b):
    n=len(A)
    M=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        p=next((i for i in range(j,n) if M[i][j]),None)
        assert p is not None
        M[j],M[p]=M[p],M[j]
        s=M[j][j]
        for t in range(j,n+1): M[j][t]/=s
        for i in range(n):
            if i==j:continue
            w=M[i][j]
            if w:
                for t in range(j,n+1):M[i][t]-=w*M[j][t]
    return [M[i][n] for i in range(n)]


def direct_score(n,lam,S):
    S=set(S)
    U=[i for i in range(2*n) if i not in S]
    if not U:return F(1)
    idx={v:i for i,v in enumerate(U)}
    A=[[F(0) for _ in U] for _ in U]
    b=[F(0) for _ in U]
    for i,v in enumerate(U):
        A[i][i]=F(1)
        neigh=range(n,2*n) if v<n else range(n)
        for w in neigh:
            if w in S:b[i]+=lam/n
            else:A[i][idx[w]]-=lam/n
    vals=solve(A,b)
    assert all(F(0)<=z<1 for z in vals)
    return min(vals)


def analytic_score(n,lam,x,y):
    if x==n and y==n:return F(1)
    if x==n or y==n:return lam
    D=F(n*n)-lam*lam*(n-x)*(n-y)
    p=(lam*n*y+lam*lam*x*(n-y))/D
    q=(lam*n*x+lam*lam*y*(n-x))/D
    return min(p,q)


def predicted(n,lam,k):
    if k==2*n:return F(1)
    if k>=n:return lam
    if k%2==0:
        j=k//2
        return lam*j/(n*(1-lam)+lam*j)
    j=(k-1)//2
    D=F(n*n)-lam*lam*(n-j-1)*(n-j)
    near=(lam*n*j+lam*lam*(n-j)*(j+1))/D
    one=lam*lam*k/(n*(1-lam*lam)+lam*lam*k)
    return max(near,one)


def predicted_profiles(n,lam,k):
    if k==2*n:return {(n,n)}
    if k>=n:return {(n,k-n),(k-n,n)}
    if k%2==0:return {(k//2,k//2)}
    j=(k-1)//2
    near={(j+1,j),(j,j+1)}
    one={(k,0),(0,k)}
    score_near=analytic_score(n,lam,j+1,j)
    score_one=analytic_score(n,lam,k,0)
    if score_near>score_one:return near
    if score_one>score_near:return one
    return near|one


profiles=0
subsets=0
linear_systems=0
for n in range(2,6):
    vertices=tuple(range(2*n))
    for lam in (F(1,3),F(1,2),F(3,4),F(9,10),F(19,20),F(99,100)):
        for k in range(1,2*n+1):
            data=[]
            for S in combinations(vertices,k):
                subsets+=1
                x=sum(v<n for v in S)
                y=k-x
                dr=direct_score(n,lam,S)
                linear_systems+=1
                ar=analytic_score(n,lam,x,y)
                assert dr==ar,(n,lam,k,S,dr,ar)
                data.append((dr,x,y))
            H=max(q[0] for q in data)
            assert H==predicted(n,lam,k),(n,lam,k,H,predicted(n,lam,k))
            optim={(x,y) for score,x,y in data if score==H}
            assert optim==predicted_profiles(n,lam,k),(n,lam,k,optim,predicted_profiles(n,lam,k))
            profiles+=1

n=4
lam=F(9,10)
near=analytic_score(n,lam,2,1)
one=analytic_score(n,lam,3,0)
assert near==F(423,557),near
assert one==F(243,319),one
assert near<F(761,1000)<one
assert predicted(n,lam,2)<F(761,1000)
assert predicted(n,lam,3)>F(761,1000)
admissible=[]
for S in combinations(range(8),3):
    if direct_score(4,lam,S)>=F(761,1000):
        admissible.append(S)
assert len(admissible)==8,(len(admissible),admissible)
assert all(sum(v<4 for v in S) in (0,3) for S in admissible)
assert 2*comb(n,3)==8

print(f'ALL CHECKS PASSED; parameter_cases={profiles}; exact_vertex_linear_systems={linear_systems}; source_subsets_checked={subsets}; n=2..5; lambdas=1/3,1/2,3/4,9/10,19/20,99/100; n4_threshold_example=8')
