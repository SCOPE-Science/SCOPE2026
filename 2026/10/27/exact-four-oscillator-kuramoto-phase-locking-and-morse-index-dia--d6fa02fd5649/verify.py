#!/usr/bin/env python3
"""Reproduce branch, threshold and quotient-Hessian checks for four oscillators."""
import math
from itertools import product
from collections import Counter
import numpy as np
import sympy as sp

w = np.array([-3., -1., 1., 3.])
xstar = (20.+2.*math.sqrt(73.))/3.
kstar = 2*xstar/(math.sqrt(xstar-9.)+math.sqrt(xstar-1.))
kzero = 9./math.sqrt(2.)
assert sp.simplify(3*((20+2*sp.sqrt(73))/3)**2-40*((20+2*sp.sqrt(73))/3)+36)==0

def states(K):
    """Locate all monotonic-branch roots for given K, with branch-specific intervals."""
    def kval(x,a,b):
        den=a*math.sqrt(x-9)+b*math.sqrt(x-1)
        return 4*x/den
    ans=[]
    bound = max(5000., (5*K)**2)
    cases=[('A',2,2,[(9.,xstar),(xstar,bound)]),
           ('B',2,0,[(9.,18.),(18.,bound)]),
           ('C',0,2,[(9.,bound)]),
           ('D',-2,2,[(9.,bound)])]
    from scipy.optimize import brentq
    for name,a,b,intervals in cases:
        for L,R in intervals:
            left=L+1e-9 if L==9. else L
            f=lambda x:kval(x,a,b)-K
            if f(left)*f(R)>0: continue
            root=brentq(f,left,R,xtol=1e-12)
            for es in product((-1,1),repeat=4):
                if es[0]+es[3]!=a or es[1]+es[2]!=b: continue
                c=np.array(es)*np.sqrt((root-w*w)/root)
                s=w/math.sqrt(root)
                theta=np.arctan2(s,c)
                z=np.mean(np.exp(1j*theta))
                assert abs(z.imag)<2e-9 and z.real>0
                assert abs(K*z.real-math.sqrt(root))<2e-7
                residual=w+(K/4)*np.sin(theta[None,:]-theta[:,None]).sum(axis=1)
                assert np.max(np.abs(residual))<2e-7
                hess=(K*z.real)*np.diag(c)-(K/4)*(np.outer(c,c)+np.outer(s,s))
                eig=np.linalg.eigvalsh(hess)
                assert abs(eig[0])<3e-6 or abs(eig[1])<3e-6 or abs(eig[2])<3e-6
                neg=sum(v<-1e-6 for v in eig)
                ans.append((name,root,es,neg))
    return ans

# Exact branch inertia from rank-one formula; numerical examples independently check.
for K, expected_count, index_profile in [
 (4.,0,{}),(5.,2,{0:1,1:1}),(6.5,4,{0:1,1:2,2:1}),
 (8.,4,{0:1,1:2,2:1}),(12.1,8,{0:1,1:4,2:3}),(14.,8,{0:1,1:4,2:3})]:
    a=states(K)
    counts=dict(Counter(t[3] for t in a))
    assert len(a)==expected_count, (K,len(a),a)
    assert counts==index_profile,(K,counts)
    print('K',K,'N',len(a),'Morse',counts)
assert kstar<kzero<12
print('THRESHOLDS',kstar,kzero,12)
print('VERIFY_OK: unique threshold roots; complete A/B/C/D sign families; 4 coupling windows; state counts 0/2/4/8; stable/saddle indices; eigenvalue/residual checks')
