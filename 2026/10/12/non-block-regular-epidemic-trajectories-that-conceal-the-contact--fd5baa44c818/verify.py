"""Exact rational checks for proportional SIS observations and two-type jets.
Public mathematical reproduction script; no network access or third-party packages.
"""
from fractions import Fraction as F


def vector_field(W, pi, gam, z):
    n=len(z)
    return [ (1-z[i])*sum(W[i][j]*pi[j]*z[j] for j in range(n))-gam[i]*z[i] for i in range(n)]

def matvec_WPi(W,pi,z):
    return [sum(W[i][j]*pi[j]*z[j] for j in range(len(z))) for i in range(len(z))]

def determinant2(a,b):
    return a[0]*b[1]-a[1]*b[0]

def jacobian2(A,g,x,y):
    a,b=A[0]; c,d=A[1]
    return [[-a*x-b*y + (1-x)*a-g[0],(1-x)*b],
            [(1-y)*c, -c*x-d*y+(1-y)*d-g[1]]]

def test_all_n():
    for n in (2,3,4,7,11,25):
        k=[F(1)+F(i,n-1) for i in range(n)]
        pi=[F(1,n)]*n
        u=[k[1],-k[0]]+[F(0)]*(n-2)
        W=[[F(2) for j in range(n)] for i in range(n)]
        V=[[W[i][j]+F(1,4)*u[i]*u[j] for j in range(n)] for i in range(n)]
        gam=[F(3)/q-F(1) for q in k]
        assert len(set(k))==n
        assert all(F(1,10)<=g<=F(4) for g in gam)
        assert all(F(1,10)<=x<=F(4) for row in V for x in row)
        assert all(F(1,10)<=x<=F(9,10) for x in [q/F(5) for q in k])
        assert V!=W and V==[list(row) for row in zip(*V)]
        assert sum(pi[i]*k[i]*u[i] for i in range(n))==0
        for t in (F(1,5),F(1,4),F(1,3)):
            z=[q*t for q in k]
            assert matvec_WPi(W,pi,z)==[3*t]*n
            assert matvec_WPi(V,pi,z)==[3*t]*n
            expected=[q*t*(1-3*t) for q in k]
            assert vector_field(W,pi,gam,z)==expected
            assert vector_field(V,pi,gam,z)==expected
        print('n=',n,'exact invariant and alternate contact matrices OK')

def test_jets():
    # Generic first transversal derivative: G determinant T^4 / 7500.
    x=F(1,5); k=F(2)
    A=[[F(1),F(1)],[F(1),F(1)]]
    gam=[F(2),F(1)]
    W=[[2*a for a in row] for row in A]
    z=[x,k*x]; f=vector_field(W,[F(1,2)]*2,gam,z)
    alpha=A[0][0]+A[0][1]*k
    beta=A[1][0]/k + A[1][1]
    P=alpha-gam[0]-beta+gam[1]
    Q=alpha-k*beta
    delta=P-Q*x
    assert delta==F(1,2) and Q==0
    assert determinant2(z,f)==-k*x*x*delta==F(-1,25)
    assert determinant2(z,f)**2/F(12)==F(1,7500)
    # Initially tangent but not invariant: determinant of G starts at T^6.
    A=[[F(1),F(1)],[F(1),F(2)]]
    gam=[F(19,10),F(1)]
    W=[[2*a for a in row] for row in A]
    z=[x,k*x]; f=vector_field(W,[F(1,2)]*2,gam,z)
    alpha=A[0][0]+A[0][1]*k
    beta=A[1][0]/k+A[1][1]
    P=alpha-gam[0]-beta+gam[1]
    Q=alpha-k*beta
    assert P==-F(2,5) and Q==-2 and P-Q*x==0 and f[0]==F(1,10)
    J=jacobian2(A,gam,*z)
    z2=[sum(J[i][j]*f[j] for j in range(2)) for i in range(2)]
    assert determinant2(z,f)==0
    assert determinant2(z,z2)==k*x*x*Q*f[0]==F(-2,125)
    assert determinant2(z,z2)**2/F(45)==F(4,703125)
    print('exact T^4 and T^6 leading Gram determinant coefficients OK')

if __name__=='__main__':
    test_all_n()
    test_jets()
    print('VERIFY_OK')
