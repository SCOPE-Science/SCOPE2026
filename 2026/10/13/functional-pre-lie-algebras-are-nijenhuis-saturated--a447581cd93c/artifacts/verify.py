from itertools import product
from collections import Counter

def matvec(M, x, q):
    n=len(x)
    return tuple(sum(M[i*n+j]*x[j] for j in range(n))%q for i in range(n))

def matmul(A,B,n,q):
    return tuple(sum(A[i*n+k]*B[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def add(*vs,q):
    n=len(vs[0])
    return tuple(sum(v[i] for v in vs)%q for i in range(n))

def smul(a,x,q):
    return tuple(a*z%q for z in x)

def prodv(x,y,q):
    return smul(x[0],y,q)

def is_nij(M,n,q):
    bas=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
    for x,y in product(bas,repeat=2):
        Nx,Ny=matvec(M,x,q),matvec(M,y,q)
        lhs=prodv(Nx,Ny,q)
        p1=prodv(Nx,y,q)
        p2=prodv(x,Ny,q)
        p3=matvec(M,prodv(x,y,q),q)
        inside=tuple((p1[i]+p2[i]-p3[i])%q for i in range(n))
        rhs=matvec(M,inside,q)
        if lhs!=rhs:
            return False
    return True

def is_rb0(M,n,q):
    bas=[tuple(1 if i==j else 0 for i in range(n)) for j in range(n)]
    for x,y in product(bas,repeat=2):
        Rx,Ry=matvec(M,x,q),matvec(M,y,q)
        lhs=prodv(Rx,Ry,q)
        inside=add(prodv(Rx,y,q),prodv(x,Ry,q),q=q)
        if lhs!=matvec(M,inside,q):
            return False
    return True

def rank(M,n,q):
    A=[list(M[i*n:(i+1)*n]) for i in range(n)]
    r=0
    for c in range(n):
        p=next((i for i in range(r,n) if A[i][c]%q),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        inv=pow(A[r][c],-1,q)
        A[r]=[(inv*z)%q for z in A[r]]
        for i in range(n):
            if i!=r and A[i][c]%q:
                f=A[i][c]%q
                A[i]=[(A[i][j]-f*A[r][j])%q for j in range(n)]
        r+=1
    return r

def matrix_rank_count(n,r,q):
    if r==0:
        return 1
    num=1
    den=1
    for i in range(r):
        num *= (q**n-q**i)**2
        den *= (q**r-q**i)
    return num//den

def qbinom(n,r,q):
    if r<0 or r>n:
        return 0
    if r==0 or r==n:
        return 1
    num=den=1
    for i in range(r):
        num*=q**(n-i)-1
        den*=q**(r-i)-1
    return num//den

def gl_count(r,q):
    z=1
    for i in range(r):
        z*=q**r-q**i
    return z

tests=[(1,2),(2,2),(2,3),(3,2),(3,3)]
for n,q in tests:
    mats=list(product(range(q),repeat=n*n))
    assert all(is_nij(M,n,q) for M in mats)
    assert len(mats)==q**(n*n)

    fibers=Counter(tuple(M[j] for j in range(n)) for M in mats)  # first row
    assert len(fibers)==q**n
    assert set(fibers.values())=={q**(n*(n-1))}

    rc=Counter(rank(M,n,q) for M in mats)
    expected=tuple(matrix_rank_count(n,r,q) for r in range(n+1))
    assert tuple(rc[r] for r in range(n+1))==expected

    rb=[M for M in mats if is_rb0(M,n,q)]
    sq=[M for M in mats if matmul(M,M,n,q)==(0,)*(n*n)]
    assert set(rb)==set(sq)
    rr=Counter(rank(M,n,q) for M in rb)
    for r in range(n+1):
        expect=(qbinom(n,r,q)*qbinom(n-r,r,q)*gl_count(r,q)
                if r<=n//2 else 0)
        assert rr[r]==expect,(n,q,r,rr[r],expect)

    print({
        "n":n,
        "q":q,
        "nijenhuis":len(mats),
        "deformation_fiber_size":q**(n*(n-1)),
        "rank_profile":tuple(rc[r] for r in range(n+1)),
        "rb0":len(rb),
        "rb0_rank_profile":tuple(rr[r] for r in range(n+1)),
    })

print("VERIFY_OK")
