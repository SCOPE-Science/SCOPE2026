"""Independent numerical checks for two-column Gaussian sketch pivot theorem.
Requires numpy and scipy. All matrix and sketch data are generated locally.
"""
import numpy as np
from scipy.special import betainc

rng = np.random.default_rng(481602)
checks=0


def analytical(M, s):
    a,b = M[:,0], M[:,1]
    u = np.dot(a,a)
    v = np.dot(b,b)
    tau = np.dot(a,b)
    D = u*v-tau*tau
    if u < v:
        M=M[:,::-1]
        a,b = M[:,0],M[:,1]
        u,v=v,u
    assert D>0
    delta = np.sqrt((u+v)**2-4*tau*tau)
    q=(1-(u-v)/delta)/2
    p=betainc(s/2,s/2,q)
    err=np.sqrt(D)*((1-p)/np.sqrt(u)+p/np.sqrt(v))
    err2=D*((1-p)/u+p/v)
    return p,err,err2,q,u,v,D

# All 2-column matrix dimensions; arbitrary conditioning and correlations.
for d in [2,3,6,12]:
    for k in range(1050):
        U,_=np.linalg.qr(rng.standard_normal((d,d)))
        if d==2:
            V,_=np.linalg.qr(rng.standard_normal((2,2)))
        else:
            V,_=np.linalg.qr(rng.standard_normal((2,2)))
        singular=np.array([10**rng.uniform(-1,3),10**rng.uniform(-3,-1)])
        singular.sort(); singular=singular[::-1]
        M=U[:,:2]@np.diag(singular)@V
        sv=np.linalg.svd(M,compute_uv=False)
        for s in [2,3,4,9,20]:
            p,err,err2,q,u,v,D=analytical(M,s)
            assert 0<=p<=q+1e-12
            assert q<=v/(u+v)+1e-12
            assert err/sv[-1] <= np.sqrt(2)+1e-9
            assert err2/sv[-1]**2 <= 2+1e-9
            checks+=1

# Reproduce Gaussian sketches and the beta-law with Monte Carlo for nonorthogonal columns.
for d,s in [(2,1),(2,2),(5,2),(6,5),(10,8)]:
    for k in range(8):
        M=rng.standard_normal((d,2))
        if np.linalg.norm(M[:,0])<np.linalg.norm(M[:,1]):M=M[:,::-1]
        p,expected,expected2,_,u,v,D=analytical(M,s)
        N=40000
        G=rng.standard_normal((N,s,d))/np.sqrt(s)
        Y=G@M
        wrong=np.sum(Y[:,:,1]**2,axis=1)>np.sum(Y[:,:,0]**2,axis=1)
        emp=np.mean(wrong)
        assert abs(emp-p)<5.2*np.sqrt(max(p*(1-p),.00001)/N)+.003
        errs=np.where(wrong,np.sqrt(D/v),np.sqrt(D/u))
        assert abs(np.mean(errs)-expected)<6*(np.sqrt(D/v)-np.sqrt(D/u))*np.sqrt(max(p*(1-p),.00001)/N)+.005
        assert abs(np.mean(errs**2)-expected2)<6*(D/v-D/u)*np.sqrt(max(p*(1-p),.00001)/N)+.005
        checks+=2

# The sharp s>=2 constant, and the one-row obstruction.
for k in [10.,100.,10000.]:
    M=np.diag([k,1.])@np.array([[1.,-1.],[1.,1.]])/np.sqrt(2)
    for s in [2,3,10]:
        _,err,err2,_,_,_,_=analytical(M,s)
        assert np.isclose(err,np.sqrt(2)*k/np.sqrt(k*k+1),atol=1e-8)
        assert np.isclose(err2,2*k*k/(k*k+1),atol=1e-8)
        checks+=1
    p,err,err2,_,_,_,_=analytical(np.diag([k,1.]),1)
    assert np.isclose(p,(2/np.pi)*np.arctan(1/k))
    assert np.isclose(err,1+(k-1)*p)
    assert np.isclose(err2,1+(k*k-1)*p)
    checks+=1
assert 1+2/np.pi > np.sqrt(2)
print(f'PASS: {checks} deterministic and Monte-Carlo checks; two-or-more-row sharp expected squared-error ratio 2; one-row squared ratio diverges')
