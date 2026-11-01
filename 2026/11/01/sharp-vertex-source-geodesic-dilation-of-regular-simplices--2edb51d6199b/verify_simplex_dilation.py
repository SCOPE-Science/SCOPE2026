"""Exact symbolic and numerical checks of the vertex-source chord-arc
constant on the boundary of a regular n-simplex; n >= 2.
Requires SymPy and NumPy: python verify_simplex_dilation.py.
Finite sampling is supplementary to the included proof.
"""
import sympy as sp
import numpy as np
n=sp.symbols('n',integer=True,positive=True)
alt_body_sq=(n+1)/(2*n)
alt_facet_sq=n/(2*(n-1))
inrad_sq=1/(2*n*(n-1))
R=(n+1)/sp.sqrt(2*n*(n-1))
K_sq=(n+1)/(n-1)
assert sp.simplify((sp.sqrt(alt_facet_sq)+sp.sqrt(inrad_sq))**2-R**2)==0
assert sp.simplify(R**2/alt_body_sq-K_sq)==0
assert sp.simplify(alt_body_sq+inrad_sq-alt_facet_sq)==0
assert sp.simplify((R**2+sp.Symbol('s')-K_sq*(alt_body_sq+sp.Symbol('s'))))==sp.simplify((1-K_sq)*sp.Symbol('s'))
print('PASS: symbolic altitude/inradius identities and sharp constant for all integers n >= 2.')
rng=np.random.default_rng(20261028)
count=0
for dim in range(2,24):
    # Canonical regular simplex in the n-dimensional affine hyperplane of R^(n+1),
    # with vertices coordinate basis divided by sqrt(2).
    verts=np.eye(dim+1)/np.sqrt(2)
    source=verts[0]
    base=verts[1:]
    G=base.mean(axis=0)
    H=np.linalg.norm(source-G)
    F=np.array([base[np.arange(dim)!=j].mean(axis=0) for j in range(dim)])
    rin=np.linalg.norm(F-G,axis=1)
    Rnow=(dim+1)/np.sqrt(2*dim*(dim-1))
    assert np.max(np.abs(rin-rin[0]))<1e-13
    assert abs(np.linalg.norm(source-F[0])+rin[0]-Rnow)<1e-13
    # The unfolded source image for ridge j is obtained by reflecting the
    # adjacent facet through that ridge in the affine plane of the base.
    # It lies along the outward normal through its ridge centroid.
    outward=(G-base)/np.linalg.norm(G-base,axis=1)[:,None]
    images=G+Rnow*outward
    assert np.linalg.norm(images-G,axis=1).max()-Rnow<1e-13
    max_ratio=0.
    for _ in range(1000):
        weights=rng.dirichlet(np.ones(dim))
        P=weights@base
        upper_squared=np.min(np.sum((images-P)**2,axis=1))
        ambient_squared=np.sum((source-P)**2)
        ratio=np.sqrt(upper_squared/ambient_squared)
        assert ratio<=np.sqrt((dim+1)/(dim-1))+1e-12
        max_ratio=max(max_ratio,ratio)
        count+=1
    assert abs(Rnow/H-np.sqrt((dim+1)/(dim-1)))<1e-12
print(f'PASS: {count} reproducible barycentric samples across dimensions 2..23; extremal-centroid identities.')
print('Geometric proof provides strictness away from the opposite facet centroid.')
