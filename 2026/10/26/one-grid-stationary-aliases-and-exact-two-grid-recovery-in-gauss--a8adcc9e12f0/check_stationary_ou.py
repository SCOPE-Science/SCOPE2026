"""Exact-rational checks for stationary Euler--Maruyama OU inverse identities.

Run: python check_stationary_ou.py
No external dependencies. Finite checks complement, not replace, the proof.
"""
from fractions import Fraction as F
from itertools import product


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]


def neg(A):
    return scale(A,-1)


def sub(A,B):
    return add(A,neg(B))


def scale(A,c):
    return [[F(c)*a for a in row] for row in A]


def mul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def trans(A):
    return [list(x) for x in zip(*A)]


def inv(A):
    n=len(A); M=[list(A[i])+eye(n)[i] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if M[i][j])
        M[j],M[k]=M[k],M[j]
        pivot=M[j][j]
        M[j]=[v/pivot for v in M[j]]
        for i in range(n):
            if i!=j:
                factor=M[i][j]
                M[i]=[x-factor*y for x,y in zip(M[i],M[j])]
    return [row[n:] for row in M]


def diag(v):
    return [[x if i==j else F(0) for j in range(len(v))] for i,x in enumerate(v)]


def precision(A,q,h):
    return scale(sub(A,scale(mul(A,A),F(h,2) if isinstance(h,int) else h/2)),F(1)/q)


def cov(A,q,h):
    return inv(precision(A,q,h))


def reconstruct(C1,C2,h1,h2):
    P1,P2=inv(C1),inv(C2)
    U=scale(sub(scale(P1,h2),scale(P2,h1)),F(1)/(h2-h1))
    V=scale(sub(P1,P2),F(2)/(h2-h1))
    A=mul(V,inv(U))
    q=sum(mul(V,mul(inv(U),inv(U)))[i][i] for i in range(len(A)))/len(A)
    return A,q,U,V


def stationary(A,q,h,C):
    n=len(A); B=sub(eye(n),scale(A,h))
    return C==add(mul(mul(B,C),trans(B)),scale(eye(n),2*q*h))


if __name__=='__main__':
    tests=0
    R=[[F(3,5),-F(4,5)],[F(4,5),F(3,5)]]
    h1,h2=F(1,2),F(1)
    for a,b in product([F(1,6),F(1,2),F(3,4),F(5,4)], repeat=2):
        for q in [F(1),F(3,7),F(7,3)]:
            A=mul(mul(R,diag([a,b])),trans(R))
            C1,C2=cov(A,q,h1),cov(A,q,h2)
            assert stationary(A,q,h1,C1) and stationary(A,q,h2,C2)
            Ahat,qhat,U,V=reconstruct(C1,C2,h1,h2)
            assert Ahat==A and qhat==q
            assert U==scale(A,F(1)/q)
            assert V==scale(mul(A,A),F(1)/q)
            tests+=1
    # All eight independent sign choices lead to the same stationary marginal.
    orig=[F(1,3),F(1,2),F(3,4)]
    C0=cov(diag(orig),F(1),F(1))
    distinct=set()
    for flips in product([0,1],repeat=3):
        a=[(2-x) if flip else x for x,flip in zip(orig,flips)]
        assert cov(diag(a),F(1),F(1))==C0
        distinct.add(tuple(a));tests+=1
    assert len(distinct)==8
    # A continuum of fibers over a repeated 2D stationary eigenvalue;
    # two explicit rational rotations provide distinct witnesses.
    target=scale(eye(2),F(8,3))
    for S in [eye(2),R,[[F(5,13),-F(12,13)],[F(12,13),F(5,13)]]]:
        A=mul(mul(S,diag([F(1,2),F(3,2)])),trans(S))
        assert cov(A,F(1),F(1))==target
        tests+=1
    # The reconstruction precision-error Lipschitz constant is attained.
    A=diag([F(1,2),F(3,4)]);q=F(1)
    P1=precision(A,q,h1);P2=precision(A,q,h2)
    eps=F(1,10000)
    Cp1=inv(add(P1,scale(eye(2),eps)))
    Cp2=inv(sub(P2,scale(eye(2),eps)))
    Phat=scale(sub(scale(inv(Cp1),h2),scale(inv(Cp2),h1)),F(1)/(h2-h1))
    assert sub(Phat,A)==scale(eye(2),eps*(h1+h2)/(h2-h1))
    tests+=1
    # Opposite rotational drifts have identical stationary marginals for all h.
    J=[[F(0),-F(1)],[F(1),F(0)]]
    k,w=F(1),F(1,3)
    Ap=add(scale(eye(2),k),scale(J,w))
    Am=sub(scale(eye(2),k),scale(J,w))
    for h in [F(1,10),F(1,2),F(1)]:
        c=F(1)/(k-h*(k*k+w*w)/2)
        C=scale(eye(2),c)
        assert stationary(Ap,F(1),h,C) and stationary(Am,F(1),h,C)
        tests+=1
    print(f'PASS: {tests} exact-rational configurations; universal conclusions require the analytical proof.')
