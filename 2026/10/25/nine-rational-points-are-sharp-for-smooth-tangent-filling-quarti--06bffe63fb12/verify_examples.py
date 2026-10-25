#!/usr/bin/env python3
"""Exact arithmetic verification of two genus-three tangent-filling quartics over GF(5).
Requires SymPy. Coefficients are in lexicographic (a,b) order for X^a Y^b Z^(4-a-b).
"""
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
variables=(X,Y,Z)
monomials=[X**a*Y**b*Z**(4-a-b) for a in range(5) for b in range(5-a)]
examples={
 'full_pencil': [0,2,0,0,0,0,3,2,1,1,1,1,4,1,1],
 'nontrivial_dual_blocking': [1,2,3,2,0,4,4,1,2,3,4,2,2,4,0],
}
projective_points=[(1,y,z) for y in range(5) for z in range(5)] + [(0,1,z) for z in range(5)]+[(0,0,1)]
assert len(set(projective_points)) == 31

def normalized(v):
 first=next(a for a in v if a%5)
 inverse=pow(first,-1,5)
 return tuple(a*inverse%5 for a in v)

for name,coefficients in examples.items():
    F=sp.Poly(sum(c*m for c,m in zip(coefficients,monomials)), X,Y,Z, modulus=5)
    grads=[F.diff(v) for v in variables]
    evaluation=lambda poly,p: int(poly.eval(dict(zip(variables,p))))%5
    rational_points=[p for p in projective_points if evaluation(F,p)==0]
    assert len(rational_points)==9
    assert all(any(evaluation(g,p) for g in grads) for p in rational_points)
    tangents=[normalized([evaluation(g,p) for g in grads]) for p in rational_points]
    assert len(set(tangents))==9
    covered=[p for p in projective_points if any(sum(a*b for a,b in zip(line,p))%5==0 for line in tangents)]
    assert len(covered)==31
    full_pencils=[p for p in projective_points if sum(sum(a*b for a,b in zip(line,p))%5==0 for line in set(tangents))==6]
    if name=='full_pencil':assert full_pencils==[(0,0,1)]
    else:assert full_pencils==[]
    for variable,rest in [(X,(Y,Z)),(Y,(X,Z)),(Z,(X,Y))]:
        gb=sp.groebner([g.as_expr().subs({variable:1}) for g in grads],*rest,modulus=5,order='lex')
        assert len(gb.polys)==1 and gb.polys[0].total_degree()==0
    print(name, 'rational_points=9', 'tangent_lines=9', 'covered_points=31',
          'full_pencil_centers=',full_pencils, 'jacobian_charts=3_unit_ideals')
    print('rational_points:',rational_points)
    print('tangents:',tangents)
print('PASS')
