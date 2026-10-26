"""Numerical replay for exact dual-leaf clique spectral-gap formulas.
Depends on scipy and numpy. Public mathematical implementation only.
"""
import numpy as np
from scipy.optimize import brentq

def witness(k, budget=1.0):
    assert k >= 1
    N = k+4
    s = np.sqrt((k+2)/(4*k))
    f = lambda t: (k*s-2*t)/N-t/(2*np.sqrt(1-t*t))
    t = brentq(f, 0, 1-1e-15, xtol=1e-14)
    u = np.sqrt(1-t*t)
    mu = (2*t-k*s)/N
    V = 3*k/4+3+2*u-(2*t-k*s)**2/N
    lam = budget/V
    rate_leaf=lam*(1+1/(2*u))
    rate_spoke=lam*(1+mu/s)/2
    rate_periphery=lam*(-mu/(k*s)) if k>1 else 0.0
    rate_hub=lam*(1+u-k*(1+mu/s)/4)
    Nmat = k+4
    L=np.zeros((Nmat,Nmat))
    def edge(i,j,w):
        L[i,i]+=w; L[j,j]+=w; L[i,j]-=w; L[j,i]-=w
    edge(0,1,rate_hub)
    for j in range(2,k+2):
        edge(0,j,rate_spoke)
        edge(1,j,rate_spoke)
    for i in range(2,k+2):
        for j in range(i+1,k+2):
            edge(i,j,rate_periphery)
    edge(0,k+2,rate_leaf)
    edge(1,k+3,rate_leaf)
    # Symmetric coordinates of the trial embedding. Peripheral simplex Gram matrix.
    Q=np.zeros((Nmat,k+1))
    Q[0,0]=.5;Q[1,0]=-.5
    Q[k+2,0]=.5+u;Q[k+3,0]=-(.5+u)
    Q[k+2,1]=t;Q[k+3,1]=t
    Q[2:k+2,1]=-s
    if k>1:
        # k-1 independent simplex basis vectors, from eigenbasis of centering projector.
        H=np.eye(k)-np.ones((k,k))/k
        Z=np.linalg.svd(H)[0][:,:k-1] / np.sqrt(2)
        Q[2:k+2,2:k+1]=Z
    assert Q.shape[1]==k+1
    centered=Q-Q.mean(axis=0)
    residual=np.linalg.norm(L@Q-lam*centered, ord='fro')
    eigenvalues=np.linalg.eigvalsh(L)
    budget_used=rate_hub+2*k*rate_spoke+k*(k-1)*rate_periphery/2+2*rate_leaf
    ratio= float(eigenvalues[1]/lam)
    diffs=[]
    edges=[(0,1)]+[(a,j) for a in (0,1) for j in range(2,k+2)]+[(i,j) for i in range(2,k+2) for j in range(i+1,k+2)]+[(0,k+2),(1,k+3)]
    for i,j in edges:
        diffs.append(float(np.linalg.norm(Q[i]-Q[j])**2))
    return dict(k=k,t=t,mu=mu,V=V,lambda_value=lam,rate_hub=rate_hub,rate_spoke=rate_spoke,rate_periphery=rate_periphery,rate_leaf=rate_leaf,spectral_min=eigenvalues[1],ratio=ratio,err_spectrum=float(abs(eigenvalues[1]-lam)),err_eigen=residual,err_budget=float(abs(budget_used-budget)),err_edges=float(np.max(np.abs(np.array(diffs)-1))),eig_mult=int(np.sum(np.abs(eigenvalues[1:]-lam)<1e-8)))

if __name__=='__main__':
    for k in list(range(1,31))+[40,60,100]:
        o=witness(k)
        assert min(o[x] for x in ('rate_hub','rate_spoke','rate_leaf')) >0
        assert o['rate_periphery']>0 if k>1 else o['rate_periphery']==0
        assert abs(o['ratio']-1)<5e-8, o
        assert o['err_eigen']<1e-7 and o['err_budget']<1e-7 and o['err_edges']<1e-7, o
        if k in (1,2,3,4,5,10,30,100):
            print(k, 'V=',format(o['V'],'.13f'),'lambda=',format(o['lambda_value'],'.13f'),'lambda_mult=',o['eig_mult'],'max_residual=',format(o['err_eigen'],'.2e'),'rates=',[round(o[z],9) for z in ('rate_hub','rate_spoke','rate_periphery','rate_leaf')])
    print('VERIFY_OK: 33 graph sizes, full matrix eigenvalues and dual length constraints')
