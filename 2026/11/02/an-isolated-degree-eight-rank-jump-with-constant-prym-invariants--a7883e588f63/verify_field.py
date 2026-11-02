"""Independent exact check in F_(5^8) = F_5[z]/(z^8-2).
Uses direct polynomial convolution, Frobenius, and Gaussian elimination.
No symbolic-computation dependency.
"""
P=5
N=8
Q=P**N
ZERO=(0,)*N
ONE=(1,)+(0,)*(N-1)
Z=(0,1)+(0,)*(N-2)

def const(i): return ((i%5),)+(0,)*(N-1)
def plus(u,v): return tuple((x+y)%P for x,y in zip(u,v))
def neg(u):return tuple((-x)%P for x in u)
def mul(u,v):
    t=[0]*15
    for i in range(N):
        for j in range(N): t[i+j]=(t[i+j]+u[i]*v[j])%P
    for k in range(14,7,-1):t[k-8]=(t[k-8]+2*t[k])%P
    return tuple(t[:8])
def power(u,n):
    v=ONE
    while n:
        if n&1:v=mul(v,u)
        u=mul(u,u)
        n//=2
    return v

def addpoly(A,B):
    C=[ZERO]*max(len(A),len(B))
    for i in range(len(C)):
        C[i]=plus(A[i] if i<len(A) else ZERO,B[i] if i<len(B) else ZERO)
    return C

def mulpoly(A,B):
    C=[ZERO]*(len(A)+len(B)-1)
    for i,ai in enumerate(A):
        for j,bj in enumerate(B):C[i+j]=plus(C[i+j],mul(ai,bj))
    return C

def coeff_matrices(degree,middle,a):
    f=[ZERO]*(degree+1)
    f[0]=ONE;f[degree]=ONE;f[middle]=a
    g=mulpoly(mulpoly(f,f),f)
    s1=(degree-1)//3;s2=(2*degree-1)//3
    H=[[ZERO]*(s1+s2) for _ in range(s1+s2)]
    # Put the coefficient matrices directly into a single raw Cartier matrix.
    for i in range(s1):
        for j in range(s2):
            k=5*j+4-i
            if 0<=k<len(g):H[s1+j][i]=g[k]
    for i in range(s2):
        for j in range(s1):
            k=5*j+4-i
            if 0<=k<len(f):H[j][s1+i]=f[k]
    return H

def mulmat(A,B):
    n=len(A); m=len(B);r=len(B[0])
    C=[[ZERO]*r for _ in range(n)]
    for i in range(n):
        for k in range(m):
            if A[i][k]==ZERO:continue
            for j in range(r):
                C[i][j]=plus(C[i][j],mul(A[i][k],B[k][j]))
    return C

def rootmat(A):return [[power(c,P**7) for c in row] for row in A]
def rank(M):
    A=[row[:] for row in M]
    n=len(A);m=len(A[0]);r=0
    for c in range(m):
        p=next((i for i in range(r,n) if A[i][c]!=ZERO),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        inv=power(A[r][c],Q-2)
        A[r]=[mul(t,inv) for t in A[r]]
        for i in range(r+1,n):
            if A[i][c]!=ZERO:
                t=A[i][c]
                A[i]=[plus(A[i][j],neg(mul(t,A[r][j]))) for j in range(m)]
        r+=1
        if r==n:break
    return r

def stable_rank(H):
    R=rootmat(H)
    A=R
    ranks=[]
    for _ in range(10):
        ranks.append(rank(A))
        A=mulmat(R,rootmat(A))
    assert ranks[-1]==ranks[-2]==ranks[-3],ranks
    return ranks[0],ranks[-1],ranks

cases=[('zero',ZERO,4,2),('one',ONE,4,2),('degree8',Z,2,0),('degree8_plus_one',plus(Z,ONE),4,2)]
for label,a,expected7,expected3 in cases:
    assert power(a,4)!=const(3)
    C=coeff_matrices(8,6,a)
    D=coeff_matrices(4,3,a)
    one7,stable7,path7=stable_rank(C)
    one3,stable3,path3=stable_rank(D)
    assert one7==4 and one3==2,(label,one7,one3)
    assert stable7==expected7 and stable3==expected3,(label,path7,path3)
    assert stable7-stable3==2
    print(label,'g7 Cartier/stable',one7,stable7,'g3 Cartier/stable',one3,stable3)
assert power(Z,8)==const(2)
assert power(power(Z,6),4)==const(3)
print('INDEPENDENT_FINITE_FIELD_OK')
