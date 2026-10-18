"""Independent numerical cross-check for intrinsic Euclidean balls in
fixed-cardinality bipartite matching polytopes. This code is not a proof.
Dependencies: numpy, scipy. Run: python check_inballs.py
"""
import math
import numpy as np
from scipy.optimize import linprog


def check_graph(p, q, edges, k):
    m=len(edges)
    assert 2 <= p < q and 1 <= k <= p
    ldeg=np.bincount([u for u,v in edges],minlength=p)
    rdeg=np.bincount([v for u,v in edges],minlength=q)
    assert len(set(ldeg)) == len(set(rdeg)) == 1
    a=int(ldeg[0]); b=int(rdeg[0]); assert p*a==q*b==m
    L=np.zeros((p,m)); R=np.zeros((q,m))
    for j,(u,v) in enumerate(edges): L[u,j]=1;R[v,j]=1
    if k<p:
        E=np.ones((1,m));f=np.array([k],float)
        d0=math.sqrt(1-1/m)
        dl=math.sqrt(a*(1-1/p))
        dr=math.sqrt(b*(1-1/q))
        bound0=k/math.sqrt(m*(m-1))
        boundL=(p-k)/math.sqrt(m*(p-1))
        radius=min(bound0,boundL)
        phase='coordinate' if bound0 < boundL-1e-10 else 'left' if boundL < bound0-1e-10 else 'tie'
        expected_dimension=0 if phase != 'left' else m-p
    else:
        E=L;f=np.ones(p)
        d0=math.sqrt(1-1/a);dl=0
        dr=math.sqrt(b*(1-1/a))
        bound0=1/math.sqrt(a*(a-1))
        boundR=(q-p)/math.sqrt(p*q*(a-1))
        radius=min(bound0,boundR)
        phase='coordinate' if bound0 < boundR-1e-10 else 'right' if boundR < bound0-1e-10 else 'tie'
        expected_dimension=m-p-q+1 if phase=='right' else 0
    upper=[];rhs=[]
    for e in range(m):
        v=np.zeros(m+1);v[e]=-1;v[-1]=d0
        upper.append(v);rhs.append(0.)
    if k<p:
        for row in L:
            v=np.r_[row,dl];upper.append(v);rhs.append(1.)
    for row in R:
        v=np.r_[row,dr];upper.append(v);rhs.append(1.)
    obj=np.zeros(m+1);obj[-1]=-1
    sol=linprog(obj,A_ub=np.array(upper),b_ub=rhs,
                A_eq=np.c_[E,np.zeros(len(f))],b_eq=f,
                bounds=[(None,None)]*m+[(0,None)],method='highs')
    assert sol.success,(p,q,k,sol.message)
    assert abs(-sol.fun-radius)<2e-8, (p,q,k,-sol.fun,radius)
    uniform=np.r_[np.full(m,k/m),radius]
    slack=np.array(rhs)-np.array(upper)@uniform
    assert slack.min()>=-1e-9,(p,q,k,slack.min())
    # Rank of all universal tight equations at the uniform center.
    tight=[E]
    if phase in ('coordinate','tie'):
        tight.append(np.eye(m))
    if k<p and phase=='left':tight.append(L)
    if k==p and phase=='right':tight.append(R)
    dimension=m-np.linalg.matrix_rank(np.vstack(tight),tol=1e-9)
    assert dimension==expected_dimension,(p,q,k,phase,dimension,expected_dimension)
    # Independent contact count from numerical residuals.
    contact=int(np.sum(np.abs(slack)<1e-8))
    expected=(m if phase in ('coordinate','tie') else 0)
    if phase=='left' or (k<p and phase=='tie'):expected+=p
    if phase=='right' or (k==p and phase=='tie'):expected+=q
    assert contact==expected,(p,q,k,phase,contact,expected)
    return phase


def complete(p,q):return [(u,v) for u in range(p) for v in range(q)]

def incidence_of_complete(n):
    pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
    return [(u,j) for j,pair in enumerate(pairs) for u in pair]

def cycle_lift(n):
    # Vertices on left indexed 0..n-1; right indexed 0..n-1;
    # degree-two regular square block (not used because p<q is required).
    return [(u,v) for u in range(n) for v in (u,(u+1)%n)]

def main():
    count=0
    for p in range(2,7):
        for q in range(p+1,11):
            es=complete(p,q)
            for k in range(1,p+1):check_graph(p,q,es,k);count+=1
    print('complete-bipartite independent LP profiles:',count)
    for n in (4,5,6,7):
        es=incidence_of_complete(n)
        for k in range(1,n+1):
            phase=check_graph(n,n*(n-1)//2,es,k)
            count+=1
            if k==n:assert phase==('right' if n==4 else 'coordinate')
    print('total numerical LP profiles including sparse incidence examples:',count)
    print('PASS: exact radius, uniform containment, equality rank, contact counts')

if __name__=='__main__':main()
