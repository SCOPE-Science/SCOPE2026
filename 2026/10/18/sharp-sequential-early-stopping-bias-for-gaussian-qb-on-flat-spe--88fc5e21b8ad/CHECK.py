"""Reproducible numerical checks for the Gaussian unit-block QB first-hit law."""
import numpy as np
from scipy.special import betainc


def analytic_probe(n, eps, trials=1000, seed=271828):
    rng = np.random.default_rng(seed+n)
    # Independent chi-square decomposition of each orthogonalized Gaussian probe.
    d = np.arange(n, 0, -1)
    p = np.arange(n)
    u = rng.chisquare(d[:, None], size=(n, trials))
    v = np.zeros_like(u)
    if n > 1:
        v[1:] = rng.chisquare(p[1:, None], size=(n-1, trials))
    means = np.cumsum(u + v, axis=0) / np.arange(1, n+1)[:, None]
    flag = u < eps**2 * means
    flag[0] = False
    assert np.all(flag[-1])
    t = np.argmax(flag, axis=0) + 1
    i0 = (1-eps**2)*n
    shifted = (i0-t) / np.sqrt(n*np.log(n))
    return shifted.mean(), np.median(shifted), (shifted.min(),shifted.max())


def qr_identity_probe(n=11, seed=1701):
    rng = np.random.default_rng(seed)
    W = rng.normal(size=(n,n))
    Q=np.empty((n,0))
    err=[]; proj=[]; norms=[]
    for i in range(n):
        w=W[:,i]
        z=w-Q@(Q.T@w)
        err.append(z@z)
        norms.append(w@w)
        proj.append(n-i)
        Q=np.column_stack((Q,z/np.linalg.norm(z)))
        assert np.linalg.norm(Q.T@Q - np.eye(i+1)) < 1e-8
    assert np.allclose(err, (np.linalg.qr(W, mode='reduced')[1].diagonal())**2)
    return np.array(err),np.array(norms)

if __name__=='__main__':
    err,norms=qr_identity_probe()
    print('direct QR sequence check passed, n=11')
    for n,eps in [(200,0.6),(800,0.6),(3200,0.6),(12800,0.6), (3200,0.3), (3200,0.8)]:
        mean,median,bounds=analytic_probe(n,eps,trials=1600)
        print(n,eps, 'shift scaled mean', round(float(mean),4), 'median',round(float(median),4), 'sharp limit',round(float(np.sqrt(2)*eps),4), 'bounds',tuple(round(float(z),3) for z in bounds))
    # Marginal-beta probability identity at two inspection times.
    for n,i,e in [(10,3,0.6),(40,8,0.7),(30,24,0.4)]:
        d=n-i+1
        prob=betainc(d/2,(i*n-d)/2,e*e/i)
        rng=np.random.default_rng(2026+n+i)
        x=rng.chisquare(d, size=120000)
        y=rng.chisquare(i*n-d, size=120000)
        mc=np.mean(x/(x+y)<e*e/i)
        assert abs(mc-prob)<0.012, (n,i,prob,mc)
        print('beta check',n,i,e,round(float(prob),5),round(float(mc),5))
