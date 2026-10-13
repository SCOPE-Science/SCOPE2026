"""Exact symbolic check of the three-site trapping-time and resource-optimality theorem.

Run: python verify.py
Requires: sympy>=1.12. No external files or network.
"""
import sympy as s

j,h,kappa,E,x = s.symbols('j h kappa E x',positive=True,real=True)
H=s.Matrix([[0,j,0],[j,0,h],[0,h,0]])
P=s.diag(1,0,0)
Q=-s.I*H-kappa*P/2
X=s.Matrix([
    [3/kappa, s.I/j, (2*h*h-j*j)/(kappa*h*j)],
    [-s.I/j,(kappa*kappa+4*h*h+4*j*j)/(2*kappa*j*j),s.I/(2*h)],
    [(2*h*h-j*j)/(kappa*h*j),-s.I/(2*h),
      (kappa*kappa*h*h+4*h**4+2*j**4)/(2*kappa*h*h*j*j)],
])
checks=0
for item in Q.conjugate().T*X + X*Q+s.eye(3):
    assert s.cancel(item)==0
    checks+=1
assert s.simplify(X-X.conjugate().T)==s.zeros(3)
checks+=1
# The Gramian is unique: any purely imaginary eigenvalue would force the
# first component, then both remaining components, to vanish when j,h>0.
assert s.simplify(X[2,2]-(kappa/(2*j*j)+(2*h*h/j/j+j*j/h/h)/kappa))==0
checks+=1
# Introduce x=j^2/h^2 and budget E=j^2+h^2.
T=(kappa/(2*E))*(1+1/x)+(x+2/x)/kappa
T_min_over_kappa=s.sqrt(2/E)*s.sqrt(x+1+2/x+2/x**2)
assert s.factor((x+1+2/x+2/x**2)-s.Rational(9,2)) == (x-2)**2*(2*x+1)/(2*x*x)
checks+=1
assert s.simplify(T.subs({x:2,kappa:2*s.sqrt(E)})-3/s.sqrt(E))==0
checks+=1
assert s.simplify(T.subs({x:1,kappa:s.sqrt(3*E)})-2*s.sqrt(3)/s.sqrt(E))==0
checks+=1
# Independently solve the linear system Q^*Y+YQ=-I at unequal rational couplings.
a=s.symbols('a0:9')
Y=s.Matrix(3,3,a)
res=Q.conjugate().T*Y+Y*Q+s.eye(3)
for jj,hh,kk in [(1,2,3),(2,3,s.Rational(1,2)),(s.Rational(3,2),2,5)]:
    equations=[v.subs({j:jj,h:hh,kappa:kk}) for v in res]
    sol=s.solve(equations,a,dict=True)
    assert len(sol)==1
    yy=Y.subs(sol[0])
    xx=X.subs({j:jj,h:hh,kappa:kk})
    assert yy==xx
    checks+=1
print('VERIFY_OK',checks)
