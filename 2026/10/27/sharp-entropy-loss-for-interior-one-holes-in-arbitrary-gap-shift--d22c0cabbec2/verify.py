"""Independent finite-state entropy and asymptotic checks for gap-shift holes."""
import itertools
import math

import numpy as np


def P(sset, t):
    return sum(t ** (s + 1) for s in sset if s > 0)


def root(sset, k=None):
    lo, hi = 0.0, 1.0
    for _ in range(100):
        t = (lo + hi) / 2.0
        val = t + P(sset, t) if k is None else P(sset,t)*(1/(1-t)-t**(k-1))
        if val > 1: hi = t
        else: lo = t
    return (lo+hi)/2


def graph_radius(sset, k):
    m = max(sset)
    L = max(m+2, k+2)
    illegal = ['1' + '0'*j + '1' for j in range(m+1) if j not in sset]
    illegal.extend(['0'*(m+1), '0'+'1'*k+'0'])
    states = [''.join(w) for w in itertools.product('01', repeat=L-1)]
    states = [u for u in states if all(v not in u for v in illegal)]
    idx = {u:i for i,u in enumerate(states)}
    mat = np.zeros((len(states),len(states)))
    for u in states:
        for v in '01':
            word = u+v
            if any(p in word for p in illegal): continue
            suffix = word[1:]
            if suffix in idx: mat[idx[u],idx[suffix]] += 1
    return max(abs(np.linalg.eigvals(mat)))


def main():
    cases=[(0,1),(0,2),(0,1,2),(0,2,4),(0,1,3)]
    checks=0
    for S in cases:
        for k in range(2, 6):
            pred=1/root(S,k)
            computed=graph_radius(S,k)
            assert abs(pred-computed) < 2e-7, (S,k,pred,computed)
            checks+=1
    for S in cases:
        q=root(S)
        Pprime=sum((s+1)*q**s for s in S if s>0)
        coef=(1-q)**2/(q*q*(1+Pprime))
        last_err=0
        for k in [12,16,20]:
            delta=math.log(root(S,k)/q)
            asym=coef*q**k
            assert abs(delta/asym-1)<0.08, (S,k,delta,asym)
            last_err=abs(delta/asym-1)
            checks+=1
    print('VERIFY_OK', checks, 'independent SFT spectral-radius and asymptotic tests')

if __name__=='__main__': main()
