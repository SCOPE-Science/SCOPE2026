from fractions import Fraction as F

r=F(5); K=F(1); m=F(5,2); n=F(6,5); e1=F(21,10); e2=F(1)
a1=F(4,5); a2=F(11,10); b=F(1,5); c=F(1,10); H1=F(3,2); H2=F(7,5); alpha=F(1,2); beta=F(1,10)

x=F(227,1000); y=F(1,2); z=F(3,2); w=F(2,5)
required_z=(b+c)/beta
assert required_z == 3
assert z != required_z

dx=r*x*(1-x/K)-m*x*y/(a1+x*x)-n*x*z/(a2+x*x)
dy=e1*m*x*y/(a1+x*x)-alpha*y*z-H1*y+b*w
dz=e2*n*x*z/(a2+x*x)+alpha*y*z-H2*z-beta*z*w
dw=beta*z*w-b*w-c*w
assert dw == F(-3,50)
assert any(v != 0 for v in (dx,dy,dz,dw))

# The earlier printed tuple uses the same K and has x*=3.36>K,
# impossible at an interior equilibrium because positive predation forces x*<K.
x_early=F(84,25)
z_early=F(177,20)
w_early=F(101,100)
assert x_early > K
assert z_early != required_z
assert w_early > 0

print('required_z=', required_z)
print('R3_residuals=', dx, dy, dz, dw)
print('VERIFY_OK')
