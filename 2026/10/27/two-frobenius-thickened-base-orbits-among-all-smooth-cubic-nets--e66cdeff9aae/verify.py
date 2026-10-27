"""Exact geometric-smoothness, linear-net, projective-orbit, and base-scheme census.

Run with Python 3 and SymPy. No input files or network access required.
All symbolic arithmetic is over GF(2); all projective orbits are exhaustive.
"""
import itertools
import json
from collections import Counter
import sympy as sp

X, Y, Z = sp.symbols('X Y Z')
VARS = (X, Y, Z)
EXP = [(a,b,3-a-b) for a in range(3,-1,-1) for b in range(3-a,-1,-1)]
INDEX = {e:i for i,e in enumerate(EXP)}

def polynomial(f):
    return sum(((f >> i) & 1) * X**a * Y**b * Z**c
               for i,(a,b,c) in enumerate(EXP))

def unit_basis(polys,variables):
    g=sp.groebner(polys,*variables,modulus=2)
    return len(g.polys)==1 and g.polys[0].is_one

def smooth(f):
    if f==0: return False
    F=polynomial(f)
    grads=[sp.diff(F,v) for v in VARS]
    if not unit_basis([g.subs(X,1) for g in grads],(Y,Z)):
        return False
    if not unit_basis([g.subs({X:0,Y:1}) for g in grads],(Z,)):
        return False
    return any(g.subs({X:0,Y:0,Z:1})%2 for g in grads)

def row_reduce(*rows):
    r=list(rows)
    n=0
    for bit in range(9,-1,-1):
        pivot=next((j for j in range(n,len(r)) if (r[j]>>bit)&1),None)
        if pivot is None:continue
        r[n],r[pivot]=r[pivot],r[n]
        for j in range(len(r)):
            if j!=n and (r[j]>>bit)&1:r[j]^=r[n]
        n+=1
        if n==len(r):break
    return tuple(r)

def matrix_rank(A):
    rows=[sum(A[i][j]<<j for j in range(3)) for i in range(3)]
    n=0
    for j in range(3):
        pivot=next((i for i in range(n,3) if (rows[i]>>j)&1),None)
        if pivot is None:continue
        rows[n],rows[pivot]=rows[pivot],rows[n]
        for i in range(3):
            if i!=n and (rows[i]>>j)&1:rows[i]^=rows[n]
        n+=1
    return n

def monomial_action(A):
    linear=[]
    for i in range(3):
        linear.append({tuple(int(j==k) for j in range(3)):1
                      for k in range(3) if A[i][k]})
    def product(a,b):
        out={}
        for u in a:
            for v in b:
                w=tuple(u[i]+v[i] for i in range(3))
                out[w]=out.get(w,0)^1
        return {k:1 for k,v in out.items() if v}
    images=[]
    for exps in EXP:
        p={(0,0,0):1}
        for i in range(3):
            for _ in range(exps[i]):p=product(p,linear[i])
        images.append(sum(1<<INDEX[t] for t in p))
    return images

def geometric_base(basis):
    F=[polynomial(v) for v in basis]
    affine=sp.groebner([f.subs(X,1) for f in F],Y,Z,modulus=2)
    x0=sp.groebner([f.subs({X:0,Y:1}) for f in F],Z,modulus=2)
    infinity=all(f.subs({X:0,Y:0,Z:1})%2==0 for f in F)
    assert unit_basis(x0.polys,(Z,)) and not infinity
    if unit_basis(affine.polys,(Y,Z)):
        return {'length':0,'affine_groebner':['1']}
    generators=[str(f.as_expr()) for f in affine.polys]
    # The only exceptional ideal type is (Y + h(Z), (Z^3+Z^2+1)^2).
    zpolys=[p.as_expr() for p in affine.polys if Y not in p.as_expr().free_symbols]
    assert len(zpolys)==1
    assert sp.Poly(zpolys[0],Z,modulus=2)==sp.Poly((Z**3+Z**2+1)**2,Z,modulus=2)
    return {'length':6,'affine_groebner':generators}


def main():
    good={f for f in range(1,1024) if smooth(f)}
    pencils={row_reduce(a,b) for a in good for b in good if a<b and (a^b) in good}
    nets={row_reduce(a,b,c) for a,b in pencils for c in good
          if c^a in good and c^b in good and c^a^b in good}
    assert (len(good),len(pencils),len(nets))==(336,5544,864)
    actions=[]
    for digits in itertools.product((0,1),repeat=9):
        A=[digits[3*i:3*i+3] for i in range(3)]
        if matrix_rank(A)!=3:continue
        mon=monomial_action(A)
        table=[0]*1024
        for i in range(1,1024):
            low=i&-i
            table[i]=table[i^low]^mon[low.bit_length()-1]
        actions.append(table)
    assert len(actions)==168
    remaining=set(nets)
    orbit_data=[]
    rational_points=[(1,y,z) for y in (0,1) for z in (0,1)] + [(0,1,z) for z in (0,1)] + [(0,0,1)]
    def point_count(f):
        P=polynomial(f)
        return sum(P.subs(dict(zip(VARS,p)))%2==0 for p in rational_points)
    while remaining:
        r=min(remaining)
        orbit={row_reduce(T[r[0]],T[r[1]],T[r[2]]) for T in actions}
        assert orbit<=remaining
        remaining-=orbit
        seven=[r[0],r[1],r[2],r[0]^r[1],r[0]^r[2],r[1]^r[2],r[0]^r[1]^r[2]]
        profile=sorted(point_count(f) for f in seven)
        common=sum(all(polynomial(f).subs(dict(zip(VARS,p)))%2==0 for f in r) for p in rational_points)
        assert common==0
        orbit_data.append({'basis':list(r),'orbit_size':len(orbit),'stabilizer_order':168//len(orbit),
                           'rational_point_profile':profile,'rational_base_points':common,
                           'geometric_base':geometric_base(r)})
    orbit_data.sort(key=lambda d:(d['orbit_size'],d['basis']))
    assert Counter(d['orbit_size'] for d in orbit_data)=={168:5,8:3}
    assert sum(d['orbit_size'] for d in orbit_data if d['geometric_base']['length']>0)==16
    print(json.dumps({'smooth_cubics':len(good),'all_smooth_pencils':len(pencils),
        'all_smooth_nets':len(nets),'projective_equivalence_classes':len(orbit_data),
        'geometrically_basepoint_free_nets':848,'nonreduced_length_six_base_nets':16,
        'orbits':orbit_data},indent=2))

if __name__=='__main__':main()
