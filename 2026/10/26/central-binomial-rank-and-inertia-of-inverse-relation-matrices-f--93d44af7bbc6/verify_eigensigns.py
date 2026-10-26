"""Optional numerical corroboration of inverse-adjacency inertia up to n=5.
Requires NumPy; the general mathematical proof does not require it.
"""
from itertools import combinations
from math import comb
import numpy as np

def partitions(n, r):
    for cuts in combinations(range(1,n),r-1):
        k=(0,)+cuts+(n,)
        yield tuple(tuple(range(k[i],k[i+1])) for i in range(r))

def verify():
    for n in range(1,6):
        for r in range(1,n+1):
            blocks=list(partitions(n,r))
            images=list(combinations(range(n),r))
            M=np.array([[int(all(len(set(B)&set(I))==1 for B in P))
                         for I in images] for P in blocks],dtype=float)
            a,b=M.shape
            A=np.array([[M[k,j]*M[l,i] for l in range(a) for j in range(b)]
                        for k in range(a) for i in range(b)],dtype=float)
            eig=np.linalg.eigvalsh(A)
            eps=1e-8
            actual=(int(np.count_nonzero(eig>eps)),
                    int(np.count_nonzero(eig< -eps)),
                    int(np.count_nonzero(abs(eig)<=eps)))
            expected=(a*(a+1)//2,a*(a-1)//2,a*(b-a))
            assert actual==expected,(n,r,actual,expected)
        print('n=',n,'EIGENSIGNS_OK')
    print('SPECTRAL_VERIFY_OK')
if __name__=='__main__':verify()
