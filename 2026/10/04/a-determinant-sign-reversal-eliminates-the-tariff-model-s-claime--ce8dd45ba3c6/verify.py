from fractions import Fraction as F


def det2(a,b,c,d):
    return a*d-b*c

# Exact interior witness.
AA=F(1); AB=F(1); BA=F(-1,2); BB=F(-1,2)
xs=-BB/AB; ys=-BA/AA
assert xs==F(1,2) and ys==F(1,2)
a=AA*xs*(1-xs)
b=AB*ys*(1-ys)
det=det2(F(0),a,b,F(0))
assert a==F(1,4) and b==F(1,4)
assert det==F(-1,16)
# lambda^2 = a*b, hence exact eigenvalues +/-1/4 in this witness.
assert a*b==F(1,16)

# Check the first-integral derivative using its exact analytic gradient.
def check_dH(x,y,xs,ys,AA,AB):
    xdot=AA*x*(1-x)*(y-ys)
    ydot=AB*y*(1-y)*(x-xs)
    Hx=AB*(xs/x-(1-xs)/(1-x))
    Hy=-AA*(ys/y-(1-ys)/(1-y))
    return Hx*xdot+Hy*ydot

pts=[(F(1,3),F(2,5)),(F(3,7),F(4,9)),(F(5,8),F(2,3))]
for x,y in pts:
    assert check_dH(x,y,F(1,2),F(1,2),F(2),F(3))==0
    assert check_dH(x,y,F(1,2),F(1,2),F(-2),F(3))==0

# Hessian signs: H_xx=-AB/[xs(1-xs)], H_yy=AA/[ys(1-ys)].
def hessian_diag(xs,ys,AA,AB):
    return (-AB/(xs*(1-xs)), AA/(ys*(1-ys)))

h1,h2=hessian_diag(F(1,2),F(1,2),F(2),F(3))
assert h1<0<h2  # product positive -> saddle level geometry
h1,h2=hessian_diag(F(1,2),F(1,2),F(-2),F(3))
assert h1<0 and h2<0  # product negative -> strict local maximum
h1,h2=hessian_diag(F(1,2),F(1,2),F(2),F(-3))
assert h1>0 and h2>0  # product negative -> strict local minimum

print('VERIFY_OK')
