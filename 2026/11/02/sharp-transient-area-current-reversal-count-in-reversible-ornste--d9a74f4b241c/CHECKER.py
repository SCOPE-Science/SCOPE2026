"""Standalone finite-dimensional checks for transient signed-area theory.
Requires numpy and scipy. These checks corroborate, but do not replace,
the analytic zero-count and interpolation proofs.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.special import comb


def current(A, C):
    return float(-(C@A)[0,1]+(C@A)[1,0])


def test_explicit_witness():
    q=np.array([[1,2,2],[2,1,-2],[2,-2,1]],dtype=float)/3
    lam=np.array([1.,2.,3.]); a=q@np.diag(lam)@q.T
    expected=np.array([[7,-2,0],[-2,6,-2],[0,-2,5]],float)/3
    assert np.allclose(a,expected,atol=1e-14)
    assert np.allclose(q@q.T,np.eye(3))
    e=np.array([[0,12/25,-3/4],[12/25,0,3/2],[-3/4,3/2,0]],float)
    cprime=np.diag(1/lam)+e/10
    assert np.min(np.linalg.eigvalsh(cprime))>0
    c0=q@cprime@q.T
    for t in np.r_[0., np.log(5/4),np.log(5),np.linspace(0,3,45)]:
        ct=np.linalg.inv(a)+expm(-a*t)@(c0-np.linalg.inv(a))@expm(-a*t)
        formula=np.exp(-3*t)*(np.exp(-t)-.2)*(np.exp(-t)-.8)/10
        assert abs(current(a,ct)-formula)<2e-13,(t,current(a,ct),formula)
    for t in [0.,.1,.5,1.,2.]:
        y=np.exp(-t)
        assert np.sign(current(a,np.linalg.inv(a)+expm(-a*t)@(c0-np.linalg.inv(a))@expm(-a*t)))==np.sign((y-.2)*(y-.8))
    return a,c0


def generic_dimension(d):
    # First and second rows of a real orthogonal matrix, by Gram Schmidt.
    u=np.ones(d)/np.sqrt(d)
    v=np.arange(1,d+1)-(d+1)/2
    v=v/np.linalg.norm(v)
    q=np.zeros((d,d));q[0]=u;q[1]=v
    # Extend rows to an orthogonal basis.
    rank=2
    for vec in np.eye(d):
        z=vec.copy()
        for k in range(rank):z-=np.dot(z,q[k])*q[k]
        if np.linalg.norm(z)>1e-8:
            q[rank]=z/np.linalg.norm(z);rank+=1
            if rank==d:break
    assert rank==d
    assert np.allclose(q@q.T,np.eye(d),atol=1e-11)
    lam=np.array([2.**(i+1) for i in range(d)])
    pairs=[(i,j) for i in range(d) for j in range(i+1,d)]
    betas=np.array([lam[i]+lam[j] for i,j in pairs])
    assert len(set(betas))==len(pairs)
    m=len(pairs)
    # Time interval shrinks with eigenvalue scale, to stabilize interpolation.
    ts=np.linspace(.03,.33,m-1)/max(1,lam.max()/8)
    b=np.exp(-np.outer(ts,betas))
    _,s,vh=np.linalg.svd(b,full_matrices=True)
    assert s[-1]>1e-13 if d==3 else s[-1]>1e-20
    coeff=vh[-1]
    # Scaling only changes the smallness of the perturbation.
    ep=np.zeros((d,d))
    for z,(i,j) in enumerate(pairs):
        denom=(lam[i]-lam[j])*(q[0,i]*q[1,j]-q[0,j]*q[1,i])
        assert abs(denom)>1e-11
        ep[i,j]=ep[j,i]=coeff[z]/denom
    eps=min(.01,.1/(lam.max()*(np.linalg.norm(ep,2)+1)))
    cprime=np.diag(1/lam)+eps*ep
    assert np.min(np.linalg.eigvalsh(cprime))>0
    a=q@np.diag(lam)@q.T;c0=q@cprime@q.T
    for t in ts:
        spec=eps*np.dot(coeff,np.exp(-betas*t))
        ct=np.linalg.inv(a)+expm(-a*t)@(c0-np.linalg.inv(a))@expm(-a*t)
        assert abs(current(a,ct)-spec)<1e-10
    return len(ts)


def main():
    test_explicit_witness()
    checks=54
    for d in [3,4]:
        checks+=generic_dimension(d)
    print(f'PASS: explicit rational 3D witness, covariance flow, and generic d=3,4 zero-interpolation checks ({checks} primary tests; multiple subsidiary identities)')

if __name__=='__main__':main()
