#!/usr/bin/env python3
"""Exact binary-quartic tangent-covering and projective-orbit certificate.

Requires Python 3.10+ and SymPy 1.12+.  All finite field arithmetic is
performed in F_2; the reduced Groebner bases decide geometric singularity
via the Nullstellensatz, not by checking finitely many extension fields.
"""
import collections
import itertools
import json
from sympy import symbols, diff, groebner

# Monomial order is x^i y^j z^(4-i-j), indexed by increasing (i,j).
MONOMIALS = tuple((i, j, 4-i-j) for i in range(5) for j in range(5-i))
MON_INDEX = {exp:i for i,exp in enumerate(MONOMIALS)}
POINTS = tuple(range(1, 8))
assert len(MONOMIALS) == 15

def bit(p, j):
    return (p >> (2-j)) & 1

def at_point(exp, p):
    return all(bit(p,j) or exp[j] == 0 for j in range(3))

EVAL_MASKS = []
DERIV_MASKS = []
for p in POINTS:
    EVAL_MASKS.append(sum(1 << i for i,m in enumerate(MONOMIALS) if at_point(m,p)))
    DERIV_MASKS.append(tuple(
        sum(1 << i for i,m in enumerate(MONOMIALS)
            if (m[j]&1) and at_point(tuple(e-(k==j) for k,e in enumerate(m)),p))
        for j in range(3)
    ))
LINE_SETS = {g: sum(1<<i for i,p in enumerate(POINTS)
                    if (g&p).bit_count()%2==0) for g in POINTS}
assert all(s.bit_count()==3 for s in LINE_SETS.values())

def class_data(mask):
    rational = []
    tangents = []
    covered = 0
    for i,p in enumerate(POINTS):
        if ((mask & EVAL_MASKS[i]).bit_count() & 1) == 0:
            rational.append(p)
            gradient = sum(1<< (2-j) for j,m in enumerate(DERIV_MASKS[i])
                           if (mask&m).bit_count()&1)
            if gradient == 0:
                return rational, tangents, -1
            tangents.append(gradient)
            covered |= LINE_SETS[gradient]
    return rational, tangents, covered

# Enumerate EVERY quartic over F_2; its only nonzero scalar is 1.
THREE = set()
for mask in range(1, 1<<len(MONOMIALS)):
    points, tangents, covered = class_data(mask)
    if len(points)==3 and covered==127:
        THREE.add(mask)
assert len(THREE)==448

# Enumerate the entire projective group PGL_3(F_2)=GL_3(F_2).
def mult(f,g):
    h = set()
    for a in f:
        for b in g:
            m=tuple(a[j]+b[j] for j in range(3))
            if m in h: h.remove(m)
            else: h.add(m)
    return h

def power(f,n):
    r={(0,0,0)}
    for _ in range(n): r=mult(r,f)
    return r

TRANSFORMS=[]
for rows in itertools.product(POINTS, repeat=3):
    a,b,c=rows
    if len({0,a,b,c,a^b,a^c,b^c,a^b^c})!=8:
        continue
    linear=[{tuple(1 if j==k else 0 for j in range(3))
             for k in range(3) if bit(row,k)} for row in rows]
    pwrs=[[power(f,n) for n in range(5)] for f in linear]
    images=[]
    for i,j,k in MONOMIALS:
        v=mult(mult(pwrs[0][i],pwrs[1][j]),pwrs[2][k])
        images.append(sum(1 << MON_INDEX[m] for m in v))
    TRANSFORMS.append(tuple(images))
assert len(TRANSFORMS)==168

def act(mask,images):
    output=0
    while mask:
        lb=mask&-mask
        output ^= images[lb.bit_length()-1]
        mask ^= lb
    return output

remaining=set(THREE)
ORBITS=[]
while remaining:
    representative=min(remaining)
    orbit={act(representative,T) for T in TRANSFORMS}
    assert orbit <= THREE
    assert orbit <= remaining
    remaining.difference_update(orbit)
    ORBITS.append((representative, orbit))
