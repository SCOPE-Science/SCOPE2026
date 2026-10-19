"""Reproducible finite diagnostics for antiphase flip normal form.
Universal assertions are established analytically in RESULT.md, not by finite tests.
"""
import numpy as np
from scipy.optimize import root

def trial(edges, weights, delta):
    n=max(max(e) for e in edges)+1
    B=np.zeros((n,len(edges)))
    color={edges[0][0]:0}
    for _ in range(n):
        for u,v in edges:
            if u in color: color[v]=1-color[u]
            if v in color: color[u]=1-color[v]
    for j,(u,v) in enumerate(edges):
        assert color[u]!=color[v]
        if color[u]==0: B[u,j]=-1;B[v,j]=1
        else:B[u,j]=1;B[v,j]=-1
    A=np.diag(weights);K=B.T@B;M=K@A
    assert np.all(K>=0)
    eig,U=np.linalg.eigh(np.diag(np.sqrt(weights))@K@np.diag(np.sqrt(weights)))
    lam=float(eig[-1]);v=U[:,-1]/np.sqrt(weights)
    if v.sum()<0:v=-v
    assert np.min(v)>0
    kappa=float(np.dot(weights,v**4)/3)
    h=(2+delta)/lam
    pred=np.sqrt(delta/kappa)*v
    sol=root(lambda x:2*x-h*M@np.sin(x),pred,tol=1e-12)
    assert sol.success or np.linalg.norm(sol.fun)<1e-10
    x=sol.x
    assert np.linalg.norm(x)>1e-8
    assert np.linalg.norm(2*x-h*M@np.sin(x))<1e-9
    amp=float(np.dot(weights*v,x))
    assert abs(kappa*amp*amp/delta-1)<.08,(kappa*amp*amp/delta,edges,delta)
    J=np.eye(len(edges))-h*M@np.diag(np.cos(x))
    multipliers=np.linalg.eigvals(J)
    assert max(abs(multipliers))<1,(multipliers,edges,delta)
    return lam,kappa,amp,max(abs(multipliers))

if __name__=='__main__':
    tests=[([(0,1)],[1.0]),
           ([(0,1),(1,2),(2,3)],[1.0,.8,1.3]),
           ([(0,1),(0,2),(0,3),(0,4)],[.8,1.4,.7,1.1]),
           ([(0,1),(1,2),(1,3),(3,4),(3,5)],[1.2,.7,1.9,.9,1.4])]
    for e,a in tests:
        for d in (1e-3,1e-4):
            print('edges',len(e),'delta',d,'Lambda,kappa,amplitude,Jacobian spectral radius',trial(e,np.array(a),d))
    print('PASS: eight nontrivial branch, Perron, and contraction diagnostics')
