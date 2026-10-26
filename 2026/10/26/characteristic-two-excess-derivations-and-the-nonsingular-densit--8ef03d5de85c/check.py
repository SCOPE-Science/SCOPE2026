"""Reproducible finite-field checks for derivations of Q_{2m}.

No external packages are needed. Every bracket and derivation identity is computed
from the defining multiplication table, not from a saved certificate.
"""
from itertools import product
from random import Random


def bracket(n, i, j):
    """Coefficient dictionary of [e_i,e_j], zero-based indices."""
    if i == j: return {}
    if i > j:
        return {k: -v for k, v in bracket(n,j,i).items()}
    if i == 0 and 1 <= j <= n-2: return {j+1:1}
    if 1 <= i <= n//2-1 and j == n-1-i:
        return {n-1:(-1)**(i+2)}
    return {}


def br(n, x, y, p):
    z=[0]*n
    for i,xi in enumerate(x):
        if xi:
            for j,yj in enumerate(y):
                if yj:
                    for k,c in bracket(n,i,j).items():
                        z[k]=(z[k]+xi*yj*c)%p
    return z


def basis(n,i):
    return [int(i==j) for j in range(n)]


def matrix_from_AB(n,A,B,p):
    cols=[A,B]
    for j in range(2,n):
        cols.append([(x+y)%p for x,y in zip(br(n,A,basis(n,j-1),p),br(n,basis(n,0),cols[j-1],p))])
    return cols


def eqholds(n,cols,p):
    for i in range(n):
        for j in range(i+1,n):
            lhs=br(n,cols[i],basis(n,j),p)
            rhs=br(n,basis(n,i),cols[j],p)
            z=br(n,basis(n,i),basis(n,j),p)
            der=[sum(z[k]*cols[k][u] for k in range(n))%p for u in range(n)]
            if der!=[(lhs[u]+rhs[u])%p for u in range(n)]:
                return False,(i,j)
    return True,None


def detmod(cols,p):
    a=[[cols[j][i]%p for j in range(len(cols))] for i in range(len(cols))]
    n=len(cols); r=1
    for j in range(n):
        pivot=next((k for k in range(j,n) if a[k][j]),None)
        if pivot is None:return 0
        if pivot!=j:
            a[j],a[pivot]=a[pivot],a[j]
            r=-r
        v=a[j][j];r=r*v%p; inv=pow(v,-1,p)
        for k in range(j+1,n):
            u=a[k][j]*inv%p
            if u:
                for s in range(j,n):a[k][s]=(a[k][s]-u*a[j][s])%p
    return r%p


def formula_det(n,A,B,p):
    a=A[0];d=B[1]
    v=a*d
    for j in range(3,n):v*=((j-2)*a+d)
    v*=((n-3)*a+2*d)
    return v%p


def legal_AB(n,A,B,p):
    if B[0]%p:return False
    if (A[1]-A[0]+B[1])%p:return False
    if p!=2 and any(B[j]%p for j in range(3,n-2,2)): return False
    return True


def rows(n):
    # Matrix of all derivation conditions with unknowns D(e_i)_j.
    res=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(n):
                row=[0]*(n*n)
                for t,c in bracket(n,i,j).items():row[t*n+k]+=c
                for t in range(n):
                    row[i*n+t]-=bracket(n,t,j).get(k,0)
                    row[j*n+t]-=bracket(n,i,t).get(k,0)
                if any(row):res.append(row)
    return res


def rank_p(matrix,p):
    A=[[v%p for v in row] for row in matrix]
    if not A:return 0
    m=len(A);n=len(A[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if A[i][j]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][j],-1,p)
        for k in range(r,j+n):
            if k<n:A[r][k]=A[r][k]*inv%p
        for i in range(r+1,m):
            f=A[i][j]
            if f:
                for k in range(j,n): A[i][k]=(A[i][k]-f*A[r][k])%p
        r+=1
        if r==m:break
    return r


def predicted_dim(n,p):
    return 2*n-2 if p==2 else 3*n//2


def random_AB(n,p,rng):
    B=[0]+[rng.randrange(p) for j in range(1,n)]
    if p!=2:
        for j in range(3,n-2,2):B[j]=0
    A=[rng.randrange(p) for _ in range(n)]
    A[1]=(A[0]-B[1])%p
    return A,B


def main():
    rng=Random(9616)
    for n in [6,8,10,12]:
        # Jacobi is checked directly for the defining bracket.
        for p in [2,3,5,7]:
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        E=[basis(n,s) for s in (i,j,k)]
                        jac=[(x+y+z)%p for x,y,z in zip(br(n,E[0],br(n,E[1],E[2],p),p),br(n,E[1],br(n,E[2],E[0],p),p),br(n,E[2],br(n,E[0],E[1],p),p))]
                        assert not any(jac),(n,p,i,j,k,jac)
            d=n*n-rank_p(rows(n),p)
            assert d==predicted_dim(n,p),(n,p,d)
            for t in range(50):
                A,B=random_AB(n,p,rng)
                assert legal_AB(n,A,B,p)
                cols=matrix_from_AB(n,A,B,p)
                assert eqholds(n,cols,p)==(True,None),(n,p,A,B)
                assert detmod(cols,p)==formula_det(n,A,B,p),(n,p,A,B)
            print('dimension_and_torsion_ok',n,p,d)
    # The first nonstandard characteristic-two example: all 2^10 derivations.
    n=6;p=2; good=0
    for vals in product(range(2),repeat=10):
        # A_1,A_3,A_4,A_5,A_6 and B_2,...,B_6 are free.
        a=vals[:5];b=vals[5:]
        A=[a[0],(a[0]-b[0])%2,*a[1:]]
        B=[0,*b]
        cols=matrix_from_AB(n,A,B,2)
        assert eqholds(n,cols,2)==(True,None)
        good += int(detmod(cols,2)!=0)
    assert good==0
    print('Q_FILIFORM_DERIVATIONS_OK')

if __name__=='__main__':main()
