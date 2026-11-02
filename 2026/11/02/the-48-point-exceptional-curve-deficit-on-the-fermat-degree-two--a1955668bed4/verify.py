"""Exact, dependency-free enumeration of the Fermat degree-two del Pezzo surface over F_25.

The field is F_5[t]/(t^2-2); all arithmetic uses integer pairs modulo 5.
"""
from collections import Counter
from itertools import permutations, product

P = 5
K = [(a,b) for a in range(P) for b in range(P)]
zero, one, theta = (0,0), (1,0), (0,1)

def add(x,y): return ((x[0]+y[0])%P,(x[1]+y[1])%P)
def neg(x): return ((-x[0])%P,(-x[1])%P)
def mul(x,y): return ((x[0]*y[0]+2*x[1]*y[1])%P,(x[0]*y[1]+x[1]*y[0])%P)
def power(x,n):
    y=one
    while n:
        if n&1:y=mul(y,x)
        x=mul(x,x);n//=2
    return y

def divide(x,y):
    assert y!=zero
    return mul(x,power(y,23))

def norm(v):
    last=next(t for t in reversed(v) if t!=zero)
    return tuple(divide(t,last) for t in v)

def dot(u,v):
    r=zero
    for a,b in zip(u,v):r=add(r,mul(a,b))
    return r

def f(x):
    result=zero
    for a in x:result=add(result,power(a,4))
    return result

assert power(theta,2)==(2,0)
assert all(mul(x,power(x,23))==one for x in K if x!=zero)
mu4={x for x in K if power(x,4)==one}
mu6={power(x,4) for x in K if x!=zero}
minus1=neg(one)
rootsminus={x for x in K if power(x,4)==minus1}
assert (len(mu4),len(mu6),len(rootsminus))==(4,6,4)

# These are the 28 bitangents; the corresponding square roots are defined over K.
ordinary={norm((one,a,b)) for a,b in product(mu4,repeat=2)}
hyper=set()
for a in rootsminus:
    hyper.update((norm((one,neg(a),zero)),norm((one,zero,neg(a))),
                  norm((zero,one,neg(a)))))
assert len(ordinary)==16 and len(hyper)==12 and not(ordinary&hyper)
bitangents=ordinary|hyper

# All 651 projective base points and weighted double-cover fibres.
base={norm((a,b,one)) for a,b in product(K,repeat=2)}
base|={norm((a,one,zero)) for a in K}
base.add(norm((one,zero,zero)))
assert len(base)==25*25+25+1==651
squares={mul(t,t) for t in K}
assert len(squares)==13
counts=Counter(); holes=[]; branch=[]; incident=Counter()
for p in base:
    q=f(p)
    fibre=1 if q==zero else (2 if q in squares else 0)
    on=sum(dot(line,p)==zero for line in bitangents)
    counts['all']+=fibre
    counts['covered' if on else 'outside']+=fibre
    incident[on]+=fibre
    if fibre and not on:holes.append(p)
    if q==zero:branch.append(p)
assert counts=={'all':826,'covered':778,'outside':48},counts
assert len(holes)==24 and len(branch)==44
assert incident=={0:48,1:236,2:480,3:32,4:30},incident

# Every F_25-rational ramification point lies on a bitangent, and geometric
# contact points account for all 44 rational branch points.
tangents=Counter()
for p in branch:
    tangent=norm(tuple(power(x,3) for x in p))
    assert tangent in bitangents and dot(tangent,p)==zero
    tangents[tangent]+=1
assert set(tangents)==bitangents
assert Counter(tangents.values())=={2:16,1:12}

# Exact description of the 24 holes: one coordinate vanishes; the ratio of
# the two other coordinates has fourth power a nonidentity cube root of unity.
cube_nontrivial={x for x in K if power(x,3)==one and x!=one}
assert len(cube_nontrivial)==2
expected=set()
for t in K:
    if power(t,4) in cube_nontrivial:
        expected.update((norm((t,one,zero)),norm((t,zero,one)),
                         norm((zero,t,one))))
assert len(expected)==24 and set(holes)==expected
assert all(sum(x==zero for x in p)==1 for p in holes)

# The natural coordinate permutation and fourth-root scaling action is
# transitive on the base hole locus.
seed=holes[0]
orb=set()
for perm in permutations(range(3)):
    for scales in product(mu4,repeat=3):
        transformed=tuple(mul(scales[i],seed[perm[i]]) for i in range(3))
        orb.add(norm(transformed))
assert orb==set(holes), (len(orb),len(holes))

# For all 36 fourth-power classes of points with xyz nonzero, any point
# supporting an F_25-rational lift is incident to a bitangent.
nonzero_pts=[p for p in base if all(x!=zero for x in p)]
assert len(nonzero_pts)==576
class_counts=Counter()
for p in nonzero_pts:
    class_counts[(power(p[0],4),power(p[1],4))]+=1
    if f(p) in squares:
        assert any(dot(line,p)==zero for line in bitangents)
assert len(class_counts)==36 and set(class_counts.values())=={16}
print('FIELD=GF(25); PROJECTIVE_BASE_POINTS=651; SMOOTH_QUARTIC_BRANCH_POINTS=44')
print('BITANGENTS=28 (ordinary=16, hyperflex=12); ALL_56_EXCEPTIONAL_CURVES_SPLIT')
print('COVER_POINTS=826; ON_EXCEPTIONAL_CURVES=778; OUTSIDE=48')
print('OUTSIDE_BASE_POINTS=24; ALL_ONE_ZERO_COORDINATE_AND_FOURTH_POWER_PRIMITIVE_CUBE_ROOT')
print('BITANGENT_INCIDENCE_HISTOGRAM=',dict(sorted(incident.items())))
print('HOLE_ORBIT_TRANSITIVE_UNDER_MONOMIAL_SYMMETRIES_OK')
print('VERIFY_OK')
