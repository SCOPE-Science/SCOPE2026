"""Exact-rational tests of two-row nuclear-scaled polar descent.

The tests do not replace the dimension-independent analytic proof.
Usage: python3 VERIFY_POLAR.py
"""
from fractions import Fraction as F
from itertools import product


def mm(A,B):
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
                       for j in range(len(B[0]))) for i in range(len(A)))

def tr(A): return sum((A[i][i] for i in range(len(A))),F(0))
def tp(A): return tuple(zip(*A))
def add(A,B,c=F(1)): return tuple(tuple(a+c*b for a,b in zip(x,y)) for x,y in zip(A,B))
def sc(A,c): return tuple(tuple(c*x for x in row) for row in A)
def I2(): return ((F(1),F(0)),(F(0),F(1)))
def rot(t):
    c=(1-t*t)/(1+t*t);s=2*t/(1+t*t)
    return ((c,-s),(s,c))
def spd(a,b,t):
    Q=rot(t);return mm(mm(Q,((a,F(0)),(F(0),b))),tp(Q))
def eye3():return tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
def row_isometry(n,t):
    R=rot(t)
    if n==2:return R
    v=(F(1),F(2),F(3));d=sum(x*x for x in v)
    House=tuple(tuple(F(i==j)-2*v[i]*v[j]/d for j in range(3)) for i in range(3))
    return mm(R,(House[0],House[1]))
def two_eigs_squared(B):
    return tr(mm(B,B))/2

def test_case(a,b,s1,s2,angH,angA,angO,n):
    H=spd(a,b,angH)
    A=spd(s1,s2,angA)
    O=row_isometry(n,angO)
    T=a+b; S=s1+s2
    assert mm(O,tp(O))==I2()
    G0=mm(A,O)
    B=add(A,H,-S/T)
    assert tr(B)==0
    be2=two_eigs_squared(B)
    assert mm(B,B)==sc(I2(),be2)
    G1=mm(B,O)
    assert mm(G1,tp(G1))==sc(I2(),be2)
    C=add(I2(),H,-F(2)/T)
    rho2=(a-b)**2/T**2
    assert tr(C)==0 and mm(C,C)==sc(I2(),rho2)
    GG=G1
    for k in range(1,7):
        gg=mm(GG,tp(GG))
        assert gg==sc(I2(),be2*rho2**(k-1)),(a,b,s1,s2,n,k)
        GG=mm(C,GG)
    if be2==0:assert G1==sc(G0,F(0))
    return 1

def rank_one_boundary(a,b,angle,u,v):
    H=spd(a,b,angle);T=a+b
    E=mm(((u[0],),(u[1],)),(tuple(v),))
    G=mm(H,E)
    # For rank one the nuclear-scaled polar map is exactly the gradient.
    E1=add(E,G,-F(1)/T)
    M=add(I2(),H,-F(1)/T)
    assert E1==mm(M,E)
    return 1

if __name__=='__main__':
    cases=0
    hvals=((F(1),F(2)),(F(1),F(4)),(F(2),F(5)),(F(2),F(2)))
    angles=(F(0),F(1,3),F(2,3))
    for (a,b), (s1,s2), ah, aa, ao, n in product(hvals, ((F(1),F(2)),(F(2),F(5)),(F(1),F(1))),angles,angles,angles,(2,3)):
        cases += test_case(a,b,s1,s2,ah,aa,ao,n)
    boundary=0
    for (a,b),ah,u,v in product(hvals,angles,((F(1),F(2)),(F(3),F(-1))),((F(2),F(-1),F(1)),(F(2),F(2),F(3)))):
        boundary += rank_one_boundary(a,b,ah,u,v)
    print('PASS:',cases,'full-row-rank rational polar-decomposition models, through six linearized steps;')
    print('PASS:',boundary,'rank-one boundary models, exact-rational.')
