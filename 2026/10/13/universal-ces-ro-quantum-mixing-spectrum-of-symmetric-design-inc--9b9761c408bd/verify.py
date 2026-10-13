"""Exact checks for the incidence-design quantum average-mixing theorem.

Python standard library only. Does not constitute an infinite proof.
"""
from fractions import Fraction as F


def zeros(m, n):
    return [[F(0) for _ in range(n)] for _ in range(m)]


def ident(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def matmul(A, B):
    bt = list(zip(*B))
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in bt]
            for row in A]


def add(A, B):
    return [[a+b for a,b in zip(r,s)] for r,s in zip(A,B)]


def sub(A, B):
    return [[a-b for a,b in zip(r,s)] for r,s in zip(A,B)]


def scale(a, A):
    return [[a*x for x in row] for row in A]


def schur(A, B):
    return [[a*b for a,b in zip(r,s)] for r,s in zip(A,B)]


def trans(A):
    return [list(x) for x in zip(*A)]


def block(A, B, C, D):
    return [x+y for x,y in zip(A,B)] + [x+y for x,y in zip(C,D)]


def rank(A):
    T=[row[:] for row in A]
    n=len(T)
    m=len(T[0])
    piv=0
    for col in range(m):
        pivot=next((j for j in range(piv,n) if T[j][col]),None)
        if pivot is None: continue
        T[piv],T[pivot]=T[pivot],T[piv]
        factor=T[piv][col]
        T[piv]=[x/factor for x in T[piv]]
        for j in range(piv+1,n):
            if T[j][col]:
                f=T[j][col]
                T[j]=[a-f*b for a,b in zip(T[j],T[piv])]
        piv+=1
        if piv==n:break
    return piv


def cyclic(v, diffs):
    D=set(diffs)
    return [[F(int((j-i)%v in D)) for j in range(v)] for i in range(v)]


def exercise(v, D):
    B=cyclic(v,D)
    k=int(sum(B[0]))
    BT=trans(B)
    BB=matmul(B,BT)
    lam=int(BB[0][1])
    s2=k-lam
    assert 2<=k<=v-1 and s2>=1
    J=[[F(1) for _ in range(v)] for _ in range(v)]
    I=ident(v)
    C=sub(I,scale(F(1,v),J))
    E=scale(F(1,v),J)
    Des=sub(B,scale(F(k,v),J))
    assert all(sum(r)==k for r in B)
    assert all(sum(r)==k for r in BT)
    assert BB == add(scale(F(s2),I),scale(F(lam),J))
    assert matmul(BT,B)==BB
    assert matmul(Des,trans(Des))==scale(F(s2),C)
    assert matmul(trans(Des),Des)==scale(F(s2),C)
    assert matmul(C,Des)==Des and matmul(Des,C)==Des

    # The four adjacency spectral idempotents are (K +/- L)/2,
    # (Q +/- R)/2 with R having off-diagonal D/s.
    # The plus/minus Schur-square sums depend on R only through R circ R.
    Z=zeros(v,v)
    K=block(E,Z,Z,E)
    L=block(Z,E,E,Z)
    Q=block(C,Z,Z,C)
    Rsq=block(Z,scale(F(1,s2),schur(Des,Des)),
               scale(F(1,s2),schur(trans(Des),trans(Des))),Z)
    assert matmul(K,K)==K and matmul(L,L)==K
    assert matmul(Q,Q)==Q
    assert matmul(K,Q)==zeros(2*v,2*v)
    assert matmul(L,Q)==zeros(2*v,2*v)
    M=scale(F(1,2),add(add(schur(K,K),schur(L,L)),add(schur(Q,Q),Rsq)))

    c=F(v-2,2*v)
    alpha=F(v-2*k,2*v*s2)
    beta=F(s2+k*k,2*s2*v*v)
    X=add(scale(c,I),scale(F(1,v*v),J))
    Y=add(scale(alpha,B),scale(beta,J))
    closed=block(X,Y,trans(Y),X)
    assert M==closed
    assert all(sum(row)==1 for row in M)
    assert all(sum(M[i][j]*z[j] for j in range(2*v))==0
               for i in range(2*v)
               for z in [[F(1)]*v+[F(-1)]*v])

    # Independent exact check of the eigenvalue polynomial (without radicals).
    mI=ident(2*v)
    inner=sub(matmul(sub(M,scale(c,mI)),sub(M,scale(c,mI))),
              scale(F((v-2*k)**2,4*v*v*s2),mI))
    polynomial=matmul(matmul(sub(M,mI),M),inner)
    assert polynomial==zeros(2*v,2*v)
    actual_rank=rank(M)
    assert actual_rank==(v if k==v-1 else 2*v-1)
    if k<=v-2:
        assert (v-2)**2*s2 > (v-2*k)**2
    if k==v-1:
        P=sub(J,B)
        for j in range(v):
            z=[F(int(i==j)) for i in range(v)] + [-P[j][i] for i in range(v)]
            assert all(sum(M[i][h]*z[h] for h in range(2*v))==0 for i in range(2*v))
    return {'v':v,'k':k,'lambda':lam,'rank':actual_rank,
            'exact_entries':4*v*v}


def main():
    cases=[(3,[1,2]),(4,[1,2,3]),
           (7,[0,1,3]),(11,[1,3,4,5,9]),(13,[0,1,3,9])]
    got=[exercise(*x) for x in cases]
    print('VERIFY_OK exact_designs=%s exact_matrix_entries=%s ranks=%s' % (
        len(got),sum(x['exact_entries'] for x in got),
        ','.join('%s:%s'%(x['v'],x['rank']) for x in got)))


if __name__=='__main__':
    main()
