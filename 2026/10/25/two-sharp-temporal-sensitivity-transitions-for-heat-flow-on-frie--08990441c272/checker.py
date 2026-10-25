"""Exact-rational tests of the friendship-graph heat-generator norm formula.

Run with Python 3. The finite tests supplement, not replace, the proof in RESULT.md.
"""
from fractions import Fraction as F


def mul(a,b):
    n=len(a)
    return [[sum(a[i][r]*b[r][j] for r in range(n)) for j in range(n)] for i in range(n)]


def identity(n):
    return [[F(i==j) for j in range(n)] for i in range(n)]


def diagadd(a,b,c=1):
    return [[a[i][j]+c*b[i][j] for j in range(len(a))] for i in range(len(a))]


def scale(a,c):
    return [[c*x for x in row] for row in a]


def projector_from_L(L,eigenvalue,levels):
    n=len(L)
    product=identity(n)
    for mu in levels:
        if mu == eigenvalue:
            continue
        product=mul(product,diagadd(L,scale(identity(n),-mu)))
        product=scale(product,F(1,eigenvalue-mu))
    return product


def friendship_laplacian(k):
    n=2*k+1
    A=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(k):
        u,v=2*i+1,2*i+2
        for a,b in ((0,u),(0,v),(u,v)):
            A[a][b]=A[b][a]=F(1)
    return [[(sum(A[i]) if i==j else F(0))-A[i][j]
             for j in range(n)] for i in range(n)]


def theoretical(k,z):
    u=z**(2*k+1)
    h=4*k*u
    neg=3*z**3+F(k-1,k)*z+u/k
    pos=F(2*(k-1),k)*z+F(2,k)*u
    return max(h,neg,pos),h,neg,pos


def test():
    assertions=0
    for k in range(2,11):
        n=2*k+1
        L=friendship_laplacian(k)
        levels=(0,1,3,2*k+1)
        projectors={level:projector_from_L(L,level,levels)
                    for level in levels}
        accum=[[sum(projectors[level][i][j] for level in levels)
                for j in range(n)] for i in range(n)]
        assert accum==identity(n)
        assertions+=n*n
        for ell in levels:
            P=projectors[ell]
            LP=mul(L,P)
            assert LP==scale(P,ell)
            assertions+=n*n
        for z in (F(1),F(1,4),F(1,2),F(2,3),F(3,4),F(9,10)):
            T=[[sum(F(ell)*z**ell*projectors[ell][i][j]
                    for ell in levels) for j in range(n)] for i in range(n)]
            tnorm,hub,negative,positive=theoretical(k,z)
            actual=max(sum(abs(v) for v in row) for row in T)
            assert actual==tnorm,(k,z,actual,tnorm)
            assertions+=1
            assert sum(abs(v) for v in T[0])==hub
            assertions+=1
            leafsum=sum(abs(v) for v in T[1])
            assert leafsum==max(negative,positive)
            assertions+=1
            assert all(sum(abs(v) for v in row)==leafsum for row in T[1:])
            assertions+=n-1
            i=max(range(n),key=lambda i:sum(abs(v) for v in T[i]))
            signs=[F(1) if a>=0 else F(-1) for a in T[i]]
            assert abs(sum(x*y for x,y in zip(T[i],signs)))==tnorm
            assertions+=1
            # Reconstruct all entry classes independently from the spectral polynomial.
            a=z; b=3*z**3; u=z**(2*k+1)
            h_diag=2*k*u
            h_other=-u
            d=F(k-1,2*k)*a+F(1,2)*b+F(1,2*k)*u
            partner=F(k-1,2*k)*a-F(1,2)*b+F(1,2*k)*u
            off=F(1,2*k)*(u-a)
            for ii in range(n):
                for jj in range(n):
                    if ii==0:
                        expected=h_diag if jj==0 else h_other
                    elif jj==0:
                        expected=h_other
                    elif ii==jj:
                        expected=d
                    elif (ii-1)//2==(jj-1)//2:
                        expected=partner
                    else:
                        expected=off
                    assert T[ii][jj]==expected,(k,z,ii,jj)
                    assertions+=1
    print(f"PASS: {assertions} exact-rational assertions; k=2..10 and six rational heat parameters each.")


if __name__=='__main__':
    test()