assert not remaining
assert sorted((m,len(s)) for m,s in ORBITS)==[
    (4114,84),(4115,84),(4306,84),(4309,28),(4383,168)
]

x,y,z=symbols('x y z')
XYZ=(x,y,z)

def expression(mask):
    return sum((x**i*y**j*z**k for b,(i,j,k) in enumerate(MONOMIALS)
                if mask&(1<<b)), 0)

def singular_chart_bases(mask):
    f=expression(mask)
    answer=[]
    for a in XYZ:
        v=tuple(t for t in XYZ if t!=a)
        g=f.subs(a,1)
        B=groebner((g,diff(g,v[0]),diff(g,v[1])),*v,order='lex',modulus=2)
        answer.append([str(p.as_expr()) for p in B.polys])
    return answer

def smooth(mask):
    return all(b==['1'] for b in singular_chart_bases(mask))

SMOOTH_REPS=[]
for rep,orb in ORBITS:
    if smooth(rep):
        SMOOTH_REPS.append((rep,len(orb)))
assert SMOOTH_REPS==[(4114,84),(4115,84),(4309,28),(4383,168)]
assert singular_chart_bases(4306)[0] != ['1']
assert sum(v for _,v in SMOOTH_REPS)==364

# The Gauss-point incidence and the projective tangent pencil are checked
# separately on each smooth representative.
ORBIT_REPORT=[]
for rep,size in SMOOTH_REPS:
    points,tangents,covered=class_data(rep)
    assert len(points)==3 and len(set(tangents))==3 and covered==127
    center=set(POINTS)
    for t in tangents:
        center &= {p for p in POINTS if (t&p).bit_count()%2==0}
    assert len(center)==1
    # The three points are not on one F_2 line.
    assert not any(all((g&p).bit_count()%2==0 for p in points)
                   for g in POINTS)
    ORBIT_REPORT.append({
        'representative_mask':rep,
        'quartic':str(expression(rep)),
        'orbit_size':size,
        'stabilizer_order':168//size,
        'rational_points':points,
        'rational_tangent_lines':tangents,
        'tangent_pencil_center':min(center),
        'center_on_curve':min(center) in points,
        'geometric_singularity_bases':singular_chart_bases(rep),
    })
assert sum(r['orbit_size'] for r in ORBIT_REPORT if r['center_on_curve'])==252
assert sum(r['orbit_size'] for r in ORBIT_REPORT if not r['center_on_curve'])==112

# Independent direct substitution tests values and all three derivatives
# of every candidate, without reusing the precomputed evaluation masks.
for rep in THREE:
    for pi,p in enumerate(POINTS):
        direct=sum(at_point(m,p) for i,m in enumerate(MONOMIALS)
                   if (rep>>i)&1)%2
        assert direct==((rep&EVAL_MASKS[pi]).bit_count()%2)
        for var in range(3):
            dval=sum(at_point(tuple(m[k]-(k==var) for k in range(3)),p)
                     for i,m in enumerate(MONOMIALS)
                     if (rep>>i)&1 and (m[var]&1))%2
            assert dval==((rep&DERIV_MASKS[pi][var]).bit_count()%2)

result={
    'total_nonzero_binary_quartics':(1<<15)-1,
    'three_point_rationally_smooth_tangent_covering_quartics':len(THREE),
    'rationally_smooth_tangent_covering_orbits':[(r,len(o)) for r,o in ORBITS],
    'geometrically_smooth_tangent_covering_three_point_quartics':364,
    'smooth_projective_orbits':ORBIT_REPORT,
    'geometrically_singular_three_point_orbit_representative':4306,
    'singular_representative_affine_bases':singular_chart_bases(4306),
    'center_on_curve_count':252,
    'center_off_curve_count':112,
}
if __name__=='__main__':
    print(json.dumps(result, indent=2))
