"""Reproducible numerical corroboration of crosspolytope-section inradius tail.

This is not an infinite-dimensional proof: the analytical argument is in RESULT.md.
"""
import itertools
import math
import numpy as np

def exact_radius(n):
    """Section inradius for unit sphere normal n, using all 2^d signs."""
    n=np.asarray(n,dtype=float)
    assert n.ndim==1 and len(n)>1 and abs(np.linalg.norm(n)-1)<1e-10
    signs=np.array(list(itertools.product((-1.,1.),repeat=len(n))))
    discrepancy=np.min(np.abs(signs@n))
    return 1/math.sqrt(len(n)-discrepancy**2)

def c(d):
    return d * 2**(d-1)*math.gamma(d/2)*(d-1)**(1.5*(d-1))/(math.pi**(d/2)*math.factorial(d-1))

def run():
    rng=np.random.default_rng(20261026)
    print('d  constant  p(eps=.05) asymptotic ratio p/(C*eps^(d-1))  p(eps=.08) ratio')
    for d in (2,3,4,5):
        size=800000
        g=rng.standard_normal((size,d));g/=np.linalg.norm(g,axis=1)[:,None]
        signs=np.array(list(itertools.product((-1.,1.),repeat=d)))
        m=np.min(np.abs(g@signs.T),axis=1)
        radius=1/np.sqrt(d-m*m)
        top=1/math.sqrt(d-1)
        ps=[]
        for eps in (.05,.08):
            p=np.mean(radius>top-eps)
            ps.append((p,p/(c(d)*eps**(d-1))))
        print(d,round(c(d),10),ps)
        assert np.all(radius<=top+1e-12)
        for i in range(30):
            assert abs(exact_radius(g[i])-radius[i])<1e-13
    print('PASS: exact sign search matches vectorized calculations; maximum bound holds.')
    for d in (2,3,4,5,6):
        normal=np.eye(d)[0]
        assert abs(exact_radius(normal)-1/math.sqrt(d-1))<1e-14
        print('coordinate extremizer',d, exact_radius(normal))

if __name__=='__main__':run()
