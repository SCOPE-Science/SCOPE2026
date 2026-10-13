"""Finite matrix checks for the rank-one bipartite dephasing theorem.

Requires numpy, scipy. Tests are corroboration, not proof of the all-size theorem.
"""
from itertools import combinations
import numpy as np
from numpy.linalg import eigvals, norm, matrix_rank
from scipy.linalg import expm


def model(a, b, D, seed=1):
    rng = np.random.default_rng(seed+101*a+17*b+sum(D))
    u = (0.75+rng.random(a))*np.exp(1j*rng.uniform(-1,1,a))
    v = (0.75+rng.random(b))*np.exp(1j*rng.uniform(-1,1,b))
    n = a+b
    H = np.zeros((n,n), complex)
    H[:a,a:] = np.outer(u,v.conj())
    H[a:,:a] = H[:a,a:].conj().T
    FA = [i for i in range(1,a) if i not in D]
    FB = [j for j in range(a,n) if j not in D]
    Q = np.zeros((n,n), complex)
    for ids,w in ((FA,u),(FB,v)):
        if ids:
            inds = np.array(ids)
            z = (u[inds] if ids == FA else v[inds-a])
            B = np.eye(len(ids)) - np.outer(z,z.conj()) / np.vdot(z,z)
            Q[np.ix_(inds,inds)] = B
    g = [1.1+0.13*(j%3) for j in D]
    P0 = np.zeros((n,n),complex); P0[0,0]=1
    Ps = []
    for j in D:
        P = np.zeros((n,n),complex);P[j,j]=1;Ps.append(P)
    def L(X):
        out = -1j*(H@X-X@H)-0.75*(P0@X+X@P0)
        for rate,P in zip(g,Ps):
            out+=rate*(P@X@P-(P@X+X@P)/2)
        return out
    Lmat = np.column_stack([L(np.eye(n,dtype=complex)[:,[i]] @ np.eye(n,dtype=complex)[[j],:]).reshape(-1) for i in range(n) for j in range(n)])
    # Inputs list E_ij flattened C order, matching output flatten C order.
    # The basis columns are arranged lexicographically, as required.
    return H, Q, Lmat, L


def run():
    cases=0;zero_tests=0;time_tests=0
    for a in range(2,5):
      for b in range(2,4):
        n=a+b
        pool=list(range(1,n))
        for size in range(len(pool)+1):
          for D in combinations(pool,size):
            H,Q,mat,L=model(a,b,D,seed=9)
            FA=[i for i in range(1,a) if i not in D]
            FB=[j for j in range(a,n) if j not in D]
            d=max(len(FA)-1,0)+max(len(FB)-1,0)
            assert abs(np.trace(Q).real-d)<1e-9
            assert norm(Q@Q-Q)<1e-10
            assert norm(H@Q)<1e-10
            assert norm(L(Q))<1e-10
            vals=eigvals(mat)
            nonzero=vals[np.abs(vals)>1e-7]
            near=np.count_nonzero(np.abs(vals)<=1e-7)
            assert near==d*d, (a,b,D,d,near,sorted(np.abs(vals))[:d*d+2])
            assert len(nonzero)==0 or max(nonzero.real)<-1e-9,(a,b,D,max(nonzero.real))
            cases+=1; zero_tests+=1
    for a,b,D in [(2,2,()),(2,2,(2,)),(3,2,(1,3)),(2,3,(3,4))]:
        H,Q,mat,L=model(a,b,D,seed=11)
        n=a+b
        rng=np.random.default_rng(31+n+sum(D))
        z=rng.normal(size=n)+1j*rng.normal(size=n)
        z=z/norm(z)
        rho=np.outer(z,z.conj())
        M=expm(mat*600)
        got=(M@rho.reshape(-1)).reshape(n,n)
        expected=Q@rho@Q
        assert norm(got-expected)<1e-7, (a,b,D,norm(got-expected))
        time_tests+=1
    print(f'VERIFY_OK rank_one_bipartite_lindblad_cases={cases} stationary_kernel={zero_tests} long_time_states={time_tests}')

if __name__=='__main__':run()
