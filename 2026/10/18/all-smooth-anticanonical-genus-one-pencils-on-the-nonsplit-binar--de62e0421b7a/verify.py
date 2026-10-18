#!/usr/bin/env python3
"""Exact finite-field verification of genus-one pencil incidence on Q^-(3,2).

Requires Python 3 and sympy. All projective and coefficient spaces are finite.
The Gröbner tests are over GF(2), so they decide geometric smoothness.
"""
import collections
import itertools
import json
from pathlib import Path
import sympy as sp

x = sp.symbols('x0:4')
M_PAIRS = [(0,0),(1,1),(2,2),(2,3),(3,3),(0,2),(0,3),(1,2),(1,3)]
MON = [x[i]*x[j] for (i,j) in M_PAIRS]
Q = x[0]*x[1] + x[2]**2 + x[2]*x[3] + x[3]**2
DQ = [sp.diff(Q, t) for t in x]

def poly(mask):
    return sum((MON[i] for i in range(9) if mask >> i & 1), sp.Integer(0))

def unit_ideal(forms, pivot):
    other = [x[k] for k in range(4) if k != pivot]
    gb = sp.groebner([p.subs(x[pivot], 1) for p in forms], *other,
                     modulus=2, order='grevlex')
    return len(gb.polys) == 1 and gb.polys[0].as_expr() == 1

def smooth(mask):
    G = poly(mask)
    DG = [sp.diff(G, t) for t in x]
    minors = [DQ[i]*DG[j] - DQ[j]*DG[i]
              for i in range(4) for j in range(i+1,4)]
    return all(unit_ideal([Q,G]+minors, k) for k in range(4))

def reduced_base(a,b):
    F,G = poly(a),poly(b)
    jac = [DQ,[sp.diff(F,t) for t in x],[sp.diff(G,t) for t in x]]
    minors = [sp.det(sp.Matrix([[jac[r][c] for c in cols]
                                for r in range(3)]))
              for cols in itertools.combinations(range(4),3)]
    return all(unit_ideal([Q,F,G]+minors, k) for k in range(4))

def bitquad(mask, v):
    return sum(((v>>i)&1)*((v>>j)&1) for k,(i,j) in enumerate(M_PAIRS)
               if (mask>>k)&1)&1

def q(v):
    return ((v&1)*((v>>1)&1)) ^ ((v>>2)&1) ^ (((v>>2)&1)*((v>>3)&1)) ^ ((v>>3)&1)

def plane_eval(plane,v):
    return ((plane&v).bit_count())&1

def vector_from_values(vals):
    d = [vals[1<<i] for i in range(4)]
    off = {(i,j):vals[(1<<i)|(1<<j)] ^ d[i] ^ d[j]
           for i in range(4) for j in range(i+1,4)}
    # Quotient by x0*x1 + x2*x2 + x2*x3 + x3*x3.
    d[2] ^= off[(0,1)]
    d[3] ^= off[(0,1)]
    off[(2,3)] ^= off[(0,1)]
    return sum((int(d[i] if i==j else off[(i,j)])<<k)
               for k,(i,j) in enumerate(M_PAIRS))

def automorphisms():
    result=[]
    for a in range(1,16):
      for b in range(1,16):
       if b == a: continue
       for c in range(1,16):
        if c in (a,b,a^b): continue
        span3={0,a,b,a^b,c,a^c,b^c,a^b^c}
        for d in range(1,16):
         if d in span3: continue
         col=(a,b,c,d)
         if [q(t) for t in col] != [q(1<<i) for i in range(4)]: continue
         if any(q(col[i]^col[j]) != q((1<<i)|(1<<j))
                for i in range(4) for j in range(i+1,4)): continue
         result.append(col)
    return result

def substitution_of_basis(col):
    def image(v):
        w=0
        for i in range(4):
            if v>>i&1: w ^= col[i]
        return w
    return tuple(vector_from_values({v:bitquad(1<<j,image(v))
                                     for v in range(1,16)}) for j in range(9))

def apply(mask, transforms):
    ans=0
    for i in range(9):
        if mask>>i&1: ans^=transforms[i]
    return ans

