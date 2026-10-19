"""Exact checks for the 24-cell single-degree harmonic interpolation theorem.

Requires Python 3.10+ standard library only. Arithmetic is rational throughout.
The unbounded degree conclusion is proved separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations


def transpose(a):
    return list(map(list, zip(*a)))


def mm(a, b):
    bt = transpose(b)
    return [[sum(x*y for x, y in zip(row,col)) for col in bt] for row in a]


def eye(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def scale(a,c):
    return [[c*x for x in row] for row in a]


def add(a,b):
    return [[x+y for x,y in zip(row1,row2)] for row1,row2 in zip(a,b)]


def mat_eq(a,b):
    return all(row1==row2 for row1,row2 in zip(a,b))


def rank(a):
    a = [[F(t) for t in row] for row in a]
    m=len(a); n=len(a[0]); p=0
    for j in range(n):
        k=next((k for k in range(p,m) if a[k][j]),None)
        if k is None: continue
        a[p],a[k]=a[k],a[p]
        factor=a[p][j]
        a[p]=[v/factor for v in a[p]]
        for i in range(m):
            if i!=p and a[i][j]:
                factor=a[i][j]
                a[i]=[x-factor*y for x,y in zip(a[i],a[p])]
        p+=1
        if p==m: break
    return p


def U(l,t):
    a,b=F(1),F(2)*t
    if l==0:return a
    if l==1:return b
    for k in range(2,l+1):
        a,b=b,2*t*b-a
    return b


roots=[]
for i,j in combinations(range(4),2):
    for sign in (1,-1):
        r=[0]*4
        r[i]=1;r[j]=sign
        roots.append(tuple(F(x,1) for x in r))


def dot(i,j):
    return sum(x*y for x,y in zip(roots[i],roots[j]))/2

N=12; I=eye(N); J=[[F(1)]*N for _ in range(N)]
A=[[F(i!=j and abs(dot(i,j))==F(1,2)) for j in range(N)] for i in range(N)]
S=[[2*dot(i,j) if i!=j else F(0) for j in range(N)] for i in range(N)]
B=[[F(1) if (i!=j and dot(i,j)==0) else F(0) for j in range(N)] for i in range(N)]
assert mat_eq(add(add(A,B),I),J)
assert all(sum(row)==8 for row in A)
assert all(sum(row)==3 for row in B)
assert mat_eq(mm(add(S,scale(I,-4)),add(S,scale(I,2))),scale(I,0))
assert mat_eq(mm(mm(A,add(A,scale(I,4))),add(A,scale(I,-8))),scale(I,0))
M=[[roots[j][i] for j in range(N)] for i in range(4)]
# Dot products use unnormalized coordinates divided by two.
assert mat_eq(mm(M,transpose(M)),scale(eye(4),6))
assert mat_eq(S,add(mm(transpose(M),M),scale(I,-2)))
P_one=scale(J,F(1,12))
P_minus4=scale(mm(A,add(A,scale(I,-8))),F(1,48))
P_zero=add(add(I,scale(P_one,-1)),scale(P_minus4,-1))
P_four=scale(add(S,scale(I,2)),F(1,6))
P_minus2=scale(add(scale(I,4),scale(S,-1)),F(1,6))
for P in (P_one,P_minus4,P_zero,P_four,P_minus2):
    assert mat_eq(mm(P,P),P)
assert mat_eq(add(add(P_one,P_minus4),P_zero),I)
assert mat_eq(add(P_four,P_minus2),I)
assert [rank(P_one),rank(P_minus4),rank(P_zero),rank(P_four),rank(P_minus2)]==[1,2,9,4,8]

expected_ranks=[1,4,9,8,11,12,10,12,12,12,11]
count=0
for ell in range(121):
    alpha=U(ell,F(1,2))
    G=[[U(ell,dot(i,j)) for j in range(N)] for i in range(N)]
    if ell%2:
        assert alpha in (-1,0,1)
        h_four=ell+1+4*alpha
        h_minus2=ell+1-2*alpha
        reconstructed=add(scale(P_four,h_four),scale(P_minus2,h_minus2))
        expected=(h_four!=0)*4+(h_minus2!=0)*8
    else:
        beta=U(ell,F(0))
        assert alpha in (-1,0,1) and beta in (-1,1)
        h_one=ell+1+8*alpha+3*beta
        h_minus4=ell+1-4*alpha+3*beta
        h_zero=ell+1-beta
        reconstructed=add(add(scale(P_one,h_one),scale(P_minus4,h_minus4)),scale(P_zero,h_zero))
        expected=(h_one!=0)+2*(h_minus4!=0)+9*(h_zero!=0)
    assert mat_eq(G,reconstructed)
    assert rank(G)==expected
    assert expected==(expected_ranks[ell] if ell<len(expected_ranks) else 12)
    count+=3
    if ell%2 and ell%6==5:
        assert mat_eq(G,scale(I,ell+1));count+=1

# The full antipodal 24-by-24 kernel must have the same rank as the 12-point compression.
for ell in range(16):
    sign=(-1)**ell
    H=[[U(ell,dot(i,j)) for j in range(N)] for i in range(N)]
    W=[[sign**(a+b)*H[i][j] for b in range(2) for j in range(N)] for a in range(2) for i in range(N)]
    assert rank(W)==(expected_ranks[ell] if ell<len(expected_ranks) else 12)
    count+=1
print(f"PASS: {count} degree/spectral/rank assertions plus exact geometry/projector identities")
