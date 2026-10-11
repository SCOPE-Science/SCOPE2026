from fractions import Fraction as F

# Abstract regression variance identity.
EA=F(7,5); EB=EA
EB2=F(19,6); EAB=EB2; EA2=F(23,5)
res=EA2-2*EAB+EB2
gap=(EA2-EA*EA)-(EB2-EB*EB)
assert res==gap

# Stationarity algebra used in the speed-slope proof.
# Let C=E[xdot*ydot], S=E[h'(x)*xdot^2], Y=E[ydot^2],
# and ZY=E[zdot*ydot]. The two stationary derivatives give C=S
# and C-Y+ZY=0; stationarity of y^2 with zdot=-beta*y gives ZY=0.
C=F(17,11); S=C; ZY=F(0); Y=C+ZY
assert C==S
assert C-Y+ZY==0
assert Y==S

m0=F(-1,7); m1=F(2,7)
r=(m1-m0)/m1
frac=(-m0)/(m1-m0)
assert r==F(3,2)
assert frac==F(1,3)

# Branchwise sign of x*h(x) for classical slopes.
def h(x):
    x=F(x)
    if x>=1:
        return m1*x+(m0-m1)
    if x<=-1:
        return m1*x-(m0-m1)
    return m0*x

for x in [F(-2),F(-3,2),F(-5,4),F(-1),F(-1,2),F(0),F(1,2),F(1),F(5,4),F(3,2),F(2)]:
    val=x*h(x)
    if abs(x)>r:
        assert val>0
    elif abs(x)==r:
        assert val==0
    else:
        assert val<=0

print('VERIFY_OK')
