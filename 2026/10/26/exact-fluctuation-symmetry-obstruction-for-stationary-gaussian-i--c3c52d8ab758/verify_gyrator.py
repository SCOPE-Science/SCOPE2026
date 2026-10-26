import numpy as np
from scipy.linalg import solve_continuous_lyapunov
from numpy.linalg import eigvalsh,det
from sympy import symbols,diff,factor
J=np.array([[0.,1.],[-1.,0.]])
N=0

def check(f,comment):
 global N
 if not f: raise AssertionError(comment)
 N+=1
h,a,b,s=symbols('h a b s',real=True,nonzero=True)
F=(1-2*h*s-a*s*s)*(1-2*h*s-b*s*s)
c=-h*(a+b)/(2*a*b)
check(factor(diff(F,s,3).subs(s,c))==0,'third derivative')
check(factor(diff(F,s).subs(s,c)-h*(a-b)**2*(a*b+h*h*(a+b))/(a*a*b*b))==0,'first derivative')
for kappa in [0.2,0.7,1.5]:
 for gamma in [0.5,1,2.5]:
  for Ta,Tb in [(0.5,2.),(1.,5.),(2.,0.3)]:
   K=np.array([[2.,kappa],[kappa,1.5]])
   A=np.block([[np.zeros((2,2)),np.eye(2)],[-K,-gamma*np.eye(2)]])
   Q=np.diag([0.,0.,2*gamma*Ta,2*gamma*Tb])
   Sigma=solve_continuous_lyapunov(A,-Q)
   C=Sigma[:2,:2]; D=Sigma[:2,2:]; E=Sigma[2:,2:]
   check(np.linalg.norm(A@Sigma+Sigma@A.T+Q)<1e-9,'stationarity')
   check(np.linalg.norm(D+D.T)<1e-9,'skew')
   check(eigvalsh(Sigma).min()>0,'cov pos')
   hh=D[0,1]
   R=E-D.T@np.linalg.solve(C,D)
   lam=eigvalsh(np.linalg.cholesky(C).T@J@R@J.T@np.linalg.cholesky(C))
   check(lam.min()>0,'schur positive')
   H=np.zeros((4,4)); H[:2,2:]=J/2; H[2:,:2]=J.T/2
   for ss in [-0.035,0.02,0.051]:
    mgfdet=1/np.sqrt(det(np.eye(4)-2*ss*Sigma@H))
    mgf=1/np.sqrt(np.prod(1-2*hh*ss-lam*ss*ss))
    check(abs(mgfdet-mgf)<3e-11,'mgf')
   check(abs(2*hh-np.trace(Sigma@H))<1e-9,'mean')
   check(abs(4*hh*hh+sum(lam)-2*np.trace((Sigma@H)@(Sigma@H)))<1e-9,'var')
for eps in [0.01,0.1,0.5,1.,4.]:
 k=1+eps
 A=np.block([[np.zeros((2,2)),np.eye(2)],[-k*np.eye(2)+J,-np.eye(2)]])
 Q=np.diag([0.,0.,2*eps,2*eps]);Sigma=solve_continuous_lyapunov(A,-Q)
 exact=np.block([[np.eye(2),-J],[J,k*np.eye(2)]])
 check(np.max(abs(Sigma-exact))<3e-12,'sharpness example')
 C=Sigma[:2,:2];D=Sigma[:2,2:];E=Sigma[2:,2:]
 R=E-D.T@np.linalg.solve(C,D)
 check(np.max(abs(R-eps*np.eye(2)))<3e-12,'lambda example')
print(f'{N} deterministic analytic/numerical checks passed')
