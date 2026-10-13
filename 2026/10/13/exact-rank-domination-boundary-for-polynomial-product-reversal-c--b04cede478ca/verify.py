#!/usr/bin/env python3
from itertools import product

def mm(A,B,p):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))%p for j in range(n)] for i in range(n)]

def madd(A,B,p):
    return [[(A[i][j]+B[i][j])%p for j in range(len(A))] for i in range(len(A))]

def mscale(c,A,p):
    return [[(c*x)%p for x in row] for row in A]

def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def zero(n):
    return [[0]*n for _ in range(n)]

def peval(coeffs,A,p):
    # coeffs low to high
    n=len(A)
    out=zero(n)
    pw=eye(n)
    for c in coeffs:
        out=madd(out,mscale(c,pw,p),p)
        pw=mm(pw,A,p)
    return out

def rank(A,p):
    M=[row[:] for row in A]
    m=len(M); n=len(M[0]) if m else 0
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if M[i][c]%p),None)
        if pivot is None: continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][c]%p,-1,p)
        M[r]=[(inv*x)%p for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]%p:
                f=M[i][c]%p
                M[i]=[(M[i][j]-f*M[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

def all_mats(n,p):
    for vals in product(range(p), repeat=n*n):
        yield [list(vals[i*n:(i+1)*n]) for i in range(n)]

def assert_domination(coeff_p, coeff_q, field=3, n=2):
    mats=list(all_mats(n,field))
    checked=0
    for X in mats:
        for Y in mats:
            XY=mm(X,Y,field); YX=mm(Y,X,field)
            rp=rank(peval(coeff_p,XY,field),field)
            rq=rank(peval(coeff_q,YX,field),field)
            assert rq <= rp, (X,Y,rp,rq)
            checked+=1
    return checked

# Branch 1: p=t-1, q=(t-1)(t+1)=t^2-1 over F_3.
c1=assert_domination([2,1],[2,0,1],3,2)
print("case_nonzero_constant_domination",c1)

# Branch 2: p=t, q=t^2; the free factorization predicts domination.
c2=assert_domination([0,1],[0,0,1],3,2)
print("case_extra_zero_factor_domination",c2)

# Explicit failure when p=t, q=t (missing the extra t).
J=[[0,1],[0,0]]
D=[[1,0],[0,0]]
X=J; Y=D
XY=mm(X,Y,3)
YX=mm(Y,X,3)
assert XY==[[0,0],[0,0]]
assert YX==J
assert rank(peval([0,1],XY,3),3)==0
assert rank(peval([0,1],YX,3),3)==1
print("case_missing_extra_zero_factor_witness", "ok")

# Failure when p does not divide q: p=(t-1)^2, q=t-1 on J_2(1).
T=[[1,1],[0,1]]
P=peval([1,1,1],T,3)  # (t-1)^2 = t^2+t+1 in F_3
Q=peval([2,1],T,3)
assert rank(P,3)==0
assert rank(Q,3)==1
print("case_nondivisibility_jordan_witness", "ok")

# Matrix identity for q=t*p*r.  Example p=t+1, r=t+2 over F_3.
# q=t(t+1)(t+2)=t^3+2t over F_3.
for X in all_mats(2,3):
    for Y in all_mats(2,3):
        XY=mm(X,Y,3); YX=mm(Y,X,3)
        qyx=peval([0,2,0,1],YX,3)
        pxy=peval([1,1],XY,3)
        ryx=peval([2,1],YX,3)
        rhs=mm(mm(mm(Y,pxy,3),X,3),ryx,3)
        assert qyx==rhs
print("free_factorization_matrix_identity", "ok")

# Kernel-equality mechanism for p(0)!=0 on a sample p=t^2+t+1 over F_3.
for X in all_mats(2,3):
    for Y in all_mats(2,3):
        XY=mm(X,Y,3); YX=mm(Y,X,3)
        assert rank(peval([1,1,1],XY,3),3)==rank(peval([1,1,1],YX,3),3)
print("nonzero_constant_rank_equality", "ok")

print("CHECK_OK")
