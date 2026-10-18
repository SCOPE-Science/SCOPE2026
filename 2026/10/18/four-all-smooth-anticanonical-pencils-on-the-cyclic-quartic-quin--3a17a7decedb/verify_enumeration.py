#!/usr/bin/env python3
"""Reproduce an anticanonical-pencil census on a C4-twisted quintic del Pezzo surface.
All arithmetic is exact. Python 3 and SymPy are required.
"""
import itertools
import json
from collections import Counter
from functools import reduce
import sympy as sp

MODULUS16 = 0b10011  # t^4+t+1 over F2
MONOMIALS = [(i,j,3-i-j) for i in range(3,-1,-1) for j in range(3-i,-1,-1)]
X,Y,Z = sp.symbols('X Y Z')


def mul(a,b,poly=MODULUS16,d=4):
    ans=0
    for _ in range(d):
        if b & 1: ans ^= a
        b >>= 1
        a <<= 1
        if a & (1<<d): a ^= poly
    assert b==0
    return ans


def pw(a,n):
    ans=1
    while n:
        if n&1: ans=mul(ans,a)
        a=mul(a,a)
        n//=2
    return ans


def value(p,e):
    ans=1
    for a,n in zip(p,e): ans=mul(ans,pw(a,n))
    return ans


def normalize(p):
    u=next(a for a in p if a)
    v=pw(u,14)
    return tuple(mul(a,v) for a in p)


def frobenius(p):
    return normalize(tuple(mul(a,a) for a in p))


def determinant(rows):
    ret=0
    for perm in itertools.permutations((0,1,2)):
        ret ^= mul(mul(rows[0][perm[0]],rows[1][perm[1]]),rows[2][perm[2]])
    return ret


def mask_eval(mask,p):
    return reduce(lambda acc,k:acc^value(p,MONOMIALS[k]),
                  (k for k in range(10) if mask>>k&1),0)


def polynomial(mask):
    return sum(X**i*Y**j*Z**k for h,(i,j,k) in enumerate(MONOMIALS) if mask>>h&1)


def is_smooth(mask):
    poly=polynomial(mask)
    for fixed in (X,Y,Z):
        variables=[v for v in (X,Y,Z) if v!=fixed]
        p=sp.Poly(poly.subs(fixed,1),*variables,modulus=2)
        ideal=sp.groebner([p]+[p.diff(t) for t in variables],*variables,modulus=2)
        if len(ideal.polys)!=1 or not ideal.polys[0].is_one:
            return False
    return True


def rank_binary_3(rows):
    mat=list(rows)
    rank=0
    for j in range(3):
        pivot=next((k for k in range(rank,3) if (mat[k]>>j)&1),None)
        if pivot is None: continue
        mat[rank],mat[pivot]=mat[pivot],mat[rank]
        for k in range(3):
            if k!=rank and mat[k]>>j&1:mat[k]^=mat[rank]
        rank+=1
    return rank


def transform_point(M,p):
    return normalize(tuple(reduce(lambda v,j:v^mul(p[j],(M[i]>>j)&1),range(3),0)
                           for i in range(3)))


def multiply_polys(a,b):
    coefficients={}
    for u in a:
        for v in b:
            e=tuple(u[k]+v[k] for k in range(3))
            coefficients[e]=coefficients.get(e,0)^1
    return {e for e,c in coefficients.items() if c}


def substitute(mask,M):
    lin=[{tuple(int(k==h) for k in range(3)) for h in range(3) if M[j]>>h&1}
         for j in range(3)]
    out=set()
    for k,e in enumerate(MONOMIALS):
        if not(mask>>k&1): continue
        term={(0,0,0)}
        for j in range(3):
            for _ in range(e[j]):term=multiply_polys(term,lin[j])
        out ^= term
    return sum(1<<MONOMIALS.index(e) for e in out)


def points2():
    return sorted({normalize(p) for p in itertools.product((0,1),repeat=3) if any(p)})


