"""Independent small-field dense singular-value check (requires NumPy)."""
import cmath
from math import pi
import numpy as np


def check(p=5,d=1):
    q=p*p
    C={(x,y) for x in range(p) for y in range(p) if (x*x-d*y*y)%p==1}
    positions=[(x,y) for x in range(p) for y in range(p)]
    index={z:i for i,z in enumerate(positions)}
    omega=cmath.exp(2j*pi/p)
    matrix=np.zeros((q*q,q*q),dtype=complex)
    amb=[]
    idx=0
    for a in positions:
      for b in positions:
        v=np.zeros(q,dtype=complex)
        for x,y in C:
          z=((x+a[0])%p,(y+a[1])%p)
          v[index[z]]=omega**((b[0]*z[0]+b[1]*z[1])%p)
        matrix[idx,:]=np.kron(np.conjugate(v),v)/p
        idx+=1
    for h in positions:
      S=[z for z in C if ((z[0]-h[0])%p,(z[1]-h[1])%p) in C]
      for b in positions:
        amb.append(abs(sum(omega**((b[0]*z[0]+b[1]*z[1])%p) for z in S)))
    calculated=np.linalg.svd(matrix,compute_uv=False)
    target=np.array(sorted(amb,reverse=True))
    err=np.max(np.abs(calculated-target))
    rank=np.count_nonzero(calculated>1e-8)
    assert rank==p*p*(1+(p-1)**2//2)
    assert err<1e-11,(err,rank)
    print(f'PASS: dense SVD p={p} d={d}: rank={rank}, largest={calculated[0]:.12f}, '
          f'least_positive={calculated[rank-1]:.12f}, max_error={err:.2g}')


if __name__=='__main__': check()
