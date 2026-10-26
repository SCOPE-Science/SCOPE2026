"""Exact exhaustive geometric-smoothness check for Ciani quartics over GF(3).
Requires Python 3 and SymPy; no external data files.
"""
import itertools
from collections import Counter
from sympy import symbols, diff, Poly, groebner

x,y,z=symbols('x y z')
variables=(x,y,z)
monomials=(x**4,y**4,z**4,x**2*y**2,x**2*z**2,y**2*z**2)

def theoretical_smooth(coeff):
    a,b,c,d,e,f=coeff
    if 0 in (a,b,c): return False
    signs=(a,b,c)
    cross=(d,e,f)
    edges=((0,1),(0,2),(1,2))
    return sum(t!=0 for t in cross)<=1 and all(t==0 or signs[i]!=signs[j] for t,(i,j) in zip(cross,edges))

def groebner_smooth(coeff):
    F=sum(k*m for k,m in zip(coeff,monomials))
    grad=[diff(F,v) for v in variables]
    # Euler's identity: 4F = xFx+yFy+zFz, and 4=1 in GF(3).
    # Thus simultaneous derivative vanishing automatically lies on the quartic.
    for u in variables:
        affine=tuple(v for v in variables if v!=u)
        forms=[Poly(g.subs(u,1),*affine,modulus=3).as_expr() for g in grad]
        basis=groebner(forms,*affine,order='grevlex',modulus=3)
        # Unit ideal means no geometric critical point on this affine chart.
        if len(basis.polys)!=1 or basis.polys[0].total_degree()!=0:
            return False
    return True

smooth=[]
counts=Counter()
for v in itertools.product(range(3),repeat=6):
    if not any(v): continue
    theo=theoretical_smooth(v)
    groeb=groebner_smooth(v)
    assert theo==groeb, (v,theo,groeb)
    if groeb:
        smooth.append(v)
        counts[(tuple(v[3:])==(0,0,0))]+=1
assert len(smooth)==32 and counts=={True:8,False:24},counts
assert all(theoretical_smooth(v) for v in smooth)
print('GEOMETRIC_SMOOTHNESS_OK')
print('nonzero_coefficient_vectors=728')
print('smooth_vectors=32 scalar_normalized=16')
print('diagonal_vectors=8 one_mixed_vectors=24')
