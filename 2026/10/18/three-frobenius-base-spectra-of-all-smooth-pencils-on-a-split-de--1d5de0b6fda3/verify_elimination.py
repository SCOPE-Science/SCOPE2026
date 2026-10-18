#!/usr/bin/env python3
"""Independent Gröbner and factorization certificates for all 13 base schemes.
Run with SymPy 1.12+. For affine Z=1 use either t=Y or t=X+Y.
Every certificate is a graph u=P(t) over a squarefree degree-seven polynomial.
"""
from sympy import symbols,groebner,Poly,factor_list
import json
u,t,X,Y=symbols('u t X Y')
REPS=((25,39,62),(25,46,55),(25,47,54),(25,166,191),
      (25,198,223),(25,239,246),(27,110,117),(27,229,254),
      (27,237,246),(29,107,118),(31,201,214),(31,233,246),(91,133,222))
MON=(X*X*Y,X*X,X*Y*Y,Y*Y,X,Y,X*Y,1)
def f(m):return sum(MON[i] for i in range(8) if m>>i&1)
CERTS=[]
for a,b,c in REPS:
    assert a^b==c
    projection='X+Y' if (a,b) in ((25,47),(29,107)) else 'Y'
    if projection=='Y':
        ff=f(a).subs({X:u,Y:t},simultaneous=True)
        gg=f(b).subs({X:u,Y:t},simultaneous=True)
    else:
        ff=f(a).subs({X:t+u,Y:u},simultaneous=True)
        gg=f(b).subs({X:t+u,Y:u},simultaneous=True)
    GB=groebner([ff,gg],u,t,order='lex',modulus=2)
    basis=[p.as_expr() for p in GB.polys]
    assert len(basis)==2
    assert basis[0].coeff(u)==1 and not (basis[0]-u).has(u)
    assert not basis[1].has(u)
    Q=Poly(basis[1],t,modulus=2)
    assert Q.degree()==7 and Q.gcd(Q.diff()).degree()==0
    _,fac=factor_list(Q.as_expr(),t,modulus=2)
    assert all(k==1 for p,k in fac)
    degrees=tuple(sorted(Poly(p,t,modulus=2).degree() for p,k in fac))
    assert degrees in ((1,6),(2,5),(7,)),(a,b,degrees)
    CERTS.append({'representative':[a,b,c], 'projection':projection,
                  'groebner_basis':[str(v) for v in basis],
                  'factorization':[[str(p),k] for p,k in fac],
                  'closed_point_degrees':degrees,'base_affine_points':7,
                  'squarefree':True})
assert sorted(CERTS[0]['closed_point_degrees'])==[1,6]
print(json.dumps({'method':'lexicographic Groebner basis over F2 and exact factorization',
                  'chart':'Z=1', 'certificates':CERTS},indent=2))
