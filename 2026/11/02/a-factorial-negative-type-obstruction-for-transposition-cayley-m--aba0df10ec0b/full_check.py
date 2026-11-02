"""Independent direct permutation distance diagonalization check, S6."""
import itertools,numpy as np
from scipy.linalg import eigh
from math import factorial
import check as ck
perms=np.array(list(itertools.permutations(range(6))),dtype=np.int8)
N=len(perms)
# Cayley distance n-cycles(pi^{-1}tau) equals rank of I-P of relative permutation;
# cycles computed independently via pairwise cyclic traversal.
D=np.zeros((N,N),dtype=np.uint8)
for a in range(N):
    inv=np.argsort(perms[a]).tolist()
    for b in range(a+1,N):
        q=[int(perms[b][inv[i]]) for i in range(6)]
        seen=0;cycles=0
        for j in range(6):
            if seen>>j&1:continue
            cycles+=1;x=j
            while not (seen>>x&1):
                seen|=1<<x;x=q[x]
        D[a,b]=D[b,a]=6-cycles
assert np.all(D.diagonal()==0)
counts=np.bincount(D[0],minlength=6)
assert list(counts)==[1,15,85,225,274,120],counts
beta=.1541377737657968
M=D.astype('float64')**beta
# Euclidean centered Gram eigenvalues, or centered D spectral; 
# eigvalsh uses no J directly by subtracting row/col mean.
X=M-M.mean(axis=0)[None,:]-M.mean(axis=1)[:,None]+M.mean()
vals=eigh(X,eigvals_only=True,check_finite=False)
assert np.sum(np.abs(vals)<1e-7)==101,(np.sum(np.abs(vals)<1e-7),vals[-1])
assert vals.max()<2e-7,vals[-1]
assert vals[101]<-1e-4
print('FULL_720_VERTEX_DISTANCE_SPECTRUM_OK',len(perms),'vertices','distance counts',counts.tolist(),'zero eigenvectors',101)
