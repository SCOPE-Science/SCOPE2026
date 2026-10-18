#!/usr/bin/env python3
"""Exact exhaustive verification for smooth six-point blocking quartics over GF(3).

Requires Python 3 and SymPy. All finite field arithmetic is performed modulo 3.
The Groebner unit-ideal test decides geometric singularities over an
algebraic closure, rather than over a sample of extension fields.
"""
import itertools
import json
import sympy as sp

q=3
X,Y,Z=sp.symbols('X Y Z')
variables=(X,Y,Z)

def normalize(p):
    p=tuple(int(v)%3 for v in p)
    v=next(v for v in p if v)
    return tuple((a*v)%3 for a in p) # nonzero elements of GF(3) invert themselves

points=sorted(set(normalize(p) for p in itertools.product(range(3),repeat=3) if any(p)))
assert len(points)==13
line_masks=[]
for a,b,c in points:
    mask=sum(1<<j for j,(x,y,z) in enumerate(points) if (a*x+b*y+c*z)%3==0)
    line_masks.append(mask)
assert len(set(line_masks))==13 and all(m.bit_count()==4 for m in line_masks)

def is_nontrivial_block(mask):
    return all(mask & lm for lm in line_masks) and not any((mask&lm)==lm for lm in line_masks)

for n in range(1,6):
    assert not any(is_nontrivial_block(sum(1<<i for i in ids))
                   for ids in itertools.combinations(range(13),n))
blocks=[]
for ids in itertools.combinations(range(13),6):
    mask=sum(1<<i for i in ids)
    if is_nontrivial_block(mask):blocks.append(mask)
assert len(blocks)==234
B=blocks[0]
inside=[i for i in range(13) if (B>>i)&1]
outside=[i for i in range(13) if not ((B>>i)&1)]

def det3(m):
    a,b,c,d,e,f,g,h,i=m
    return (a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g))%3

permutation_matrices={}
for m in itertools.product(range(3),repeat=9):
    if det3(m)==0:continue
    permutation=tuple(points.index(normalize((sum(m[3*j+k]*p[k] for k in range(3))
                                               for j in range(3)))) for p in points)
    permutation_matrices.setdefault(permutation,m)
assert len(permutation_matrices)==5616

def image_block(b,perm):
    return sum(1<<perm[i] for i in range(13) if (b>>i)&1)
assert {image_block(B,perm) for perm in permutation_matrices}==set(blocks)
stabilizer=[m for perm,m in permutation_matrices.items() if image_block(B,perm)==B]
assert len(stabilizer)==24

# Full fifteen-dimensional vector space of ternary quartics.
exponents=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
monomials=[X**a*Y**b*Z**c for a,b,c in exponents]
assert len(exponents)==15
E=[[((x**a)*(y**b)*(z**c))%3 for a,b,c in exponents] for x,y,z in points]

# Row-reduce the six independent evaluation conditions.
rref=[E[i][:] for i in inside]
pivots=[]
row=0
for col in range(15):
    pivot=next((k for k in range(row,6) if rref[k][col]!=0),None)
    if pivot is None: continue
    rref[row],rref[pivot]=rref[pivot],rref[row]
    inv=rref[row][col] # inverse in GF(3)
    rref[row]=[(v*inv)%3 for v in rref[row]]
    for k in range(6):
        if k!=row:
            lam=rref[k][col]
            rref[k]=[(x-lam*y)%3 for x,y in zip(rref[k],rref[row])]
    pivots.append(col)
    row+=1
    if row==6:break
assert row==6
free=[j for j in range(15) if j not in pivots]
assert len(free)==9
basis=[]
for col in free:
    c=[0]*15;c[col]=1
    for j,pivot in enumerate(pivots):c[pivot]=(-rref[j][col])%3
    basis.append(tuple(c))
assert all(sum(r[j]*c[j] for j in range(15))%3==0
           for r in (E[i] for i in inside) for c in basis)

# Enumerate all 3^9 forms through B; exclude outside rational zeros.
outside_evaluations=[[sum(E[p][k]*basis[j][k] for k in range(15))%3
                      for j in range(9)] for p in outside]
