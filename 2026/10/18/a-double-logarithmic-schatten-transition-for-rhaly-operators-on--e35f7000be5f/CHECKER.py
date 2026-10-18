"""Finite diagnostics for the lower-triangular Dirichlet Rhaly model.
Requires NumPy; these tests are not proofs of infinite-dimensional assertions.
"""
import math
import numpy as np

counter=0
for N in (1, 2, 3, 8, 16, 32):
    J=np.tril(np.ones((N,N)))
    observed=np.linalg.svd(J,compute_uv=False)
    predicted=np.array([1/(2*math.sin((2*k-1)*math.pi/(4*N+2))) for k in range(1,N+1)])
    assert np.allclose(observed,predicted,atol=2e-13,rtol=2e-13)
    counter+=N
for beta in (0.8,1.0,1.2,1.7,2.0,2.4,3.0):
    for N in (2,4,8,16,32,64):
        m=np.arange(1,N+1,dtype=float)
        c=1/(np.sqrt(m)*np.log(np.e+m-1)**beta)
        d=1/np.sqrt(m)
        A=np.tril(c[:,None]*d[None,:])
        x=np.array([math.sin(k+1)/math.sqrt(k+1) for k in range(N)])
        coeff_input=x/np.sqrt(m)
        direct_coeff=np.cumsum(coeff_input)/(m*np.log(np.e+m-1)**beta)
        assert np.allclose(A@x,direct_coeff*np.sqrt(m),atol=1e-12,rtol=1e-12)
        singular_values=np.linalg.svd(A,compute_uv=False)
        assert len(singular_values)==N and min(singular_values)>=0
        counter+=N*N
print('PASS',counter,'finite diagnostic configurations')
