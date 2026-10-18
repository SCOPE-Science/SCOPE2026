import numpy as np
from scipy.special import jv
from scipy.optimize import brentq
from scipy.linalg import eigh

def zeros(mu,k):
    z=np.geomspace(1e-8,80,25001)
    vals=jv(mu,z)
    roots=[]
    for a,b,fa,fb in zip(z[:-1],z[1:],vals[:-1],vals[1:]):
        if fa*fb < 0:
            roots.append(brentq(lambda x:jv(mu,x),a,b,xtol=1e-13))
            if len(roots)>=k:break
    return np.array(roots)

for alpha in [0.06,0.2,0.5,1.,2.,6.,25.]:
    gamma=1/alpha;nu=gamma/(gamma+1)
    roots=zeros(-nu,5)
    pred=2*np.sqrt(gamma)/(gamma+1)/roots
    N=350; x=(np.arange(N)+.5)/N
    kern=1-np.maximum.outer(x,x)**gamma
    vals=eigh(kern/N,subset_by_index=(N-5,N-1),eigvals_only=True)[::-1]
    est=np.sqrt(np.maximum(vals,0))
    print(alpha,'nu',nu,'singular',np.round(pred,7),'nystrom',np.round(est,7),'err',np.round(np.abs(pred-est),6),'exact_M2',1/(1+alpha),'exact_M4',1/((1+alpha)*(1+2*alpha)))

for alpha in [1e-5,1e-4,1e-3]:
  gamma=1/alpha;nu=gamma/(gamma+1);r=zeros(-nu,4); s=2*np.sqrt(gamma)/(gamma+1)/r
  print('small alpha',alpha,'s1',s[0],'scaled rest',s[1:]/np.sqrt(alpha))
for alpha in [1e3,1e4]:
  gamma=1/alpha;nu=gamma/(gamma+1);r=zeros(-nu,4);s=2*np.sqrt(gamma)/(gamma+1)/r
  print('large alpha',alpha,'scaled all',s*np.sqrt(alpha))

# Independent pass/fail checks used for reproducibility.
from scipy.special import jn_zeros
passes=0
for a in (0.06,0.2,0.5,1.,2.,6.,25.):
    mu=-1/(1+a)
    r=zeros(mu,5)
    prediction=2*np.sqrt(a)/(1+a)/r
    N=350
    nodes=(np.arange(N)+.5)/N
    K=(1-np.maximum.outer(nodes,nodes)**(1/a))/N
    numerical=np.sqrt(eigh(K,subset_by_index=(N-5,N-1),eigvals_only=True)[::-1])
    assert np.max(np.abs(prediction-numerical))<7e-5,(a,prediction,numerical)
    assert np.all(np.diff(r)>0)
    passes+=2
for a in (1e-5,1e-4,1e-3):
    r=zeros(-1/(1+a),4)
    sv=2*np.sqrt(a)/(1+a)/r
    assert abs((1-sv[0])/a-0.75)<0.001
    assert np.max(np.abs(sv[1:]/np.sqrt(a)-2/jn_zeros(1,3)))<0.001
    passes+=2
for a in (1e3,1e4):
    r=zeros(-1/(1+a),4)
    sv=2*np.sqrt(a)/(1+a)/r
    assert np.max(np.abs(sv*np.sqrt(a)-2/jn_zeros(0,4)))<0.002
    passes+=1
print('PASS',passes,'independent spectral-discretization and boundary tests')
