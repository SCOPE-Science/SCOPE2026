"""Numerical checks of finite-population annulus edge constants.

Only standard mathematical/statistical libraries; numerical checks do not certify limits.
"""
from math import gamma, sqrt, pi
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc
from scipy.special import hyp0f1


def edge_constant(n, alpha, relative=True):
    weights = np.array([(n-1)/n] + [1/n]*(n-1))
    W = float(weights.sum())
    beta = n*alpha+(n-1)/2
    prefactor = (2**alpha * gamma(alpha+1))**n
    constant = prefactor * sqrt(W) / ((2*pi)**((n-1)/2)*gamma(beta+1)*np.prod(weights)**(alpha+.5))
    return constant*W**beta if relative else constant


def n2_uniform_exact(eps):
    # Two independent uniform points in the unit disk. Their difference
    # has area-of-overlap radial density; relative distance is half the difference.
    def overlap(d):
        return 2*np.arccos(d/2)-(d/2)*np.sqrt(max(0,4-d*d))
    return quad(lambda d:2*d*overlap(d)/pi,2*(1-eps),2,epsabs=1e-13,epsrel=1e-11)[0]


def qmc_tail(n, alpha, epsilons, power=20):
    sampler=qmc.Sobol(d=2*n,scramble=True,seed=274913)
    a=sampler.random_base2(power)
    # r^2 has Beta(1,alpha) law, thus 1-r^2 = (1-U)^(1/alpha).
    radius=np.sqrt(1-(1-a[:,0::2])**(1/alpha))
    theta=2*pi*a[:,1::2]
    X=radius*np.cos(theta)
    Y=radius*np.sin(theta)
    L=np.hypot(X[:,0]-X.mean(axis=1),Y[:,0]-Y.mean(axis=1))
    W=2*(n-1)/n
    beta=n*alpha+(n-1)/2
    K=edge_constant(n,alpha)
    return [(eps,float(np.mean(L>W*(1-eps))),K*eps**beta) for eps in epsilons]


def run():
    assert abs(edge_constant(2,1) - (32/(15*pi))*2**2.5)<1e-10
    print('N=2, alpha=1: exact two-disk convolution')
    for eps in (.12,.06,.03,.015,.0075):
        probability=n2_uniform_exact(eps)
        asymptotic=edge_constant(2,1)*eps**2.5
        print(f'  eps={eps:.4g} exact={probability:.10g} leading={asymptotic:.10g} ratio={probability/asymptotic:.6f}')
        assert probability>0 and .7<probability/asymptotic<1.15
    for n,a,e in [(2,.5,[.2,.1,.05,.025]),(3,.3,[.2,.1,.05,.025])]:
        print(f'N={n}, alpha={a}: quasi-Monte Carlo')
        for eps,observed,predicted in qmc_tail(n,a,e):
            print(f'  eps={eps:.3f} observed={observed:.9g} asymptotic={predicted:.9g} ratio={observed/predicted:.5f}')
            assert observed>0
    # Exact finite-N characteristic function from independent beta-disk vectors.
    for n,alpha in [(2,.5),(3,.3),(5,1.2)]:
        sampler=qmc.Sobol(d=2*n,scramble=True,seed=2783+n)
        data=sampler.random_base2(18)
        rad=np.sqrt(1-(1-data[:,0::2])**(1/alpha))
        th=2*pi*data[:,1::2]
        dx=rad*np.cos(th)
        delta=dx[:,0]-dx.mean(axis=1)
        b=(n-1)/n
        for k in (.5,1.5,3.0):
            model=hyp0f1(1+alpha,-(b*k)**2/4) * hyp0f1(1+alpha,-(k/n)**2/4)**(n-1)
            sample=np.cos(k*delta).mean()
            print(f'CF N={n} alpha={alpha} k={k}: exact={model:.7f}, QMC={sample:.7f}')
            assert abs(model-sample)<.004
    # Structural determinant test for angular quadratic form.
    for n in range(2,15):
        w=np.array([(n-1)/n]+[1/n]*(n-1));W=w.sum()
        others=w[1:]
        H=np.diag(others)-np.outer(others,others)/W
        assert np.isclose(np.linalg.det(H), np.prod(w)/W,rtol=2e-11)
    print('Hessian determinant identities verified for 2<=N<=14')

if __name__=='__main__':run()
