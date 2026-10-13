from fractions import Fraction


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def flat(X):
    return [x for row in X for x in row]


def add(*Xs):
    n=len(Xs[0]); Y=zero(n)
    for X in Xs:
        for i in range(n):
            for j in range(n):
                Y[i][j]+=X[i][j]
    return Y


def scale(a,X):
    return [[a*x for x in row] for row in X]


def eq(X,Y):
    return X==Y


def Aop(X):
    n=len(X)
    s=sum(sum(row) for row in X)
    rows=[sum(row) for row in X]
    cols=[sum(X[i][j] for i in range(n)) for j in range(n)]
    Y=zero(n)
    for i in range(n):
        for j in range(n):
            Y[i][j]=s-rows[j]-cols[i]+X[j][i]
            if i!=j:
                Y[i][j]-=X[i][j]
    return Y


def rank(M):
    if not M: return 0
    A=[list(map(Fraction,row)) for row in M]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]
        A[r]=[v/z for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r


def nullspace(M):
    A=[list(map(Fraction,row)) for row in M]
    m=len(A); n=len(A[0]) if m else 0
    piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        z=A[r][c]; A[r]=[v/z for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[A[i][j]-z*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for f in free:
        v=[Fraction(0)]*n; v[f]=1
        for rr,p in enumerate(piv): v[p]=-A[rr][f]
        out.append(v)
    return out


def matrix_from_vecs(vecs):
    # columns are vectors
    if not vecs: return []
    return [[vecs[c][r] for c in range(len(vecs))] for r in range(len(vecs[0]))]


def check(n):
    one=[Fraction(1)]*n
    I=zero(n); J=zero(n)
    for i in range(n):
        I[i][i]=1
        for j in range(n): J[i][j]=1
    assert eq(Aop(I),add(I,scale(n-2,J)))
    assert eq(Aop(J),add(I,scale(n*(n-2),J)))
    basis=[I,J]

    for a in range(n-1):
        u=[Fraction(0)]*n; u[a]=1; u[-1]=-1
        D=zero(n); P=zero(n); Q=zero(n)
        for i in range(n):
            D[i][i]=u[i]
            for j in range(n):
                P[i][j]=u[i]+u[j]
                Q[i][j]=u[j]-u[i]
        assert eq(Aop(D),add(D,scale(-1,P)))
        assert eq(Aop(P),add(scale(2,D),scale(-n,P)))
        assert eq(Aop(Q),scale(n-2,Q))
        basis.extend([D,P,Q])

    # skew row-sum-zero basis
    km=[]
    for i in range(n-1):
        for j in range(i+1,n-1):
            X=zero(n)
            def kedge(a,b,c):
                X[a][b]+=c; X[b][a]-=c
            kedge(i,j,1); kedge(i,n-1,-1); kedge(j,n-1,1)
            assert all(sum(row)==0 for row in X)
            assert eq(Aop(X),scale(-2,X))
            km.append(X)
    assert len(km)==(n-1)*(n-2)//2
    basis.extend(km)

    # symmetric zero-diagonal row-sum-zero space as kernel of unsigned incidence matrix
    edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    incidence=[[Fraction(1) if (i in e) else Fraction(0) for e in edges] for i in range(n)]
    ns=nullspace(incidence)
    assert len(ns)==n*(n-3)//2
    k0=[]
    for v in ns:
        X=zero(n)
        for coeff,(i,j) in zip(v,edges):
            X[i][j]=X[j][i]=coeff
        assert all(X[i][i]==0 for i in range(n))
        assert all(sum(row)==0 for row in X)
        assert eq(Aop(X),zero(n))
        k0.append(X)
    basis.extend(k0)

    vecs=[flat(X) for X in basis]
    assert len(vecs)==n*n
    assert rank(matrix_from_vecs(vecs))==n*n
    print(f'n={n} dim={n*n} skew={len(km)} null={len(k0)} decomposition=OK')


for n in range(3,9):
    check(n)
print('VERIFY_OK')
