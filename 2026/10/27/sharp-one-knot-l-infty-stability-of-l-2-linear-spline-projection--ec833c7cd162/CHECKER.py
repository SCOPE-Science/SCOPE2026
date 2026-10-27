"""Exact symbolic and rational checks for a one-knot linear-spline projection."""
from fractions import Fraction
import sympy as sp

u,a,x,y=sp.symbols('u a x y',positive=True)
G=sp.Matrix([[a/sp.Integer(3),a/sp.Integer(6),0],
             [a/sp.Integer(6),sp.Rational(1,3),(1-a)/6],
             [0,(1-a)/6,(1-a)/3]])
assert sp.factor(G.det()) == sp.factor(a*(1-a)/36)  # see determinant below
Ginv=G.inv()

def basis(t,aa):
    if t<=aa:
        return sp.Matrix([1-t/aa,t/aa,0])
    return sp.Matrix([0,(1-t)/(1-aa),(t-aa)/(1-aa)])

def check(eq):
    assert sp.simplify(eq)==0

# Check the exact endpoint and interior-knot reproducing kernels.
Yleft=sp.Matrix([1-y/a,y/a,0])
Yright=sp.Matrix([0,(1-y)/(1-a),(y-a)/(1-a)])
B0=sp.Matrix([1,0,0]).T
Ba=sp.Matrix([0,1,0]).T
B1=sp.Matrix([0,0,1]).T
check((B1*Ginv*Yleft)[0]-(1-3*y/a))
check((B1*Ginv*Yright)[0]-(-2+3*(2-a)*(y-a)/(1-a)**2))
check((Ba*Ginv*Yleft)[0]-(-2+6*y/a))
check((Ba*Ginv*Yright)[0]-(-2+6*(1-y)/(1-a)))
check((B0*Ginv*Yleft)[0]-(-2+3*(a+1)*(a-y)/a**2))
check((B0*Ginv*Yright)[0]-(1-3*(1-y)/(1-a)))

# Endpoint absolute-integral calculations, with zero crossings inside the intervals.
B=3*(2-a)/(1-a)**2
cross=a+2/B
check(cross-(a+2*(1-a)**2/(3*(2-a))))
check(sp.integrate(-(1-3*y/a),(y,a/3,a))+sp.integrate(1-3*y/a,(y,0,a/3))-5*a/6)
I2 = sp.integrate(-(-2+B*(y-a)),(y,a,cross)) + sp.integrate(-2+B*(y-a),(y,cross,1))
check(I2-(1+a/2+4*(1-a)**2/(3*(2-a))))
check(5*a/6+I2-(1+4/(3*(2-a))))

# Independent numerical-free rational Green kernel integration.
def area_linear(v0,v1,length):
    if v0*v1>=0: return length*(abs(v0)+abs(v1))/2
    u,w=abs(v0),abs(v1)
    return length*(u*u+w*w)/(2*(u+w))

def row_abs(aa,xx):
    Binv=G.subs(a,aa).inv()
    kx=basis(xx,aa).T*Binv
    points=[sp.Rational(0),aa,sp.Rational(1)]
    vals=[(kx*basis(z,aa))[0] for z in points]
    return sum(area_linear(vals[j],vals[j+1],points[j+1]-points[j]) for j in (0,1))

count=0
for den in range(3,18):
    for num in range(1,den):
        aa=sp.Rational(num,den)
        expected=1+sp.Rational(4,3)/(1+min(aa,1-aa))
        assert row_abs(aa,0)==1+sp.Rational(4,3)/(1+aa); count+=1
        assert row_abs(aa,aa)==sp.Rational(5,3); count+=1
        assert row_abs(aa,1)==1+sp.Rational(4,3)/(2-aa); count+=1
        for j in range(1,9):
            xx=sp.Rational(j,9)
            assert row_abs(aa,xx)<=expected; count+=1
assert count>1000
print('PASS: general symbolic identities and',count,'exact-rational row comparisons')
