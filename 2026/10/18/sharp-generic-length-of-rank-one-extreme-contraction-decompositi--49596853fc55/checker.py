"""Exact finite examples and supporting identities for sign-rank-one convex decompositions.
The proof for arbitrary dimensions and generic parameters is in RESULT.md.
"""
from itertools import product, combinations
from fractions import Fraction
from math import prod
from sympy import Matrix

def configurations(m,n,r,c):
    for x in product((-1,1),repeat=m-r):
        rows=(1,)*r+x
        for y in product((-1,1),repeat=n-c):
            cols=(1,)*c+y
            yield tuple(rows[i]*cols[j] for i in range(m) for j in range(n)),x,y

def check(m,n,r,c):
    vv=list(configurations(m,n,r,c))
    vertices=[v[0] for v in vv]
    dim=(m-r+1)*(n-c+1)-1
    rank=Matrix([[1]+list(v) for v in vertices]).rank()-1
    assert rank==dim,(m,n,r,c,rank,dim)
    a=[Fraction(1)]*r+[Fraction(1,i+3) for i in range(m-r)]
    b=[Fraction(1)]*c+[Fraction(1,j+4) for j in range(n-c)]
    weights=[]
    for _,x,y in vv:
        factors=[(1+a[r+i]*z)/2 for i,z in enumerate(x)]+[(1+b[c+j]*z)/2 for j,z in enumerate(y)]
        weights.append(prod(factors))
    assert sum(weights)==1
    assert all(w>0 for w in weights)
    avg=tuple(sum(w*v[idx] for w,v in zip(weights,vertices)) for idx in range(m*n))
    expected=tuple(a[i]*b[j] for i in range(m) for j in range(n))
    assert avg==expected
    return len(vertices),dim

def four_term_example():
    # Matrix with rows (1,1/5), (1/3,1/15).
    a=Fraction(1,3);b=Fraction(1,5)
    verts=[]; w=[]
    for x,y in product((-1,1),repeat=2):
        verts.append((1,y,x,x*y))
        w.append((1+x*a)*(1+y*b)/4)
    assert all(v>0 for v in w)
    assert Matrix(verts).det()!=0
    assert tuple(sum(wt*v[i] for wt,v in zip(w,verts)) for i in range(4))==(1,b,a,a*b)
    print('four-vertex rational witness',[(str(z),vec) for z,vec in zip(w,verts)])

def small_generic_2x3():
    # 2x3: a=(1,1/3), b=(1,1/5,1/7).
    # Exact affine exclusion for support <=5 (all 8 vertices).
    vertices=[v for v,_,_ in configurations(2,3,1,1)]
    t=Matrix([1,Fraction(1,5),Fraction(1,7),Fraction(1,3),Fraction(1,15),Fraction(1,21)])
    for subset in combinations(vertices,5):
        cols=[Matrix(v) for v in subset]
        assert Matrix.hstack(*cols).rank()<Matrix.hstack(*cols,t).rank(), ('unexpected affine containment',subset)
    print('2x3 rational witness excludes all 5-term decompositions')

if __name__=='__main__':
    count=0
    for m in range(1,5):
      for n in range(1,5):
       for r in range(1,m+1):
        for c in range(1,n+1):
         number,dim=check(m,n,r,c)
         count+=1
    four_term_example(); small_generic_2x3()
    print('PASS',count,'exact face-rank / Bernoulli identities and separate witnesses')
