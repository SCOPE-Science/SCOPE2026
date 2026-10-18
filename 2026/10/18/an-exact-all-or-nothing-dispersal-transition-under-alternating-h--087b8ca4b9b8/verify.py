"""Exact checks for a two-patch seasonal dispersal classification.

Python 3, standard library only. All matrix identities and the boundary
positive-definiteness certificate are checked over rational numbers.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from itertools import product


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def mat(d,c,B,b):
    P = ((1-d,c*d),(c*d,1-d))
    D1 = ((B,F(0)),(F(0),b))
    D2 = ((b,F(0)),(F(0),B))
    J = ((F(0),F(1)),(F(1),F(0)))
    M1=mm(P,D1)
    M2=mm(P,D2)
    return M1,M2,mm(J,M1)


def lam(d,c,B,b):
    with localcontext() as ctx:
        ctx.prec=70
        cv=lambda z:Decimal(z.numerator)/Decimal(z.denominator)
        D,C,BB,bb=map(cv,(d,c,B,b))
        return (C*D*(BB+bb) + (C*C*D*D*(BB-bb)**2+4*BB*bb*(1-D)**2).sqrt())/2


def check():
    matrices=0
    for B,b,c,d in product((F(2),F(4),F(9)),(F(1),F(3,2)),(F(1,5),F(1,2),F(1)),(F(0),F(1,7),F(3,5),F(1))):
        if B<=b:continue
        M1,M2,H=mat(d,c,B,b)
        assert mm(M2,M1)==mm(H,H)
        assert H[0][0]+H[1][1] == c*d*(B+b)
        # The discriminant of the quadratic characteristic polynomial.
        disc=(H[0][0]-H[1][1])**2+4*H[0][1]*H[1][0]
        assert disc==c*c*d*d*(B-b)**2 + 4*B*b*(1-d)**2
        matrices+=1
    B,b,c=F(4),F(1),F(1,2)
    exact_witness=0
    for k in range(1,100):
        d=F(k,100)
        # Symmetric similarity has diag (2d,d/2), offdiag 2(1-d).
        assert F(2)-F(2)*d>0
        determinant=(F(2)-F(2)*d)*(F(2)-d/2)-4*(1-d)**2
        assert determinant==3*d*(1-d)>0
        exact_witness+=1
    comparisons=0
    with localcontext() as ctx:
        ctx.prec=70
        for c in (F(1,4),F(1,2),F(3,4),F(1)):
            e0=lam(F(0),c,B,b)
            e1=lam(F(1),c,B,b)
            best=max(e0,e1)
            for k in range(1,100):
                assert lam(F(k,100),c,B,b)<best
                comparisons+=1
            assert (e0>e1 if c<F(1,2) else e1>e0 if c>F(1,2) else e1==e0)
    print('PASS: exact matrix identities:', matrices)
    print('PASS: exact rational interior positive-definiteness:',exact_witness)
    print('PASS: 70-digit numerical endpoint dominance:',comparisons)

if __name__=='__main__':
    check()
