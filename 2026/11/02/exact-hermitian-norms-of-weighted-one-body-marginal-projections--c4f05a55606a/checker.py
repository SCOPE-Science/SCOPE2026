"""Supplementary finite-dimensional checks for the one-body marginal projection theorem.
Only standard Python/numpy used; infinite assertions require the proof in RESULT.md.
"""
from itertools import product
from math import comb, sqrt, pi, exp, factorial
from fractions import Fraction
from functools import reduce
import numpy as np


def exact_moment(dims, weights):
    p = Fraction(0)
    for bits in product((0, 1), repeat=len(dims)):
        prob = Fraction(1)
        s = Fraction(0)
        for d, t, bit in zip(dims, weights, bits):
            prob *= Fraction(1, d) if bit else Fraction(d - 1, d)
            s += Fraction(t) * (d * bit - 1)
        p += prob * abs(s)
    return p


def binomial_moment(n, d):
    return sum(Fraction(comb(n, k) * (d-1)**(n-k), d**n) * abs(d*k-n)
               for k in range(n+1))


def binomial_closed(n,d):
    k=n//d
    return Fraction(2*n*comb(n-1,k) * (d-1)**(n-k), d**n)


def kron(ops):
    return reduce(np.kron, ops)


def partial_trace_keep(A, dims, j):
    # A has shape dims+dims; contract the complementary indices.
    n=len(dims)
    M=A.reshape(tuple(dims)+tuple(dims))
    for k in range(n-1,-1,-1):
        if k!=j:
            M=np.trace(M,axis1=k,axis2=k+M.ndim//2)
    return M


def local_projection(A, dims, weights):
    D=int(np.prod(dims));tr=np.trace(A)
    out=-sum(weights)*tr/D*np.eye(D,dtype=complex)
    for j,(d,t) in enumerate(zip(dims,weights)):
        marginal=partial_trace_keep(A,dims,j)
        assert marginal.shape==(d,d)
        out+=t*kron([marginal if k==j else np.eye(dims[k]) for k in range(len(dims))])/(D/d)
    return out


def trace_norm(A):
    return np.sum(np.linalg.svd(A,compute_uv=False))


def operator_norm(A):
    return np.linalg.svd(A,compute_uv=False)[0]


def check():
    tests=0
    for n in range(1,9):
        for d in range(2,8):
            assert binomial_moment(n,d)==binomial_closed(n,d)
            if n<=5:
                assert binomial_moment(n,d)==exact_moment([d]*n,[1]*n)
            tests+=2 if n<=5 else 1
    for dims,weights in [([2],[1]),([3],[1]),([2,2],[1,1]),([2,3],[1,2]),([2,2,2],[1,-2,3]),([3,2,2],[1,0,1]),([2,3,2],[-1,2,-1])]:
        rng=np.random.default_rng(17+sum(dims));D=int(np.prod(dims));bound=float(exact_moment(dims,weights))
        # Product-pure local state supplies equality in trace norm.
        v=np.zeros(D,dtype=complex);v[0]=1
        rho=np.outer(v,v.conj())
        assert abs(trace_norm(local_projection(rho,dims,weights))-bound)<3e-10
        tests+=1
        # Hermitian dual sign of the output certifies induced-norm lower bound.
        B=local_projection(rho,dims,weights)
        eig,U=np.linalg.eigh(B)
        sgn=U@np.diag(np.where(eig>=0,1.,-1.))@U.conj().T
        assert abs(operator_norm(sgn)-1)<3e-10
        assert abs(np.real(np.trace(rho@local_projection(sgn,dims,weights)))-bound)<3e-10
        tests+=2
        for q in range(12):
            z=rng.normal(size=D)+1j*rng.normal(size=D)
            z/=np.linalg.norm(z)
            state=np.outer(z,z.conj())
            val=trace_norm(local_projection(state,dims,weights))
            assert val <= bound + 4e-10,(dims,weights,val,bound)
            tests+=1
            M=rng.normal(size=(D,D))+1j*rng.normal(size=(D,D));M=(M+M.conj().T)/2
            assert operator_norm(local_projection(M,dims,weights))<= bound*operator_norm(M)+4e-10
            tests+=1
    # Compare fixed-d Gaussian approximation and Poisson crossover numerically.
    for d in (2,3,5):
        n=1200
        val=float(binomial_closed(n,d))
        asym=sqrt(2*n*(d-1)/pi)
        assert abs(val/asym-1)<0.005
        tests+=1
    for rate in (0.5,1,2,3.25,8):
        n=300
        d=max(2,round(n/rate))
        lam=n/d
        k=int(lam)
        poisson=2*exp(-lam)*lam**k/factorial(k)
        val=float(binomial_closed(n,d))/n
        assert abs(val-poisson)<0.015,(rate,val,poisson)
        tests+=1
    print('PASS:',tests,'finite checks; all source normalizations and random inequalities consistent')

if __name__=='__main__':
    check()
