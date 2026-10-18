"""Independent geometric-smoothness cross-check on projective orbit representatives.

The input integer bit-mask convention is decreasing X exponent and then decreasing Y exponent
among total-degree-four monomials. For each representative, the affine Jacobian ideal is
checked over the algebraic closure by the unit-ideal criterion in F_2[u,v].
"""
from pathlib import Path
from sympy import symbols, groebner, Poly

X,Y,Z=symbols('X Y Z')
mon=[]
for i in range(4,-1,-1):
    for j in range(4-i,-1,-1):
        mon.append(X**i*Y**j*Z**(4-i-j))
assert len(mon)==15
reps=[int(s) for s in Path('smooth_representatives.txt').read_text().split()]
assert len(reps)==78 and len(set(reps))==78
for r in reps:
    F=sum(term for i,term in enumerate(mon) if r>>i&1)
    for var in (X,Y,Z):
        aff=F.subs(var,1)
        remaining=[v for v in (X,Y,Z) if v!=var]
        polys=[aff]+[aff.diff(v) for v in remaining]
        G=groebner(polys,*remaining,order='lex',modulus=2)
        assert len(G.polys)==1 and G.polys[0].as_expr()==1,(r,var,G)
print('GROEBNER_OK',len(reps),'smooth projective orbits x 3 affine charts =',3*len(reps),'unit ideals')
