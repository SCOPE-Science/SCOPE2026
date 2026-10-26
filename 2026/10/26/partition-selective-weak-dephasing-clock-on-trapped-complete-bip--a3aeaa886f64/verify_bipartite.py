"""Reproduce finite-dimensional checks for a weak-dephasing absorption theorem.

Requires Python 3.10+ and NumPy 1.24+. All random data use a fixed seed.
The infinite-parameter proof is in RESULT.md; finite checks are not a proof.
"""
from fractions import Fraction
import numpy as np


def projectors(m, n, dtype=float):
    N = m + n
    k = m - 1
    A, B = np.zeros((N, N), dtype=dtype), np.zeros((N, N), dtype=dtype)
    A[1:m, 1:m] = np.eye(k) - np.ones((k, k)) / k
    B[m:, m:] = np.eye(n) - np.ones((n, n)) / n
    return A, B


def liouvillian(m, n, gamma, epsilon, alpha=1.0, beta=1.0, eta=0.0, J=1.0):
    N = m + n
    H = np.zeros((N, N))
    H[:m, m:] = J
    H[m:, :m] = J
    P0 = np.zeros((N, N))
    P0[0, 0] = 1
    K = -1j * H - gamma * P0
    L = np.kron(np.eye(N), K) + np.kron(K.conj(), np.eye(N))
    # Independent site dephasing: the ij coherence decays at epsilon*(r_i+r_j)/2.
    rates=np.array([eta]+[alpha]*(m-1)+[beta]*n)
    for j in range(N):
        for i in range(N):
            if i != j:
                L[i + N*j, i + N*j] -= epsilon*(rates[i]+rates[j])/2
    return L


def mean_time(L, rho):
    N = rho.shape[0]
    sol = np.linalg.solve(-L, rho.reshape(N*N, order='F'))
    return float(np.trace(sol.reshape((N, N), order='F')).real)


def coefficient(m, n, rho, alpha=1.0, beta=1.0):
    A, B = projectors(m, n)
    return float((((m - 1)/alpha)*np.trace(A @ rho) + (n/beta)*np.trace(B @ rho)).real)


def projected_dephasing(m, n, X, alpha=1.0, beta=1.0, eta=0.0):
    N = m+n
    A, B = projectors(m, n)
    P = A+B
    rates=np.array([eta]+[alpha]*(m-1)+[beta]*n)
    diagonal=np.diag(rates*np.diag(X))
    D=diagonal-0.5*(rates[:,None]*X+X*rates[None,:])
    return P @ D @ P


def exact_projected_check(m, n):
    # Rational arithmetic tests the critical projector identity without tolerance.
    k=m-1
    for l in (k, n):
        q=[[Fraction(int(i==j),1)-Fraction(1,l) for j in range(l)] for i in range(l)]
        if l==1:
            assert all(x == 0 for row in q for x in row)
            continue
        # sum diag(Q) * outer(Q_column_j,Q_row_j) - Q
        for a in range(l):
            for b in range(l):
                val=sum(q[j][j]*q[a][j]*q[j][b] for j in range(l))-q[a][b]
                assert val == -q[a][b]/l, (m,n,l,a,b,val)


def run():
    rng=np.random.default_rng(20261020)
    count_exact=count_spectral=count_asym=0
    worst=0.0
    for m in range(2, 8):
        for n in range(2, 8):
            exact_projected_check(m,n)
            count_exact+=2*(m+n) # individual pair-level rational assertions lower-bound
    for m in range(2,6):
        for n in range(2,6):
            N=m+n
            A,B=projectors(m,n)
            P=A+B
            assert np.linalg.norm(P@P-P) < 1e-12
            for Q,l,rate in [(A,m-1,0.6),(B,n,1.7)]:
                assert np.linalg.norm(projected_dephasing(m,n,Q,0.6,1.7,0.4)+rate*Q/l)<1e-12
                count_spectral+=1
            # The restricted dephasing operator is strictly dissipative.
            basis=[]
            eigvals, eigvecs = np.linalg.eigh(P)
            U=eigvecs[:,eigvals>0.5]
            for i in range(U.shape[1]):
                for j in range(U.shape[1]):
                    basis.append(np.outer(U[:,i],U[:,j]))
            if basis:
                M=np.array([[np.vdot(E,projected_dephasing(m,n,F)) for F in basis] for E in basis])
                assert np.linalg.eigvalsh((M+M.conj().T)/2).max() < -1e-9
                count_spectral+=1
            for gamma, alpha, beta, eta, J in [(0.5,1.0,1.0,0.0,1.0),(2.0,0.6,1.7,0.4,1.3)]:
                states=[]
                for a in (0,1,m):
                    z=np.zeros(N,dtype=complex); z[a]=1
                    states.append(np.outer(z,z.conj()))
                z=rng.normal(size=N)+1j*rng.normal(size=N)
                z=z/np.linalg.norm(z)
                states.append(np.outer(z,z.conj()))
                # One state in bright sector should have zero divergent term.
                z=np.zeros(N,dtype=complex);z[0]=0.3
                z[1:m]+=0.4/np.sqrt(m-1)
                z[m:]+=0.5/np.sqrt(n)
                z/=np.linalg.norm(z)
                states.append(np.outer(z,z.conj()))
                L=liouvillian(m,n,gamma,0.001,alpha,beta,eta,J)
                assert np.linalg.eigvals(L).real.max() < -1e-7
                count_spectral+=1
                for rho in states:
                    c=coefficient(m,n,rho,alpha,beta)
                    assert c>=-1e-12
                    empirical=0.001*mean_time(L,rho)
                    err=abs(empirical-c)
                    worst=max(worst,err)
                    assert err < 0.14, (m,n,gamma,alpha,beta,c,empirical,err)
                    count_asym+=1
    print(f'PASS rational assertions (lower bound): {count_exact}')
    print(f'PASS projected/spectral checks: {count_spectral}')
    print(f'PASS small-dephasing mean-time comparisons: {count_asym}')
    print(f'largest abs error of epsilon*T versus coefficient at epsilon=0.001: {worst:.8g}')
    print('Analytic proof required for all m,n and the epsilon->0 limit.')


if __name__ == '__main__':
    run()