def calculate():
    pts = [v for v in range(1,16) if not q(v)]
    assert pts == [1,2,7,11,15]
    good={m for m in range(1,512) if smooth(m)}
    assert len(good)==240
    # The 15 sections through the entire five-point ovoid are reducible:
    kernel={m for m in range(512) if all(bitquad(m,p)==0 for p in pts)}
    assert len(kernel)==16
    union_products=set()
    for L1 in range(1,16):
      for L2 in range(L1+1,16):
        if not all(plane_eval(L1,p)==0 or plane_eval(L2,p)==0 for p in pts):continue
        v=vector_from_values({t: plane_eval(L1,t)*plane_eval(L2,t)
                              for t in range(1,16)})
        union_products.add(v)
    assert len(union_products)==15 and union_products==kernel-{0}
    assert not good.intersection(kernel)
    # A line over F2 has three nonzero elements. Count each only once.
    pencils=set()
    for a in sorted(good):
        for b in sorted(good):
            if a<b and (a^b) in good:
                pencils.add(tuple(sorted((a,b,a^b))))
    assert len(pencils)==4020
    def bcount(w):
        return sum(all(bitquad(m,p)==0 for m in w) for p in pts)
    counts=collections.Counter(bcount(w) for w in pencils)
    assert dict(sorted(counts.items()))=={0:1440,1:1920,2:540,3:120}
    matrices=automorphisms()
    assert len(matrices)==120
    trans=[substitution_of_basis(M) for M in matrices]
    # Complete group acts faithfully on the five rational points (a projective frame).
    assert all({apply(m,t) for m in good}==good for t in trans)
    remaining=pencils.copy()
    rows=[]
    while remaining:
        w=min(remaining)
        orbit={tuple(sorted(apply(m,t) for m in w)) for t in trans}
        assert orbit <= pencils
        rows.append((bcount(w),len(orbit),w))
        remaining -= orbit
    rows.sort()
    assert len(rows)==36
    strata={b:(sum(size for z,size,_ in rows if z==b),
               sum(1 for z,size,_ in rows if z==b)) for b in range(4)}
    assert strata=={0:(1440,13),1:(1920,16),2:(540,6),3:(120,1)}
    # All maximal pencils have eight distinct base points over the algebraic closure.
    red=collections.Counter()
    for b,size,w in rows:
        red[(b,reduced_base(w[0],w[1]))]+=size
    expected_red={(0,True):1200,(0,False):240,
                  (1,True):1680,(1,False):240,
                  (2,True):260,(2,False):280,
                  (3,True):120}
    assert dict(red)==expected_red
    ext=[w for b,size,w in rows if b==3]
    assert ext==[(34,202,232)]
    assert reduced_base(34,202)
    assert [p for p in pts if bitquad(34,p)==0 and bitquad(202,p)==0]==[1,7,15]
    # Elimination for the unique extremal orbit, on x0 != 0.
    gb=sp.groebner([e.subs(x[0],1) for e in [Q,poly(34),poly(202)]],
                   *x[1:],modulus=2,order='lex')
    e3=next(p.as_expr() for p in gb.polys if p.as_expr().free_symbols=={x[3]})
    fac=sp.factor_list(e3,modulus=2)[1]
    assert sorted((sp.degree(f,x[3]),n) for f,n in fac)==[(1,1),(1,1),(5,1)]
    assert any(sp.degree(f,x[3])==5 and
               sp.Poly(f,x[3],modulus=2).is_irreducible for f,n in fac)
    out={
      'quadric':'x0*x1+x2^2+x2*x3+x3^2',
      'total_nonzero_sections':511,'smooth_sections':240,
      'rational_quadric_points':pts,'all_five_point_kernel_nonzero':15,
      'smooth_pencils':len(pencils),'full_automorphism_order':len(matrices),
      'pencil_orbits':len(rows),
      'strata':[{'rational_base_points':b,'pencils':strata[b][0],
                 'projective_orbits':strata[b][1],
                 'reduced_bases':red[(b,True)],
                 'nonreduced_bases':red[(b,False)]} for b in range(4)],
      'maximal_representative_masks':[34,202,232],
      'maximal_base_point_labels':[1,7,15],
      'maximal_orbit_size':120,
      'maximal_base_frobenius_degrees':[1,1,1,5],
      'orbits':[{'rational_base_points':b,'orbit_size':size,'masks':list(w)}
                for b,size,w in rows]
    }
    return out

if __name__=='__main__':
    got=calculate()
    directory=Path(__file__).resolve().parent
    expected=json.loads((directory/'data'/'expected.json').read_text(encoding='utf-8'))
    assert got==expected, 'Exhaustive finite-field invariants differ from expected values'
    print('PASS: 511 complete sections, 4020 complete pencils, 36 orbits, 120 extremal pencils')
    print('PASS: exact geometric smoothness, base reducedness, 15 reducible ovoid sections')
    print('PASS: extremal degree pattern (1,1,1,5); all results match data/expected.json')
