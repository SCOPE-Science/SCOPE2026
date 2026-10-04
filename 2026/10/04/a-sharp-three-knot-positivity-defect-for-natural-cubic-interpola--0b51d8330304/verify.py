from fractions import Fraction as F

def interior_second(h, k, y0, y1, y2):
    return F(3,1)/(h+k)*((y2-y1)/k - (y1-y0)/h)

def spline_left(h, k, y0, y1, y2, t):
    m1 = interior_second(h,k,y0,y1,y2)
    return m1*h*h*(t**3-t)/F(6,1) + y0*(1-t) + y1*t

def spline_right(h, k, y0, y1, y2, u):
    m1 = interior_second(h,k,y0,y1,y2)
    return m1*k*k*(1-u)**3/F(6,1) + (y1-m1*k*k/F(6,1))*(1-u) + y2*u

def left_basis(r,t):
    A0=(1-t)*(2*r+2-t-t*t)/(2*(1+r))
    A1=t*(2*r+1-t*t)/(2*r)
    A2=-t*(1-t*t)/(2*r*(1+r))
    return A0,A1,A2

def right_basis(r,u):
    B0=-r*r*u*(1-u)*(2-u)/(2*(1+r))
    B1=(1-u)*(2+2*r*u-r*u*u)/2
    B2=u*(2+3*r*u-r*u*u)/(2*(1+r))
    return B0,B1,B2

for r in [F(1,5),F(1,2),F(1),F(3,2),F(7)]:
    h=F(5,3)
    k=r*h
    for t in [F(0),F(1,7),F(2,5),F(4,5),F(1)]:
        A=left_basis(r,t)
        assert sum(A)==1
        assert A[0]>=0 and A[1]>=0 and A[2]<=0
        for data in [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),
                     (F(2,7),F(3,5),F(11,13))]:
            direct=spline_left(h,k,*data,t)
            combo=sum(a*y for a,y in zip(A,data))
            assert direct==combo
    for u in [F(0),F(1,7),F(2,5),F(4,5),F(1)]:
        B=right_basis(r,u)
        assert sum(B)==1
        assert B[0]<=0 and B[1]>=0 and B[2]>=0
        for data in [(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1)),
                     (F(2,7),F(3,5),F(11,13))]:
            direct=spline_right(h,k,*data,u)
            combo=sum(b*y for b,y in zip(B,data))
            assert direct==combo

# The cubic shape has derivative 1-3 t^2; at t^2=1/3,
# (t-t^3)^2 = 4/27, which is the square of 2/(3 sqrt(3)).
# This exact polynomial identity avoids treating a floating sample as proof.
q2 = F(1,3)*(1-F(1,3))**2
assert q2 == F(4,27)

# Reflection identity for the right interval:
# u(1-u)(2-u) = v-v^3 with v=1-u.
for u in [F(0),F(1,9),F(2,5),F(7,8),F(1)]:
    v=1-u
    assert u*(1-u)*(2-u) == v-v**3

# Strictly positive witness at a rational point near the analytic extremum.
# This is supplementary only; the exact threshold is proved in the text.
r=F(1)
t=F(3,5)
A=left_basis(r,t)
c=-A[2]
eps=c/(2*(1+c))
val=sum(a*y for a,y in zip(A,(eps,eps,F(1))))
assert eps>0 and val<0

print("VERIFY_OK")
