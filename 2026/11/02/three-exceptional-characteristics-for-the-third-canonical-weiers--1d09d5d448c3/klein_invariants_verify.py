import sympy as s
x,y,z=s.symbols('x y z')
f=x**3*y+y**3*z+z**3*x
u=x**5*z+x*y**5+y*z**5-5*x**2*y**2*z**2
H=s.hessian(f,(x,y,z));v=s.Matrix([s.diff(u,t) for t in (x,y,z)])
M=H.row_join(v).col_join(s.Matrix([list(v)+[0]]))
A=s.expand(M.det(method='berkowitz')/9)
B=s.expand(s.det(s.Matrix([[s.diff(h,t) for t in (x,y,z)] for h in (f,u,A)]))/14)
# reduce in chart z=1 using y^3=-x^3*y-x; sympy remainder, numerically complicated
f0=s.Poly(f.subs(z,1),y,x,domain='ZZ')
def red(E):
 return s.Poly(E.subs(z,1),y,x,domain='ZZ').rem(f0)
res=red(B*B-A*A*A+1728*u**7)
print('invariant_relation_remainder_zero',res.is_zero,'termcount',len(res.terms()))
print('phi6',str(u))
print('phi14_terms',len(s.Poly(A,x,y,z).terms()),'phi21_terms',len(s.Poly(B,x,y,z).terms()))
print('check Phi14 leading',s.Poly(A,x,y,z).coeff_monomial(x**14))
assert res.is_zero
print('VERIFY_INVARIANTS_OK')
