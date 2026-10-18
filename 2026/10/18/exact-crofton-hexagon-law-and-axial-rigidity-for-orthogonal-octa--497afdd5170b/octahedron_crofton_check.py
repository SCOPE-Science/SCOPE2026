"""Independent checks for Crofton affine section counts of axis-aligned octahedra.
Run with Python 3 and numpy: python octahedron_crofton_check.py
"""
import math
import numpy as np

def predicted(a,b,c):
    L=[math.hypot(a,b),math.hypot(b,c),math.hypot(c,a)]
    angles=[math.atan2(a*b,c*L[0]), math.atan2(b*c,a*L[1]), math.atan2(c*a,b*L[2])]
    A=sum(x*y for x,y in zip(L,angles))
    S=sum(L)
    return math.pi*S/(2*A)-2.0

def run():
    rng=np.random.default_rng(20261017)
    for a,b,c in [(1.,1.,1.),(2.,1.,1.),(1.,2.,.5),(.2,3.,1.),(1.,1.,.02),(.1,.2,10.)]:
        verts=np.array([[a,0.,0.],[-a,0.,0.],[0.,b,0.],[0.,-b,0.],[0.,0.,c],[0.,0.,-c]])
        edges=[(i,j) for i in range(6) for j in range(i+1,6) if i//2!=j//2]
        normals=rng.normal(size=(200000,3));normals/=np.linalg.norm(normals,axis=1)[:,None]
        proj=normals@verts.T
        A=np.max(proj,axis=1)
        offsets=(rng.uniform(-1,1,size=len(A))*A)
        count=np.zeros(len(A),dtype=np.int8)
        for i,j in edges:
            count+=((proj[:,i]-offsets)*(proj[:,j]-offsets)<0).astype(np.int8)
        assert set(np.unique(count))=={4,6}
        # Uniform-normal conditional-offset estimator must be weighted by support A.
        observed=np.mean(A*(count==6))/np.mean(A)
        pred=predicted(a,b,c)
        print(f'{(a,b,c)}: formula={pred:.9f}, weighted_edges={observed:.9f}, discrepancy={abs(observed-pred):.5f}')
        assert abs(observed-pred)<0.012
    z=predicted(1,1,1)
    assert abs(z-(math.pi/math.acos(1/3)-2))<1e-12
    print('OCTAHEDRON_CROFTON_CHECK_OK')
if __name__=='__main__': run()
