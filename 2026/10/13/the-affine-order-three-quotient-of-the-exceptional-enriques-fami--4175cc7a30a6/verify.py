import sympy as sp

s,u,v,y,a,t,x=sp.symbols("s u v y a t x")
F1=sp.Poly(u**3+s*v,s,u,v,y,a,modulus=2)
F2=sp.Poly(y**2+u*v+a*s*u**2+s**2*u+s,s,u,v,y,a,modulus=2)
source=sp.Poly(y**2+t*x**4+a*t**5*x**2+t**7*x+t**3,t,x,y,a,modulus=2)
quotient=sp.Poly((y**2+u*v+a*s*u**2+s**2*u+s).subs({s:t**3,u:t*x,v:x**3}),t,x,y,a,modulus=2)
assert source==quotient
assert sp.Poly((u**3+s*v).subs({s:t**3,u:t*x,v:x**3}),t,x,modulus=2).is_zero
r1=[v,u**2,s]
r2=[1+a*u**2,v+s**2,u]
Msu=sp.Poly(r1[0]*r2[1]+r1[1]*r2[0],s,u,v,a,modulus=2)
Muv=sp.Poly(r1[1]*r2[2]+r1[2]*r2[1],s,u,v,a,modulus=2)
assert sp.Poly(Muv.as_expr()+F1.as_expr()+s**3,s,u,v,a,modulus=2).is_zero
assert sp.Poly(Msu.as_expr().subs({s:0,u:0}),v,a,modulus=2)==sp.Poly(v**2,v,a,modulus=2)
assert sp.Poly(F2.as_expr().subs({s:0,u:0,v:0}),y,a,modulus=2)==sp.Poly(y**2,y,a,modulus=2)
assert [sp.Poly(z,s,u,v,y,a,modulus=2).as_expr().subs({s:0,u:0,v:0,y:0}) for z in r1]==[0,0,0]
assert sp.Poly(r2[0],s,u,v,y,a,modulus=2).as_expr().subs({s:0,u:0,v:0,y:0})==1
initial=sp.Poly(u**3+u*v**2+v*y**2,u,v,y,modulus=2)
assert initial.total_degree()==3 and not initial.is_zero
print("VERIFY_OK invariant_ring_relations=2 singular_locus=origin local_multiplicity=3")
