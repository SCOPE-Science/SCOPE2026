import numpy as np
from scipy.linalg import solve

def independent_full(m,J,k,gL,gH):
    N=m+1
    H=np.zeros((N,N),dtype=complex)
    H[0,1:]=J;H[1:,0]=J
    I=np.eye(N,dtype=complex)
    # column-major vectorization
    L=-1j*(np.kron(I,H)-np.kron(H.T,I))
    rates=[gH]+[gL]*m
    for q,r in enumerate(rates):
        P=np.zeros((N,N),complex); P[q,q]=1
        L+=r*(np.kron(P.T,P)-.5*(np.kron(I,P)+np.kron(P.T,I)))
    P=np.zeros((N,N),complex);P[0,0]=1
    L-=k/2*(np.kron(I,P)+np.kron(P.T,I))
    rho=np.zeros((N,N),complex);rho[1,1]=1
    M=solve(-L,rho.reshape(N*N,order='F')).reshape((N,N),order='F')
    return M.trace().real, M

def formula(m,J,k,gL,gH):
    return (m+1)/k+(m-1)/gL+(k+gL+gH)/(4*J**2)

if __name__=='__main__':
    import random
    random.seed(42)
    count=0
    for m in range(2,9):
      for t in range(12):
        J=10**random.uniform(-.8,.8);k=10**random.uniform(-.8,.8)
        gL=10**random.uniform(-1,1);gH=10**random.uniform(-2,1)
        val,_=independent_full(m,J,k,gL,gH)
        predicted=formula(m,J,k,gL,gH)
        if abs(val-predicted)>2e-8*max(1,val):
            print('FAIL',m,J,k,gL,gH,val,predicted);raise SystemExit(1)
        count+=1
    print('PASS full Liouvillian',count)
    for m in [2,3,4,10,25,100]:
      J=1.7; k=2*J*np.sqrt(m+1);g=2*J*np.sqrt(m-1)
      t=formula(m,J,k,g,0)
      optimum=(np.sqrt(m+1)+np.sqrt(m-1))/J
      assert abs(t-optimum)<1e-12
      assert formula(m,J,k,g*1.02,0)>t
      assert formula(m,J,k*1.02,g,0)>t
    print('PASS analytic optimum',6)
