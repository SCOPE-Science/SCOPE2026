import numpy as np
from scipy.linalg import expm
from scipy.sparse import lil_matrix

for L in range(3,9):
  A=np.zeros((L,L))
  for i in range(L):
    A[i,i]=-2
    for j,sign in (((i-1)%L, -1 if i==0 else 1), ((i+1)%L,-1 if i==L-1 else 1)):
      A[i,j]+=sign
  heat=expm(.73*A)
  G=-np.linalg.inv(A)
  for parity in (0,1):
    states=[s for s in range(1<<L) if s.bit_count()%2==parity]
    ind={s:j for j,s in enumerate(states)}
    Q=lil_matrix((len(states),len(states)),dtype=float)
    for x,s in enumerate(states):
      for k in range(L-1):
        if ((s>>k)&1)!=((s>>(k+1))&1):
          Q[x,ind[s^((1<<k)|(1<<(k+1)))]]+=1
          Q[x,x]-=1
      if (s&1)==((s>>(L-1))&1):
        Q[x,ind[s^1^(1<<(L-1))]]+=1
        Q[x,x]-=1
    Q=Q.toarray()
    spin=np.array([[1-2*((s>>i)&1) for i in range(L)] for s in states])
    C=(spin.T@expm(.73*Q)@spin)/len(states)
    assert np.max(np.abs(C-heat))<2e-13,(L,parity,'cov',np.max(abs(C-heat)))
    assert np.max(abs(Q@spin-spin@A))<1e-12
    # independent integrated covariance via spectral eigenvectors of full sector generator, removing null mode
    w,U=np.linalg.eigh(-Q)
    invw=np.where(w>1e-8,1/np.maximum(w,1e-30),0)
    Cint=spin.T@((U*invw)@U.T)@spin/len(states)
    assert np.max(abs(Cint-G))<1e-10,(L,parity,'int',np.max(abs(Cint-G)))
    assert np.max(abs(G-np.array([[L/4-abs(i-j)/2 for j in range(L)] for i in range(L)])))<1e-12
    for i in range(L):
      for j in range(L):
        d=abs(i-j)
        if d<L/2: assert C[i,j]>0
        elif d>L/2: assert C[i,j]<0
        else: assert abs(C[i,j])<1e-13
    gtot=float(np.ones(L)@G@np.ones(L))
    assert abs(gtot - L*(L*L+2)/12)<1e-11
  print('PASS L=',L,'both parities; independent full Markov matrix, covariance, exact Green, sign')
