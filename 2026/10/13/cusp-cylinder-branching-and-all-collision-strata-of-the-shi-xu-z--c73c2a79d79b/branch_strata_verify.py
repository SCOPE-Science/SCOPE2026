"""Exact polynomial checks for the branch/collision stratification of a finite map.
Python 3 and SymPy required. All identities are over Q; geometry is over C.
"""
import sympy as sp
u,v,w,x,y,z=sp.symbols('u v w x y z')
F=sp.Matrix([y,y*z-x**2,z**2+y*x**2+y**2*z+x**3])
J=sp.factor(F.jacobian([x,y,z]).det())
assert J==x*(3*x*y+4*y**2+4*z)
B=v**2+u**3*v-u**2*w
Q=(32*u**9-256*u**8+27*u**7*v-192*u**6*v-27*u**6*w
   -512*u**5*v+288*u**5*w+27*u**4*v**2-512*u**4*w
   -480*u**3*v**2-256*u**2*v**2+288*u**2*v*w-512*u*v*w
   -256*v**3-256*w**2)
S=9*u**4-64*u**3-64*v
T=512*w+u*(27*u**5-288*u**4+512*u**3-288*u*v+512*v)
assert sp.expand(S**3-T**2-1024*Q)==0
p=x**4+u**2*x**3+2*(v+u**3)*x**2+B
assert sp.factor(p.subs({u:y,v:y*z-x**2,w:z**2+y*x**2+y**2*z+x**3}))==0
assert sp.factor(sp.discriminant(p,x)+u**4*B*Q)==0
assert sp.factor(sp.together(u**4*Q.subs(w,(v**2+u**3*v)/u**2))-32*(u**3+v)**3*(u**4-8*u**3-8*v))==0
v31,w31=-u**3,sp.S.Zero
v22,w22=u**3*(u-8)/8,u**5*(u-8)/64
assert sp.factor(p.subs({v:v31,w:w31})-x**3*(x+u**2))==0
assert sp.factor(p.subs({v:v22,w:w22})-x**2*(x+u**2/2)**2)==0
assert sp.simplify(S.subs({v:v31,w:w31})-9*u**4)==0
assert sp.simplify(T.subs({v:v31,w:w31})-27*u**6)==0
assert sp.simplify(S.subs({v:v22,w:w22})-u**4)==0
assert sp.simplify(T.subs({v:v22,w:w22})+u**6)==0
vc=(9*u**4-64*u**3)/64
wc=sp.solve(T.subs(v,vc),w)[0]
assert sp.factor(B.subs({v:vc,w:wc})+27*u**8/4096)==0
assert sp.factor(p.subs({v:vc,w:wc}).subs(x,-3*u**2/8))==0
assert sp.factor(sp.diff(p,x).subs({v:vc,w:wc}).subs(x,-3*u**2/8))==0
assert sp.factor(sp.diff(p,x,2).subs({v:vc,w:wc}).subs(x,-3*u**2/8))==0
assert sp.factor(sp.diff(p,x,3).subs({v:vc,w:wc}).subs(x,-3*u**2/8))!=0
# At u=0, equations give x^2=-v and z^2=w-x^3.
# v=w=0 yields Q[x,z]/(x^2,z^2), length 4 at one point;
# v=0,w!=0 gives two points of length 2;
# v!=0,w^2=-v^3 gives one length-2 and two length-1 points.
assert sp.factor(Q.subs(u,0)+256*(v**3+w**2))==0
assert sp.factor(B.subs(u,0)-v**2)==0
print('BRANCH_COLLISION_EXACT_OK')
