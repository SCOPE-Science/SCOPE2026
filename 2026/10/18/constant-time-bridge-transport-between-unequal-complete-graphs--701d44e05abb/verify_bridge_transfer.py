"""Independent finite-matrix checks of a coherent transport asymptotic.
Run: python verify_bridge_transfer.py (numpy and scipy required).
Finite computations corroborate but do not prove the asymptotic theorem.
"""
import math
import numpy as np
from scipy.linalg import eigh

def full_matrix(p,q,w):
    H=np.zeros((p+q,p+q),dtype=float)
    H[:p,:p]=1-np.eye(p)
    H[p:,p:]=1-np.eye(q)
    H[0,p]=H[p,0]=w
    return H

def reduced_matrix(p,q,w):
    a,b=np.sqrt(p-1),np.sqrt(q-1)
    return np.array([[0,a,w,0],[a,p-2,0,0],[w,0,0,b],[0,0,b,q-2]],dtype=float)

def amplitude(H,origin,target,t):
    d,V=eigh(H)
    return np.dot(V[origin,:]*V[target,:],np.exp(-1j*t*d))

def low_high_block(p,q,w):
    ap,aq=math.sqrt(1-1/p),math.sqrt(1-1/q)
    ep,eq=1/math.sqrt(p),1/math.sqrt(q)
    K=np.array([[-1,w*ap*aq],[w*ap*aq,-1]])
    B=np.array([[0,w*ap*eq],[w*aq*ep,0]])
    D=np.array([[p-1,w*ep*eq],[w*ep*eq,q-1]])
    return np.block([[K,B],[B.T,D]])

def change_basis(p,q):
    # Coordinates of (v_p,v_q,u_p,u_q) in the order (a,A,b,B).
    e1,e2=1/math.sqrt(p),1/math.sqrt(q)
    a1,a2=math.sqrt(1-1/p),math.sqrt(1-1/q)
    return np.array([[a1,0,e1,0],[-e1,0,a1,0],[0,a2,0,e2],[0,-e2,0,a2]])

checks=0
for p,q in [(2,3),(3,3),(3,8),(5,7),(8,13),(15,21)]:
  for w in [0.35,1.0,1.8]:
    R=reduced_matrix(p,q,w)
    full=full_matrix(p,q,w)
    Q=change_basis(p,q)
    err=np.linalg.norm(Q.T@R@Q-low_high_block(p,q,w))
    assert err<2e-12,(p,q,w,err)
    checks+=1
    for t in (0.1,0.9,math.pi/(2*w),4.1):
      a=amplitude(full,0,p,t)
      b=amplitude(R,0,2,t)
      assert abs(a-b)<2e-12,(p,q,w,t,a,b)
      checks+=1

# An independent large-size spectral calculation probes the sharp coefficient.
rows=[]
for w in (0.4,1.0,1.7):
  for p,q in ((60,60),(80,130),(100,1000),(200,301),(500,900),(900,1300)):
    t=math.pi/(2*w)
    probability=abs(amplitude(reduced_matrix(p,q,w),0,2,t))**2
    prediction=1/p+1/q
    ratio=(1-probability)/prediction
    assert 0.92<ratio<1.13,(w,p,q,ratio)
    checks+=1
    rows.append((w,p,q,probability,ratio))
print('PASS',checks,'matrix-and-asymptotic diagnostic comparisons')
print('Selected fidelity/leading-error ratios:')
for x in rows:
  if x[1]>=200:
    print(f'w={x[0]:.1f}, p={x[1]}, q={x[2]}, probability={x[3]:.10f}, ratio={x[4]:.6f}')
