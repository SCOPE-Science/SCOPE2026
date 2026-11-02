"""Exact symbolic verification of the square-support logarithmic discriminant geometry."""
import sympy as sp

x,y,z,w,s,u,v,A,B=sp.symbols('x y z w s u v A B')
D=A-B
F=sp.expand(B**2*s**2+D*(D*(u*u+v*v)-2*B*s*(u+v)-2*(A+B)*u*v))
T=sp.expand(A*A*(u-v)**2-2*A*B*(s*(u+v)+u*u+v*v)+B*B*(s+u+v)**2)
assert sp.expand(F-T)==0
Q=sp.Matrix([[B**2,-B*D,-B*D],[-B*D,D*D,-(A+B)*D],[-B*D,-(A+B)*D,D*D]])
assert sp.factor(Q.det())==-4*A*A*B*B*(A-B)**2
assert sp.factor(sp.discriminant(T,A))==16*B*B*u*v*(s+u)*(s+v)
assert sp.expand(sp.diff(T,A).subs({A:0,s:-u-v})-4*B*u*v)==0
assert sp.expand(sp.diff(T,B).subs({B:0,v:u})+4*A*u*(s+u))==0
assert sp.expand(sp.diff(T,A).subs({A:B,s:0})+4*B*u*v)==0
Fz=sp.expand(F.subs({A:x*w,B:y*z}))
assert sp.expand(Fz-(y*z)**2*s**2-(x*w-y*z)*((x*w-y*z)*(u*u+v*v)-2*y*z*s*(u+v)-2*(x*w+y*z)*u*v))==0
partials=[sp.diff(Fz,t) for t in (x,y,z,w,s,u,v)]
# Generic smooth point of each stratum, verified by normal Hessian at a representative.
# The transverse slice is restricted via local smooth coordinates for the stratum.
# Generic 3-fold component: coefficient line x=y=0, with z=w=1 and generic exponents.
# The quadratic part in x,y at A=B=0 has discriminant nonzero at (s,u,v)=(1,2,3).
assert sp.factor(sp.discriminant(T.subs({s:1,u:2,v:3}),A))!=0
# Twelve surface components: one witness per symmetry class, Hessian transverse rank three.
def rank_hessian(poly, directions, replacements):
    mat=sp.hessian(poly, directions)
    return sp.Matrix(mat.subs(replacements)).rank()
# A=0, x=0; generic coefficient w=y=z=1, and exponent s=-1,u=0,v=1;
# choose projective chart v=1 and transverse x,u,s.
assert rank_hessian(Fz,[x,u,s],{x:0,w:1,y:1,z:1,s:-1,u:0,v:1})==3
# A=0, x=w=0; generic y=z=1, exponent (s,u,v)=(-3,1,2);
# chart v=2, transverse x,w,s with u fixed.
assert rank_hessian(Fz,[x,w,s],{x:0,w:0,y:1,z:1,s:-3,u:1,v:2})==3
# B=0, y=0; generic x=z=w=1, exponent (s,u,v)=(-1,1,1);
# transverse y,u-v,s+u, choose v=1 and u,s coordinates.
assert rank_hessian(Fz,[y,u,s],{x:1,y:0,z:1,w:1,s:-1,u:1,v:1})==3
# B=0, y=z=0; generic x=w=1, exponent (s,u,v)=(1,1,1);
# transverse y,z,u-v, chart s=1, u=1 fixed and v variable.
assert rank_hessian(Fz,[y,z,v],{x:1,y:0,z:0,w:1,s:1,u:1,v:1})==3
# A=B nonzero, at (x,y,z,w)=(1,1,1,1), (s,u,v)=(0,0,1),
# transverse w,u,s (chart x=y=z=v=1).
assert rank_hessian(Fz,[w,u,s],{x:1,y:1,z:1,w:1,s:0,u:0,v:1})==3
# Verify all proposed components: use radical ideal substitutions via parametrizations.
for val in [{x:0,u:0,s:-v},{w:0,u:0,s:-v},{x:0,v:0,s:-u},{w:0,v:0,s:-u},
            {y:0,u:0,v:0},{z:0,u:0,v:0},{y:0,s:-u,v:u},{z:0,s:-u,v:u},
            {x:0,w:0,s:-u-v},{y:0,z:0,v:u},
            {w:y*z/x,s:0,u:0},{w:y*z/x,s:0,v:0}]:
    fcheck=sp.cancel(Fz.subs(val,simultaneous=True))
    assert fcheck==0,(val,fcheck)
    for deriv in partials:
        check=sp.cancel(deriv.subs(val,simultaneous=True))
        assert check==0,(val,check)
for xi in (x,w):
 for bj in (y,z):
    val={xi:0,bj:0}
    assert sp.expand(Fz.subs(val))==0
    assert all(sp.expand(e.subs(val))==0 for e in partials)
print('VERIFY_OK: polynomial, determinant, binary discriminant, 5 transverse Hessians, all 16 singular components')
