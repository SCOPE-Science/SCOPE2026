"""Numerically compare the second eigenvalue of Gaussian/Fock disk concentration on fixed-area radial deformations with analytic second-order coefficients."""
import numpy as np
from scipy.special import gammainc, gamma, gammaln

def matrix(R,eps,mode,K=24,M=1024):
    theta=np.arange(M)*2*np.pi/M
    h=np.cos(mode*theta)
    t=R+eps*h
    E=np.exp(1j*np.outer(np.arange(K),theta))
    B=np.empty((K,K),dtype=complex)
    invfac=np.exp(-0.5*gammaln(np.arange(K)+1))
    for j in range(K):
       for k in range(j,K):
          a=0.5*(j+k)+1
          integ=gammainc(a,t)*gamma(a)
          B[j,k]=invfac[j]*invfac[k]*np.mean(integ*np.exp(1j*(j-k)*theta))
          if j!=k: B[k,j]=np.conj(B[j,k])
    return B

def analytic(R,mode):
    if mode==1:return 0.
    k=mode+1
    T=np.array([R**j / float(__import__("math").factorial(j)) for j in range(2,k+1)])
    return np.exp(-R)*(1-R+R*T[-1]/sum(T))*0.25 # cos h Fourier coeff=1/2, abs squared=1/4

if __name__=='__main__':
 for R in (0.5,1.2,1.5,2.):
  for mode in (1,2,4,9):
   vals=[]
   for e in (0,0.025,-0.025,0.05,-0.05):
    E=np.linalg.eigvalsh(matrix(R,e,mode,K=24,M=512))
    vals.append(E[-2])
   cur=(vals[1]+vals[2]-2*vals[0])/(2*0.025**2)
   c2=(vals[3]+vals[4]-2*vals[0])/(2*0.05**2)
   pred=analytic(R,mode)
   print(f'R={R} mode={mode} analytic={pred:+.9e}, numerical={cur:+.9e}, h2={c2:+.9e}, diff={cur-pred:+.3e}')
