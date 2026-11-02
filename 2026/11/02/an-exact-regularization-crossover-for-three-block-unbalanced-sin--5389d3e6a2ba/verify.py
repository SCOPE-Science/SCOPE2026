"""Reproduce local rate comparisons for KL unbalanced Sinkhorn maps."""
import numpy as np
from numpy.linalg import eigvals, svd


def maps(eps, rho, kernel):
    n = kernel.shape[0]
    tau = rho / (rho + eps)

    def block(update_from, matrix):
        z = update_from / eps
        zmax = z.max()
        return -eps*tau*(np.log((matrix@np.exp(z-zmax))/n)+zmax)

    def one(f, g, variant):
        g_raw = block(f, kernel.T)
        f_raw = block(g_raw, kernel)
        if variant == "G":
            af = -f_raw/rho
            bg = -g_raw/rho
            ma = af.max()
            mb = bg.max()
            d = (rho/2)*((ma+np.log(np.exp(af-ma).mean()))-
                          (mb+np.log(np.exp(bg-mb).mean())))
            return f_raw+d, g_raw-d
        return f_raw, g_raw

    return one


def example(eps, rho, w):
    n=len(w)
    # The Gibbs kernel is itself strictly positive and doubly stochastic.
    kernel=w
    c=-(eps*rho/(eps+2*rho))*np.log(1/n)
    one=maps(eps,rho,kernel)
    base=np.full(2*n,c)
    u=np.eye(2*n)
    h=1.e-5
    target_s=svd(w,compute_uv=False)[1]
    tau=rho/(rho+eps)
    predF=tau*tau
    predG=tau*tau*max(eps/(2*rho),target_s**2)
    for method, pred in [('F',predF),('G',predG)]:
        def q(z):
            a,b=one(z[:n],z[n:],method)
            return np.r_[a,b]
        assert np.max(np.abs(q(base)-base)) < 1e-12
        jac=np.column_stack([(q(base+h*u[j])-q(base-h*u[j]))/(2*h) for j in range(2*n)])
        val=max(abs(eigvals(jac)))
        assert abs(val-pred)<3e-7, (eps,rho,method,val,pred)
        print(f'{method} eps/rho={eps/rho:g} n={n} local_rate={val:.12g} theory={pred:.12g}')
    return predF,predG


if __name__=='__main__':
    for n in [2,3,5]:
        i=np.eye(n)
        p=np.roll(i,1,axis=1)
        j=np.ones((n,n))/n
        w=.32*i+.36*p+.32*j
        assert np.min(w)>0
        assert np.max(np.abs(w.sum(axis=0)-1))<1e-14
        assert np.max(np.abs(w.sum(axis=1)-1))<1e-14
        for ratio in [.1, .5, 1., 1.7, 2., 3., 12.]:
            f,g=example(ratio,1.,w)
            if ratio<2: assert g<f
            elif ratio>2: assert g>f
            else: assert abs(f-g)<1e-12
    # An exact finite-dimensional basis calculation for two sites:
    # W=[[u,1-u],[1-u,u]] has singular values 1 and |2u-1|.
    from fractions import Fraction as Q
    rho=Q(1); eps=Q(3); u=Q(3,4)
    tau=rho/(rho+eps)
    assert tau*tau == Q(1,16)
    assert tau*tau*max(eps/(2*rho),(2*u-1)**2)==Q(3,32)
    print('VERIFY_OK: all 42 independent finite-difference Jacobians; exact 2x2 rate; sharp crossover')
