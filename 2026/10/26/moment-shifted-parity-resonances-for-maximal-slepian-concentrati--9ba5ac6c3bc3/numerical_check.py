import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh
from scipy.optimize import brentq

def main():
 B=1.0; ell=0.8; nquad=64
 nodes,weight=leggauss(nquad)
 x=ell/2*nodes; w=ell/2*weight
 rootw=np.sqrt(w)
 X=x[:,None]; Y=x[None,:]
 A=B*np.sinc(B*(X-Y))*rootw[:,None]*rootw[None,:]
 evals, evecs=eigh(A)
 u=evecs[:,-1]
 if sum(rootw*u)<0:u=-u
 M=np.dot(rootw*u,np.cos(np.pi*B*x))
 M1=np.dot(rootw*u,x*np.sin(np.pi*B*x))
 print('B',B,'ell',ell,'lambda0',evals[-1],'gap',evals[-1]-evals[-2],'M',M,'M1',M1)
 def diff(L):
  C=B*np.sinc(B*(2*L+X+Y))*rootw[:,None]*rootw[None,:]
  return eigh(A+C,eigvals_only=True)[-1]-eigh(A-C,eigvals_only=True)[-1]
 for n in [6,10,20,40,80]:
  base=n/(2*B)
  root=brentq(diff,base-.15,base+.15,xtol=1e-12)
  prediction=base+M1/(np.pi*M*n)
  print(n,'root',root,'base',base,'shift',root-base,'pred',prediction,'error',root-prediction,'gap from rest',evals[-1]-evals[-2])
if __name__=='__main__':main()
