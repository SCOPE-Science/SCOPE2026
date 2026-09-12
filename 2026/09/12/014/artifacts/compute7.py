from fractions import Fraction
from math import gcd

def matmul(A,B):
    n,m,p=len(A),len(B),len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]
def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def meq(A,B):
    return all(A[i][j]==B[i][j] for i in range(len(A)) for j in range(len(A[0])))
def matpow(A,e):
    n=len(A); R=eye(n); B=[r[:] for r in A]
    while e:
        if e&1: R=matmul(R,B)
        B=matmul(B,B); e>>=1
    return R
def msub(A,B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def transp(A):
    return [list(r) for r in zip(*A)]
def bdet(M):
    n=len(M); A=[[Fraction(x) for x in row] for row in M]; prev=Fraction(1)
    for k in range(n-1):
        piv=k
        while piv<n and A[piv][k]==0: piv+=1
        if piv==n: return Fraction(0)
        if piv!=k: A[k],A[piv]=A[piv],A[k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*A[k][k]-A[i][k]*A[k][j])/prev
            A[i][k]=Fraction(0)
        prev=A[k][k]
        if prev==0: return Fraction(0)
    return A[n-1][n-1]
def charpoly_coeffs(A):
    n=len(A); vals=[]
    for t in range(n+1):
        M=[[(t if i==j else 0)-A[i][j] for j in range(n)] for i in range(n)]
        vals.append(bdet(M))
    V=[[Fraction(i**j) for j in range(n+1)] for i in range(n+1)]
    Aug=[row[:]+[vals[i]] for i,row in enumerate(V)]
    for col in range(n+1):
        piv=col
        while Aug[piv][col]==0: piv+=1
        Aug[col],Aug[piv]=Aug[piv],Aug[col]
        d=Aug[col][col]
        Aug[col]=[v/d for v in Aug[col]]
        for i in range(n+1):
            if i!=col and Aug[i][col]!=0:
                t=Aug[i][col]
                Aug[i]=[a-t*b for a,b in zip(Aug[i],Aug[col])]
    return list(reversed([Aug[i][n+1] for i in range(n+1)]))
def smith2x2_all(M):
    # returns invariant factors for integer matrix via gcds (for small matrices, brute force minors)
    import itertools
    m,n=len(M),len(M[0])
    g0=0
    for i in range(m):
        for j in range(n): g0=gcd(g0,abs(int(M[i][j])))
    g1=0
    for i1 in range(m):
        for i2 in range(i1+1,m):
            for j1 in range(n):
                for j2 in range(j1+1,n):
                    g1=gcd(g1,abs(int(M[i1][j1]*M[i2][j2]-M[i1][j2]*M[i2][j1])))
    return g0,g1

C = [[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],[0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]]
G11=[[-C[i][j] for j in range(6)] for i in range(6)]
col6=[0,1,0,0,0,0]; col7=[0,1,0,-1,0,0]
G=[[0]*8 for _ in range(8)]
for i in range(6):
    for j in range(6): G[i][j]=G11[i][j]
    G[i][6],G[i][7]=col6[i],col7[i]
    G[6][i],G[7][i]=col6[i],col7[i]
G[6][6],G[6][7],G[7][6],G[7][7]=-2,1,1,-2
def Gpair(x,y):
    return sum(x[i]*G[i][j]*y[j] for i in range(8) for j in range(8))
def refl(i):
    n=8; S=eye(n)
    for b in range(8): S[i][b]+=G[b][i]
    return S
Ss=[refl(i) for i in range(8)]
r0=[1,2,2,3,2,1,1,0]; r1=[-1,-1,-2,-3,-2,-1,0,1]
# verify radical is kernel: G*r == 0
def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]
print("G*r0=",matvec(G,r0),"G*r1=",matvec(G,r1))
print("det G =",bdet(G))
# primitivity of r0,r1: gcd of coords
from math import gcd
def vg(v):
    g=0
    for x in v: g=gcd(g,abs(x))
    return g
print("gcd r0:",vg(r0),"gcd r1:",vg(r1))
# saturation: any integer combination a r0 + b r1 primitive check? lattice R saturate: check M/R torsionfree: smith of inclusion? check: if x in M pairs... use: R saturated iff gcd conditions. Compute: projection M->Z^6, kernel exactly R and image all Z^6 => saturated.
# verify Phi image: Phi cols span Z^6? Phi[:,:6]=I so yes surjective, kernel rank 2 = R. So R saturated, and (r0,r1) extendable? check 2x2 minors gcd of [r0;r1] rows? compute gcd of all 2x2 minors of 8x2 matrix
import itertools
M8=[[r0[i],r1[i]] for i in range(8)]
g=0
for i1,i2 in itertools.combinations(range(8),2):
    g=gcd(g,abs(M8[i1][0]*M8[i2][1]-M8[i1][1]*M8[i2][0]))
print("gcd 2x2 minors (1 iff primitive sublattice):",g)
# Coxeter both conventions
cM=eye(8)
for i in [0,1,2,3,4,5]: cM=matmul(Ss[i],cM)
print("cM isom:",meq(matmul(transp(cM),matmul(G,cM)),G))
for k in range(1,13):
    if meq(matpow(cM,k),eye(8)): print("cM order:",k); break
# powers minimal: show cM^k != I for k<12 with witness entries
for k in [1,2,3,4,6]:
    P=matpow(cM,k)
    nz=[(i,j,P[i][j]) for i in range(8) for j in range(8) if P[i][j]!=(1 if i==j else 0)][:3]
    print(k,"witness:",nz)
# cM^12 == I witnessed
print("cM^12==I:",meq(matpow(cM,12),eye(8)))
# quotient
Phi=[[1 if i==j else 0 for j in range(8)] for i in range(6)]
Phi[0]=[1,0,0,0,0,0,-1,1]; Phi[1]=[0,1,0,0,0,0,-2,1]; Phi[2]=[0,0,1,0,0,0,-2,2]
Phi[3]=[0,0,0,1,0,0,-3,3]; Phi[4]=[0,0,0,0,1,0,-2,2]; Phi[5]=[0,0,0,0,0,1,-1,1]
PhiT=matmul(Phi,cM)
Cq=[[PhiT[i][j] for j in range(6)] for i in range(6)]
print("Cq charpoly:",[str(c) for c in charpoly_coeffs(Cq)])
P=eye(6)
for k in range(1,25):
    P=matmul(P,Cq)
    if meq(P,eye(6)): print("Cq order:",k); break
# proper divisors != I witnesses
for k in [1,2,3,4,6]:
    P=matpow(Cq,k)
    nz=[(i,j,P[i][j]) for i in range(6) for j in range(6) if P[i][j]!=(1 if i==j else 0)][:3]
    print("Cq^%d witness:"%k,nz)
# 8x8 charpoly of cM: should be (x^6+x^5-x^3+x+1)(x-1)^2
print("cM charpoly:",[str(c) for c in charpoly_coeffs(cM)])
# Seifert divisibility: since cM^12 = I, translation vector is 0; divisibility: compute cM^12 - I = 0 matrix; gcd of entries 0.
# Also record discriminant: det(-G11)=3; signature of G: negative semi-definite with 2 zeros: eigenvalues signs via LDL? compute characteristic values numerically? Use exact: G11 neg-def (leading principal minors alternate), plus 2-dim kernel.
print("det(-G11):",bdet([[-x for x in row] for row in G11]))
# leading principal minors of -G11
import copy
PM=[[-G11[i][j] for j in range(6)] for i in range(6)]
for k in range(1,7):
    print("lpm",k,bdet([row[:k] for row in PM[:k]]))
