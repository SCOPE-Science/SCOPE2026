import sympy as sp
x,y,r,K,m,p,q,a,b,c,H1,H2,qd=sp.symbols('x y r K m p q a b c H1 H2 qd', nonzero=True)
s=q*p
D=x**2+a**2
G=r*x*(1-x/K)*(x-m)
dx=G-s*x**2*y/D-H1
dy=(p*x**2/D-b*y-c)*y-H2
lhs=sp.expand(dx+q*dy+qd*y)
target=sp.expand(G-H1-q*H2-q*b*y**2-(q*c-qd)*y)
assert sp.simplify(lhs-target)==0
u=sp.symbols('u')
disc=K**2-K*m+m**2
ustar=(K+m+sp.sqrt(disc))/3
h=u*(K-u)*(u-m)
assert sp.simplify(sp.diff(h,u).subs(u,ustar))==0
th,eta,Delta=sp.symbols('theta eta Delta', positive=True)
yroot=(sp.sqrt(eta**2+4*th*Delta)-eta)/(2*th)
assert sp.simplify(th*yroot**2+eta*yroot-Delta)==0
print('VERIFY_OK')
