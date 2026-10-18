"""Exact-rational checks for homogeneous adoption–opinion equilibria and their spectra.

Requires Python 3 standard library only. Run: python verify.py
"""
from fractions import Fraction as F

beta,delta,g,alpha,lam,xi=F(4,9),F(1,128),F(1,8),F(3,8),F(1,4),F(3,8)
q=xi/(1-lam); H=1-delta/(g*q)
assert alpha+lam+xi==1 and 0 < beta+g < 1 and 0<2*g<1
assert q==F(1,2) and H==F(7,8)
assert 27*delta/(4*q*q*H**3)==F(108,343)<beta

def det3(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])

def poly3(J):
    tr=sum(J[i][i] for i in range(3))
    c2=sum(J[i][i]*J[j][j]-J[i][j]*J[j][i] for i,j in [(0,1),(0,2),(1,2)])
    return [F(1),-tr,c2,-det3(J)]

def poly2(J):
    return [F(1),-J[0][0]-J[1][1],J[0][0]*J[1][1]-J[0][1]*J[1][0]]

def evalpoly(p,z):
    y=F(0)
    for c in p:y=y*z+c
    return y

def check_brackets(p, intervals):
    for x,y in intervals:
        assert x<y and evalpoly(p,x)*evalpoly(p,y)<0,(p,x,y,evalpoly(p,x),evalpoly(p,y))

assert [(x, x*x*(H-x)*beta*q*q) for x in [F(3,8),F(3,4)]]==[(F(3,8),delta),(F(3,4),delta)]

for a,vexp,yexp,Jexpect,Qexpect,pc,qc,br_p,br_q in [
    (F(3,8),F(17,32),F(3,16),
     [[F(31,32),-F(1,32),F(1,64)],[-F(3,32),F(7,8),-F(5,64)],[F(3,8),F(0),F(1,4)]],
     [[F(123,128),-F(1,32)],[-F(3,32),F(7,8)]],
     [F(1),-F(34304,16384),F(21296,16384),-F(3391,16384)],
     [F(1),-F(235,128),F(429,512)],
     [(F(0),F(1,4)),(F(4,5),F(9,10)),(F(1),F(21,20))],
     [(F(4,5),F(9,10)),(F(19,20),F(1))]),
    (F(3,4),F(13,64),F(3,8),
     [[F(7,8),-F(1,8),F(1,64)],[-F(9,128),F(7,8),-F(1,32)],[F(3,8),F(0),F(1,4)]],
     [[F(111,128),-F(1,8)],[-F(9,128),F(7,8)]],
     [F(1),-F(2),F(1217,1024),-F(190,1024)],
     [F(1),-F(223,128),F(3,4)],
     [(F(0),F(1,4)),(F(3,4),F(4,5)),(F(19,20),F(1))],
     [(F(3,4),F(4,5)),(F(19,20),F(1))])
]:
    y=q*a
    s=y*(1-a)-(delta/g)*a
    v=1-a-s
    assert y==yexp and v==vexp and 0< a and 0<s and 0<v and a+v+s==1
    assert (1-delta)*a + beta*y*s*a==a
    assert v+delta*a-g*y*v+g*(1-y)*s==v
    assert alpha*0+lam*y+xi*a==y
    Jh=[[1-delta+beta*y*(s-a),-beta*y*a,beta*a*s],
        [delta-g*(1-y),1-g,-g*(1-a)],
        [xi,F(0),lam]]
    Qt=[[1-delta-beta*y*a,-beta*y*a],
        [delta-g*(1-y),1-g]]
    assert Jh==Jexpect and Qt==Qexpect
    assert poly3(Jh)==pc and poly2(Qt)==qc
    check_brackets(pc,br_p);check_brackets(qc,br_q)
# Adoption-free equilibrium: exactly stable eigenvalues for homogeneous/transverse.
assert 0<1-delta<1 and 0<1-g<1 and 0<lam<1
print('PASS: exact equilibria, cubic threshold, positive simplex, complete spectra and strict interval certificates.')
