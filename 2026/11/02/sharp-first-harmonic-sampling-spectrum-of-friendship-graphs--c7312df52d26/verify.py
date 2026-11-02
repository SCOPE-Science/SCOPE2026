"""Independent exact pair-probability and numerical eigenspectrum check.
Use python windmill_frame_check.py (Python 3, NumPy)."""
from itertools import product, permutations
from fractions import Fraction
import numpy as np

def enumerate_coloring_counts(q,m):
    n=2*m+1
    z=np.zeros((n,n,q),dtype=np.int64)
    count=0
    for h in range(q):
        options=[(u,v) for u in range(q) for v in range(q) if h!=u and h!=v and u!=v]
        for petals in product(options,repeat=m):
            colors=[h]+[x for pair in petals for x in pair]
            count+=1
            for i in range(n):
                for j in range(n):
                    z[i,j,(colors[i]-colors[j])%q]+=1
    return z,count

def formula(q,m):
    r=1/(q-1)
    n=2*m+1
    b=np.eye(n,dtype=float)
    for v in range(1,n): b[0,v]=b[v,0]=-r
    for i in range(m): b[1+2*i,2+2*i]=b[2+2*i,1+2*i]=-r
    for i in range(m):
      for j in range(m):
        if i!=j:
          for a in (0,1):
            for c in (0,1):b[1+2*i+a,1+2*j+c]=r*r
    A=1+r; S=1-r-2*r*r
    L=1-r+2*(m-1)*r*r
    mat=np.array([[1.,-np.sqrt(2*m)*r],[-np.sqrt(2*m)*r,L]])
    pm=np.linalg.eigvalsh(mat)
    want=sorted([A]*m+[S]*(m-1)+list(pm))
    return b,np.array(want),float(pm[1]),float(pm[0])

def main():
  cases=0
  for q,m in [(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,2),(5,3),(6,2)]:
    z,ncolor=enumerate_coloring_counts(q,m)
    b,expected,up,down=formula(q,m)
    assert ncolor==q*((q-1)*(q-2))**m
    for k in range(1,q):
      roots=np.exp(2j*np.pi*k*np.arange(q)/q)
      actual=np.einsum('ijk,k->ij',z,roots)/ncolor
      assert np.max(abs(actual-b))<3e-12,(q,m,k)
      assert np.max(abs(np.sort(np.linalg.eigvalsh(actual))-expected))<3e-12,(q,m,k)
      cases+=1
    # all different frequency characters orthogonal: use direct invariance
    assert np.allclose(b,b.T)
    assert down > -2e-12
    assert up > 1+1/(q-1) - 2e-12
    if q==3:assert np.sum(expected<1e-11)==m
    else:assert np.min(expected)>0
  print(f'CHECK_OK {cases} frequency blocks, 9 independent full-coloring enumerations')
if __name__=='__main__':main()
