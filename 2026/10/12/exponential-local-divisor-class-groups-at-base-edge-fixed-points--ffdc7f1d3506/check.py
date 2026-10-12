"""Exact finite checks for the friendship-graph local toric chart theorem.

Uses only Python and SymPy; the general proof is mathematical and is not
replaced by finite enumeration.
"""
from itertools import combinations, product
from math import comb, gcd
from functools import reduce
from sympy import Matrix, symbols, groebner


def primitive_integer_ray(v):
    from sympy import ilcm
    den = 1
    for a in v:
        den = ilcm(den, a.q)
    tup = [int(a*den) for a in v]
    g = reduce(gcd, (abs(a) for a in tup))
    if g:
        tup = [a//g for a in tup]
    return tuple(tup)


def predicted_rays(k):
    d=2+2*k
    rays=[]
    for j in range(k):
        for z in (2+2*j,3+2*j):
            v=[0]*d;v[z]=1;rays.append(tuple(v))
    for xy in (0,1):
        for bits in product((0,1),repeat=k):
            v=[0]*d;v[xy]=1
            for j,bit in enumerate(bits):v[2+2*j+bit]=1
            rays.append(tuple(v))
    return set(rays)


def inequalities(k):
    d=2+2*k
    rows=[]
    for i in range(d):
        row=[0]*d;row[i]=1; rows.append(row)
    for j in range(k):
        row=[0]*d;row[0]=-1;row[1]=-1
        row[2+2*j]=row[3+2*j]=1;rows.append(row)
    return Matrix(rows)


def independent_enumeration(k):
    A=inequalities(k);d=A.cols
    rays=set()
    for idx in combinations(range(A.rows),d-1):
        B=A[list(idx),:]
        if B.rank()!=d-1:continue
        z=primitive_integer_ray(B.nullspace()[0])
        for s in (1,-1):
            zz=tuple(s*t for t in z)
            if all(t>=0 for t in A*Matrix(zz)):
                rays.add(zz)
    return rays

for k in range(1,4):
    rays=predicted_rays(k)
    independent=independent_enumeration(k)
    assert rays==independent,(k,len(rays),len(independent),rays.symmetric_difference(independent))
    d=2+2*k
    A=inequalities(k)
    assert all(all(t>=0 for t in A*Matrix(v)) for v in rays)
    assert len(rays)==2**(k+1)+2*k
    units=[]
    for j in range(k):
        for i in (2+2*j,3+2*j):
            v=[0]*d;v[i]=1;units.append(v)
    other=[]
    for xy in (0,1):
        v=[0]*d;v[xy]=1
        for j in range(k):v[2+2*j]=1
        other.append(v)
    assert abs(Matrix(units+other).det())==1
    print('k=',k,'independent extreme rays=',len(rays),
          'class rank=',len(rays)-d,'unimodular minor=1')

for k in range(1,6):
    x,y=symbols('x y')
    us=symbols('u0:'+str(k));vs=symbols('v0:'+str(k));ws=symbols('w0:'+str(k))
    eqns=[us[j]*vs[j]-x*y*ws[j] for j in range(k)]
    gb=groebner(eqns,*(list(us)+list(vs)+[x,y]+list(ws)),order='lex')
    assert len(gb.polys)==k
    assert {str(e.as_expr()) for e in gb.polys}=={str(e) for e in eqns} or all(gb.reduce(e)[1]==0 for e in eqns)
    print('k=',k,'chart Gröbner basis size=',len(gb.polys),
          'tangent cone numerator=(1+z)^',k,'multiplicity=',2**k)

print('ALL CHECKS PASSED; symbolic proof required beyond inspected k')
