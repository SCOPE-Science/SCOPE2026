"""Finite checks for mutual-annihilator representation geometry.

The matrix equations and tangent Jacobians are independently constructed.
This script is an auxiliary finite check, not a proof for all fields/tuple lengths.
"""
from itertools import product


def mul(A, B, p, n=3):
    return tuple(sum(A[3*i+k]*B[3*k+j] for k in range(n)) % p
                 for i in range(n) for j in range(n))


def rank_mod(rows, p):
    a = [list(map(lambda x: x % p, row)) for row in rows]
    if not a: return 0
    ncol = len(a[0]); piv=0
    for col in range(ncol):
        k=next((i for i in range(piv,len(a)) if a[i][col]),None)
        if k is None: continue
        a[piv],a[k]=a[k],a[piv]
        inv=pow(a[piv][col],-1,p)
        a[piv]=[(z*inv)%p for z in a[piv]]
        for j in range(piv+1,len(a)):
            if a[j][col]:
                fac=a[j][col]
                a[j]=[(a[j][c]-fac*a[piv][c])%p for c in range(ncol)]
        piv+=1
        if piv==len(a):break
    return piv


def jacobian_rank(X,p):
    r=len(X)
    rows=[]
    for i in range(r):
        for j in range(r):
            for a in range(3):
                for b in range(3):
                    row=[0]*(9*r)
                    for k in range(3):
                        row[9*j+3*k+b]+=X[i][3*a+k]
                        row[9*i+3*a+k]+=X[j][3*k+b]
                    rows.append(row)
    return rank_mod(rows,p)


def ei(a,b):
    M=[0]*9;M[3*a+b]=1;return tuple(M)


def geom_count(q,r):
    s=q*q+q+1
    C=1+s*(q**(2*r)-1)
    Z=1+s*(q+1)*(q**r-1)
    return 2*C-Z, Z, C


def brute_pairs(q):
    zero=(0,)*9
    squares=[]
    for M in product(range(q),repeat=9):
        if mul(M,M,q)==zero: squares.append(M)
    total=0
    for A in squares:
        for B in squares:
            if mul(A,B,q)==zero and mul(B,A,q)==zero:
                total+=1
    return total,len(squares)


def main():
    checks=0
    for q in (2,3):
        total,sq=brute_pairs(q)
        expected=geom_count(q,2)[0]
        assert total==expected,(q,total,expected)
        assert sq==1+(q**3-1)*(q**2-1)//(q-1),(q,sq)
        checks+=2
        print('field',q,'square_zero',sq,'mutually_annihilating_pairs',total)
    for p in (2,3,5,7):
        for r in (2,3,4,5):
            O=[(0,)*9 for _ in range(r)]
            canonical_overlap=list(O); canonical_overlap[0]=ei(0,2)
            canonical_component=list(O);canonical_component[0]=ei(0,1);canonical_component[1]=ei(0,2)
            canonical_transpose=list(O);canonical_transpose[0]=ei(0,2);canonical_transpose[1]=ei(1,2)
            for typ,XX,want in [('intersection',canonical_overlap,4*r+1),('first_component',canonical_component,2*r+2),('second_component',canonical_transpose,2*r+2),('origin',O,9*r)]:
                dim=9*r-jacobian_rank(XX,p)
                assert dim==want,(p,r,typ,dim,want)
                checks+=1
    print('VERIFY_OK_RADICAL_SQUARE_ZERO_REP_SCHEME',checks)

if __name__=='__main__':main()
