"""Reproducible exact algebra checks for the two-agent gradient-tracking frontier."""
import sympy as s
import numpy as np
lam, d, z = s.symbols('lam d z')
M=s.Matrix([[0,d*(lam-1),-d*lam],[0,lam,-lam],[-d,lam-1,0]])
p=s.expand(M.charpoly(z).as_expr())
assert s.expand(p-(z**3-lam*z**2+lam*(lam-1-d**2)*z+lam*d**2))==0
coef_a,coef_b,coef_c=[p.coeff(z,j) for j in (2,1,0)]
J=s.factor(1-coef_b+coef_a*coef_c-coef_c**2)
assert s.simplify(J-(1+lam-lam**2+lam*(1-lam)*d**2-lam**2*d**4))==0
assert s.simplify(p.subs(z,1)-(1-lam)**2)==0
assert s.simplify(-p.subs(z,-1)-(1+lam**2-2*lam*d**2))==0
v1=s.Matrix([1,0,d]);v2=s.Matrix([d,1,1])
assert s.simplify(s.det(s.Matrix.hstack(v1,v2,M*v2))-(lam-1))==0
# Invariant primal/gradient coordinates, including arbitrary heterogeneous centers.
h1,h2,b1,b2,xc,xd,zzc,zzd=s.symbols('h1 h2 b1 b2 xc xd zzc zzd')
hbar=(h1+h2)/2; delta=(h1-h2)/(h1+h2)
L=s.symbols('L')
x1,x2=xc+xd,xc-xd
y1,y2=hbar*(zzc+zzd),hbar*(zzc-zzd)
# With alpha=1/hbar, scaled trackers are (zzc+zzd), (zzc-zzd).
x1new=s.expand((1+L)/2*(x1-(zzc+zzd))+(1-L)/2*(x2-(zzc-zzd)))
x2new=s.expand((1-L)/2*(x1-(zzc+zzd))+(1+L)/2*(x2-(zzc-zzd)))
y1new=(1+L)/2*y1+(1-L)/2*y2+h1*(x1new-x1)
y2new=(1-L)/2*y1+(1+L)/2*y2+h2*(x2new-x2)
zcnew=s.simplify((y1new+y2new)/(2*hbar))
zdnew=s.simplify((y1new-y2new)/(2*hbar))
assert s.simplify((x1new-x2new)/2-L*(xd-zzd))==0
assert s.simplify(zcnew-delta*((L-1)*xd-L*zzd))==0
assert s.simplify(zdnew-(-delta*zzc+(L-1)*xd))==0
for L0,d0,want in [(-.5,0.5,True),(-.5,0.6,False),(-.25,.99,True),(-.65,0,False),(.25,.99,True),(0,.99,True)]:
 mm=np.array(M.subs({lam:L0,d:d0}),dtype=float)
 rho=max(abs(np.linalg.eigvals(mm)))
 assert (rho<1)==want,(L0,d0,rho,want)
 print('spectrum',L0,d0,rho)
t=s.symbols('t',positive=True)
Jneg=s.factor(J.subs({lam:-t,d**2:s.Symbol('u')}))
assert s.expand(Jneg-(1-t-t**2-t*(1+t)*s.Symbol('u')-t**2*s.Symbol('u')**2))==0
print('SYMBOLIC_IDENTITY_AND_INITIALIZATION_CYCLICITY_OK')
