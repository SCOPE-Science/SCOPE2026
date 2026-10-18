import numpy as np
from scipy.linalg import expm
from fractions import Fraction

def p(m,n,i,j,res):
 r=int(i==0);c=int(j==0)
 off=(1 if r else 1/(m-1))*(1 if c else 1/(n-1))
 if not res:return off
 return off-(m-1)*(n-1)/(m*n*(m+n-2))*((n*c-1)/(n-1)-(m*r-1)/(m-1))**2
for m,n,gamma in [(2,2,.8),(2,3,1.2),(3,4,2.),(4,4,1.6)]:
 beta=1.2;aa=n*beta/m
 for i,j in [(0,0),(0,1),(1,0),(1,1)]:
  if i>=m or j>=n:continue
  delta=.02
  a=aa+delta/m
  H=a*np.kron(np.ones((m,m))-np.eye(m),np.eye(n))+beta*np.kron(np.eye(m),np.ones((n,n))-np.eye(n))
  H=H.astype(complex);H[0,0]-=1j*gamma/2
  v=np.eye(m*n)[:,i*n+j]
  for s in (.3,1.):
   t=s/delta**2
   actual=np.linalg.norm(expm(-1j*H*t)@v)**2
   K=4*m*n*(m-1)*(n-1)/(gamma*(m+n-2)**3)
   expected=1-p(m,n,i,j,False)+(p(m,n,i,j,False)-p(m,n,i,j,True))*np.exp(-K*s)
   assert abs(actual-expected)<.025,(m,n,i,j,s,actual,expected)
 print(m,n,'OK')
