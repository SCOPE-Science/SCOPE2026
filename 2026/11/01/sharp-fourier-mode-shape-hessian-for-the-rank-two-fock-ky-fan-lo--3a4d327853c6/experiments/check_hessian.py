import math
import numpy as np
from scipy.special import gammainc, gamma

def s2_operator(x,eps,h_coeffs,q_coeffs=None,dim=18,ntheta=512):
    theta=2*np.pi*np.arange(ntheta)/ntheta
    h=sum(2*np.real(c*np.exp(1j*k*theta)) for k,c in h_coeffs.items())
    q=sum(2*np.real(c*np.exp(1j*k*theta)) for k,c in (q_coeffs or {}).items())
    u=x+eps*h+eps**2*q
    assert min(u)>0
    mat=np.empty((dim,dim),dtype=complex)
    fact=np.array([math.factorial(j) for j in range(dim)],dtype=float)
    em={k:np.exp(1j*k*theta) for k in range(-dim+1,dim)}
    gs={r:gamma(1+r/2)*gammainc(1+r/2,u) for r in range(2*dim-1)}
    for m in range(dim):
      for n in range(dim):
        mat[m,n]=np.mean(em[n-m]*gs[m+n])/math.sqrt(fact[m]*fact[n])
    mat=(mat+mat.conj().T)/2
    return np.linalg.eigvalsh(mat)[-2:].sum()

def hessian_h(x,k):
    a=[1.]
    for j in range(1,k+2):a.append(a[-1]*x/j)
    X=(a[k]/sum(a[1:k+1]) if k>=2 else 0.0)
    Y=x*a[k+1]/sum(a[2:k+2])
    return -x+X+Y

if __name__=='__main__':
    count=0
    for x in (.4,1.0,3.0):
      for k in (1,2,3,4,5):
        h={k:1.0}
        eps=.005
        sp=s2_operator(x,eps,h)
        sm=s2_operator(x,-eps,h)
        s0=s2_operator(x,0.0,h)
        observed=(sp+sm-2*s0)/(2*eps**2)
        predicted=math.exp(-x)*hessian_h(x,k)
        diff=abs(observed-predicted)
        print(f'x={x:g} k={k} coeff={observed:.10g} pred={predicted:.10g} error={diff:.3g}')
        assert diff<.003*max(0.1,abs(predicted)),(x,k,diff)
        count+=1
    for x in (.15,.5,1,2,10,50):
      vals=[hessian_h(x,k) for k in range(2,45)]
      exact=-x*(2*x+3)/((x+2)*(x+3))
      assert abs(vals[0]-exact)<2e-12*max(x,1)
      assert all(vals[i]>vals[i+1]-1e-13 for i in range(len(vals)-1))
      assert all(val<0 for val in vals)
      count+=1
    print('PASS',count,'model and shape checks')
