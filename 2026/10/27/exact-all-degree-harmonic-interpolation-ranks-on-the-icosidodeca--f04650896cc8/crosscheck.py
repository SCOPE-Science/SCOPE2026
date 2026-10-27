"""Independent numerical spherical-harmonic evaluation comparison (not a proof)."""
import numpy as np
from scipy.special import sph_harm_y

phi=(1+np.sqrt(5.0))/2.0
V=[]
for a in (-1,1):
    for b in (-1,1):
        V.extend([(0,a,b*phi),(a,b*phi,0),(b*phi,0,a)])
V=np.array(V,float)
E=[(i,j) for i in range(12) for j in range(i+1,12)
   if abs(np.sum((V[i]-V[j])**2)-4.0)<1e-12]
assert len(E)==30
X=np.array([(V[i]+V[j])/(2*phi) for i,j in E])
az=np.arctan2(X[:,1],X[:,0])
colat=np.arccos(np.clip(X[:,2],-1,1))
expected=[1,3,5,7,9,11,10,15,14,15,15,15,15,15,14,15,15]
for ell in range(17):
    values=np.array([[sph_harm_y(ell,m,colat[i],az[i]) for m in range(-ell,ell+1)]
                     for i in range(30)])
    rank=int(np.sum(np.linalg.svd(values,compute_uv=False)>1e-7))
    assert rank==expected[ell], (ell,rank,expected[ell])
print('PASS: direct complex spherical-harmonic evaluation ranks 0..16 agree with exact theorem')
