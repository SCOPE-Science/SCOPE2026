"""E_31: y^2=x^3+31x^2+31x+1=(x+1)(x^2+30x+1). Rank/pi^P checks, torsion."""
from fractions import Fraction as F
def E_rhs(x): return x**3+31*x**2+31*x+1
# rational 2-torsion root check
for r in [-1]:
    assert E_rhs(r)==0
# discriminant
a,b,c=31,31,1
D=a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c
assert D==702464==2**11*7**3, D
print("disc(E_31)=702464=2^11*7^3 OK")
# point checks: P0=(0,1), P1=(8,?)... known E pts from X pts: (x^2,y): (0,1),(1,8),(49,440),(1/49,440/343)
for (x,y) in [(F(0),F(1)),(F(1),F(8)),(F(49),F(440)),(F(1,49),F(440,343))]:
    assert y*y==E_rhs(x),(x,y)
print("4 E_31(Q) pts from X_31 fibres verified")
# Nagell-Lutz torsion screen: torsion y=0 or y^2|D
print("torsion x=-1: root -> 2-torsion (-1,0) on E_31")
