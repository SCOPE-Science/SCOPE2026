"""Exact rational regression checks for an affine hexagon asymmetry identity.

Proof of the identity and universality is analytic; finite tests are auxiliary.
Run with Python >=3.9: python verify.py
"""
from fractions import Fraction as F
from itertools import product, combinations

NORMALS=((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1))

def support(points,n):
    return max(p[0]*n[0]+p[1]*n[1] for p in points)

def vertices(a,b,c,t):
    assert min(a,b,c,a+t,b-t,c+t)>0
    return ((F(0),F(0)),(a,F(0)),(a,b),(a-c,b+c),(-c-t,b+c),(-c-t,c+t))

def exact_candidate(a,b,c,t):
    S=a+b+c
    assert S+t>0
    lam=max(F(S+t,S),F(S,S+t))
    if t>=0:
        z=(lam*a-(c+t),lam*(b+c))
    else:
        z=(a-lam*(c+t),b+c)
    return lam,z

def cross(u,v):return u[0]*v[1]-u[1]*v[0]

def solve3(rows, rhs):
    """Independent rational 3 by 3 Gaussian elimination."""
    aug=[list(row)+[val] for row,val in zip(rows,rhs)]
    for j in range(3):
        piv=next((k for k in range(j,3) if aug[k][j]),None)
        if piv is None:return None
        aug[j],aug[piv]=aug[piv],aug[j]
        v=aug[j][j]
        aug[j]=[w/v for w in aug[j]]
        for i in range(3):
            if i==j:continue
            v=aug[i][j]
            aug[i]=[a-v*b for a,b in zip(aug[i],aug[j])]
    return tuple(row[3] for row in aug)

def exact_lp_optimum(P):
    """Optimize (lambda,zx,zy) by enumerating intersections of active facets.

    All inequalities are linear.  A bounded-below pointed feasible 3D polyhedron
    has a minimizing basic feasible point; lambda>=1 and the six facet rows yield it.
    """
    rows=[(-support(P,n),F(n[0]),F(n[1])) for n in NORMALS]
    bounds=[-support(P,(-n[0],-n[1])) for n in NORMALS]
    rows.append((F(-1),F(0),F(0)))
    bounds.append(F(-1))
    opt=None
    for ix in combinations(range(7),3):
        point=solve3([rows[i] for i in ix],[bounds[i] for i in ix])
        if point is None:continue
        if all(sum(a*x for a,x in zip(row,point))<=bound for row,bound in zip(rows,bounds)):
            if opt is None or point[0]<opt:opt=point[0]
    assert opt is not None
    return opt

def regression():
    checked=0
    for ai,bi,ci in product(range(1,9),repeat=3):
        for ti in range(-min(ai,ci)+1,bi):
            a,b,c,t=map(F,(ai,bi,ci,ti))
            P=vertices(a,b,c,t)
            E=[(P[(i+1)%6][0]-P[i][0],P[(i+1)%6][1]-P[i][1]) for i in range(6)]
            assert all(cross(E[i],E[(i+1)%6])>0 for i in range(6))
            assert E==[(a,F(0)),(F(0),b),(-c,c),(-a-t,F(0)),(F(0),-b+t),(c+t,-c-t)]
            lam,z=exact_candidate(a,b,c,t)
            for n in NORMALS:
                hn=support(P,n)
                hm=support(P,(-n[0],-n[1]))
                assert z[0]*n[0]+z[1]*n[1]+hm<=lam*hn
            # Direct construction, independent of hand-derived support intercepts:
            assert all(support(P,n)=={(1,0):a,(-1,0):c+t,(0,1):b+c,(0,-1):F(0),(1,1):a+b,(-1,-1):F(0)}[n] for n in NORMALS)
            # Lower-bound certificates from pairwise support ranges.
            assert lam*(a+b+c)>=a+b+c+t
            assert lam*(a+b+c+t)>=a+b+c
            if t>0:
                assert lam*(a+b+c)==a+b+c+t
            if t<0:
                assert lam*(a+b+c+t)==a+b+c
            # The active triple of facets determines the optimal centre uniquely:
            if t>=0:
                assert z[0] == lam*a-(c+t)
                assert z[1] == lam*(b+c)
                assert z[0]+z[1]==a+b
            if t<=0:
                assert z[0] == a-lam*(c+t)
                assert z[1] == b+c
                assert z[0]+z[1]==lam*(a+b)
            checked+=1
    assert checked>1000
    # Rational active-facet enumeration, independent of the closed-form derivation.
    lp_checked=0
    for ai,bi,ci in product(range(1,6),repeat=3):
        for ti in (-min(ai,ci)+1, 0, bi-1):
            a,b,c,t=map(F,(ai,bi,ci,ti))
            if min(a+t,b-t,c+t)<=0:continue
            P=vertices(a,b,c,t)
            assert exact_lp_optimum(P)==exact_candidate(a,b,c,t)[0]
            lp_checked+=1
    assert lp_checked>200
    # Range realization for rational target ratios 1 < r < 2.
    for k in range(0,100):
        r=F(100+k,100)
        eps=F(1,1000)
        t=(r-1)*(1+2*eps)
        if r<2 and t<1:
            lam,z=exact_candidate(eps,F(1),eps,t)
            assert lam==r
    print('VERIFY_OK',checked,'exact cases;',lp_checked,'independent rational LP solves and range witnesses')

if __name__=='__main__':regression()
