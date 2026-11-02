#!/usr/bin/env python3
"""Independent finite checks for phase-memory qubit dephasing formulas.

Run: python verify.py.  NumPy is required.  Analytic statements for all
memory sizes are established in RESULT.md and are not inferred from tests.
"""
import math
import random
from itertools import product
import numpy as np

count=0

def test(condition, message):
    global count
    if not bool(condition):
        raise AssertionError(message)
    count+=1

rng=random.Random(20261025)
for r in (1, 2, 3, 4):
    m=2**r
    n=m-1
    tau=math.pi/(2*m)
    omega=np.array([sum(2**j*s[j] for j in range(r)) for s in product((-1,1), repeat=r)],dtype=float)
    test(sorted(omega.astype(int))==list(range(-(m-1),m,2)),f'Ising spectrum r={r}')
    z=np.exp(2j*omega*tau)
    for d in range(1,m):
        f=sum(np.exp(-2j*omega*d*tau))/m
        test(abs(f)<3e-12,f'Pairwise dephasing r={r}, d={d}')
    # The phase orbit must be a rotated copy of all m-th roots.
    for i in range(m):
        test(abs(z[i]**m-z[0]**m)<1e-10,f'Root class r={r}')
        for j in range(i):
            test(abs(z[i]-z[j])>1e-7,f'Distinct roots r={r}')
    # Number-distribution spectrum via the branch Gram matrix.
    phi=[np.array([1,zz],dtype=complex)/math.sqrt(2) for zz in z]
    gram=np.array([[(np.vdot(phi[i],phi[j]))**n/m for j in range(m)] for i in range(m)])
    expected=sorted(math.comb(n,k)/2**n for k in range(n+1))
    observed=sorted(np.linalg.eigvalsh(gram))
    test(np.allclose(observed,expected,atol=3e-11),f'Process Gram spectrum r={r}')
    if r<=3:
        vectors=[]
        for one in phi:
            v=np.array([1+0j])
            for _ in range(n):v=np.kron(v,one)
            vectors.append(v)
        rho=sum(np.outer(v,np.conjugate(v)) for v in vectors)/m
        test(np.allclose(np.diag(rho),2**(-n),atol=3e-12),f'Flat dephased diagonal r={r}')
        eig=sorted(np.linalg.eigvalsh(rho))[-m:]
        test(np.allclose(eig,expected,atol=3e-11),f'Full process spectrum r={r}')
    if r==2:
        entropy=-sum(p*math.log(p) for p in expected)
        test(abs(n*math.log(2)-entropy-0.75*math.log(3))<1e-13,'Four-time result')
    # Frame-potential inequality, sharp for the regular Fourier clock.
    for q in range(9):
        weights=np.array([0.05+rng.random() for _ in range(m)])
        weights/=sum(weights)
        rhs=(m*sum(weights**2)-1)/(m-1)
        times=np.array([tau*k for k in range(m)])
        def avgvisibility(times):
            w=np.array([sum(weights*np.exp(-2j*omega*(times[k]-times[l]))) for k in range(m) for l in range(m) if k!=l])
            return float(np.mean(abs(w)**2))
        fixed=avgvisibility(times)
        test(abs(fixed-rhs)<3e-12,f'Sharp frame identity r={r}, q={q}')
        times=np.array([rng.uniform(-2,2) for _ in range(m)])
        random_level=avgvisibility(times)
        test(random_level+1e-11>=rhs,f'Frame bound r={r}, q={q}')

# Direct Choi-state test for independent memories: normalized channel Choi
# is supported on {|00>, |11>}, and the off-diagonal is gamma/2.
for r in (1,2,3):
    m=2**r;tau=math.pi/(2*m)
    frequencies=np.array([sum(2**j*s[j] for j in range(r)) for s in product((-1,1),repeat=r)])
    for d in range(m):
        mixture=np.zeros((2,2),dtype=complex)
        for w in frequencies:
            vec=np.array([np.exp(-1j*w*d*tau),np.exp(+1j*w*d*tau)])/math.sqrt(2)
            mixture+=np.outer(vec,vec.conjugate())/m
        gamma=sum(np.exp(-2j*w*d*tau) for w in frequencies)/m
        test(abs(mixture[0,1]-gamma/2)<1e-12,f'Physical Choi convention r={r}, d={d}')
        test(np.allclose(np.diag(mixture),.5,atol=1e-12),f'Physical Choi diagonal r={r}, d={d}')

print('PASS:',count,'finite assertions. Global proofs are analytic, not numerical.')
