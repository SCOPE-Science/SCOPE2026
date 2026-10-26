"""Independent Lyapunov checks for graph-matched colored forcing in a damped harmonic network.

The verification concerns stationary second moments only. It is not a proof of
universality; the accompanying result derives the formulas algebraically.
Run: python verify.py
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov


def ring_laplacian(n, w):
    e = np.eye(n)
    adj = np.roll(e, 1, axis=0) + np.roll(e, -1, axis=0)
    return w * (2 * e - adj), adj


def graph_laplacian(n, rng):
    weights = rng.uniform(0, 1.5, (n, n))
    weights = np.triu(weights, 1)
    weights = weights + weights.T
    weights += (np.roll(np.eye(n), 1, axis=0) + np.roll(np.eye(n), -1, axis=0)) * .15
    np.fill_diagonal(weights, 0.)
    return np.diag(weights.sum(axis=1)) - weights


def full_stationary_covariance(L, Sigma, m, gamma, tau, T):
    n = L.shape[0]
    eig, u = np.linalg.eigh(L)
    assert eig[1] > 1e-8
    B = u[:, 1:]
    dim = 3*n - 1
    H = np.zeros((dim, dim))
    iy = slice(0, n-1)
    iv = slice(n-1, 2*n-1)
    iff = slice(2*n-1, 3*n-1)
    H[iy, iv] = B.T
    H[iv, iy] = -L @ B
    H[iv, iv] = -gamma * np.eye(n)
    H[iv, iff] = np.eye(n)/m
    H[iff, iff] = -np.eye(n)/tau
    D = np.zeros((dim, dim))
    D[iv, iv] = 2*gamma*T/m*np.eye(n)
    D[iff, iff] = 2*Sigma/tau
    X = solve_continuous_lyapunov(H, -D)
    return X[iy, iy], X[iv, iv], X[iv, iff], X[iy, iv], B, np.max(np.abs(H@X+X@H.T+D))


def check_graph(n, L, c, m, gamma, tau, T):
    A0 = 1 + gamma*tau
    Sigma = c*(A0*np.eye(n) + tau**2*L)
    assert np.linalg.eigvalsh(Sigma).min() > 0
    yy, vv, vf, yv, B, resid = full_stationary_covariance(L, Sigma, m, gamma, tau, T)
    Tk = T + c*tau/(m*gamma)
    Tx = T + (1+gamma*tau)*c*tau/(m*gamma)
    vv_expected = Tk/m*np.eye(n)
    yy_expected = Tx/m*np.linalg.inv(B.T@L@B)
    active_power = c*tau/m
    err = max(np.max(np.abs(vv - vv_expected)), np.max(np.abs(yy - yy_expected)), np.max(np.abs(yv)), np.max(np.abs(np.diag(vf)-active_power)))
    assert err < 2e-9 and resid < 2e-9
    assert abs(Tx-Tk-tau*active_power) < 1e-11
    return err, resid


def check_ring(n, w, sigma2, m, gamma, tau, T):
    L, adj = ring_laplacian(n,w)
    A0=1+gamma*tau
    a=A0+2*tau*tau*w
    b=tau*tau*w
    ec=-b/a
    assert -.5<ec<0
    ee=[-.49,(ec-.49)/2,ec,ec/2,.49]
    max_err=0
    for epsilon in ee:
        Sigma=sigma2*(np.eye(n)+epsilon*adj)
        assert np.linalg.eigvalsh(Sigma).min()>-1e-10
        yy,vv,vf,yv,B,resid=full_stationary_covariance(L,Sigma,m,gamma,tau,T)
        expected=T/m*np.eye(n)+tau/(m*m*gamma)*Sigma@np.linalg.inv(A0*np.eye(n)+tau*tau*L)
        err=np.max(np.abs(vv-expected))
        max_err=max(max_err,err,resid)
        assert err<2e-9 and np.max(np.abs(yv))<2e-9
        off=vv.copy(); np.fill_diagonal(off,0)
        vals=off[~np.eye(n,dtype=bool)]
        if epsilon > ec+1e-9:
            assert vals.min()>1e-12
        elif epsilon < ec-1e-9:
            assert vals.max()<-1e-12
        else:
            assert np.max(np.abs(vals))<2e-9
            c=sigma2/a
            val, residual=check_graph(n,L,c,m,gamma,tau,T)
            max_err=max(max_err,val,residual)
    return ec,max_err


def main():
    rng=np.random.default_rng(20241024)
    greatest_error=0.
    cases=0
    thresholds=[]
    for n in [3,4,5,7,9]:
        for _ in range(8):
            m=rng.uniform(.4, 3.)
            gamma=rng.uniform(.3, 2.)
            tau=rng.uniform(.3, 2.)
            T=rng.uniform(.1, 3.)
            c=rng.uniform(.1, 2.)
            L=graph_laplacian(n,rng)
            err,_=check_graph(n,L,c,m,gamma,tau,T)
            greatest_error=max(greatest_error,err)
            cases+=1
    for n in [3,4,5,8,12]:
        for _ in range(8):
            m=rng.uniform(.4, 3.)
            gamma=rng.uniform(.3, 2.)
            tau=rng.uniform(.3, 2.)
            T=rng.uniform(.1, 3.)
            sigma2=rng.uniform(.1, 2.)
            w=rng.uniform(.2, 3.)
            ec,err=check_ring(n,w,sigma2,m,gamma,tau,T)
            thresholds.append(ec)
            greatest_error=max(greatest_error,err)
            cases+=1
    print(f'PASS: {cases} independently solved full covariance Lyapunov cases')
    print(f'maximum absolute covariance discrepancy: {greatest_error:.3e}')
    print(f'ring cancellation epsilon range in tested cases: [{min(thresholds):.6f},{max(thresholds):.6f}]')
    print('checked: graph-matched two-temperature covariance; zero y-v covariance;')
    print('per-site injected power; gap=lag-times-power; and all-pair ring covariance signs')

if __name__=='__main__':
    main()
