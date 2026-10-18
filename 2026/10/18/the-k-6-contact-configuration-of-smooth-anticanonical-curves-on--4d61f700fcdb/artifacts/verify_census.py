"""Exact anticanonical census on the split quintic del Pezzo over F2.
Only the polynomial ideal membership tests require SymPy; all finite incidence
bookkeeping is implemented directly over F2.
Run: python3 verify_census.py
"""
import itertools, collections, json
from pathlib import Path
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
mons=[X*X*Y,X*X*Z,X*Y*Y,X*Y*Z,X*Z*Z,Y*Y*Z,Y*Z*Z]
base=[(1,0,0),(0,1,0),(0,0,1),(1,1,1)]
open_points=[(1,1,0),(1,0,1),(0,1,1)]
params=[(X,Y,1),(X,1,Z),(1,Y,Z)]

def poly_from_mask(mask):
    bits=tuple((mask>>i)&1 for i in range(6))
    return sp.Poly(sum(bits[i]*mons[i] for i in range(6)) + (sum(bits)%2)*mons[6], X,Y,Z, modulus=2).as_expr()

def nonsingular(f):
    # All three projective charts; the reduced Groebner basis [1] means
    # the geometric singular-point ideal has empty zero locus.
    for u,v,w in params:
        repl={X:u,Y:v,Z:w}
        pol=sp.Poly(f.subs(repl, simultaneous=True), *[t for t in (X,Y,Z) if t in (u,v,w)],modulus=2)
        g=pol.as_expr(); variables=pol.gens
        ideal=sp.groebner([g, sp.diff(g,variables[0]), sp.diff(g,variables[1])], *variables,order='lex',modulus=2)
        if list(ideal)!=[sp.Integer(1)]: return False
    return True

def evaluate(f,p):
    return int(f.subs({X:p[0],Y:p[1],Z:p[2]})%2)

def g_point(f,p):
    return tuple(int(sp.diff(f,u).subs({X:p[0],Y:p[1],Z:p[2]})%2) for u in (X,Y,Z))

smooth=[]; plane_point_spectrum=collections.Counter(); point_incidence=collections.defaultdict(list)
for mask in range(1,64):
    f=poly_from_mask(mask)
    n=sum(1-evaluate(f,p) for p in base+open_points)
    ok=nonsingular(f)
    plane_point_spectrum[(int(ok),n)]+=1
    if ok:
        k=len(smooth);smooth.append(mask)
        for j,p in enumerate(base):
            grad=g_point(f,p)
            assert grad != (0,0,0), (mask,p)
            point_incidence[('exceptional',j,grad)].append(k)
        for p in open_points:
            if evaluate(f,p)==0:point_incidence[('open',p)].append(k)

assert len(smooth)==6
assert set(n for (ok,n),count in plane_point_spectrum.items() if ok)=={5}
assert len(point_incidence)==15
assert collections.Counter(map(len,point_incidence.values()))=={2:15}
assert set(tuple(sorted(indices)) for indices in point_incidence.values())==set(itertools.combinations(range(6),2))
assert all((i^j) not in smooth for i,j in itertools.combinations(smooth,2))

result={
 'total_nonzero_sections':63,
 'geometrically_smooth_sections':len(smooth),
 'smooth_masks':smooth,
 'smooth_polynomials':[str(poly_from_mask(m)) for m in smooth],
 'projective_plane_cubic_point_spectrum':[{'smooth':bool(k[0]),'plane_points':k[1],'count':v} for k,v in sorted(plane_point_spectrum.items())],
 'smooth_section_points':{'each':5,'surface_total':15},
 'point_to_curve_incidence_count':15,
 'number_of_curves_through_each_surface_point':2,
 'number_of_surface_points_on_each_smooth_curve':5,
 'each_pair_on_exactly_one_surface_point':True,
 'all_smooth_F2_pencils':0,
 'incidence':[{'point':repr(p),'curves':v} for p,v in sorted(point_incidence.items(),key=lambda item:repr(item[0]))]
}
print(json.dumps(result,indent=2,sort_keys=True))
