#!/usr/bin/env python3
"""Reproduce two-site Dicke reduction, damping, concurrence and scaling checks.
Requires Python 3.9+ and NumPy. Analytic all-dimension arguments are in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt
import numpy as np

Y=np.array([[0,-1j],[1j,0]],complex)
YY=np.kron(Y,Y)
counts=0
for n in range(2,65):
    for k in range(1,n):
        A=F((n-k)*(n-k-1), n*(n-1))
        B=F(k*(n-k), n*(n-1))
        D=F(k*(k-1), n*(n-1))
        assert A+2*B+D==1
        assert B+D==F(k,n)
        assert B*B-A*D==F(k*(n-k),n*n*(n-1))
        for q in (F(0),F(1,7),F(1,2),F(6,7),F(1)):
            a=A+2*(1-q)*B+(1-q)**2*D
            assert a==1-2*q*F(k,n)+q*q*D
            b=q*B+q*(1-q)*D
            assert a+2*b+q*q*D==1
            if k>=2 and B*B<D and q==0:
                assert B*B<D*a
        counts+=1

for n in range(2,8):
    for k in range(1,n):
        vec=np.zeros(2**n,dtype=complex)
        for bit in product((0,1),repeat=n):
            if sum(bit)==k:
                idx=sum(v<<(n-1-i) for i,v in enumerate(bit))
                vec[idx]=1/sqrt(comb(n,k))
        reduced=vec.reshape(4,-1)@vec.reshape(4,-1).conj().T
        A=(n-k)*(n-k-1)/(n*(n-1))
        B=k*(n-k)/(n*(n-1))
        D=k*(k-1)/(n*(n-1))
        expected=np.array([[A,0,0,0],[0,B,B,0],[0,B,B,0],[0,0,0,D]],complex)
        assert np.allclose(reduced,expected,atol=2e-14)
        for q in (0,.1,.25,.5,.75,.9,1):
            E0=np.diag([1,sqrt(q)])
            E1=np.array([[0,sqrt(1-q)],[0,0]])
            out=sum(K@reduced@K.conj().T for e in (E0,E1) for f in (E0,E1) for K in [np.kron(e,f)])
            a=1-2*q*k/n+q*q*D
            b=q*B+q*(1-q)*D
            target=np.array([[a,0,0,0],[0,b,q*B,0],[0,q*B,b,0],[0,0,0,q*q*D]],complex)
            assert np.allclose(out,target,atol=2e-14)
            assert np.allclose(np.linalg.eigvalsh(out).min()>=-1e-14,True)
            W=out@YY@out.conj()@YY
            vals=np.maximum(0,np.linalg.eigvals(W).real)
            roots=np.sort(np.sqrt(vals))[::-1]
            actual=max(0,roots[0]-sum(roots[1:]))
            formula=2*q*max(0,B-sqrt(max(0,a*D)))
            assert abs(actual-formula)<2e-7,(n,k,q,actual,formula)
for n in (1000,10000,100000):
    for alpha in (.2,.5,.8):
        k=round(n*alpha)
        A=(n-k)*(n-k-1)/(n*(n-1)); B=k*(n-k)/(n*(n-1)); D=k*(k-1)/(n*(n-1))
        E=B*B-A*D
        eps=E/(D*(sqrt(B*B+E)+B))
        if n>=10000:
            assert abs(n*eps-1/(2*alpha*alpha))<.004
print('VERIFY_OK exact_count_identities=%d vector_trace_and_Kraus_cases=passed Wootters_concurrence=passed asymptotic_checks=passed'%counts)
