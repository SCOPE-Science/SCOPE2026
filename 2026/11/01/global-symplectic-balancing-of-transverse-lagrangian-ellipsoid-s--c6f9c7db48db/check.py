"""Exact rational consistency checks for Lagrangian ellipsoid-sum balancing.
Run with Python 3. No external packages required.
The universal analytic inequality is proved in RESULT.md, not by this finite test.
"""
from fractions import Fraction as Q
from itertools import product

def mul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def tr(A):
    return [list(row) for row in zip(*A)]
def add(A,B):
    return [[a+b for a,b in zip(x,y)] for x,y in zip(A,B)]
def block(A,B,C,D):
    return [a+b for a,b in zip(A,B)]+[c+d for c,d in zip(C,D)]
def zero(n): return [[Q(0) for _ in range(n)] for __ in range(n)]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def neg(A): return [[-x for x in row] for row in A]
def gram(A): return mul(tr(A),A)
def quad(A,x): return mul([x],mul(A,[[z] for z in x]))[0][0]
def equal(A,B): return A==B

def test(n):
    I,Z=eye(n),zero(n)
    J=block(Z,I,neg(I),Z)
    # Use invertible rational shear L, diagonal scaling A, with B=L^t L A.
    L=eye(n)
    for i in range(n-1): L[i][i+1]=Q(i+1, i+2)
    A=eye(n)
    for i in range(n): A[i][i]=Q(i+2, i+1)
    # Invert upper bidiagonal L by exact Gaussian elimination.
    aug=[row[:] + ir[:] for row,ir in zip(L,I)]
    for i in range(n):
        t=aug[i][i]
        aug[i]=[v/t for v in aug[i]]
        for j in range(n):
            if i!=j:
                t=aug[j][i]
                aug[j]=[u-t*v for u,v in zip(aug[j],aug[i])]
    Linv=[row[n:] for row in aug]
    B=mul(tr(L),mul(L,A))
    F=A+Z
    G=Z+B
    H=mul(tr(F),mul(J,G))
    assert mul(tr(F),mul(J,F))==Z
    assert mul(tr(G),mul(J,G))==Z
    assert H==mul(tr(A),B)
    T=block(L,Z,Z,tr(Linv))
    assert mul(tr(T),mul(J,T))==J
    E,D=mul(T,F),mul(T,G)
    assert gram(E)==H and gram(D)==H
    assert D==mul(neg(J),E)
    # An independent symplectic shear produces a non-minimizing test position.
    C=zero(n)
    for i in range(n): C[i][i]=Q(i+1)
    Sh=block(I,C,Z,I)
    assert mul(tr(Sh),mul(J,Sh))==J
    En,Dn=mul(Sh,E),mul(Sh,D)
    tests=0; strictly=0
    for entries in product((-2,-1,0,1,2),repeat=n):
        if not any(entries):continue
        v=[Q(x) for x in entries]
        h=quad(H,v)
        a2=quad(gram(En),v);b2=quad(gram(Dn),v)
        assert h>0 and a2*b2>=h*h
        # Norm AM-GM and symplectic Cauchy imply ||En v||+||Dn v|| >= 2 sqrt(h).
        if a2*b2>h*h or a2!=b2:strictly+=1
        tests+=1
    return tests,strictly

if __name__=='__main__':
    total=0
    for n in (1,2,3,4):
        count,strict=test(n)
        total+=count
        print(f'dimension {2*n}: {count} exact test vectors, {strict} strict shear cases')
    assert total==4+24+124+624
    print(f'PASS: {total} exact rational vector checks, Lagrangian Gram identities and balancing symplecticity')
