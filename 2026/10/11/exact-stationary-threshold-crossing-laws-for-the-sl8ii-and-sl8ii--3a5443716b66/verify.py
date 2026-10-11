from fractions import Fraction as F

def check(r,kappa,a,b,c,x,y,z):
    xdot=kappa*y**(2*r+1)-y*y
    ydot=a*z*z+x*y
    zdot=b*x*x+c*x*y
    assert c*ydot-zdot == a*c*z*z-b*x*x
    assert xdot == y*y*(kappa*y**(2*r-1)-1)

a=F(1,2); c=F(6,5)
assert a*c/F(11,10) == F(6,11)
assert a*c/F(3,5) == F(1,1)
states=[(F(2,3),F(-5,4),F(7,6)),(F(-3,5),F(4,7),F(-9,8)),(F(0),F(3,2),F(1,11))]
for r,k in [(1,F(5,3)),(2,F(7,4))]:
    for s in states:
        check(r,k,F(1,2),F(11,10) if r==1 else F(3,5),F(6,5),*s)
print('VERIFY_OK')
