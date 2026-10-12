"""Exact-rational algebra and independent numerical checks for a two-site VFE frontier."""
from fractions import Fraction as F
from math import log, isclose


def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


def inv2(M):
    d=det2(M)
    assert d>0
    return ((M[1][1]/d,-M[0][1]/d),(-M[1][0]/d,M[0][0]/d))


def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def matvec(A,v):
    return (A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])


def objective_gain(K,r,a,index_set):
    zero=F(0); one=F(1)
    if index_set==0:
        Q=((zero,zero),(zero,zero))
    elif index_set==3:
        Q=K
    else:
        j=0 if index_set==1 else 1
        denom=K[j][j]
        Q=tuple(tuple(K[i][j]*K[j][k]/denom for k in range(2)) for i in range(2))
    P=((one+Q[0][0],Q[0][1]),(Q[1][0],one+Q[1][1]))
    PI=inv2(P)
    y=(a,-a)
    yy=matvec(PI,y)
    gainfit=(sum(y[i]*y[i] for i in range(2))-sum(y[i]*yy[i] for i in range(2)))/2
    trace=(Q[0][0]+Q[1][1])/2
    return trace+gainfit-log(float(det2(P)))/2


def expected(r,a):
    b=r*r-log(2+r*r)+log(4-r*r)/2
    c=3*r*(1-r)/((2+r*r)*(2-r))
    return b-c*a*a


def check():
    z=0
    for den in range(3,31):
        for numer in range(1,den):
            r=F(numer,den)
            K=((F(1),r),(r,F(1)))
            assert det2(K)==1-r*r>0
            for a in (F(0),F(1,4),F(1),F(3),F(15,2)):
                g1=objective_gain(K,r,a,1)
                g2=objective_gain(K,r,a,2)
                g12=objective_gain(K,r,a,3)
                assert isclose(g1,g2,rel_tol=3e-13,abs_tol=3e-13)
                assert isclose(g1+g2-g12,expected(float(r),float(a)),rel_tol=3e-12,abs_tol=3e-12)
                assert g1>=0 and g12>=g1
                z+=1
    r=.5
    assert expected(r,1)<-0.12
    assert isclose(expected(r,1), 1/36+log(20/27)/2,abs_tol=1e-14)
    for j in (20,50,100,300,1000):
        assert expected(1/j,1)<0
        r=1-1/j
        a=j*j*j
        K=((F(1), F(j-1,j)),(F(j-1,j),F(1)))
        singleton=objective_gain(K,F(j-1,j),F(a),1)
        full=objective_gain(K,F(j-1,j),F(a),3)
        ratio=(full-singleton)/singleton
        limit=2*(2+r*r)/((1-r)*(2-r))-1
        assert isclose(ratio,limit,rel_tol=1e-4)
        assert ratio>j
    print('VERIFY_OK exact_rational_matrix_reconstructions=',z,'asymptotic_cases=10')

if __name__=='__main__':
    check()
