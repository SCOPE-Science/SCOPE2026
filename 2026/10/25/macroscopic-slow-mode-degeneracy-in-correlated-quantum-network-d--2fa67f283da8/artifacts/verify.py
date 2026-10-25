"""Independent finite-dimensional checks of the stated Lindblad eigenspaces."""
import numpy as np
from scipy.linalg import eigvals


def build(n, kappa, J=1.0, dt=0.013, xi=0.5):
    N = 2*n
    eye = np.eye(N)
    u = np.ones(N)
    s = np.r_[np.ones(n), -np.ones(n)]
    S = np.outer(u, u)-eye
    Q = np.outer(s, s)-eye

    def diss(V):
        W = V@V
        return np.kron(V, V)-0.5*(np.kron(eye, W)+np.kron(W.T, eye))

    independent = np.zeros((N*N, N*N))
    for i in range(N):
        for j in range(i+1, N):
            V = np.zeros((N, N))
            V[i, j] = V[j, i] = 1
            independent += diss(V)
    a = J*J*dt*xi*(1-xi)*(1-kappa*kappa)
    b = J*J*dt*xi*(1-xi)*kappa*kappa
    H = J*xi*S
    generator = (-1j*(np.kron(eye, H)-np.kron(H.T, eye))
                 +a*independent+b*diss(Q))
    return generator, independent, a, s


def expected_dimension(n, kappa):
    N=2*n
    if kappa == 0:
        return (N-1)*(N-2)//2
    return (n-1)*(2*n-3) if n >= 3 else 3


def constrained_space(n, kappa):
    N=2*n
    pairs=[(i,j) for i in range(N) for j in range(i+1,N)]
    u=np.ones(N)
    s=np.r_[np.ones(n),-np.ones(n)]
    columns=[]
    for i,j in pairs:
        E=np.zeros((N,N)); E[i,j]=E[j,i]=1
        c=list((E@u)[1:]-(E@u)[0])
        if kappa > 0:
            x=(E@s)/s
            c+=list(x[1:]-x[0])
        columns.append(c)
    M=np.array(columns).T
    rank=np.linalg.matrix_rank(M, tol=1e-10)
    return len(pairs)-rank


def test():
    checks=0
    for n in (2,3,4):
        for kappa in (0.0,0.5,0.9):
            N=2*n
            L,D,a,s=build(n,kappa)
            spectrum=eigvals(L)
            gamma=a*(N-2)
            assert np.count_nonzero(np.abs(spectrum)<1e-8)==1
            assert np.all(spectrum.real <= 1e-8)
            assert np.count_nonzero(spectrum.real > 1e-8)==0
            assert abs(min(-x.real for x in spectrum if abs(x)>1e-8)-gamma)<1e-8
            multiplicity=np.count_nonzero(np.abs(spectrum+gamma)<1e-8)
            target=expected_dimension(n,kappa)
            assert multiplicity==target,(N,kappa,multiplicity,target)
            assert constrained_space(n,kappa)==target
            g=np.sort(np.linalg.eigvalsh(D))
            predicted=np.sort(np.r_[0.0,np.full(N*(N-1)//2,-(N-2.)),
                                      np.full(N*(N-1)//2+N-1,-float(N))])
            assert np.allclose(g,predicted)
            u=np.ones(N)
            P_u=np.outer(u,u)/N
            P_s=np.outer(s,s)/N
            R=P_u-P_s
            assert np.linalg.norm(L@R.reshape(-1,order='F')+gamma*R.reshape(-1,order='F'))<1e-9
            checks+=7
            print(f'N={N}, kappa={kappa}, rate={gamma:.9g}, multiplicity={multiplicity}: passed')
    print(f'PASS: {checks} assertions in 9 full-Liouvillian cases')


if __name__=='__main__':
    test()
