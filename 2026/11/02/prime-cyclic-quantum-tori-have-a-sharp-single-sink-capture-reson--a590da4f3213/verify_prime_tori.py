"""Independent finite-dimensional checks of exact corner capture on prime cyclic tori.

Runs from the included source without external data files. Requires numpy.
"""
import math
import numpy as np


def cycle(p):
    a = np.zeros((p, p))
    for i in range(p):
        a[i, (i + 1) % p] = a[i, (i - 1) % p] = 1
    return a


def capture_spectral(p, q, a, b):
    h = a * np.kron(cycle(p), np.eye(q)) + b * np.kron(np.eye(p), cycle(q))
    w, u = np.linalg.eigh(h)
    out = np.zeros(p*q)
    active = 0
    j = 0
    while j < len(w):
        k = j + 1
        while k < len(w) and abs(w[k] - w[j]) < 1.e-7:
            k += 1
        z = u[:, j:k] @ u[0, j:k]
        den = z[0]
        assert den > 1e-11, (p, q, a, b, j, k, den)
        out += z*z/den
        active += 1
        j = k
    return out.reshape((p, q)), active


def predicted(p,q,a,b):
    ans = np.empty((p,q))
    iso = (p==q and a==b)
    for x in range(p):
        for y in range(q):
            if not iso:
                ans[x,y] = (1 if x==0 else .5) * (1 if y==0 else .5)
            elif x==0 and y==0:
                ans[x,y] = 1
            elif (x==0) != (y==0) or (x and y and (x-y)%p==0 or x and y and (x+y)%p==0):
                ans[x,y] = .25
            else:
                ans[x,y] = .125
    m=(p-1)//2; n=(q-1)//2
    rank=(m+1)*(n+1) if not iso else (m+1)*(m+2)//2
    return ans,rank


def main():
    checked=0; sites=0; max_error=0.
    cases=[]
    for p,q in [(5,5),(7,7),(11,11),(5,7),(5,11),(7,11)]:
        for a,b in [(1.,1.),(2.,1.),(1.,2.),(3.,2.)]:
            cases.append((p,q,a,b))
    for p,q,a,b in cases:
        actual,bright=capture_spectral(p,q,a,b)
        target,target_rank=predicted(p,q,a,b)
        err=float(np.max(np.abs(actual-target)))
        assert bright==target_rank,(p,q,a,b,bright,target_rank)
        assert err<1e-10,(p,q,a,b,err)
        assert abs(actual.sum()-bright)<1e-9
        max_error=max(max_error,err)
        checked+=1;sites+=p*q
    print('PASS: %d spectral cases, %d site captures, maximal absolute error %.3e' % (checked,sites,max_error))
    print('PASS: all active ranks and all site sums agree with exact formulas')


if __name__=='__main__': main()
