"""Numerical cross-checks for normalized circular Fock-polynomial sampling.
Dependencies: Python 3.10+, numpy, scipy. Numerical checks support but do not replace proofs.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.special import gammaln, logsumexp


def weights(m, t):
    k = np.arange(m + 1)
    logs = k * math.log(t) - gammaln(k + 1)
    return np.exp(logs - logsumexp(logs))


def mu(m, t):
    return float(np.arange(m + 1) @ weights(m, t))


def gram(m, t, angles):
    n = m + 1
    a = weights(m, t)
    E = np.exp(1j * np.outer(angles, np.arange(n))) * np.sqrt(a)[None, :]
    return E.conj().T @ E


def run():
    cases = []
    max_spectrum_error = 0.0
    total = 0
    for m in range(1, 23):
        n = m + 1
        tc = math.exp(gammaln(m + 1) / m)
        td = brentq(lambda x: mu(m, x)-m/2, 0.001, 2*m, xtol=2e-13)
        assert abs(mu(m, td)-m/2) < 2e-12
        if m <= 2:
            assert abs(td-tc) < 5e-11
        else:
            assert td > tc
        for t in [tc, td, (tc + td)/2]:
            angles = np.arange(n) * 2*math.pi / n
            eig = np.linalg.eigvalsh(gram(m, t, angles))
            predicted = n * weights(m, t)
            err = max(abs(eig - np.sort(predicted)))
            max_spectrum_error = max(max_spectrum_error, float(err))
            assert err < 2e-12
            total += 1
        if m <= 11:
            rng = np.random.default_rng(17000+m)
            for _ in range(25):
                t = math.exp(rng.uniform(math.log(tc/2),math.log(td*2)))
                angles = np.sort(rng.uniform(0,2*math.pi,n))
                lam = np.linalg.eigvalsh(gram(m,t,angles))
                ac = n*weights(m,t)
                assert lam[0] <= min(ac) + 3e-12
                assert lam[-1] >= max(ac)-3e-12
                _,logdet=np.linalg.slogdet(gram(m,t,angles))
                diaglog=sum(np.log(ac))
                assert logdet <= diaglog+1e-8
                total += 1
        if m in [1,2,3,4,7,10,15,22]:
            ac=weights(m,tc);ad=weights(m,td)
            cases.append((m,tc,td,max(ac)/min(ac),max(ad)/min(ad)))
    for m in [40,80,160,320,640]:
        tc=math.exp(gammaln(m+1)/m)
        # bisection in a region where Poisson probabilities stay numerically stable
        td=(brentq(lambda x: mu(m,x)-m/2,m/2,m*.65,xtol=1e-12) if m<=80 else m/2)
        wc=weights(m,tc); wd=weights(m,td)
        ln_ratio=math.log(max(wd)/min(wd))-math.log(max(wc)/min(wc))
        print(f'large m={m}: tc/m={tc/m:.9f}, td/m={td/m:.9f}, log_condition_squared_ratio/m={ln_ratio/m:.9f}')
        assert abs(ln_ratio/m-(0.5-1/math.e))<.05
    print('checked_cases',total,'max_abs_spectrum_error',format(max_spectrum_error,'.3g'))
    for m,tc,td,kc,kd in cases:
        print(f'm={m:2d} t_condition={tc:.12f} t_determinant={td:.12f} condition_sq_opt={kc:.9f} condition_sq_at_D={kd:.9f}')
    print('ALL CHECKS PASS')

if __name__=='__main__':
    run()
