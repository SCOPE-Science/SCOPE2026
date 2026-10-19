"""Independent finite-state check of directed cycle competitive equilibria.
Every support and every retained-edge graph is enumerated for small sizes.
Analytical theorems cover arbitrary size; this is supplementary only.
"""
import itertools, math
import numpy as np

def predicted(n,mask,sigma):
    full = mask == (1<<n)-1
    if not full or sigma < 1:
        return 1
    if n % 2 == 0:
        return 2
    return 1 if sigma < 1/math.cos(math.pi/n) else 0

def expected_support(n,mask,sigma):
    assert mask != (1<<n)-1
    xs = [None] * n
    for i in range(n):
        if not (mask >> i) & 1:
            x = i
            break
    xs[x] = 1.
    j=(x-1)%n
    while j != x:
        val=1-sigma*xs[(j+1)%n] if (mask >> j)&1 else 1
        xs[j] = max(0.,val)
        j=(j-1)%n
    return xs

def all_stable(n, mask, sigma):
    a=np.eye(n)
    for i in range(n):
        if (mask>>i)&1: a[i,(i+1)%n]+=sigma
    candidates=[]
    for support in range(1<<n):
        I=[i for i in range(n) if (support>>i)&1]
        x=np.zeros(n)
        if I:
            try: x[I]=np.linalg.solve(a[np.ix_(I,I)],np.ones(len(I)))
            except np.linalg.LinAlgError: continue
            if min(x[I])<1e-8: continue
        g=1-a@x
        J=np.diag(g-x) - np.diag(x)@(a-np.eye(n))
        if max(np.linalg.eigvals(J).real)<-1e-7:
            candidates.append(x)
    return candidates

if __name__=='__main__':
    total=0
    for n in range(3,8):
        for sigma in (0.5, 1.25, 1.5, 2.5):
            if n % 2 and abs(sigma-1/math.cos(math.pi/n))<1e-8:continue
            for mask in range(1<<n):
                C=all_stable(n,mask,sigma)
                assert len(C)==predicted(n,mask,sigma),(n,sigma,mask,len(C))
                if mask!=(1<<n)-1 and sigma>1:
                    xs=expected_support(n,mask,sigma)
                    assert np.max(np.abs(xs-C[0]))<1e-8
                total += 1
        print('passed size',n)
    print('PASS', total, 'complete graph/support/spectral comparisons')
    for n in range(3,12):
        for q in (.2,.5,.8):
            exp=sum((q**mask.bit_count()*(1-q)**(n-mask.bit_count()))*sum(expected_support(n,mask,2.5))
                    for mask in range((1<<n)-1))
            formula=n*(1-q**(n+(n%2)))/(1+q)
            assert abs(exp-formula)<1e-9,(n,q,exp,formula)
    print('PASS Bernoulli richness formula')
