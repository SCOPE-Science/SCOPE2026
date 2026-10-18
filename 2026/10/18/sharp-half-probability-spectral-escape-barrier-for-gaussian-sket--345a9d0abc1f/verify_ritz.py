"""Reproducible finite-sample checks for the Gaussian one-dimensional sketched Ritz law.

Requires Python 3, NumPy, SciPy. Run: python verify_ritz.py
Finite checks are not proofs of the universal probabilistic statements.
"""
import math
import numpy as np
from scipy import special, stats


def qtail(s, t):
    """P{standard normal / chi_s > t}, t >= 0."""
    return stats.t.sf(t * math.sqrt(s), df=s)


def envelope(s, p):
    q = math.sqrt(p / (1.0 - p))
    return qtail(s, q) + qtail(s, 1.0 / q)


def main():
    rng = np.random.default_rng(240703)
    checks = 0
    for s in (1, 2, 3, 4, 8, 16):
        for p in (0.01, 0.2, 0.5, 0.8, 0.99):
            n = 180000 if s <= 4 else 120000
            # Direct sketched Rayleigh--Ritz of A=diag(1,3), v=(sqrt(1-p),sqrt(p)).
            sketch = rng.normal(size=(n, s, 2)) / math.sqrt(s)
            b = np.array([math.sqrt(1-p), math.sqrt(p)])
            ab = np.array([math.sqrt(1-p), 3 * math.sqrt(p)])
            x = sketch @ b
            ax = sketch @ ab
            rayleigh = np.einsum('ij,ij->i',x,ax) / np.einsum('ij,ij->i',x,x)
            actual = np.mean((rayleigh < 1) | (rayleigh > 3))
            formula = envelope(s,p)
            error = abs(actual-formula)
            allowance = 6*math.sqrt(max(formula*(1-formula),0.01)/n)+0.002
            assert error < allowance, (s,p,actual,formula,error,allowance)
            checks += 1
        balanced = special.betainc(s/2,0.5,0.5)
        assert abs(envelope(s,0.5)-balanced) < 1e-12
        checks += 1
        for p in (0.05, 0.1, 0.3, 0.7, 0.95):
            assert envelope(s,p) <= 0.5+1e-14
            assert abs(envelope(s,p)-envelope(s,1-p)) < 1e-12
            checks += 2
        if s == 1:
            for p in (0.05, 0.2, 0.5, 0.8, 0.95):
                assert abs(envelope(s,p)-0.5) < 1e-13
                checks += 1
        else:
            assert envelope(s,0.5) < envelope(s,0.2) < envelope(s,0.01) < .5
            checks += 1
    # A general SPD matrix: the envelope is attained only by extreme-eigenspace inputs.
    a = np.diag([1.,2.,3.])
    v = np.array([2.,3.,4.]); v /= np.linalg.norm(v)
    mu = float(v@a@v); sig = float(np.linalg.norm(a@v-mu*v))
    p=(mu-1)/2
    x=qtail(8,(mu-1)/sig)+qtail(8,(3-mu)/sig)
    assert x < envelope(8,p)
    checks += 1
    # Balanced large-s asymptotic, which has relative correction O(1/s).
    for s in (32,64,128,256):
        exact=special.betainc(s/2,.5,.5)
        lead=2/math.sqrt(math.pi*s)*2**(-s/2)
        assert 0 < exact/lead < 1
        assert abs(exact/lead-1)<2/s
        checks += 2
    print(f'PASS: {checks} direct/moment/interval/asymptotic checks; seed 240703')
    print('balanced escape s=4:', special.betainc(2,.5,.5))

if __name__ == '__main__':
    main()
