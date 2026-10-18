#!/usr/bin/env python3
"""Independent Gröbner and elimination checks; requires SymPy >=1.12."""
import json
from pathlib import Path
from sympy import symbols, expand, groebner, Poly, resultant, S as SYMPY_S
x,y,z=symbols('x y z')
mons=[x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y*y*z,y*z*z]

def form(m):return expand(sum(t for i,t in enumerate(mons) if (m>>i)&1))

def independent_smooth(m):
    f=form(m)
    for v,active in [(x,(y,z)),(y,(x,z)),(z,(x,y))]:
        fchart=expand(f.subs(v,1))
        I=[fchart]+[fchart.diff(t) for t in active]
        G=groebner(I,*active,order='lex',modulus=2)
        if not G.contains(SYMPY_S.One):return False
    return True
S=sorted(m for m in range(1,128) if independent_smooth(m))
assert len(S)==23
pencils=sorted({tuple(sorted((a,b,a^b))) for a in S for b in S if a<b and a^b in S})
assert len(pencils)==12
assert all(all(independent_smooth(m) for m in Q) for Q in pencils)
certs=[]
for Q in [(49,71,118),(51,93,110)]:
    ff,gg=[form(m).subs(z,1) for m in Q[:2]]
    G=groebner([ff,gg],x,y,order='lex',modulus=2)
    R=Poly(resultant(ff,gg,x),y,modulus=2)
    qfactor=R.factor_list()[1]
    assert sorted((p.degree(),n) for p,n in qfactor)==[(1,1),(6,1)]
    assert qfactor[-1][0].is_irreducible
    certs.append({'pencil':Q,'groebner':[str(q) for q in G],
                  'resultant':str(R.as_expr()),'sextic':str(qfactor[-1][0].as_expr())})

print(json.dumps({'independent_smooth_masks':S,
                  'independent_pencils':[list(Q) for Q in pencils],
                  'independent_groebner_and_resultants':certs},sort_keys=True,indent=2))
