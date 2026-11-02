"""Independent geometric numerical sanity checks for local D2 laws."""
import numpy as np
from scipy.stats import qmc
from math import pi

def cdf_formula(a,b,c,r):
    area=2*(a*b+b*c+c*a)
    return (pi*area*r*r+(8*pi-16)/3*(a+b+c)*r**3+3*(1-pi)*r**4)/(area*area)

def sample_box(a,b,c,logn=21,seed=7):
    # Six faces sampled with area weights; both points sampled independently.
    v=qmc.Sobol(d=6,scramble=True,seed=seed).random_base2(logn)
    areas=np.array([b*c,b*c,a*c,a*c,a*b,a*b],float)
    cums=np.cumsum(areas/areas.sum())
    def points(u):
        inds=np.searchsorted(cums,u[:,0])
        X=np.empty((len(u),3),float)
        x=u[:,1];y=u[:,2]
        for j in range(6):
            ix=(inds==j)
            if j==0: X[ix]=np.column_stack((np.zeros(ix.sum()),b*x[ix],c*y[ix]))
            elif j==1: X[ix]=np.column_stack((np.full(ix.sum(),a),b*x[ix],c*y[ix]))
            elif j==2: X[ix]=np.column_stack((a*x[ix],np.zeros(ix.sum()),c*y[ix]))
            elif j==3: X[ix]=np.column_stack((a*x[ix],np.full(ix.sum(),b),c*y[ix]))
            elif j==4: X[ix]=np.column_stack((a*x[ix],b*y[ix],np.zeros(ix.sum())))
            else: X[ix]=np.column_stack((a*x[ix],b*y[ix],np.full(ix.sum(),c)))
        return X
    p=points(v[:,:3]);z=points(v[:,3:]); ds=np.sum((p-z)**2,axis=1)
    return ds

if __name__=='__main__':
    triples=[(1.,1.,1.),(1.,2.,3.),(11/7,9/7,22/7),(1.2,1.8,2.5)]
    rad=[0.3,0.6,0.85,1.0]
    for tri in triples:
        ds=sample_box(*tri,logn=21,seed=37)
        print('box',tri,'surface area',2*(tri[0]*tri[1]+tri[1]*tri[2]+tri[2]*tri[0]))
        for r in rad:
            if r>min(tri):continue
            observed=(ds<=r*r).mean(); expected=cdf_formula(*tri,r)
            print(f'r={r:.3f} observed={observed:.8f} exact={expected:.8f} diff={observed-expected:+.7f}')
            assert abs(observed-expected)<0.0018
    for r in np.linspace(0,1,11):
        assert abs(cdf_formula(1,2,3,float(r))-cdf_formula(11/7,9/7,22/7,float(r)))<1e-13
    assert sorted([1,2,3]) != sorted([11/7,9/7,22/7])
    print('verified 10-point exact local-collision identity')
