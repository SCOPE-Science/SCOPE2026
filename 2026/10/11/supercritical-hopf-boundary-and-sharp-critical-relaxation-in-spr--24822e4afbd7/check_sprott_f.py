import sympy as s
b=s.symbols('b',positive=True,real=True)
I=s.I
A=s.Matrix([[0,1,1],[-1,0,0],[0,0,-b]])
q=s.Matrix([1,I,0])
p=s.Matrix([s.Rational(1,2),I/2,1/(2*(b-I))])
B=lambda u,v:s.Matrix([0,0,2*u[0]*v[0]])
herm=lambda p,v: (s.conjugate(p.T)*v)[0]
assert s.simplify(A*q-I*q)==s.zeros(3,1)
assert s.simplify(A.T*p+I*p)==s.zeros(3,1)
assert s.simplify(herm(p,q)-1)==0
h11=s.simplify(A.inv()*B(q,s.conjugate(q)))
h20=s.simplify((2*I*s.eye(3)-A).inv()*B(q,q))
G=s.simplify(herm(p,-2*B(q,h11)+B(s.conjugate(q),h20)))
print('h11=',h11.T)
print('h20=',h20.T)
print('G21=',s.factor(G))
print('real_G21=',s.factor(s.re(s.expand_complex(G))))
print('imag_G21=',s.factor(s.im(s.expand_complex(G))))
expected=-4*b/((b*b+1)*(b*b+4))
assert s.simplify(s.re(s.expand_complex(G))-expected)==0
print('l1=',s.factor(s.re(s.expand_complex(G))/2))
print('radius_limit=',s.simplify(-4/s.re(s.expand_complex(G))))
# continuous family parameter: jacobian charpoly (lambda+b)(lambda^2-a lambda+1)
a=s.symbols('a',real=True)
l=s.symbols('l')
J=s.Matrix([[0,1,1],[-1,a,0],[0,0,-b]])
print('characteristic=',s.factor(J.charpoly(l).as_expr()))
assert s.simplify(J.charpoly(l).as_expr()-(b+l)*(1-a*l+l*l))==0
# Quadratic center graph z=h(x,y)+higher order at a=0.
x,y=s.symbols('x y',real=True)
h=((b*b+2)*x*x-2*b*x*y+2*y*y)/(b*(b*b+4))
res=s.simplify(s.diff(h,x)*y-s.diff(h,y)*x-(x*x-b*h))
assert res==0
print('center_quadratic_invariance=',res)
print('PASS')
