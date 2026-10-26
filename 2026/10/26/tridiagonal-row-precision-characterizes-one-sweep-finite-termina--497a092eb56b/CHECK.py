"""Exact-rational checks of the oblique-Kaczmarz finite-sweep theorem.

No random inputs, network access, or third-party dependencies.
Checks are illustrative; the theorem's universal claims use the paper proof.
"""
from fractions import Fraction as F


def transpose(A):
    return list(map(list, zip(*A)))


def mul(A, B):
    return [[sum((x*y for x,y in zip(row,col)),F(0)) for col in transpose(B)] for row in A]


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def dot(x,y):
    return sum((a*b for a,b in zip(x,y)),F(0))


def inv(A):
    n=len(A)
    B=[list(A[i])+identity(n)[i] for i in range(n)]
    for j in range(n):
        p=next(i for i in range(j,n) if B[i][j])
        B[j],B[p]=B[p],B[j]
        z=B[j][j]
        B[j]=[x/z for x in B[j]]
        for i in range(n):
            if i!=j:
                m=B[i][j]
                B[i]=[x-m*y for x,y in zip(B[i],B[j])]
    return [row[n:] for row in B]


def sweep(A):
    n=len(A)
    assert all(len(row)==n for row in A)
    I=identity(n)
    T=I
    last=None
    for i,row in enumerate(A):
        if i==0:
            w=row
        else:
            c=dot(row,last)/dot(last,last)
            w=[x-c*y for x,y in zip(row,last)]
        denominator=dot(row,w)
        assert denominator==dot(w,w)>0
        P=[[I[j][k]-w[j]*row[k]/denominator for k in range(n)] for j in range(n)]
        T=mul(P,T)
        last=row
    return T


def gram(A):
    return mul(A,transpose(A))


def tridiagonal(A):
    n=len(A)
    return all(A[i][j]==0 for i in range(n) for j in range(n) if abs(i-j)>=2)


def zero_matrix(A):
    return all(x==0 for row in A for x in row)


def norm_rank_one_square(A):
    assert len(A)==3
    assert all(len(row)==3 for row in A)
    return sum((x*x for row in A for x in row),F(0))


def check(A):
    G=gram(A)
    J=inv(G)
    T=sweep(A)
    assert zero_matrix(T)==tridiagonal(J)
    return (G,J,T)


count=0
for n in range(2,9):
    for rho in [F(1,7),F(-2,5),F(3,4)]:
        A=[]
        for i in range(n):
            if i==0:
                A.append([F(int(j==0)) for j in range(n)])
            else:
                A.append([rho*A[-1][j]+F(int(j==i)) for j in range(n)])
        G,J,T=check(A)
        assert zero_matrix(T)
        assert tridiagonal(J)
        count+=1

for u in [F(0),F(1,3),F(-2,5),F(4,5)]:
    for v in [F(0),F(1,4),F(-3,8)]:
        for w in [F(0),F(1,7),F(-2,7),F(3,5)]:
            A=[[F(1),F(0),F(0)],[u,F(1),F(0)],[v,w,F(1)]]
            G,J,T=check(A)
            equality=J[0][2]**2/(J[0][0]*J[2][2])
            assert norm_rank_one_square(T)==equality
            assert F(0)<=equality<F(1)
            count+=1

A=[[F(1),F(0),F(0)],[F(1,2),F(1),F(0)],[F(1,5),F(1,3),F(1)]]
G,J,T=check(A)
assert norm_rank_one_square(T)==J[0][2]**2/(J[0][0]*J[2][2])>0
print('PASS: %d exact-rational Gram/precision/sweep and rank-one norm checks' % count)
print('Non-Markov example squared sweep norm:',norm_rank_one_square(T))
print('Non-Markov example Gram precision corner:',J[0][2])
