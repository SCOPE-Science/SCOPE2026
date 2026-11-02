"""Independent numerical tests of a rotated-dephasing qubit channel and its entanglement-breaking crossover."""
import math, numpy as np
from numpy.linalg import svd
from scipy.linalg import expm
from scipy.optimize import brentq

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
P=[X,Y,Z]

def channel(lam, theta, A):
    U=math.cos(theta/2)*I-1j*math.sin(theta/2)*Y
    return U@((1+lam**2)/2*A+(1-lam**2)/2*Z@A@Z)@U.conj().T

def blok(lam,theta):
    return np.array([[lam**2*math.cos(theta),math.sin(theta)],[-lam**2*math.sin(theta),math.cos(theta)]])

def trnorm_closed(lam,theta,n):
    x=(lam+1/lam)*math.cos(theta)/2
    if n==1: u=1
    else:
        um2=0.; um1=1.
        for j in range(2,n+1):
            um2,um1=um1,2*x*um1-um2
        u=um1
    return lam**n*math.hypot(2,(1/lam-lam)*u)+lam**(2*n)

def choi(lam,theta,n):
    basis=[np.array([[1.,0],[0,0]],complex),np.array([[0,1],[0,0]],complex),np.array([[0,0],[1,0]],complex),np.array([[0,0],[0,1]],complex)]
    target=np.zeros((4,4),complex)
    for a in range(2):
      for b in range(2):
        mat=basis[2*a+b]
        for _ in range(n):mat=channel(lam,theta,mat)
        target+=np.kron(mat,basis[2*a+b])/2
    return target

def ppt(lam,theta,n):
    C=choi(lam,theta,n)
    return np.linalg.eigvalsh(C.reshape(2,2,2,2).transpose(2,1,0,3).reshape(4,4)).min()

if __name__=='__main__':
    rng=np.random.default_rng(40)
    assertions=0
    for _ in range(400):
        lam=rng.uniform(.1,.95);theta=rng.uniform(-3.05,3.05); n=int(rng.integers(1,15))
        M=blok(lam,theta)
        exact=np.linalg.svd(np.linalg.matrix_power(M,n),compute_uv=False).sum()+lam**(2*n)
        closed=trnorm_closed(lam,theta,n)
        assert abs(exact-closed)<3.e-10*max(1,exact),(lam,theta,n,exact,closed)
        assertions+=1
        if n<=7:
          neg=ppt(lam,theta,n)
          assert (closed<=1+1e-8)==(neg>=-1e-8),(lam,theta,n,closed,neg)
          assertions+=1
    for c in [.1,.3,.7,1.,1.4,2.,4.]:
      def s(t):
        if abs(c-1.)<1.e-15:return t
        if c<1:
            k=math.sqrt(1-c*c);return math.sinh(k*t)/k
        k=math.sqrt(c*c-1);return math.sin(k*t)/k
      def f(t): return 2*math.exp(-t)*math.hypot(1,s(t))+math.exp(-2*t)-1
      tc=brentq(f,0,100)
      for delta in [.004,.002,.001]:
         lam=1-delta;theta=c*delta
         n=1
         # robust direct matrix powers for n large rather than Cheb unbounded
         M=blok(lam,theta); T=np.eye(2)
         while True:
             T=M@T
             g=np.linalg.svd(T,compute_uv=False).sum()+lam**(2*n)
             if g<=1:break
             n+=1
             if n>20000:raise RuntimeError('not EB')
         assert abs(delta*n-tc)<.03, (c,delta,n,tc)
         assertions+=1
      print('c=',c,'t_c=',round(tc,10),'n(delta=0.001)=',n,'scaled=',round(n*.001,4))
    # Exact EP condition and Jordan coefficient check
    for lam in [.2,.5,.8,.97]:
        theta=2*math.atan((1-lam)/(1+lam)); M=blok(lam,theta)
        N=M-lam*np.eye(2)
        assert np.linalg.norm(N@N)<1.e-13; assertions+=1
        assert abs(np.linalg.norm(N,'fro')-(1-lam**2))<1.e-12;assertions+=1
    print('ALL_ASSERTIONS',assertions)
