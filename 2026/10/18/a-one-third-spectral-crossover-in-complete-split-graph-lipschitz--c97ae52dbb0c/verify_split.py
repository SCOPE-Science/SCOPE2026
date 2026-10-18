"""Reproduce exact volume and covariance of complete split-graph Lipschitz dual balls.

Requires Python 3, numpy, scipy and sympy. Does not use the disintegration
proof: it enumerates all extreme Lipschitz potentials from active constraints,
triangulates polytope facets and integrates monomials on simplices exactly.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
import numpy as np
from scipy.spatial import ConvexHull
from sympy import Matrix


def moments(p, q):
    assert p >= 2 and q >= 1
    def integ(j):
        return sum((F((-1)**k * comb(q,k) * 2**(q-k), p-1+j+k)
                    for k in range(q+1)), F(0))
    i0, i1, i2 = (integ(j) for j in range(3))
    r2 = i2 / i0
    w2 = (4*i0-4*i1+i2)/i0
    n=p+q
    aa = F((p+1)*(p+2),12*p*(p-1))*r2
    bb = w2/12
    cc = F(q*(p-2),12*p*n)*r2+F(p,12*n)*w2
    return F(p*(p-1))*i0, aa, bb, cc


def independent_polytope(p,q):
    n=p+q; d=n-1
    edges=list(combinations(range(p),2)) + [(i,j) for i in range(p) for j in range(p,n)]
    rows=[]
    for u,v in edges:
        h=np.zeros(d,dtype=np.int64)
        if u: h[u-1]+=1
        if v: h[v-1]-=1
        rows.append(h)
    E=np.array(rows,dtype=np.int64)
    signs=np.vstack((E,-E))
    ones=np.ones(len(signs),dtype=np.int64)
    vertices=set()
    for indices in combinations(range(len(signs)), d):
        a=signs[list(indices)]
        if abs(np.linalg.det(a))<.5: continue
        x=np.linalg.solve(a,np.ones(d))
        if np.max(abs(x-np.rint(x)))>1e-7: raise AssertionError('Non-integral extreme point')
        v=np.rint(x).astype(np.int64)
        if np.array_equal(a@v,np.ones(d,dtype=np.int64)) and np.all(signs@v<=ones):
            vertices.add(tuple(map(int,v)))
    vs=np.array(sorted(vertices),dtype=np.int64)
    hull=ConvexHull(vs.astype(float))
    vol=F(0); m=[F(0) for _ in range(d)]; quad=[[F(0) for _ in range(d)] for _ in range(d)]
    for face in hull.simplices:
        V=vs[face]
        det=abs(int(Matrix(V.T.tolist()).det()))
        if not det: continue
        simplex_vol=F(det,factorial(d))
        vol+=simplex_vol
        s=V.sum(axis=0)
        for i in range(d):
            m[i]+=simplex_vol*F(int(s[i]),d+1)
            for j in range(d):
                x=int(s[i]*s[j]+sum(int(v[i]*v[j]) for v in V))
                quad[i][j]+=simplex_vol*F(x,(d+1)*(d+2))
    assert all(x==0 for x in m), 'Unexpected nonzero centroid'
    exx=[[x/vol for x in row] for row in quad]
    # Apply centering into the canonical zero-sum Euclidean hyperplane.
    B=[[F((1 if i==j+1 else 0),1)-F(1,n) for j in range(d)] for i in range(n)]
    cov=[[sum((B[i][a]*exx[a][b]*B[j][b] for a in range(d) for b in range(d)),F(0))
          for j in range(n)] for i in range(n)]
    return vol,cov,len(vs),len(hull.simplices)


def expected_cov(p,q,a,b,c):
    n=p+q
    w=[q]*p +[-p]*q
    P=[[F(int(i==j),1)-F(1,p) if i<p and j<p else F(0) for j in range(n)] for i in range(n)]
    Q=[[F(int(i==j),1)-F(1,q) if i>=p and j>=p else F(0) for j in range(n)] for i in range(n)]
    return [[a*P[i][j]+b*Q[i][j]+c*F(w[i]*w[j],p*q*n) for j in range(n)] for i in range(n)]


def run():
    cases=[(2,1),(3,1),(4,1),(2,2),(2,3),(3,2)]
    for p,q in cases:
        v,a,b,c=moments(p,q)
        real_v,real_cov,nverts,nsim=independent_polytope(p,q)
        assert v==real_v,(p,q,'volume',v,real_v)
        target=expected_cov(p,q,a,b,c)
        assert real_cov==target,(p,q,'covariance',real_cov,target)
        print('EXACT_POLYTOPE_PASS',p,q,'vertices',nverts,'simplices',nsim,'volume',v,'spectrum',a,b,c)
    # Exact rational moment identities, independent of any floating asymptotics.
    for p in range(2,19):
      for q in range(1,20):
        vol,a,b,c=moments(p,q)
        assert vol>0 and a>0 and b>0 and c>0
        if q==1:
            assert a==c, (p,q,a,c)  # Complete graph when q=1.
        if (p,q)==(2,3):
            assert a==c
    print('EXACT_MOMENT_CHECKS_PASS',17*19,'cases')

if __name__=='__main__':run()
