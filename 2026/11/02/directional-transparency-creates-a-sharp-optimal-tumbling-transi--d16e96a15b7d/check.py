#!/usr/bin/env python3
"""Independent finite-volume check of directional target capture for a velocity-jump process."""
import math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve

def predicted(L, v, switch, p, q):
    z = switch*L/v
    s = p+q-p*q
    b = 12-6*(p+q)+4*p*q
    return L/v*(s*z*z+b*z+3*s)/(6*(s*z+p*q))

def finite_volume(L, v, switch, p, q, N):
    # Each velocity advects through N serial exponential holding cells, preserving
    # the same independent absorption probabilities at the wrap edge.
    adv = v*N/L
    rr=[];cc=[];vv=[]
    def entry(i,j,x): rr.append(i);cc.append(j);vv.append(x)
    for d in range(2):
        for k in range(N):
            i=d*N+k
            entry(i,i,-(adv+switch))
            entry(i,(1-d)*N+k,switch)
            if d==0:
                kk=k+1; survive=1 if kk<N else 1-p; kk%=N
            else:
                kk=k-1; survive=1 if kk>=0 else 1-q; kk%=N
            entry(i,d*N+kk,adv*survive)
    G=coo_matrix((vv,(rr,cc)),shape=(2*N,2*N)).tocsr()
    t=spsolve(-G,np.ones(2*N))
    return float(t.mean())

def test():
    cases=[(1,1,0,1,.25),(1,1,.1,1,.25),(1,1,(3*math.sqrt(3)-1)/4,1,.25),
           (1,1,2,1,.25),(1,1,1,.6,.6),(3,2,.7,.05,.7),
           (2.4,1.6,.09,.3,.9),(1,3,2,.8,.35)]
    for L,v,r,p,q in cases:
        t=predicted(L,v,r,p,q)
        for N in (80,200,500):
            x=finite_volume(L,v,r,p,q,N)
            # Finite Erlang step approximation has first-order convergence;
            # a conservative bounded error sufficient to corroborate formula.
            assert abs(x-t) <= 6*(L/v)/N, (L,v,r,p,q,N,t,x)
        print(f'PASS p={p:.4g} q={q:.4g} switch={r:.6g} exact={t:.10g} FV500={x:.10g}')
    p,q=1,.25
    zstar=(math.sqrt(3)*abs(p-q)-p*q)/(p+q-p*q)
    assert abs(zstar-(3*math.sqrt(3)-1)/4)<1.e-12
    tstar=predicted(1,1,zstar,p,q)
    assert abs(tstar-(5/6+math.sqrt(3)/4))<1e-12
    assert tstar<predicted(1,1,0,p,q)
    for p,q in ((.3,.3),(.9,.7),(.9,.1),(.01,.95)):
        z=max(0,(math.sqrt(3)*abs(p-q)-p*q)/(p+q-p*q))
        opt=predicted(1,1,z,p,q)
        for zz in (0,.001,.01,.1,.3,.6,1,1.5,2.5,5,10,50):
            assert opt <= predicted(1,1,zz,p,q)+1e-12
    print('PASS optimizer, limiting and equal-reactivity boundaries')

if __name__=='__main__':test()
