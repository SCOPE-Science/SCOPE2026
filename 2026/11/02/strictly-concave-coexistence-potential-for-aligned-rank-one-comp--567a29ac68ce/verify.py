from fractions import Fraction as F
import numpy as np
from scipy.optimize import brentq, minimize

def calc(a,beta,u,v,delta,h):
 n=len(u)
 C=np.array(a,float)
 s=1/(1+np.sum((u[:,None]/delta)*C,axis=1))
 X=s[:,None]*(u[:,None]/delta)*C
 assert np.max(abs(beta*(v@X)-C))<1e-6
 assert np.all(X>0) and np.all(s>0)
 M=2*n;J=np.zeros((M,M))
 for ell in range(2):
  for i in range(n):
   row=ell*n+i
   for m in range(2):
    for j in range(n):
     col=m*n+j
     J[row,col]=(s[i]*beta[ell]*u[i]*v[j] if ell==m else 0) - (delta[i,ell] if ell==m and i==j else 0) - (u[i]*C[ell] if i==j else 0)
 W=np.array([v[i]/(s[i]*u[i]*C[ell]) for ell in range(2) for i in range(n)])
 assert np.linalg.norm(W[:,None]*J-(W[:,None]*J).T)<1e-10
 e=np.linalg.eigvalsh(np.sqrt(W)[:,None]*J/np.sqrt(W)[None,:])
 assert np.max(e)<0,(e,C)
 assert max(abs(np.linalg.eigvals(np.eye(M)+h*J)))<1
 return X,s,e
# Exact-rational stationarity for the stated two-node example.
xe=[[F(4,25),F(1,25)],[F(1,25),F(4,25)]]
recovery=[[F(1),F(4)],[F(4),F(1)]]
for i in range(2):
 for ell in range(2):
  susceptible=F(1)-sum(xe[i])
  force=sum(xe[j][ell] for j in range(2))
  assert -recovery[i][ell]*xe[i][ell]+susceptible*force==0
assert sum(xe[0])==F(1,5) and sum(xe[1])==F(1,5)
u=np.array([1.,1.]);v=np.array([1.,1.]);delta=np.array([[1.,4.],[4.,1.]])
x,s,e=calc([.2,.2],np.array([1.,1.]),u,v,delta,1/16)
print('Example X, S, eigs=',x,s,e)
for ell in range(2):
 C0=brentq(lambda C: np.sum(v*u/delta[:,ell]/(1+u*C/delta[:,ell]))-1,1e-10,4)
 other=1-ell
 Rinv=sum(v*u/delta[:,other]/(1+u*C0/delta[:,ell]))
 print('on axis',ell,'force',C0,'opposite invasion',Rinv)

# random strict concave rank-one examples: maximize on quadrant, validate KKT/necessary and resulting J
rng=np.random.default_rng(41444); accepted=0
for _ in range(300):
 n=int(rng.integers(2,8));u=rng.uniform(.2,2,n);v=rng.uniform(.2,2,n)
 delta=rng.uniform(.25,3,(n,2)); beta=rng.uniform(.2,3,2)
 a=u[:,None]/delta
 if np.linalg.matrix_rank(a)<2:continue
 fun=lambda C: -sum(v*np.log1p(a@C))+sum(C/beta)
 grad=lambda C: -a.T@(v/(1+a@C))+1/beta
 ans=minimize(fun, np.array([.3,.3]),jac=grad,bounds=[(0,None)]*2,method='L-BFGS-B',options={'ftol':1e-13,'gtol':1e-11})
 if np.min(ans.x)>1e-3 and np.linalg.norm(grad(ans.x))<1e-7:
  h=min(1/(delta[i,ell]+u[i]*sum(beta)*sum(v)) for i in range(n) for ell in range(2))/2
  X,s,e=calc(ans.x,beta,u,v,delta,h)
  accepted+=1
print('random verified interior configurations',accepted)
