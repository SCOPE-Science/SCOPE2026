"""Reproduce the exact local mean-square stability frontier for the indicated two-dimensional Itô system."""
import sympy as sp
import numpy as np

u,c,P,Q=sp.symbols('u c P Q', positive=True)
z=(3*u*u-1)/2
b=u
d=c*(1-u*u)/2
h=b*d
delta=2*z-P
K=sp.Matrix([[P-2*z,-2*b,0],[d,-z,-b],[0,2*d,Q]])
poly=sp.Poly(K.charpoly().as_expr(),sp.Symbol('lambda')).all_coeffs()
assert sp.simplify(poly[3]-(2*h*delta-Q*(2*h+z*delta)))==0
assert sp.simplify(poly[2]-(4*h+z*delta-(z+delta)*Q))==0
assert sp.simplify(poly[1]-(z+delta-Q))==0
A=sp.Matrix([[-z,-b],[d,0]])
Heta,Hzeta=sp.symbols('eta zeta',real=True)
H=sp.Matrix([[1,Heta],[Heta,Hzeta]])
E1=sp.diag(1,0);E2=sp.diag(0,1)
L=sp.simplify(A.T*H+H*A+P*E1*H*E1+Q*E2*H*E2)
assert sp.simplify(L[0,0]-(P-2*z+2*d*Heta))==0
assert sp.simplify(L[1,1]-(-2*b*Heta+Q*Hzeta))==0
assert sp.simplify(L[0,1]-(-b-z*Heta+d*Hzeta))==0
case_count=0
for v in np.linspace(.59,.99,9):
 for cc in (.1,.7,1,3,20):
  zz=(3*v*v-1)/2; bb=v;dd=cc*(1-v*v)/2;hh=bb*dd
  for pp in (0,.15*2*zz,.7*2*zz,.99*2*zz,1.05*2*zz):
   D=2*zz-pp
   if D<=0:continue
   qc=2*hh*D/(2*hh+zz*D)
   for scale in (0,.15,.5,.99,1,1.01,1.5):
    case_count+=1
    qq=qc*scale
    KK=np.array([[pp-2*zz,-2*bb,0],[dd,-zz,-bb],[0,2*dd,qq]])
    stable=np.max(np.linalg.eigvals(KK).real)<-1e-9
    expected=scale<1
    if scale==1: assert abs(np.linalg.det(KK))<1e-7*max(1,np.linalg.norm(KK)**3)
    else: assert stable==expected,(v,cc,pp,qq,stable,expected)
    if scale<1:
     low=qq*bb/(2*hh-qq*zz) if qq>0 else 0
     up=D/(2*dd)
     eta=(low+up)/2
     zzeta=(bb+zz*eta)/dd
     HH=np.array([[1,eta],[eta,zzeta]])
     AA=np.array([[-zz,-bb],[dd,0]])
     GG1=np.diag([1,0]);GG2=np.diag([0,1])
     LL=AA.T@HH+HH@AA+pp*GG1@HH@GG1+qq*GG2@HH@GG2
     assert np.linalg.eigvalsh(HH).min()>-1e-8,('H',v,cc,pp,qq)
     assert np.linalg.eigvalsh(LL).max()<1e-7,('L',v,cc,pp,qq)
print(f'VERIFY_OK exact second-moment characteristic polynomial, Lyapunov identities, and {case_count} numerical parameter-grid cases')
