"""Independent finite-state checks for the Feres angular lattice.

Requires Python >=3.9 with NumPy and SciPy.  These finite checks corroborate,
but do not replace, the analytic spectral-gap asymptotic.
"""
import math
import numpy as np
from scipy.linalg import eigvalsh


def transition_from_billiard(n):
    a = math.pi / n
    theta = np.array([(j + 0.5)*a for j in range(n)])
    p = np.zeros((n,n))
    def u(beta,t):
        return 0.5*(1+math.tan(beta)/math.tan(t))
    for j,t in enumerate(theta):
        p1 = (1 if t<a else u(a,t) if t<math.pi-3*a
              else 2*math.cos(2*a)*u(2*a,t) if t<math.pi-2*a else 0)
        p2 = (0 if t<math.pi-3*a
              else u(a,t)-2*math.cos(2*a)*u(2*a,t) if t<math.pi-2*a
              else u(a,t) if t<math.pi-a else 0)
        p3 = (0 if t<2*a
              else 2*math.cos(2*a)*u(2*a,-t) if t<3*a
              else u(a,-t) if t<math.pi-a else 1)
        p4 = (0 if t<a else u(a,-t) if t<2*a
              else u(a,-t)-2*math.cos(2*a)*u(2*a,-t) if t<3*a else 0)
        probs=[p1,p2,p3,p4]
        images=[t+2*a,-t+2*math.pi-4*a,t-2*a,-t+4*a]
        assert min(probs)>-1e-9 and abs(sum(probs)-1)<1e-9
        for prob,image in zip(probs,images):
            if prob>1e-12:
                dest=round(image/a-0.5)
                assert 0<=dest<n and abs(image-theta[dest])<1e-9
                p[j,dest]+=prob
    return p,theta


def weighted_edge_model(n,theta):
    a=math.pi/n
    c=np.zeros((n,n))
    def edge(i,j,v):
        assert i!=j and v>0 and c[i,j]==0
        c[i,j]=c[j,i]=v
    for j in range(1,n-3):
        edge(j,j+2,math.sin((j+1.5)*a)/(2*math.cos(a)))
    edge(0,2,math.sin(a/2))
    edge(n-3,n-1,math.sin(a/2))
    edge(1,2,math.sin(a/2)/(2*math.cos(a)))
    edge(n-3,n-2,math.sin(a/2)/(2*math.cos(a)))
    return c


def check(n):
    p,theta=transition_from_billiard(n)
    s=np.sin(theta);mass=s/s.sum()
    edges=weighted_edge_model(n,theta)
    assert np.max(np.abs(p*s[:,None]-edges))<2e-10
    assert np.max(np.abs(p.sum(axis=1)-1))<2e-10
    assert np.max(np.abs(mass@p-mass))<2e-10
    sym=np.sqrt(mass[:,None]/mass[None,:])*p
    assert np.max(np.abs(sym-sym.T))<2e-10
    lam=eigvalsh(sym)[-2]
    assert lam<1
    if n%2==0:
        assert abs(eigvalsh(sym)[0]+1)<2e-10
    result=(n,1-lam,(1-lam)*n*n*math.log(n),sum(mass[::2]))
    return result


if __name__=='__main__':
    print('n, 1-lambda_2(P_n), scaled_by_n^2_log_n, even-index mass')
    for n in (7,8,9,12,20,40,80,120):
        print('%3d  %.11g  %.8f  %.9f'%check(n))
    print('TARGET n^2 log(n) gap -> 2 pi^2 = %.9f'%(2*math.pi**2))
    print('All finite checks passed.')
