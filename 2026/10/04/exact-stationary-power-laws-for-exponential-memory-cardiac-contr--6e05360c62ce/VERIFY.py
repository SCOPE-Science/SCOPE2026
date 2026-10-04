import sympy as s
x,y,u,th,a,v1,v2,d,e,A,alpha,beta=s.symbols('x y u th a v1 v2 d e A alpha beta')
G=x*(x+d)*(x+e)/(d*e)
U=x**2/s.Integer(2)+(d+e)*x**3/(3*d*e)+x**4/(4*d*e)
q=(x-v1)*(x-v2)
P=s.integrate(q,x)
xd=y
yd=-a*q*y-G+A*s.sin(th)-alpha*u
ud=y-beta*u
E=y**2/s.Integer(2)+U+alpha*u**2/s.Integer(2)
Ed=s.diff(E,x)*xd+s.diff(E,y)*yd+s.diff(E,u)*ud
expected=-a*q*y**2-alpha*beta*u**2+A*y*s.sin(th)
assert s.simplify(s.diff(U,x)-G)==0
assert s.simplify(Ed-expected)==0
assert s.simplify(s.diff(P,x)-q)==0
print('VERIFY_OK')
