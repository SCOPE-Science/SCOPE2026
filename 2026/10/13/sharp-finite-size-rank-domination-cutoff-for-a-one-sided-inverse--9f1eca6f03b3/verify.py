"""Exact finite checks for the truncated two-variable rank-domination criterion.

Run: python3 verify.py
Requires only Python 3 standard library. Uses prime fields for finite checks;
proof in RESULT.md treats all prime powers.
"""
from itertools import product
from math import gcd


def mul(A, B, p):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) % p
                       for j in range(n)) for i in range(n))


def add(A, B, p):
    return tuple(tuple((A[i][j]+B[i][j])%p for j in range(len(A))) for i in range(len(A)))


def zero(n):
    return tuple(tuple(0 for _ in range(n)) for _ in range(n))


def ident(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))


def rank(A, p):
    a = [list(row) for row in A]
    n=len(a); r=0
    for c in range(n):
        k=next((j for j in range(r,n) if a[j][c] % p),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        v=pow(a[r][c],-1,p)
        a[r]=[(v*x)%p for x in a[r]]
        for j in range(n):
            if j != r and a[j][c]:
                v=a[j][c]
                a[j]=[(x-v*y)%p for x,y in zip(a[j],a[r])]
        r+=1
    return r


def power(A, e, p):
    n=len(A); out=ident(n)
    while e:
        if e&1: out=mul(out,A,p)
        e>>=1
        if e: A=mul(A,A,p)
    return out


def inv(A,p):
    n=len(A)
    B=[list(A[i])+list(ident(n)[i]) for i in range(n)]
    for c in range(n):
        j=next((i for i in range(c,n) if B[i][c]),None)
        if j is None: return None
        B[c],B[j]=B[j],B[c]
        v=pow(B[c][c],-1,p)
        B[c]=[(v*x)%p for x in B[c]]
        for i in range(n):
            if i != c and B[i][c]:
                v=B[i][c]
                B[i]=[(x-v*y)%p for x,y in zip(B[i],B[c])]
    return tuple(tuple(row[n:]) for row in B)


def matrices(p,n):
    for data in product(range(p),repeat=n*n):
        yield tuple(tuple(data[i*n:(i+1)*n]) for i in range(n))


def poly_mul(f,g,p):
    out=[0]*(len(f)+len(g)-1)
    for i,a in enumerate(f):
        for j,b in enumerate(g): out[i+j]=(out[i+j]+a*b)%p
    while len(out)>1 and not out[-1]:out.pop()
    return out


def poly_rem(f,g,p):
    f=list(f);d=len(g)-1
    while len(f)>=len(g):
        a=f[-1]*pow(g[-1],-1,p)%p
        for j in range(len(g)):
            f[len(f)-len(g)+j]=(f[len(f)-len(g)+j]-a*g[j])%p
        while f and not f[-1]:f.pop()
    return f


def monic_irreds(p,d):
    for a in product(range(p),repeat=d):
        if not a[0]: continue
        f=list(a)+[1]
        if all(poly_rem(f,list(b)+[1],p) for k in range(1,d//2+1)
               for b in product(range(p),repeat=k)):
            yield f


def canonical(p,N):
    P=[1];degrees=[]
    for d in range(1,N+1):
        fac=list(monic_irreds(p,d));degrees.append((d,len(fac)))
        for f in fac:
            for _ in range(N//d): P=poly_mul(P,f,p)
    return P,degrees


def polynomial_matrix(P,A,p):
    # Horner at A, scalar coefficients added on the diagonal.
    n=len(A);cur=zero(n)
    for c in reversed(P):
        cur=mul(cur,A,p)
        cur=tuple(tuple((cur[i][j]+c*int(i==j))%p for j in range(n)) for i in range(n))
    return cur


def symmetric_lift(P):
    d=len(P)-1;L=(d+1)//2
    # t^{-L} P(t) has exponents in [-L,L].
    return {i-L:c for i,c in enumerate(P) if c}


def Laurent_eval(C,A,Ainv,p):
    n=len(A);out=zero(n)
    for k,c in C.items():
        T=power(A if k>=0 else Ainv,abs(k),p)
        out=tuple(tuple((out[i][j]+c*T[i][j])%p for j in range(n)) for i in range(n))
    return out


def explicit_bounded_rank_check(p,N):
    P,_=canonical(p,N)
    lift=symmetric_lift(P)
    total=0
    for m in range(1,N+1):
        mats=list(matrices(p,m))
        I=ident(m)
        for X in mats:
            for Y in mats:
                f=add(mul(X,Y,p),tuple(tuple(-z%p for z in row) for row in I),p)
                h=add(mul(Y,X,p),tuple(tuple(-z%p for z in row) for row in I),p)
                assert rank(f,p)==rank(h,p)
                g=zero(m)
                for e,c in lift.items():
                    Z=power(X if e>=0 else Y,abs(e),p)
                    g=add(g,tuple(tuple(c*z%p for z in row) for row in Z),p)
                assert rank(g,p)<=N*rank(f,p)
                total+=1
    return total

def exhaustive(p,N):
    P,degrees=canonical(p,N)
    assert P[0]!=0 and P[-1]==1
    witness=symmetric_lift(P)
    d=len(P)-1;L=max(map(abs,witness))
    assert L==(d+1)//2
    counts=[]
    for m in range(1,N+1):
        cnt=0
        for X in matrices(p,m):
            Y=inv(X,p)
            if Y is None: continue
            cnt+=1
            assert polynomial_matrix(P,X,p)==zero(m)
            assert Laurent_eval(witness,X,Y,p)==zero(m)
        counts.append(cnt)
    # For some m=N+1, the canonical polynomial does not vanish:
    found=False
    for X in matrices(p,N+1):
        Y=inv(X,p)
        if Y is None:continue
        if Laurent_eval(witness,X,Y,p)!=zero(N+1):
            found=True
            break
    assert found
    return {'prime_field':p,'N':N,'D':d,'min_degree':L,
            'tested_invertibles':counts,'next_size_separation':True,'irreducible_counts':degrees}


if __name__=='__main__':
    import json
    # Small prime fields, including all invertible 3x3 binary matrices.
    rows=[exhaustive(2,1),exhaustive(2,2),exhaustive(3,1),exhaustive(3,2)]
    pair_checks={str((2,2)):explicit_bounded_rank_check(2,2),str((3,1)):explicit_bounded_rank_check(3,1),str((3,2)):explicit_bounded_rank_check(3,2)}
    # For GF(2), N=3, show exact P3 and its degree, without a 4x4 census.
    P3,deg3=canonical(2,3)
    assert len(P3)-1==11 and deg3==[(1,1),(2,1),(3,2)]
    # Explicit size-three binary counterexample for g=x^2+x+y+y^2.
    P2,_=canonical(2,2)
    assert P2==[1,1,0,1,1],P2
    X=((0,0,1),(1,0,1),(0,1,0))
    Xi=inv(X,2)
    assert Xi is not None
    assert Laurent_eval({2:1,1:1,-1:1,-2:1},X,Xi,2)!=zero(3)
    print(json.dumps({'checked':rows,'GF2_N3_degree':len(P3)-1,
                      'explicit_binary_degree_two_counterexample':True,
                      'full_matrix_pair_checks':pair_checks,
                      'status':'VERIFY_OK'},sort_keys=True))
