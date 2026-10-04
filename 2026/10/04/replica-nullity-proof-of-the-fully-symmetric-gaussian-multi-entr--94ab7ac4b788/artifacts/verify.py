#!/usr/bin/env python3
import math


def e_minus(a, N):
    return (((a*a-1)*(N-2) - math.sqrt(a*a-1)*math.sqrt((a*a-1)*N*N+4*(N-1)))
            /(2*a*(N-1)))


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def add(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def det(A):
    A=[row[:] for row in A]
    n=len(A); out=1.0
    for k in range(n):
        p=max(range(k,n), key=lambda i: abs(A[i][k]))
        if abs(A[p][k]) < 1e-15: return 0.0
        if p != k:
            A[k],A[p]=A[p],A[k]; out=-out
        piv=A[k][k]; out*=piv
        for i in range(k+1,n):
            f=A[i][k]/piv
            for j in range(k+1,n): A[i][j]-=f*A[k][j]
    return out


def perm(n, axis):
    r=n*n; P=[[0.0]*r for _ in range(r)]
    for i in range(n):
        for j in range(n):
            s=i*n+j
            t=(i*n+(j+1)%n) if axis==0 else (((i+1)%n)*n+j)
            P[s][t]=1.0
    return P


def blockdiag(blocks):
    sizes=[len(b) for b in blocks]; total=sum(sizes)
    M=[[0.0]*total for _ in range(total)]; off=0
    for B in blocks:
        m=len(B)
        for i in range(m):
            for j in range(m): M[off+i][off+j]=B[i][j]
        off+=m
    return M


def kron_outer(v, r):
    q=len(v); M=[[0.0]*(q*r) for _ in range(q*r)]
    for x in range(q):
        for y in range(q):
            c=v[x]*v[y]
            for i in range(r): M[x*r+i][y*r+i]=c
    return M


def z3(a, sizes, n):
    N=sum(sizes); r=n*n
    e=e_minus(a,N); alpha=a-e
    lam=(alpha+N*e)/alpha; t=e/(2*alpha)
    PA,PB=perm(n,0),perm(n,1); I=eye(r)
    Q=blockdiag([PA,PB,I]); B=kron_outer([math.sqrt(x) for x in sizes],r)
    K=add(B,matmul(transpose(Q),matmul(B,Q)))
    D=eye(3*r)
    for i in range(3*r):
        for j in range(3*r): D[i][j]+=t*K[i][j]
    return lam**(r/2)/math.sqrt(det(D))


def z2(a, m, N, n):
    r=n; P=[[0.0]*r for _ in range(r)]
    for i in range(r): P[i][(i+1)%r]=1.0
    I=eye(r); Q=blockdiag([P,I]); B=kron_outer([math.sqrt(m),math.sqrt(N-m)],r)
    K=add(B,matmul(transpose(Q),matmul(B,Q)))
    e=e_minus(a,N); alpha=a-e; lam=(alpha+N*e)/alpha; t=e/(2*alpha)
    D=eye(2*r)
    for i in range(2*r):
        for j in range(2*r): D[i][j]+=t*K[i][j]
    return lam**(r/2)/math.sqrt(det(D))


def gm(a,sizes,n):
    S3=math.log(z3(a,sizes,n))/(n*(1-n))
    S2=sum(math.log(z2(a,m,sum(sizes),n))/(1-n) for m in sizes)
    return S3-0.5*S2


def close(x,y,tol=2e-9):
    if abs(x-y)>tol*max(1.0,abs(x),abs(y)):
        raise AssertionError((x,y))

# Source Table 1: N=3, n=3.
for a in (1.2,2.0,5.0):
    expected=(1/12)*math.log(((9*a*a-1)**2)/((3*a*a+1)**3))
    close(gm(a,[1,1,1],3),expected)

# Source Table 1: N=4, (2,1,1), n=4.
for a in (1.2,2.0,5.0):
    expected=(1/24)*math.log(((7*a*a-1)**4)/(3*(a*a+1)**4*(2*a*a+1)**2*(4*a*a-1)))
    close(gm(a,[2,1,1],4),expected)

# lambda has the claimed a^-2 coefficient.
for N in (3,4,7,12):
    a=1.0e5; e=e_minus(a,N); alpha=a-e; lam=(alpha+N*e)/alpha
    close(a*a*lam,(N-1)/(N*N),2e-5)

# Row and column shifts generate one orbit on the n x n replica grid.
for n in range(2,11):
    seen={(0,0)}; stack=[(0,0)]
    while stack:
        i,j=stack.pop()
        for w in (((i+1)%n,j),(i,(j+1)%n)):
            if w not in seen: seen.add(w); stack.append(w)
    if len(seen)!=n*n: raise AssertionError(('orbit',n,len(seen)))

print('VERIFY_OK')
