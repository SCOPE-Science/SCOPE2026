"""Independent finite matrix-exponential and transport dual checks for the stated graph result."""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog

def verify(n,t):
    N=n+1
    edges=[(0,1)]+[(1,i) for i in range(2,N)]+[(i,j) for i in range(2,N) for j in range(i+1,N)]
    L=np.zeros((N,N))
    for a,b in edges:
        L[a,a]+=1;L[b,b]+=1;L[a,b]-=1;L[b,a]-=1
    H=expm(-t*L)
    u=np.exp(-t); z=np.exp(-(n+1)*t); q=np.exp(-n*t)
    F=2*(n-1)/n*u-(n-2)/n*z
    G=2/n*u+(n-2)/n*z
    for x,y,w in [(0,1,F),(1,2,G)]+([(2,3,q)] if n>=3 else []):
        a=H[x]-H[y]
        # All pairwise distances are 1 apart from pendant to other clique vertices (distance 2).
        dist=np.ones((N,N));np.fill_diagonal(dist,0)
        dist[0,2:]=2;dist[2:,0]=2
        pos=np.where(a>1e-12)[0];neg=np.where(a < -1e-12)[0]
        if len(pos)==0 or len(neg)==0: val=0.0
        else:
            ce=np.array([dist[i,j] for i in pos for j in neg])
            rows=[]; rhs=[]
            for i in pos:
                rows.append([float(aa==i) for aa in pos for bb in neg]);rhs.append(a[i])
            for j in neg:
                rows.append([float(bb==j) for aa in pos for bb in neg]);rhs.append(-a[j])
            opt=linprog(ce,A_eq=np.array(rows),b_eq=np.array(rhs),bounds=(0,None),method='highs')
            assert opt.success,(n,t,x,y,opt.message)
            val=opt.fun
        assert abs(val-w)<2e-7,(n,t,x,y,val,w)
    # On every edge the endpoint formula dominates the other two formulas.
    assert F+1e-10>=G and F+1e-10>=q
    return 1

count=0
for n in range(2,23):
    for t in [0,0.005,0.03,0.12,0.4,0.8,1.2]:
        count+=verify(n,t)
print(f"PASS: {count} graph/time instances, 3 edge types where defined; independent LP and matrix exponentials")
