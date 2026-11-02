# Python 3 and NumPy; independent finite tests only, not a proof.
import math
import numpy as np

def distance_matrix(n):
    nodes=[('A',i,-1) for i in range(n)]+[('B',j,-1) for j in range(n)]+[('E',i,j) for i in range(n) for j in range(n)]
    t=len(nodes)
    D=np.zeros((t,t),dtype=np.float64)
    for a,(k,i,j) in enumerate(nodes):
      for b,(h,x,y) in enumerate(nodes):
       if a==b: continue
       if k in 'AB' and h in 'AB':
         d=4 if k==h else 2
       elif k=='E' and h=='E':
         d=2 if (i==x or j==y) else 4
       else:
         orig=(k,i) if k!='E' else (h,x)
         edge=(x,y) if h=='E' else (i,j)
         d=1 if (orig[0]=='A' and orig[1]==edge[0]) or (orig[0]=='B' and orig[1]==edge[1]) else 3
       D[a,b]=d
    return D

def sector_data(n,p):
 a=2.0**p;b=3.0**p;c=4.0**p
 W=c-2*a
 block=np.array([[-c,(1-b)*math.sqrt(n)],[(1-b)*math.sqrt(n),n*(a-c)+c-2*a]])
 beta=math.log2(n/(n-1))
 q_diff=2*n*((n-1)*c-n*a)
 q_rest=2*(n-1)*(3*n-2)*c+2*(n*n+4*n-4)*a-8*n*(n-1)*b-8*n
 return W, np.linalg.eigvalsh(block),q_diff,q_rest

def test():
 for n in range(2,12):
  p=math.log2(n/(n-1))
  D=distance_matrix(n)**p
  H=np.eye(len(D))-np.ones_like(D)/len(D)
  eig=np.linalg.eigvalsh(H@D@H)
  z=sum(abs(v)<2e-7 for v in eig)
  expected=4 if n==2 else 2 # includes all-ones
  assert z==expected,(n,z,eig[-8:])
  assert eig[-1]<1e-7,(n,eig[-1])
  W,E,qd,qr=sector_data(n,p)
  assert W<1e-10 and max(E)<1e-10 and abs(qd)<1e-6 and qr<1e-8
  above=np.linalg.eigvalsh(H@(distance_matrix(n)**(p+1e-3))@H)
  assert above[-1]>1e-5
  print(n,len(D),round(p,12),z,'lambdaMax',f'{eig[-1]:.2e}')
if __name__=='__main__':test()
