import sympy as sp

a,b,c=sp.symbols("a b c", positive=True)
P=a+b+c
u=(b**2+c**2-a**2)/(2*c)
v2=b**2-u**2
mx=(a*(c+u)+b*u+c*c)/(2*P)
my_factor=(a+b)/(2*P)
EY2=(a*(c**2+c*u+b**2)+b*b**2+c*c**2)/(3*P)
D_boundary=sp.factor(2*(EY2-(mx**2+my_factor**2*v2)))
assert sp.simplify(D_boundary-(a**3+b**3+c**3+3*a*b*c)/(6*P)) == 0
D_interior=(a**2+b**2+c**2)/18
N=sp.factor(18*P*(D_boundary-D_interior))
x,y,z=sp.symbols("x y z", positive=True)
N_xyz=sp.expand(N.subs({a:y+z,b:z+x,c:x+y}))
Q=2*(x**3+y**3+z**3+5*x**2*y+5*x**2*z+5*x*y**2+5*x*z**2+5*y**2*z+5*y*z**2+3*x*y*z)
assert sp.expand(N_xyz-Q) == 0
s=x+y+z
r2=x*y*z/s
Rr=((y+z)*(z+x)*(x+y))/(4*s)
gap_xyz=sp.factor(N_xyz/(18*(2*s)))
assert sp.simplify(gap_xyz-(s**2+8*Rr-7*r2)/18) == 0
print("verification ok")
