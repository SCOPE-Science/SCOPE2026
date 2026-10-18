"""Finite-dimensional independent checks of the alternating-dephasing ring theorem."""
import numpy as np
from scipy.linalg import eigvals, expm
import sympy as sp


def arrays(n, a, b, gamma=0.73):
    B = np.zeros((n, n), dtype=float)
    for j in range(n):
        B[j, j] = a[j]
        B[j, (j - 1) % n] = b[j]
    H = np.zeros((2*n, 2*n), dtype=float)
    H[:n, n:] = B
    H[n:, :n] = B.T
    I = np.eye(2*n)
    Li = -1j*(np.kron(I,H)-np.kron(H.T,I))
    for j in range(n):
        P = np.zeros((2*n,2*n)); P[j,j]=1
        Li += gamma*(np.kron(P,P)-0.5*(np.kron(I,P)+np.kron(P.T,I)))
    return B,H,Li


def dark_vector(B):
    u,s,vh = np.linalg.svd(B)
    d=vh[-1].astype(complex)
    d /= np.linalg.norm(d)
    return d


def test_case(n,a,b,singular):
    B,H,Li = arrays(n,a,b)
    should = np.prod(a) - ((-1)**n)*np.prod(b)
    assert abs(np.linalg.det(B) - should) < 1e-8*(1+abs(should))
    eig = eigvals(Li)
    nzero = sum(abs(eig)<1e-7)
    assert nzero == (2 if singular else 1), (n, singular, nzero)
    assert all((z.real < -1e-8 or abs(z)<1e-7) for z in eig), (n,max(z.real for z in eig))
    I=np.eye(2*n)
    assert np.linalg.norm(Li @ I.reshape(-1,order='F')) < 1e-9
    if singular:
        d=dark_vector(B)
        assert np.linalg.norm(B@d)<1e-9
        D=np.zeros((2*n,2*n),dtype=complex)
        D[n:,n:]=np.outer(d,d.conj())
        assert np.linalg.norm(Li @ D.reshape(-1,order='F'))<1e-9
        assert np.linalg.norm(Li.conj().T @ D.reshape(-1,order='F'))<1e-9
    return nzero


def check():
    for n in (3, 4):
        a = sp.symbols("a0:"+str(n)); b = sp.symbols("b0:"+str(n))
        T=sp.zeros(n)
        for j in range(n):
            T[j,j] = a[j]
            T[j,(j-1)%n] = b[j]
        identity = sp.factor(T.det() - (sp.prod(a)-(-1)**n*sp.prod(b)))
        assert identity == 0, (n,identity)
        print("checked symbolic determinant n=",n)
    cases = [
        (3,[1,1,1],[1,1,1],False),
        (4,[1,1,1,1],[1,1,1,1],True),
        (4,[1,1,1,1],[2,1,1,1],False),
        (4,[1,2,3,4],[3,2,4,2],False),
        (5,[1]*5,[1]*5,False),
        (6,[1]*6,[2,0.5,0.5,0.5,2,2],True),
        (6,[1]*6,[2,0.5,0.5,0.5,2,1],False),
    ]
    for n,a,b,expected in cases:
        if n==6:
            # One sample may be deliberately unbalanced: identify from the product.
            expected = abs(np.prod(a)-np.prod(b))<1e-10
        print('checked n=',n,'resonant=',expected,'kernel=',test_case(n,a,b,expected))
    # Independently evolve an initial site projector to check the full limiting state.
    n = 4
    B,H,Li = arrays(n, [1]*n, [2, .5, .5, 2])
    d = dark_vector(B)
    D = np.zeros((2*n,2*n), dtype=complex)
    D[n:,n:] = np.outer(d,d.conj())
    initial = np.zeros((2*n,2*n),dtype=complex)
    initial[n,n] = 1
    p = float(abs(d[0])**2)
    predicted = p*D+(1-p)*(np.eye(2*n)-D)/(2*n-1)
    actual = (expm(200*Li) @ initial.reshape(-1,order='F')).reshape((2*n,2*n),order='F')
    assert np.linalg.norm(actual-predicted) < 1e-8
    print('checked direct dynamical limit n=4')
    for n in [4,6,8,12,16]:
        m=n//2
        q=0.5
        a=np.ones(n); b=np.array([1/q]+[q]*m+[1/q]*(m-1))
        B=np.zeros((n,n))
        for j in range(n): B[j,j]=a[j];B[j,(j-1)%n]=b[j]
        d=np.array([(-1)**j*q**min(j,n-j) for j in range(n)])
        assert np.linalg.norm(B@d)<1e-12
        Z=1+2*sum(q**(2*k) for k in range(1,m))+q**(2*m)
        assert abs(np.dot(d,d)-Z)<1e-12
        p=1/Z
        assert abs(p-(1-q*q)/(1+q*q)) < 2*q**n
        print('local n=',n,'p=',p,'return=',p*p+(1-p)**2/(2*n-1))
    print('ALL CHECKS PASSED')

if __name__=='__main__': check()