forms=set()
raw_count=0
for a in itertools.product(range(3),repeat=9):
    if all(sum(u*v for u,v in zip(row,a))%3!=0 for row in outside_evaluations):
        raw_count+=1
        c=tuple(sum(a[j]*basis[j][k] for j in range(9))%3 for k in range(15))
        scale=next(v for v in c if v!=0)
        forms.add(tuple((scale*v)%3 for v in c))
assert raw_count==1134 and len(forms)==567

# Transform quartic equations under every automorphism of B.
exp_lookup={e:i for i,e in enumerate(exponents)}
substitution_matrices=[]
for m in stabilizer:
    linear=[sum(m[3*i+j]*variables[j] for j in range(3)) for i in range(3)]
    T=[[0]*15 for _ in range(15)]
    for i,(a,b,c) in enumerate(exponents):
        f=sp.Poly(linear[0]**a*linear[1]**b*linear[2]**c, X,Y,Z)
        for power,coefficient in f.terms():
            T[i][exp_lookup[power]]=int(coefficient)%3
    substitution_matrices.append(T)

def transform(c,T):
    v=[sum(c[i]*T[i][j] for i in range(15))%3 for j in range(15)]
    scale=next(x for x in v if x)
    return tuple((scale*x)%3 for x in v)

# These are full stabilizer orbits, with no need to enumerate 5616*567 equations.
remaining=set(forms)
orbits=[]
while remaining:
    representative=min(remaining)
    orbit={transform(representative,T) for T in substitution_matrices}
    assert representative in orbit and orbit<=forms
    orbits.append((representative,orbit))
    remaining-=orbit
assert len(orbits)==30 and sum(len(o) for _,o in orbits)==567

def is_smooth_over_closure(c):
    f=sum(coef*term for coef,term in zip(c,monomials))
    for chart in range(3):
        affine=tuple(v for j,v in enumerate(variables) if j!=chart)
        dehomogenized=sp.Poly(f.subs(variables[chart],1),*affine,modulus=3).as_expr()
        ideal=sp.groebner([dehomogenized,sp.diff(dehomogenized,affine[0]),
                           sp.diff(dehomogenized,affine[1])],*affine,modulus=3)
        if len(ideal.polys)!=1 or not ideal.polys[0].is_one:
            return False
    return True

def smooth_at_rational_points(c):
    f=sum(coef*term for coef,term in zip(c,monomials))
    deriv=[sp.Poly(sp.diff(f,v),X,Y,Z,modulus=3) for v in variables]
    return all(any(int(d.eval(dict(zip(variables,points[i]))))%3 for d in deriv)
               for i in inside)

smooth=[]
singular=[]
for c,orbit in orbits:
    if is_smooth_over_closure(c):smooth.append((c,orbit))
    else: singular.append((c,orbit))
assert len(smooth)==10
assert sorted(len(o) for _,o in smooth)==[6]+[24]*9
assert sum(len(o) for _,o in smooth)==222
assert all(smooth_at_rational_points(c) for c,o in smooth)
assert all(not smooth_at_rational_points(c) for c,o in singular)
assert sum(len(o) for _,o in singular)==345
assert len(singular)==20

# One distinguished geometric automorphism orbit has order four; all others trivial.
assert sorted(24//len(o) for _,o in smooth)==[1]*9+[4]
assert 222*234==51948
assert 9*5616+5616//4==51948

result={
    'field':'F_3',
    'projective_points':13,
    'nontrivial_blocking_sixsets':234,
    'projective_group_order':5616,
    'fixed_sixset_point_indices':inside,
    'fixed_sixset_point_coordinates':[points[i] for i in inside],
    'fixed_sixset_stabilizer_order':24,
    'quartic_monomial_exponents':exponents,
    'quartic_linear_system_dimension':9,
    'exact_sixset_projective_equations':567,
    'fixed_sixset_orbits_all':30,
    'fixed_sixset_geometrically_smooth_equations':222,
    'fixed_sixset_geometrically_smooth_orbits':10,
    'all_geometrically_smooth_projective_equations':51948,
    'smooth_orbits':[{'coefficient_vector':list(c),'fixed_sixset_orbit_size':len(o),
                      'full_orbit_size':len(o)*234,'projective_stabilizer_order':24//len(o)}
                     for c,o in smooth]
}
print('VERIFY_OK')
print(json.dumps(result,sort_keys=True,separators=(',',':')))
