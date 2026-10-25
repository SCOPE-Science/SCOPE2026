"""Supplementary Monte Carlo checks for exact joint vertex–facet margins."""
import numpy as np
from scipy.spatial import ConvexHull
from scipy.stats import kstest
from itertools import product

rng=np.random.default_rng(19371)
phi=(1+np.sqrt(5))/2
objects={
    'tetrahedron':np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float),
    'cube':np.array(list(product((-1,1),repeat=3)),dtype=float),
    'octahedron':np.vstack([np.eye(3),-np.eye(3)]),
    'icosahedron':np.array([(0,s,t*phi) for s in (-1,1) for t in (-1,1)]+[(s,t*phi,0) for s in (-1,1) for t in (-1,1)]+[(t*phi,0,s) for s in (-1,1) for t in (-1,1)],float)
}
# A dodecahedron is dual to the icosahedron.
h=ConvexHull(objects['icosahedron']);planes=h.equations.copy();objects['dodecahedron']=planes[:,:-1]/(-planes[:,-1,None]);

def unique_planes(h):
    p=h.equations;out=[]
    for v in p:
        v=np.r_[v[:3],v[3]] # unit outward normals, negative support offset
        if not any(np.linalg.norm(v-w)<1e-7 for w in out):out.append(v)
    return np.array(out)

def check(name,verts,N=80000):
    h=ConvexHull(verts);eq=unique_planes(h);ns=eq[:,:3];a=-eq[:,3]
    assert np.max(a)-np.min(a)<1e-7,(name,'not tangential')
    sim=h.simplices
    vols=np.abs(np.einsum('ij,ij->i',verts[sim[:,0]],np.cross(verts[sim[:,1]],verts[sim[:,2]])))/6
    q=rng.choice(len(vols),size=N,p=vols/vols.sum())
    weights=rng.dirichlet([1,1,1,1],size=N)
    x=(weights[:,1:,None]*verts[sim[q]]).sum(axis=1)
    dd=a[None,:]-x@ns.T
    sorted_d=np.partition(dd,1,axis=1)[:,:2];delta=np.abs(sorted_d[:,0]-sorted_d[:,1]);
    # Polytope facet center is projected normal direction a*n; the face incenter when regular.
    centers=a[:,None]*ns
    scores=a[None,:]-centers@ns.T
    lower=np.partition(scores,1,axis=1)[:,:2]
    vals=np.abs(lower[:,0]-lower[:,1]);gmax=vals.mean()
    assert np.max(vals)-np.min(vals)<1e-6,(name,'varying facet centers')
    z=delta/gmax
    dv=((x[:,None,:]-verts[None,:,:])**2).sum(axis=2)
    ds=np.partition(dv,1,axis=1)[:,:2]
    s2=np.min(np.sum((verts[:,None,:]-verts[None,:,:])**2,axis=2)[np.triu_indices(len(verts),1)])
    u=np.abs(ds[:,1]-ds[:,0])/s2
    assert u.max()<1.001
    jt=np.mean((u>0.2)&(z>0.15))
    corr=np.corrcoef(u,z)[0,1]
    print('Joint', name, 'meanU',round(u.mean(),6),'meanV',round(z.mean(),6),'correlation',round(corr,5),'target',-1/3,'joint survival',round(jt,6),'target',0.65**3,'max sum',round((u+z).max(),6))
    assert abs(corr+1/3)<0.016 and abs(jt-0.65**3)<0.01 and np.max(u+z)<1.0001
    dstat,pval=kstest(z,lambda t:1-(1-np.clip(t,0,1))**3)
    print(name,'v',len(verts),'facets',len(eq),'gmax',round(gmax,9),'sample mean',round(z.mean(),6),'target mean',1/4,'KS',round(dstat,6),'pvalue',round(pval,5),'max z',round(np.max(z),6))
    assert dstat<0.012
for name,verts in objects.items():check(name,verts)
