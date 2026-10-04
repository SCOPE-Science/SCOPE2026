from fractions import Fraction as F

# Elements a + b*sqrt(2) + c*sqrt(3) + d*sqrt(6).
def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def neg(x): return tuple(-v for v in x)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (
        a*e+2*b*f+3*c*g+6*d*h,
        a*f+b*e+3*c*h+3*d*g,
        a*g+c*e+2*b*h+2*d*f,
        a*h+d*e+b*g+c*f,
    )
def scale(q,x): return tuple(q*v for v in x)
Z=(F(0),)*4; ONE=(F(1),F(0),F(0),F(0)); S2=(F(0),F(1),F(0),F(0)); S3=(F(0),F(0),F(1),F(0)); S6=(F(0),F(0),F(0),F(1))
def rat(q): return (F(q),F(0),F(0),F(0))

def eq(x,y): return x==y

# Vertices A,U,C,D,B,U' in cyclic order.
A=(Z,S3)
U=(scale(F(2,5),sub(S6,ONE)), add(scale(F(1,5),S3),scale(F(2,5),S2)))
C=(ONE,Z)
D=(Z,add(scale(F(3,5),S3),scale(F(-4,5),S2)))
B=(neg(ONE),Z)
Up=(neg(U[0]),U[1])
V=[A,U,C,D,B,Up]

# Each half-plane is a*x+b*y <= c. Coefficients are in Q(sqrt2,sqrt3).
hp=[]
hp.append((S2,ONE,S3))
hp.append((neg(S2),ONE,S3))
# B inward median u=(sqrt3/2,1/2), perpendicular v=(-1/2,sqrt3/2).
# -du +/- sqrt2*dv <= 0, expanded in x,y.
hp.append((scale(F(-1,2),add(S3,S2)), scale(F(1,2),sub(S6,ONE)), scale(F(1,2),add(S2,S3))))
hp.append((scale(F(1,2),sub(S2,S3)), scale(F(-1,2),add(S6,ONE)), scale(F(1,2),sub(S3,S2))))
# C by reflection.
hp.append((scale(F(1,2),add(S2,S3)), scale(F(1,2),sub(S6,ONE)), scale(F(1,2),add(S2,S3))))
hp.append((scale(F(1,2),sub(S3,S2)), scale(F(-1,2),add(S6,ONE)), scale(F(1,2),sub(S3,S2))))

# Sign oracle by high-precision decimal evaluation is used only after exact simplification.
from decimal import Decimal, getcontext
getcontext().prec=80
rt2=Decimal(2).sqrt(); rt3=Decimal(3).sqrt(); rt6=Decimal(6).sqrt()
def dec(z):
    return Decimal(z[0].numerator)/Decimal(z[0].denominator)+Decimal(z[1].numerator)/Decimal(z[1].denominator)*rt2+Decimal(z[2].numerator)/Decimal(z[2].denominator)*rt3+Decimal(z[3].numerator)/Decimal(z[3].denominator)*rt6

def lhs_minus_c(H,P):
    a,b,c=H; x,y=P
    return sub(add(mul(a,x),mul(b,y)),c)

for j,p in enumerate(V):
    for i,H in enumerate(hp):
        z=lhs_minus_c(H,p)
        assert dec(z) <= Decimal('1e-70'), (j,i,z,dec(z))

# Active pairs in cyclic order: A:(0,1), U:(0,4), C:(4,5), D:(3,5), B:(2,3), U':(1,2).
for j,(i,k) in enumerate([(0,1),(0,4),(4,5),(3,5),(2,3),(1,2)]):
    assert eq(lhs_minus_c(hp[i],V[j]),Z)
    assert eq(lhs_minus_c(hp[k],V[j]),Z)

# Twice signed area by shoelace.
twice=Z
for p,q in zip(V,V[1:]+V[:1]):
    twice=add(twice,sub(mul(p[0],q[1]),mul(q[0],p[1])))
if dec(twice)<0:
    twice=neg(twice)
area=scale(F(1,2),twice)
expected=add(scale(F(12,5),S2),scale(F(-4,5),S3))
assert eq(area,expected), (area,expected)

# area/sqrt(3) = 4/5*(sqrt(6)-1), checked without division.
ratio=scale(F(4,5),sub(S6,ONE))
assert eq(area,mul(S3,ratio))
print('VERIFY_OK')
print('area = (12*sqrt(2)-4*sqrt(3))/5')
print('area_ratio = 4*(sqrt(6)-1)/5')
