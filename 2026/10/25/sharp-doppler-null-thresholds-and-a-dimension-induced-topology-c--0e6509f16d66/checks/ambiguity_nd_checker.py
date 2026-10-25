import numpy as np
import sympy as sp
from numpy.polynomial.hermite import hermgauss
c,d,X,Y,Z=sp.symbols('c d X Y Z', real=True)
a=4*c+2*d-4
C=16*c*c+16*c*d+4*d*(d+2)
P=(X-Y)**2+4*Z+(8*c+4*d-8)*X-(8*c+4*d+8)*Y+C
assert sp.expand(P-((X-Y+a)**2+4*Z-16*(Y+1-2*c-sp.Rational(3,2)*d)))==0
Y0=2*c+sp.Rational(3,2)*d-1
assert sp.simplify(Y0-a)==3-2*c-d/2
Yminus=4*c+2*d+4-2*sp.sqrt(2*(4*c+d+2))
assert sp.simplify(P.subs({X:0,Z:0,Y:Yminus}))==0
for dim,cval,tt,ww in [
 (1,0.1,[0.9],[1.5]),
 (2,0.5,[1.0,0.2],[0.4,1.3]),
 (2,3,[2.0,0],[0,5]),
 (3,0.9,[0.8,-0.1,0.3],[0.4,1.1,-0.9]),
 (3,3,[1.0,2.0,0.2],[0.1,-0.9,1.2]),
]:
 n=72 if dim<3 else 36
 nodes,weights=hermgauss(n)
 x=np.stack(np.meshgrid(*([nodes]*dim),indexing='ij'),axis=-1).reshape(-1,dim)
 W=np.prod(np.stack(np.meshgrid(*([weights]*dim),indexing='ij'),axis=-1),axis=-1).ravel()
 t=np.array(tt); w=np.array(ww)
 v1=np.sum((x+t/2)**2,axis=1)+cval
 v2=np.sum((x-t/2)**2,axis=1)+cval
 # weighted polynomial factor, Fourier complex exponential
 numerical=np.dot(W,v1*v2*np.exp(-1j*x@w))*np.exp(-np.dot(t,t)/4)
 xv=t@t; yv=w@w; zv=(t@w)**2
 pval=float(P.subs({X:xv,Y:yv,Z:zv,c:cval,d:dim}))
 predicted=np.pi**(dim/2)*np.exp(-(xv+yv)/4)*pval/16
 assert abs(numerical-predicted)<1e-10,(dim,numerical,predicted)
for dim in [2,3,4,7,12]:
 for cval in [.01,.25,1,5.]:
  c0=float(cval); a0=4*c0+2*dim-4; y0=2*c0+1.5*dim-1
  lower=float((4*c+2*d+4-2*sp.sqrt(2*(4*c+d+2))).subs({c:c0,d:dim}))
  miny=y0 if dim+4*c0<=6 else lower
  assert miny>0
  for y in [miny+1e-4,miny+0.1,miny+5,miny+10000]:
   # Orthogonal geometry, one of the two X branches is nonnegative.
   r=np.sqrt(16*(y-y0))
   h=-a0+r
   xv=y+h
   assert xv>=-1e-8
   zz=0
   pp=float(P.subs({X:xv,Y:y,Z:zz,c:c0,d:dim}))
   assert abs(pp)<2e-6,(dim,c0,y,pp)
print('PASS: dimension-uniform completed-square identity, exact frequency thresholds, 5 multidimensional quadratures, 80 orthogonal zero witnesses')
