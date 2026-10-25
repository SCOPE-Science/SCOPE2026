"""Independent finite-dimensional checks for Euclidean radii of highest boundary-simplex Laplacian polytopes."""
import math, numpy as np
from scipy.linalg import null_space
from scipy.spatial import ConvexHull
from scipy.optimize import linprog, minimize

def laplacian_boundary(n):
    # boundary facets of simplex on n vertices; d=n-2
    facets=[tuple(j for j in range(n) if j!=i) for i in range(n)]
    faces=sorted(set(tuple(v for v in facet if v!=w) for facet in facets for w in facet))
    B=np.zeros((len(faces),n))
    for j,facet in enumerate(facets):
        for i in range(len(facet)):
            sub=facet[:i]+facet[i+1:]
            B[faces.index(sub),j]=(-1)**i
    return B.T@B

def one(n):
    s=np.array([(-1)**i for i in range(n)],float)
    if n%2==0:
        E=null_space(np.vstack([s,np.ones(n)]))
    else:
        E=null_space(s[None,:])
    L=laplacian_boundary(n)
    expect=n*np.eye(n)-np.outer(s,s)
    assert np.allclose(L,expect)
    V=L.T
    center_of_affine=np.ones(n) if n%2==0 else np.zeros(n)
    pts=(V-center_of_affine)@E
    hull=ConvexHull(pts)
    normals=hull.equations[:,:-1]
    offsets=hull.equations[:,-1]
    norm=np.linalg.norm(normals,axis=1)
    normals=normals/norm[:,None]; offsets=offsets/norm
    dim=E.shape[1]
    obj=np.r_[np.zeros(dim),-1]
    Am=np.c_[normals,np.ones(len(normals))]
    sol=linprog(obj,A_ub=Am,b_ub=-offsets,bounds=[(None,None)]*dim+[(0,None)],method='highs')
    assert sol.success,sol.message
    rin=sol.x[-1]
    if n%2==0:
        m=n//2
        rtrue=n/math.sqrt(2*m*(m-1))
        ctrue=np.ones(n)
        Rtrue=math.sqrt(n*(n-2))
        contact=n
    else:
        p=(n+1)//2; q=(n-1)//2
        rtrue=n/(p*math.sqrt(n-1)+q*math.sqrt(n+3))
        ctrue=np.where(s>0,q/p,1.)
        Rtrue=n*math.sqrt((p-1)/p)
        contact=p
    # Verify the proposed minimum enclosing ball directly.
    dist=np.linalg.norm(V-ctrue,axis=1)
    assert abs(max(dist)-Rtrue)<1e-8
    assert sum(np.isclose(dist,Rtrue,atol=1e-7))==contact
    assert abs(rin-rtrue)<5e-7,(n,rin,rtrue)
    # Direct check of all polytope facet distances at incenter.
    if n%2:
        grad_norms=np.where(s>0,np.sqrt(n-1)/n,np.sqrt(n+3)/n)
        lam=grad_norms/grad_norms.sum()
        c_in=lam@V
    else:
        c_in=ctrue
    c_in_coords=(c_in-center_of_affine)@E
    facet_dists=-offsets-normals@c_in_coords
    assert abs(min(facet_dists)-rtrue)<1e-8,(n,min(facet_dists),rtrue)
    assert np.all(facet_dists>=rtrue-1e-8)
    print('n=%d dim=%d num_facets=%d inradius=%.12g circ_radius=%.12g circ_contacts=%d'%(n,dim,len(normals),rin,Rtrue,contact))

for n in range(3,11): one(n)
print('all independent numerical checks passed')
