#!/usr/bin/env python3
"""Exact small-characteristic chart checks for three explicit
canonical genus-four models. The proof for every finite field is in RESULT.md.
Run: python3 gonality4_verifier.py (requires sympy >= 1.12).
"""
import sympy as sp
from itertools import combinations
x,y,z,w=sp.symbols('x y z w')
variables=[x,y,z,w]

def models(p,c):
    if p==2:
        q=x*y+z*z+z*w+c*w*w
        f=x**3+y**3+z*z*w+x*x*w
    elif p==3:
        q=x*y+z*z-c*w*w
        f=x**3+y**3+z*z*w+x*w*w-y*w*w+z*w*w
    else:
        q=x*y+z*z-c*w*w
        f=x**3+y**3+w**3
    return q,f

def checks(p,c):
    q,f=models(p,c)
    dq=[sp.diff(q,v) for v in variables]
    df=[sp.diff(f,v) for v in variables]
    minors=[sp.expand(dq[i]*df[j]-dq[j]*df[i]) for i,j in combinations(range(4),2)]
    for i,v in enumerate(variables):
        others=[t for t in variables if t!=v]
        polys=[sp.expand(t.subs(v,1)) for t in [q,f]+minors]
        gb=sp.groebner(polys,*others,order='lex',modulus=p)
        assert gb.is_zero_dimensional or list(gb)==[sp.Integer(1)], (p,c,i,gb)
        assert list(gb)==[sp.Integer(1)], (p,c,i,gb)
    pt=(1,1,1,0) if p==2 else (1,p-1,1,0)
    vals=dict(zip(variables,pt))
    assert int(q.subs(vals))%p==0 and int(f.subs(vals))%p==0
    print(f'characteristic {p}, c={c}: four geometric chart smoothness ideals are the unit ideal; rational point {pt} present')

if __name__=='__main__':
    # c has absolute trace 1 in F2; c=2 nonsquare in F3,F5;
    # c=3 nonsquare in F7; c=2 nonsquare in F11.
    for p,c in [(2,1),(3,2),(5,2),(7,3),(11,2)]:checks(p,c)
    print('All exact sample checks passed; general all-field proof is algebraic.')
