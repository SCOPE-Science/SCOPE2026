"""Master verification: re-checks every computed certificate of the emergent claim.
Run: python3 output/artifacts/verify_all.py (needs pulp, scipy, numpy)."""
import itertools, json
from math import comb
import numpy as np
try:
    import pulp
    HAVE_PULP=True
except ImportError:
    HAVE_PULP=False

q,n,d=3,3,2
verts=list(itertools.product(range(q),repeat=n))
N=len(verts)
def dh(a,b): return sum(1 for x,y in zip(a,b) if x!=y)
edges=[(i,j) for i in range(N) for j in range(i+1,N) if dh(verts[i],verts[j])==d]
assert N==27 and len(edges)==162
print("[1] graph: 27 vertices, 162 edges OK")

def K(k,x):
    return sum(((-1)**j)*((q-1)**(k-j))*comb(x,j)*comb(n-x,k-j) for j in range(k+1))
eigs=[K(d,i) for i in range(n+1)]
assert eigs==[12,0,-3,3],eigs
assert sum(comb(n,i)*(q-1)**i for i in range(n+1))==27
assert 1-eigs[0]/min(eigs)==5
print("[2] spectrum [12,0,-3,3], Hoffman chi_q>=5 OK")

om=np.exp(2j*np.pi/3)
F=np.array([[1,1],[1,-1]],dtype=complex)/np.sqrt(2)
Ua=[np.diag([om**a,om**(2*a)])@F for a in range(3)]
for a in range(3):
    assert np.allclose(Ua[a]@Ua[a].conj().T,np.eye(2))
    for b in range(3):
        if a!=b:
            assert np.allclose(np.diag(Ua[a].conj().T@Ua[b]),-0.5*np.ones(2))
def v(x,k,s):
    w=np.zeros(6,dtype=complex)
    for j in range(3):
        w[j*2:(j+1)*2]=om**(j*k)*Ua[x[j]][:,s]
    return w/np.sqrt(3)
cols=[(k,s) for k in range(3) for s in range(2)]
for x in verts:
    M=np.stack([v(x,k,s) for (k,s) in cols],axis=1)
    assert np.allclose(M.conj().T@M,np.eye(6),atol=1e-9)
for i,x in enumerate(verts):
    for y in verts[i+1:]:
        if dh(x,y)==d:
            for (k,s) in cols:
                assert abs(np.vdot(v(x,k,s),v(y,k,s)))<1e-9
print("[3] explicit 6-dim quantum 6-coloring verified OK")

d7=json.load(open("output/artifacts/coloring7.json"))
col=d7["coloring"]
assert len(col)==27 and len(set(col))<=7
assert all(col[i]!=col[j] for (i,j) in edges)
print("[4] classical 7-coloring verified OK (6-infeasibility: exact CBC ILP, see DRAFT)")

# omega witness + alpha witness
W=[(0,0,1),(0,1,0),(1,0,0),(1,1,1)]
assert all(dh(a,b)==d for ii,a in enumerate(W) for b in W[ii+1:])
A=[(0,2,2),(1,2,2),(2,0,0),(2,0,1)]
assert all(dh(a,b)!=d for ii,a in enumerate(A) for b in A[ii+1:])
print("[5] 4-clique and 4-independent-set witnesses OK (optimality: exact CBC ILP, see DRAFT)")

# covariant no-go identity: shell kernel values by weight
shell2=[z for z in verts if dh(z,(0,0,0))==2]
assert len(shell2)==12
def Kw(w): return sum(om**sum(a*b for a,b in zip(w,z)) for z in shell2)
got=sorted(set((round(Kw(w).real,6),round(Kw(w).imag,6)) for w in verts))
assert got==[(-3.0,0.0),(0.0,0.0),(3.0,0.0),(12.0,0.0)],got
print("[6] covariant no-go character sums {12,0,-3,+3} OK")
print("ALL CHECKS PASSED")
