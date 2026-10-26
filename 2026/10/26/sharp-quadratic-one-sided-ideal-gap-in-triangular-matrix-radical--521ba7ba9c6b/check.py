#!/usr/bin/env python3
"""Independent finite-field enumeration of principal-ideal asymmetry in triangular algebras.

No third-party packages are needed.  Exhaustive tests are finite sanity checks;
the accompanying proof supplies the unrestricted-field argument.
"""
from itertools import product


def add(a,b,q):
    return a^b if q==4 else (a+b)%q


def neg(a,q):
    return a if q==4 else (-a)%q


def mul(a,b,q):
    if q!=4: return (a*b)%q
    if not (a and b): return 0
    # GF(4) = F_2[z]/(z^2+z+1), integer coefficients in basis {1,z}.
    t=(a&1)*(b&1)
    u=((a&1)*((b>>1)&1))^(((a>>1)&1)*(b&1))
    v=((a>>1)&1)*((b>>1)&1)
    return (t^v) | ((u^v)<<1)


def inv(a,q):
    assert a
    for i in range(1,q):
        if mul(a,i,q)==1:return i
    raise AssertionError('field inverse missing')


def mat_rank(rows,q):
    if not rows:return 0
    m=[list(row) for row in rows]
    h=len(m); w=len(m[0]); r=0
    for j in range(w):
        p=next((i for i in range(r,h) if m[i][j]),None)
        if p is None:continue
        m[r],m[p]=m[p],m[r]
        z=inv(m[r][j],q)
        m[r]=[mul(z,t,q) for t in m[r]]
        for k in range(r+1,h):
            if m[k][j]:
                a=m[k][j]
                m[k]=[add(m[k][c], neg(mul(a,m[r][c],q),q),q) for c in range(w)]
        r+=1
        if r==h:break
    return r


def decode(n, v):
    X=[[0]*n for _ in range(n)]
    for a,(i,j) in zip(v,((i,j) for i in range(n) for j in range(i+1,n))):
        X[i][j]=a
    return X


def principal_dimensions(X,q):
    n=len(X)
    a=sum(mat_rank([row[:j] for row in X[:j]],q) for j in range(1,n+1))
    b=sum(mat_rank([row[i:] for row in X[i:]],q) for i in range(n))
    return a,b


def direct_dimensions(X,q):
    n=len(X)
    upper=[(i,j) for i in range(n) for j in range(i,n)]
    v=[];w=[]
    for i,j in upper:
        # X*E_ij has column j equal to column i of X.
        v.append([X[a][i] if b==j else 0 for a,b in upper])
        # E_ij*X has row i equal to row j of X.
        w.append([X[j][b] if a==i else 0 for a,b in upper])
    return mat_rank(v,q),mat_rank(w,q)


def run():
    configurations=[(2,2),(2,3),(2,4),(2,5),(2,6),
                    (3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3),(5,4)]
    checked=0
    for q,n in configurations:
        expected_by_rank={}
        for r in range(n):
            m=r*(n-r-1)
            expected_by_rank[r]= (q-1)**r * q**(r*n-r*(r+1)//2-r)
        optimum=(n-1)**2//4
        seen_by_rank={r:set() for r in range(n)}
        positive={r:0 for r in range(n)}
        negative={r:0 for r in range(n)}
        count=0
        for v in product(range(q), repeat=n*(n-1)//2):
            X=decode(n,v)
            r=mat_rank(X,q)
            A,B=principal_dimensions(X,q)
            assert abs(A-B)<=r*(n-r-1),(q,n,v,r,A,B)
            seen_by_rank[r].add(A-B)
            if A-B==r*(n-r-1):
                positive[r]+=1
                cond=all(X[i][i+1]!=0 for i in range(r)) and all(
                    X[i][j]==0 for i in range(r,n) for j in range(i+1,n))
                assert cond,(q,n,v,r,'false positive extremizer')
            if B-A==r*(n-r-1):negative[r]+=1
            if n<=4 or (q==2 and n==5):
                assert direct_dimensions(X,q)==(A,B),(q,n,v,A,B)
            count+=1
        assert count==q**(n*(n-1)//2)
        for r in range(n):
            bound=r*(n-r-1)
            assert seen_by_rank[r]==set(range(-bound,bound+1)),(q,n,r,seen_by_rank[r])
            assert positive[r]==expected_by_rank[r],(q,n,r,positive[r],expected_by_rank[r])
            assert negative[r]==expected_by_rank[r],(q,n,r,negative[r],expected_by_rank[r])
        checked+=1
    print('TRIANGULAR_ONE_SIDED_GAP_OK',checked,'exhaustive field-and-size cases')

if __name__=='__main__':run()
