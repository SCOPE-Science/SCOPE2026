"""Independent finite-state checks for the periodic binary probabilistic cellular automaton.

Run: python verify_noisy_pca.py   (requires NumPy).
Finite checks corroborate, but do not replace, the all-size analytical proof.
"""
import itertools
import math
import numpy as np


def states(n):
    return list(itertools.product((-1, 1), repeat=n))


def kernel(s, t, p, r):
    n = len(s)
    out = 1.0
    for i in range(n):
        left, right = s[(i - 1) % n], s[(i + 1) % n]
        if left == right:
            plus = r if left == 1 else 1 - r
        else:
            plus = p if s[i] == 1 else 1 - p
        out *= plus if t[i] == 1 else 1 - plus
    return out


def gibbs(s, r):
    n = len(s)
    coupling = -0.25 * math.log(4 * r * (1 - r))
    return math.exp(coupling * sum(s[i] * s[(i + 2) % n] for i in range(n)))


def predicted_corr(n, d, r):
    h = 2 * math.sqrt(r * (1-r))
    q = (1-h) / (1+h)
    if n % 2 == 0 and d % 2 == 1:
        return 0.0
    m = n // math.gcd(2, n)
    k = next(j for j in range(m) if 2*j % n == d % n)
    return (q**k + q**(m-k)) / (1+q**m)


def cycle_witness(n, p, r):
    a = (-1,)*n
    b = (-1,)*(n-1)+(1,)
    c = (-1,)*(n-2)+(1,1)
    num = kernel(a,b,p,r)*kernel(b,c,p,r)*kernel(c,a,p,r)
    den = kernel(a,c,p,r)*kernel(c,b,p,r)*kernel(b,a,p,r)
    return num/den


def close(a, b, tol=3e-11):
    if abs(a-b) > tol:
        raise AssertionError((a,b))


def main():
    checks=0
    for n in range(3, 9):
        for p in (0.17, 0.36, 0.5, 0.79):
            for r in (0.18, 0.46, 0.83):
                close(cycle_witness(n,p,r), ((1-p)/p)**2, 2e-12)
                checks+=1
        conf=states(n)
        for r in (0.18, 0.5, 0.83):
            weights=np.array([gibbs(s,r) for s in conf])
            weights/=weights.sum()
            weights_other=np.array([gibbs(s,1-r) for s in conf]);weights_other/=weights_other.sum()
            close(max(abs(weights-weights_other)),0)
            trans=np.array([[kernel(s,t,0.5,r) for t in conf] for s in conf])
            close(float(np.max(abs(trans.sum(axis=1)-1))),0)
            close(float(np.max(abs(weights@trans-weights))),0)
            close(float(np.max(abs(weights[:,None]*trans-weights[None,:]*trans.T))),0)
            checks+=4
            for d in range(n):
                value = sum(weights[k]*s[0]*s[d] for k,s in enumerate(conf))
                close(value, predicted_corr(n,d,r))
                checks+=1
            m=n//math.gcd(n,2)
            h=2*math.sqrt(r*(1-r));q=(1-h)/(1+h)
            susceptibility=((1+q)/(1-q))*(1-q**m)/(1+q**m)
            lhs=sum(weights[k]*(sum(s)/n)**2 for k,s in enumerate(conf))*n
            close(lhs,susceptibility)
            checks+=1
            if n%2==0:
                # Whole even and odd sublattice configurations, not just one-site marginals.
                ev=sorted({tuple(s[::2]) for s in conf})
                od=sorted({tuple(s[1::2]) for s in conf})
                pe={s:sum(weights[k] for k,v in enumerate(conf) if v[::2]==s) for s in ev}
                po={s:sum(weights[k] for k,v in enumerate(conf) if v[1::2]==s) for s in od}
                for k,s in enumerate(conf):
                    close(weights[k],pe[s[::2]]*po[s[1::2]])
                    checks+=1
    print(f'PASS: {checks} finite checks; all tested sizes N=3..8, positive p,r, stationary formula, correlations, susceptibility, detailed balance, and parity factorization.')

if __name__=='__main__':
    main()
