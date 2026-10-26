"""Exact cyclic-matrix identity checks and numerical spectral spot checks."""
import math
from fractions import Fraction
import numpy as np
checks=0
for d in [2,4,6,8,10,12,14,16,18,20,24,30,40,50]:
 P=np.zeros((d,d),dtype=int)
 for i in range(d):P[i,(i+1)%d]=1
 Q=np.diag([(-1)**i for i in range(d)])
 assert np.array_equal(P@Q,-Q@P);checks+=1
 B=(np.eye(d,dtype=int)+P)@Q@P/2
 assert np.array_equal(4*B@B,np.linalg.matrix_power(P,4)-np.linalg.matrix_power(P,2)); checks+=1
 eig=np.linalg.eigvals(B)
 maxreal=max(eig.real)
 prediction=(d not in (2,6))
 assert (maxreal>0.5+1e-8)==prediction,(d,maxreal);checks+=1
 assert max(abs(eig))<=1/math.sqrt(2)+1e-8;checks+=1
 # eigenvalue squared formula, exact with complex unit-circle modes
 predicted=[]
 for j in range(d//2):
  z=np.exp(2j*math.pi*j/d)
  root=np.sqrt((z**4-z**2)/4)
  predicted.extend([root,-root])
 assert len(predicted)==d
 assert max(min(abs(x-y) for y in predicted) for x in eig)<1e-6;checks+=1
 print('d',d,'max_Re',round(float(maxreal),8),'regime', 'superdiffusive' if prediction else 'Gaussian')
# Noncommutativity of sampling and sign matrix for d=4, 6
for d in (4,6):
 P=np.zeros((d,d),dtype=int)
 for i in range(d):P[i,(i+1)%d]=1
 Q=np.diag([(-1)**i for i in range(d)])
 assert not np.array_equal((np.eye(d,dtype=int)+P)@Q,Q@(np.eye(d,dtype=int)+P)); checks+=1
# Critical small d6 upper bound exact: sqrt(3)/8 < 1/4 -> sqrt(3)<2.
assert 3<4;checks+=1
# d>=8 sampling nearest theta to pi/2 gives |sin theta|>=cos(pi/8),
# sin(3theta)<=-sin(pi/8): cos(pi/8)*(1+sin(pi/8))>1.
assert math.cos(math.pi/8)*(1+math.sin(math.pi/8))>1;checks+=1
print('PASSED', checks, 'checks')