def main():
    # The field F16 is F2[t]/(t^4+t+1); p is the closed orbit of [1:t:t^2].
    assert pw(2,4)!=2 and pw(2,16)==2
    start=(1,2,4)
    orbit=[start]
    for k in range(3): orbit.append(frobenius(orbit[-1]))
    assert frobenius(orbit[-1])==start
    assert len(set(orbit))==4
    assert all(determinant([orbit[i],orbit[j],orbit[k]])!=0
               for i,j,k in itertools.combinations(range(4),3))

    # All four geometric conjugates are zeros of a rational cubic iff its
    # coefficients satisfy one F16-valued (four F2-linear) evaluation equation.
    sections=[m for m in range(1,1<<10) if mask_eval(m,start)==0]
    assert len(sections)==63
    smooth=sorted(m for m in sections if is_smooth(m))
    assert len(smooth)==18
    qpts=points2()
    point_numbers={m:sum(mask_eval(m,p)==0 for p in qpts) for m in smooth}
    counts=Counter(point_numbers.values())
    assert counts==Counter({1:5,2:4,4:4,5:5})

    pencils=set()
    for f,g in itertools.combinations(smooth,2):
        if (f^g) in smooth:
            pencils.add(frozenset((f,g,f^g)))
    assert len(pencils)==4
    pencil_profiles=Counter(tuple(sorted(point_numbers[m] for m in pencil))
                            for pencil in pencils)
    assert pencil_profiles==Counter({(1,1,5):4})

    # The full rational automorphism group of this blow-up is the subgroup
    # of PGL3(F2) preserving the four-point orbit; enumerate without assumptions.
    stabilizer=[]
    for M in itertools.product(range(8),repeat=3):
        if rank_binary_3(M)!=3: continue
        if {transform_point(M,p) for p in orbit}==set(orbit):stabilizer.append(M)
    assert len(stabilizer)==4
    assert len([M for M in itertools.product(range(8),repeat=3)
                if rank_binary_3(M)==3])==168
    representative=next(t for t in pencils if 0x189 in t and 0x2e4 in t)
    orbit_of_pencil={frozenset(substitute(m,M) for m in representative)
                     for M in stabilizer}
    assert orbit_of_pencil==pencils

    # A single orbit representative is enough for the base-scheme calculation.
    a,b=sorted(representative)[:2]
    f=polynomial(a);g=polynomial(b)
    gb=sp.groebner([f.subs(X,1),g.subs(X,1)],Z,Y,modulus=2)
    exprs=[p.as_expr() for p in gb.polys]
    linear=next(expr for expr in exprs if expr.has(Z))
    eliminant=next(expr for expr in exprs if not expr.has(Z))
    factors=sp.factor_list(eliminant,modulus=2)[1]
    degrees=sorted((sp.Poly(p,Y,modulus=2).degree(),e) for p,e in factors)
    assert degrees==[(4,1),(5,1)]
    assert sp.degree(linear,Z)==1
    assert sp.diff(linear,Z)==1
    assert not sp.Poly(eliminant,Y,modulus=2).gcd(sp.Poly(sp.diff(eliminant,Y),Y,modulus=2)).degree()
    # Check the intersection has no points with X=0.
    inf_f=sp.Poly(f.subs({X:0,Z:1}),Y,modulus=2)
    inf_g=sp.Poly(g.subs({X:0,Z:1}),Y,modulus=2)
    assert inf_f.gcd(inf_g).degree()==0
    assert not(f.subs({X:0,Y:1,Z:0})==0 and g.subs({X:0,Y:1,Z:0})==0)
    assert not any(mask_eval(a,p)==0 and mask_eval(b,p)==0 for p in qpts)

    result={
      'field':'F2[t]/(t^4+t+1)','closed_point_orbit':[list(p) for p in orbit],
      'section_dimension':6,'nonzero_anticanonical_members':len(sections),
      'smooth_anticanonical_members':len(smooth),'smooth_masks':[hex(x) for x in smooth],
      'rational_point_distribution':dict(sorted(counts.items())),
      'all_smooth_pencils':len(pencils),
      'pencils':[[hex(m) for m in sorted(p)] for p in sorted(pencils,key=lambda t:sorted(t))],
      'pencil_member_point_profile':[1,1,5],
      'surface_automorphism_group_size':len(stabilizer),
      'surface_automorphism_matrices':[list(M) for M in stabilizer],
      'number_of_pencil_orbits':1,'representative':[hex(a),hex(b)],
      'representative_groebner_basis':[str(z) for z in exprs],
      'elimination_factor_degrees':[d for d,e in degrees],
      'base_closed_point_degrees':[5]
    }
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__=='__main__':main()
