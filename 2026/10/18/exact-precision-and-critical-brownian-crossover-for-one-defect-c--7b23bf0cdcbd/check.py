"""Independent finite-dimensional tests of the stated cube-slab moment identities.
Uses exact rational vertex arithmetic and simplex moments; scipy only triangulates facets.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb, factorial
import numpy as np
from scipy.spatial import ConvexHull
import sympy as sp

def moment(d, p, a, b):
    # Integrates s^p times the Irwin-Hall density h_d(s) exactly over [a,b].
    a,b=Q(a),Q(b)
    a=max(a,Q(-d));b=min(b,Q(d))
    if b<=a:return Q(0)
    ans=Q(0)
    for k in range(d+1):
        c=d-2*k;left=max(a,Q(-c))
        if b<=left:continue
        piece=sum(Q(comb(p,j)*(-c)**(p-j),d+j)*((b+c)**(d+j)-(left+c)**(d+j)) for j in range(p+1))
        ans+=(-1)**k*comb(d,k)*piece
    return ans/Q(2**d*factorial(d-1))

def formula(d,t):
    t=min(Q(t),Q(d))
    F=2*moment(d,0,0,t)
    J=moment(d,2,0,t)
    K=moment(d,1,t,d)
    v=1-Q(4,d*F)*(J+t*K)
    S2=2*J/F
    c=(S2-d*v)/Q(d*(d-1))
    lam=v-c
    mu=S2/d
    cov=sp.Matrix(d,d,lambda i,j:lam*min(i+1,j+1)+c*(i+1)*(j+1))
    D=sp.eye(d)
    for i in range(1,d):D[i,i-1]=-1
    prec=(D.T*D)/lam-(c/(lam*mu))*sp.eye(d)[:,d-1]*sp.eye(d)[d-1,:]
    return F,cov,prec, v,c,lam,mu

def independent(d,t):
    # Polytope |-1<=z_i<=1|, |-t<=sum_i z_i<=t|, exact rational vertices.
    A=[];b=[]
    for i in range(d):
        v=[Q(0)]*d;v[i]=Q(1);A.append(v);b.append(Q(1))
        v=[Q(0)]*d;v[i]=Q(-1);A.append(v);b.append(Q(1))
    A.extend([[Q(1)]*d,[Q(-1)]*d]);b.extend([Q(t),Q(t)])
    verts=set()
    for inds in combinations(range(len(A)),d):
        X=sp.Matrix([[sp.Rational(z.numerator,z.denominator) for z in A[i]] for i in inds])
        if X.det()==0:continue
        Y=sp.Matrix([sp.Rational(b[i].numerator,b[i].denominator) for i in inds]);sol=X.inv()*Y
        v=tuple(Q(int(z.p),int(z.q)) for z in sol)
        if all(sum(a[j]*v[j] for j in range(d))<=h for a,h in zip(A,b)):
            verts.add(v)
    vertices=sorted(verts)
    hull=ConvexHull(np.array(vertices,dtype=float),qhull_options='Qx')
    volume=Q(0);second=sp.zeros(d)
    for inds in hull.simplices:
        vecs=[vertices[int(i)] for i in inds]
        mat=sp.Matrix([[sp.Rational(v[i].numerator,v[i].denominator) for v in vecs] for i in range(d)])
        det=abs(int(mat.det().p))/int(mat.det().q) if False else abs(mat.det())
        vol=Q(int(det.p),int(det.q)*factorial(d))
        vmat=mat
        covpiece=(vmat*vmat.T+(vmat*sp.ones(d,1))*(vmat*sp.ones(d,1)).T)/Q((d+1)*(d+2))
        second+=vol*covpiece
        volume+=vol
    return volume,sp.simplify(second/sp.Rational(volume.numerator,volume.denominator)),len(vertices)

if __name__=='__main__':
    cases=0
    for d in (2,3,4):
      for t in (Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(4)):
        f,c,p,v,cross,lam,mu=formula(d,t)
        assert c*p==sp.eye(d), ('inv',d,t)
        vol,ic,nv=independent(d,t)
        assert vol==2**d*f,('volume',d,t,vol,2**d*f)
        L=sp.Matrix(d,d,lambda i,j:1 if j<=i else 0)
        assert L*ic*L.T==c,('cov',d,t,L*ic*L.T,c)
        assert cross<0 if t<d else cross==0,('cross sign',d,t,cross)
        cases+=1
        print('pass',d,t,'vertices',nv,'volume',str(vol),'cross',cross)
    print('EXACT_INDEPENDENT_SIMPLEX_CASES_PASSED',cases)
