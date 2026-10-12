from fractions import Fraction
import sympy as sp

a,b,c,d,e,f=sp.symbols('a b c d e f')
s,u,v,z,r,t=sp.symbols('s u v z r t', nonzero=True)
M=sp.Matrix([
[0,1,1,1,1],
[1,0,a**2,b**2,c**2],
[1,a**2,0,d**2,e**2],
[1,b**2,d**2,0,f**2],
[1,c**2,e**2,f**2,0],
])
CM=sp.factor(M.det()/2)
sub={a:s*u**2,b:s*v**2,c:s*u*v,d:r,e:u*z,f:v*z}
expected=-u**2*v**2*(r-s*u**2+s*v**2)*(r+s*u**2-s*v**2)*(r**2*s**2-2*s**2*u**2*z**2-2*s**2*v**2*z**2+z**4)
assert sp.expand(CM.subs(sub)-expected)==0

X=((t**2-1)*(u+v)-2*t*(u-v))/(1+t**2)
Y=((1-t**2)*(u-v)-2*t*(u+v))/(1+t**2)
assert sp.factor(X**2+Y**2-2*(u**2+v**2))==0

# Exact positive geometric witness from s=25,u=2,v=1,t=-4/3.
sv=Fraction(25); uv=Fraction(2); vv=Fraction(1); tv=Fraction(-4,3)
Xv=Fraction(9,5); Yv=Fraction(13,5)
zv=sv*Xv; rv=zv*Yv
D=(sv*uv*uv,sv*vv*vv,sv*uv*vv,rv,uv*zv,vv*zv)
assert D==(Fraction(100),Fraction(25),Fraction(50),Fraction(117),Fraction(90),Fraction(45))
A,B,C,D23,E,F=D
assert C*C==A*B
assert C*E==A*F
assert C*F==B*E
# Direct fixed-map replay.
IH=(A,B,A*B/C,D23,A*F/C,B*E/C)
assert IH==D
cmv=sp.expand(CM.subs({a:A,b:B,c:C,d:D23,e:E,f:F}))
assert cmv==0
triangles=[(A,B,D23),(A,C,E),(B,C,F),(D23,E,F)]
assert all(2*max(q)<sum(q) for q in triangles)
print('VERIFY_OK factorization=yes conic_identity=yes fixed_witness=100,25,50,117,90,45 all_triangle_inequalities=strict CM=0')
