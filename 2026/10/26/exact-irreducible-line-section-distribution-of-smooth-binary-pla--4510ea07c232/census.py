#!/usr/bin/env python3
"""Exact census of irreducible rational line sections of binary plane quartics.

No numerical approximation: coefficients and projective symmetries are over F2,
point tests over F4, and geometric smoothness is decided by Groebner bases.
Requires Python 3 and SymPy (tested 1.14.0).
"""
import collections
import csv
import itertools
from pathlib import Path
from sympy import symbols, groebner

MONOMIALS = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
INDEX = {m:i for i,m in enumerate(MONOMIALS)}
OUT = Path(__file__).resolve().parent

# GF(4) = F2[u]/(u^2+u+1); bit 0=constant, bit 1=u.
def multiply4(a,b):
    t = ((a&1)*(b&1)) ^ (((a&1)*((b>>1)&1) ^ ((a>>1)&1)*(b&1)) << 1) ^ (((a>>1)&1)*((b>>1)&1) << 2)
    if t&4: t ^= 7
    return t

def power4(a,n):
    r=1
    for _ in range(n):r=multiply4(r,a)
    return r

def all_points4():
    pts=set()
    for p in itertools.product(range(4),repeat=3):
        if p == (0,0,0): continue
        nonzero=next(v for v in p if v)
        inv=power4(nonzero,2)
        pts.add(tuple(multiply4(inv,v) for v in p))
    assert len(pts)==21
    return sorted(pts)

POINTS=all_points4()
LINES=[]
for line in itertools.product((0,1),repeat=3):
    if not any(line):continue
    subset=tuple(j for j,p in enumerate(POINTS)
                 if multiply4(line[0],p[0]) ^ multiply4(line[1],p[1]) ^ multiply4(line[2],p[2]) == 0)
    assert len(subset)==5
    LINES.append((line,subset))
assert len(LINES)==7
VALUES=[]
for p in POINTS:
    VALUES.append([multiply4(multiply4(power4(p[0],a),power4(p[1],b)),power4(p[2],c))
                   for a,b,c in MONOMIALS])

def poly_value(coeff,point_index):
    v=0
    while coeff:
        lb=coeff & -coeff
        v ^= VALUES[point_index][lb.bit_length()-1]
        coeff ^= lb
    return v

def inert_lines(coeff):
    return sum(all(poly_value(coeff,j)!=0 for j in subset) for _,subset in LINES)

def polymul(p,q):
    ans={}
    for x in p:
        for y in q:
            e=tuple(xi+yi for xi,yi in zip(x,y))
            ans[e]=1-ans.get(e,0)
    return {e:1 for e,v in ans.items() if v}

def image_table(matrix):
    basis=[{tuple(int(i==j) for i in range(3)):1} for j in range(3)]
    forms=[{e:1 for i,b in enumerate(row) if b for e in basis[i]} for row in matrix]
    powers=[]
    for f in forms:
        arr=[{(0,0,0):1}]
        for _ in range(4):arr.append(polymul(arr[-1],f))
        powers.append(arr)
    out=[]
    for a,b,c in MONOMIALS:
        terms=polymul(polymul(powers[0][a],powers[1][b]),powers[2][c])
        out.append(sum(1<<INDEX[m] for m in terms))
    return out

GENERATORS=[
  ((0,1,0),(0,0,1),(1,0,0)),
  ((0,1,0),(1,0,0),(0,0,1)),
  ((1,1,0),(0,1,0),(0,0,1)),
]
MAPS=[image_table(g) for g in GENERATORS]

def transform(coeff,table):
    out=0
    while coeff:
        lb=coeff & -coeff
        out ^= table[lb.bit_length()-1]
        coeff ^= lb
    return out

X,Y,Z=symbols('X Y Z')
def is_geometrically_smooth(coeff):
    F=sum(X**a*Y**b*Z**c for i,(a,b,c) in enumerate(MONOMIALS) if (coeff>>i)&1)
    for t in (X,Y,Z):
        u,v=[w for w in (X,Y,Z) if w != t]
        p=F.subs(t,1)
        ideal=groebner([p,p.diff(u),p.diff(v)],u,v,modulus=2,order='lex')
        if not (len(ideal.polys)==1 and ideal.polys[0].is_one):
            return False
    return True

def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))%2 for j in range(3)) for i in range(3))

def group_order():
    identity=((1,0,0),(0,1,0),(0,0,1))
    todo=[identity];seen={identity}
    for a in todo:
        for g in GENERATORS:
            b=matmul(a,g)
            if b not in seen:seen.add(b);todo.append(b)
    return len(seen)

def run(write_certificate=True):
    assert group_order()==168, 'Generators must generate GL3(F2)'
    seen=bytearray(32768)
    hist=collections.Counter()
    rows=[]
    for coeff in range(1,32768):
        if seen[coeff]:continue
        seen[coeff]=1
        orbit=[coeff]
        for p in orbit:
            for table in MAPS:
                q=transform(p,table)
                if not seen[q]:seen[q]=1;orbit.append(q)
        k=inert_lines(coeff)
        assert all(inert_lines(p)==k for p in orbit)
        smooth=is_geometrically_smooth(coeff)
        rows.append((coeff,len(orbit),k,int(smooth)))
        if smooth:hist[k]+=len(orbit)
    assert len(rows)==279 and sum(a[1] for a in rows)==32767
    assert sum(s for _,s,_,smooth in rows if smooth)==10920
    expected={0:4666,1:3444,2:1722,3:504,4:420,5:84,6:56,7:24}
    assert dict(sorted(hist.items()))==expected, (hist,expected)
    if write_certificate:
        with (OUT/'orbit_certificate.csv').open('w',newline='',encoding='utf8') as f:
            w=csv.writer(f,lineterminator='\n')
            w.writerow(['coefficient_bitmask','orbit_size','inert_line_count','geometrically_smooth'])
            w.writerows(rows)
    print('coordinate_group_order=168')
    print('all_nonzero_quartic_equations=32767')
    print('projective_orbits=279')
    print('geometrically_smooth_orbits='+str(sum(s for _,_,_,s in rows)))
    print('geometrically_smooth_equations='+str(sum(hist.values())))
    print('irreducible_line_section_distribution='+str(dict(sorted(hist.items()))))
    print('equations_with_positive_inert_count='+str(sum(v for k,v in hist.items() if k)))
    print('sum_inert_lines_over_smooth_equations='+str(sum(k*v for k,v in hist.items())))
    print('all_tests_passed=true')

if __name__=='__main__':run()
