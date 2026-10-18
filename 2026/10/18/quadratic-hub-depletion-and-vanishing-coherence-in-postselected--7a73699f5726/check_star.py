"""Reproducible checks of finite postselected QSW star theorem (NumPy/SciPy)."""
import numpy as np
from scipy.linalg import eig, eigvals

def red(m,p,eta):
    w=1-p; c=1-eta; A=m+eta*m*m; B=1+eta; G=(m*m+m+2)/2
    return np.array([[-p*A,p*c*m,0,2*w*m,0],
                     [p*c,-p*B,0,-2*w,0],
                     [0,0,-p*G,w*(m-1),0],
                     [-w,w,-w*(m-1),-p*G,w*(m-1)],
                     [0,0,0,-2*w,-2*p]],float)

def solve(m,p,eta):
    A=red(m,p,eta); e,v=eig(A); k=np.argmax(e.real)
    assert abs(e[k].imag)<1e-7
    z=v[:,k].real
    z=z/(z[0]+m*z[1]); lam=e[k].real
    return lam,z

def full(m,p,eta):
    n=m+1; adj=np.zeros((n,n)); adj[0,1:]=1;adj[1:,0]=1
    H=np.diag(adj.sum(axis=1))-adj
    jumps=[]
    for j in range(n):
      for k in range(n):
        if H[k,j]:
          P=np.zeros((n,n));P[k,j]=H[k,j]; jumps.append(P)
    G=sum((P.T@P for P in jumps), np.zeros((n,n)))
    def L(X):
      return (-1j*(1-p)*(H@X-X@H)
              -p/2*(G@X+X@G)
              +p*(1-eta)*sum((P@X@P.T for P in jumps),np.zeros_like(X)))
    S=np.zeros((n*n,n*n),complex)
    for i in range(n*n):
       X=np.zeros((n,n),complex); X.flat[i]=1;S[:,i]=L(X).ravel()
    E,V=eig(S);k=E.real.argmax(); Y=V[:,k].reshape((n,n))
    Y=(Y+Y.conj().T)/2;Y/=np.trace(Y).real
    return E[k],Y,L

def state(m,z):
    a,b,u,v,d=z;n=m+1;X=np.full((n,n),d,dtype=complex)
    np.fill_diagonal(X,b);X[0,0]=a
    X[0,1:]=u+1j*v;X[1:,0]=u-1j*v
    return X
count=0
for m in [2,3,4,6]:
  for p in [.2,.5,1.]:
    for eta in [.1,.5,.9]:
      lam,z=solve(m,p,eta)
      E,X,L=full(m,p,eta)
      assert abs(E-lam)<1e-8,(m,p,eta,E,lam)
      Y=state(m,z)
      assert np.linalg.norm(L(Y)-lam*Y)<2e-8,(m,p,eta,np.linalg.norm(L(Y)-lam*Y))
      assert np.linalg.norm(X-Y)<2e-7,(m,p,eta,np.linalg.norm(X-Y))
      assert np.linalg.eigvalsh(Y).min()>0,(m,p,eta,np.linalg.eigvalsh(Y))
      count+=4
for p in [.25,.5,.85,1.]:
 for eta in [.2,.5,.85]:
   m=10000
   lam,z=solve(m,p,eta);a,b,u,v,d=z
   c=1-eta;w=1-p
   assert abs(m*m*a-c/eta)<0.018*max(1,c/eta)
   assert abs(m**3*v-2*w/p)<0.07*max(1,2*w/p)
   assert abs(m**3*d+4*w*w/(p*p*c))<0.07*max(1,4*w*w/(p*p*c))
   assert abs((lam+p*(1+eta))*m-p*c*c/eta)<0.07*max(1,p*c*c/eta)
   count+=4
for p in [.25,.5,.85,1.]:
 for xi in [.1,1,5]:
   for m in [10000]:
    eta=xi/m;lam,z=solve(m,p,eta)
    a,b,*_=z
    assert abs(m*a-1/(1+xi))<.003,(p,xi,m,m*a)
    assert abs(lam+p*xi/(1+xi))<.003,(p,xi,m,lam)
    count+=2
print('Passed',count,'full operator, asymptotic, and crossover assertions')
