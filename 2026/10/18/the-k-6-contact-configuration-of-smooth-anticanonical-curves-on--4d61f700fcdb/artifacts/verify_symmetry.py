"""Exact finite group computation for the split quintic del Pezzo surface.
Enumerates plane transformations stabilizing four base points and the
standard quadratic Cremona generator, then acts on cubic coefficients.
Run: python3 verify_symmetry.py
"""
import itertools, json
from functools import reduce
import sympy as sp
X,Y,Z=sp.symbols('X Y Z')
V=[X,Y,Z]
mon=[X*X*Y,X*X*Z,X*Y*Y,X*Y*Z,X*Z*Z,Y*Y*Z,Y*Z*Z]
basis=[mon[i]+mon[6] for i in range(6)]
base={(1,0,0),(0,1,0),(0,0,1),(1,1,1)}

def coefficients(f):
    pp=sp.Poly(f,X,Y,Z,modulus=2)
    return tuple(int(pp.coeff_monomial(t))&1 for t in mon)

def det2(a):
    perms=list(itertools.permutations((0,1,2)))
    return reduce(lambda q,p:q^reduce(lambda t,i:t&a[i][p[i]],range(3),1),perms,0)

def linear_matrix(a):
    forms=[sum(a[i][j]*V[j] for j in range(3)) for i in range(3)]
    return tuple(coefficients(f.subs({X:forms[0],Y:forms[1],Z:forms[2]},simultaneous=True).expand())[:6] for f in basis)

T=[]
for bits in itertools.product((0,1),repeat=9):
    a=(bits[:3],bits[3:6],bits[6:9])
    if not det2(a):continue
    mapped={tuple(sum(a[i][j]*p[j] for j in range(3))&1 for i in range(3)) for p in base}
    if mapped==base:T.append(linear_matrix(a))
assert len(T)==24
cremona=[]
for f in basis:
    pp=sp.Poly(f.subs({X:Y*Z,Y:X*Z,Z:X*Y},simultaneous=True).expand(),X,Y,Z,modulus=2)
    transformed=0
    for exponent,c in pp.terms():
        assert min(exponent)>=1
        transformed+=int(c)*X**(exponent[0]-1)*Y**(exponent[1]-1)*Z**(exponent[2]-1)
    cremona.append(coefficients(transformed)[:6])
cremona=tuple(cremona)

def multiply(a,b):
    return tuple(tuple(reduce(lambda u,v:u^v,(a[i][k]&b[k][j] for k in range(6)),0) for j in range(6)) for i in range(6))

identity=tuple(tuple(int(i==j) for j in range(6)) for i in range(6))
G={identity};todo=[identity]
while todo:
    a=todo.pop()
    for b in T+[cremona]:
        product=multiply(a,b)
        if product not in G:G.add(product);todo.append(product)
assert len(G)==120

def act(a,n):
    return sum((reduce(lambda u,v:u^v,((n>>i&1)&a[i][j] for i in range(6)),0))<<j for j in range(6))

rest=set(range(1,64));orbits=[]
while rest:
    a=min(rest)
    orbit={act(g,a) for g in G}
    assert orbit<=rest
    orbits.append(orbit)
    rest-=orbit
sizes=sorted(len(o) for o in orbits)
assert sizes==[6,10,12,15,20]
smooth=sorted(next(o for o in orbits if 7 in o))
assert smooth==[7,22,38,49,51,53]
induced_perms={tuple(smooth.index(act(g,n)) for n in smooth) for g in G}
assert len(induced_perms)==120
assert len({(p[0],p[1],p[2]) for p in induced_perms})==120
result={'linear_stabilizer_order':len(T),'automorphism_group_order':len(G),'orbit_sizes':sizes,
        'six_smooth_curve_orbit':smooth,'smooth_curve_stabilizer_order':len(G)//6,
        'induced_permutation_group_order':len(induced_perms),
        'ordered_triple_orbit_size':120,'sharply_three_transitive':True,
        'all_smooth_pencils':sum(1 for a,b in itertools.combinations(smooth,2) if a^b in smooth)}
print(json.dumps(result,indent=2,sort_keys=True))
