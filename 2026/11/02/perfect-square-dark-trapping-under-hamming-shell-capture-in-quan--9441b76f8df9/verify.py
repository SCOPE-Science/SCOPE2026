"""Numerical/exact checks for coherent absorption from a Hamming-shell monitor.

Public science artifact: independent finite-dimensional spectral and semigroup checks.
Dependencies: Python 3, numpy, scipy.
"""
import math
import numpy as np
from scipy.linalg import expm


def kraw(d, radius, degree):
    return sum((-1)**j * math.comb(degree, j) * math.comb(d-degree, radius-j)
               for j in range(max(0, radius-(d-degree)), min(radius, degree)+1))


def predicted(d, radius):
    return sum(math.comb(d, j) for j in range(d+1) if kraw(d, radius, j)==0)/2**d


def radial(d):
    A=np.zeros((d+1,d+1))
    for j in range(d):
        A[j,j+1]=A[j+1,j]=math.sqrt((j+1)*(d-j))
    return A

count=0
for d in range(2,301):
    p=predicted(d,2)
    s=math.isqrt(d)
    target= (2*math.comb(d,(d+s)//2)/2**d if s*s==d else 0.)
    assert abs(p-target)<3e-14,(d,p,target)
    assert not any(kraw(d,1,k)==0 and kraw(d,2,k)==0 for k in range(d+1))
    count+=2

for d in range(2,31):
    J=radial(d)
    w,V=np.linalg.eigh(J)
    np.testing.assert_allclose(np.sort(w),np.arange(-d,d+1,2),atol=1e-11)
    # exact overlaps at every shell against independent symmetric eigensolver
    for radius in range(d+1):
        spectral=sum(V[0,k]**2 for k in range(d+1) if abs(V[radius,k])<3e-12)
        assert abs(spectral-predicted(d,radius))<3e-10,(d,radius,spectral,predicted(d,radius))
        count+=1

# Compare full 2^d-vertex evolution with d+1-site radial walk, independently constructed.
for d in range(2,8):
    n=2**d
    Afull=np.zeros((n,n),dtype=float)
    for v in range(n):
        for b in range(d): Afull[v,v^(1<<b)]=1
    for gamma in (.2,1.4):
        Gfull=-1j*Afull-np.diag([gamma if v.bit_count()==2 else 0 for v in range(n)])
        Gr=-1j*radial(d)-np.diag([gamma if j==2 else 0 for j in range(d+1)])
        for t in (0.17,0.9,2.3):
            u=np.zeros(n);u[0]=1
            v=np.zeros(d+1);v[0]=1
            f=expm(t*Gfull)@u
            r=expm(t*Gr)@v
            norms=[math.sqrt(sum(abs(f[x])**2 for x in range(n) if x.bit_count()==j)) for j in range(d+1)]
            np.testing.assert_allclose(norms,np.abs(r),atol=3e-10,rtol=3e-10)
            count+=1

for d,target in [(4,.5),(9,21/64),(16,1001/4096)]:
    assert abs(predicted(d,2)-target)<1e-15
    count+=1

print('PASS diagnostic groups:',count)
print('first square-dimension shell-two survival fractions:')
for d in (4,9,16,25,36,49,64,81,100):
    print(d, f'{predicted(d,2):.12g}')
print('limits: arbitrary-dimensional theorem relies on exact proof, not finite tests')
