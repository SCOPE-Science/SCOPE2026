#!/usr/bin/env python3
"""Reproduce rational identities and bracket the optimizer; Python 3 standard library only."""
from fractions import Fraction as F
from decimal import Decimal, localcontext


def matmul(A, B):
    return [[sum((x*y for x,y in zip(row,col)), F(0)) for col in zip(*B)] for row in A]


def transpose(A):
    return [list(row) for row in zip(*A)]


def add(A,B):
    return [[a+b for a,b in zip(row1,row2)] for row1,row2 in zip(A,B)]


def scale(A,s):
    return [[s*v for v in row] for row in A]


def pair_projection(n,j):
    M=[[F(i==k) for k in range(n)] for i in range(n)]
    for k,l,s in [(j,j,F(-1,2)),(j+1,j+1,F(-1,2)),(j,j+1,F(1,2)),(j+1,j,F(1,2))]:
        M[k][l]+=s
    return M


def one(ps):
    n=len(ps)+1
    return sum_mats([scale(pair_projection(n,j),p) for j,p in enumerate(ps)],n)


def sum_mats(xs,n):
    r=[[F(0) for _ in range(n)] for _ in range(n)]
    for x in xs:r=add(r,x)
    return r


def two(ps):
    n=len(ps)+1
    P=[pair_projection(n,j) for j in range(n-1)]
    return sum_mats([scale(matmul(matmul(P[i],P[j]),P[i]),pi*pj)
                     for i,pi in enumerate(ps) for j,pj in enumerate(ps)],n)


def quad(v,M,w):
    return sum((v[i]*M[i][j]*w[j] for i in range(len(v)) for j in range(len(w))),F(0))


def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]


def q(a):
    return 116*a**4+68*a**3+5*a*a-48*a+16


def qprime(a):
    return 464*a**3+204*a*a+10*a-48


def ddec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)


def fd(a):
    return (ddec(20*a-3)/8 + ddec(qprime(a))/(16*ddec(q(a)).sqrt()))


def derivative_sign(a):
    """Exact sign of 16 sqrt(Q(a)) f'(a) = 2(20a-3)sqrt(Q(a))+Q'(a)."""
    b=2*(20*a-3)
    c=qprime(a)
    qq=q(a)
    assert qq>0
    if b>=0 and c>=0:
        return 1 if b or c else 0
    if b<=0 and c<=0:
        return -1 if b or c else 0
    z=b*b*qq-c*c
    if not z:
        return 0
    if b>0:
        return 1 if z>0 else -1
    return -1 if z>0 else 1

def main():
    # Orthogonal projection, symmetry and full P4 two-step block identities.
    ss=[F(1,2),F(-1,2),F(-1,2),F(1,2)]
    uu=[F(1),F(0),F(0),F(-1)]  # norm sqrt(2)
    vv=[F(0),F(1),F(-1),F(0)]  # norm sqrt(2)
    P=[pair_projection(4,j) for j in range(3)]
    I=[[F(i==j) for j in range(4)] for i in range(4)]
    for T in P:
        assert matmul(T,T)==T and transpose(T)==T
    for a in [F(0),F(1,13),F(1,4),F(3,10),F(2,5),F(1,2)]:
        M=two([a,1-2*a,a])
        assert quad(ss,M,ss)==(6*a*a-9*a+4)/4
        assert quad(uu,M,uu)/2==(6*a*a-9*a+8)/8
        assert quad(uu,M,vv)/2==a*(10*a+1)/8
        assert quad(vv,M,vv)/2==a*(14*a+3)/8
        assert quad(ss,M,uu)==0 and quad(ss,M,vv)==0
        assert quad(uu,M,vv)==quad(vv,M,uu)
        for d in [F(0),F(1,17),F(2,19)]:
            b=two([a+d,1-2*a,a-d]); c=two([a-d,1-2*a,a+d])
            H=scale(add(add(P[0],P[2]),scale(matmul(P[0],P[2]),-2)),F(1))
            assert scale(add(b,c),F(1,2))==add(M,scale(H,d*d))
            assert H==matmul(add(P[0],scale(P[2],-1)),add(P[0],scale(P[2],-1)))
        # Expected matrix fixes constants, although they are excluded from the norm.
        ones=[F(1)]*4
        assert [sum(row) for row in M]==ones
    # One-step symmetric gap at (3/10, 2/5, 3/10).
    p=[F(3,10),F(2,5),F(3,10)]
    x=[F(-3),F(-1),F(1),F(3)]
    M=one(p)
    assert matmul(M,[[z] for z in x])==[[F(9,10)*z] for z in x]
    # P3 two-step trace and determinant, expressed in t=p(1-p).
    u=[F(1),F(-1),F(0)]
    v=[F(1),F(1),F(-2)]
    for p in [F(0),F(1,7),F(1,3),F(1,2),F(4,5),F(1)]:
        t=p*(1-p)
        M=two([p,1-p]);
        # u/sqrt(2),v/sqrt(6): avoid irrational arithmetic in characteristic polynomial.
        a11=quad(u,M,u)/2; a22=quad(v,M,v)/6
        od_prod=quad(u,M,v)*quad(v,M,u)/12
        assert a11+a22==1-F(3,2)*t
        assert a11*a22-od_prod==F(3,16)*t+F(27,64)*t*t
    assert q(F(3,10))==F(3016,625)  # sqrt(Q)/8 corresponds to sqrt(754)/100
    with localcontext() as ctx:
        ctx.prec=75
        lo=F(302839075823,10**12); hi=F(302839075824,10**12)
        assert derivative_sign(lo)==-1 and derivative_sign(hi)==1
        assert derivative_sign(F(3,10))==-1
        assert fd(lo)<0<fd(hi)
        assert fd(F(3,10))<0
        assert fd(F(0))==Decimal(-9)/8
        assert fd(F(1,2))==Decimal(9)/4
        # Strict convexity is proved analytically in RESULT.md, not by this sample.
        amin=(ddec(lo)+ddec(hi))/2
        Q=116*amin**4+68*amin**3+5*amin**2-48*amin+16
        val=Decimal(1)/2+(10*amin**2-3*amin+Q.sqrt())/8
        assert Decimal('0.77455285319')<val<Decimal('0.77455285320')
    print('VERIFY_OK: exact P4 blocks and symmetrization, exact P3 determinants, optimizer bracket')

if __name__=='__main__':main()
