"""Deterministic independent finite-dimensional checks of a renewal-reset dual-map identity.

Uses column vectorization of matrices and independently composes the Heisenberg
maps, comparing their inverse intertwiner to a closed expression. No
simulation is taken as a proof for arbitrary times or Hilbert dimensions.
"""
import numpy as np
from numpy.linalg import inv, eigvalsh, norm


def renewal(h):
    N=len(h)
    S=np.ones(N+1)
    for t in range(1,N+1): S[t]=S[t-1]*(1-h[t-1])
    nu=np.zeros(N+1)
    for t in range(1,N+1):
        nu[t]=h[t-1]*S[t-1]+sum(nu[s]*S[t-1-s]*h[t-s-1] for s in range(1,t))
    return S,nu


def superop(fn,d):
    A=np.zeros((d*d,d*d),complex)
    for j in range(d):
        for i in range(d):
            E=np.zeros((d,d),complex);E[i,j]=1
            A[:,i+d*j]=fn(E).reshape(-1,order='F')
    return A


def family(h,U,rho):
    d=U.shape[0];N=len(h)
    S,nu=renewal(h)
    P=[np.linalg.matrix_power(U,j) for j in range(N+1)]
    sigmas=[P[j]@rho@P[j].conj().T for j in range(N+1)]
    B=[np.zeros((d,d),complex)]
    for t in range(1,N+1):
        B.append(sum((nu[t-j]*S[j]*sigmas[j] for j in range(t)),np.zeros((d,d),complex)))
    return S,nu,P,B


def check(h,U,rho):
    S,nu,P,B=family(h,U,rho);d=U.shape[0]
    I=np.eye(d);Aprev=superop(lambda X:X,d)
    errors=[];min_ev=[]
    for t in range(1,len(h)+1):
        Ut=P[t]
        A=superop(lambda X:S[t]*Ut.conj().T@X@Ut+np.trace(B[t]@X)*I,d)
        Psi=A@inv(Aprev)
        k=S[t]/S[t-1]
        F=P[t-1].conj().T@(B[t]-B[t-1])@P[t-1]/S[t-1]
        Pdelta=U.conj().T
        pred=superop(lambda X:k*Pdelta@X@U+np.trace(F@X)*I,d)
        errors.append(norm(Psi-pred))
        min_ev.append(eigvalsh(F).min())
        Aprev=A
    return S,nu,errors,min_ev


def unitary(d,seed):
    rng=np.random.default_rng(seed)
    Q,R=np.linalg.qr(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))
    return Q@np.diag(np.diag(R)/np.abs(np.diag(R)))


def main():
    checks=0
    for d in (2,3,4):
        U=unitary(d,d+17)
        rho=np.diag(np.arange(1,d+1)/sum(range(1,d+1)))
        for h in ([.1,.2,.3,.4,.5],[.1,.9,.91,.92,.93],[.3,.1,.25,.4,.3],[.2]*5):
            S,nu,errs,vals=check(h,U,rho)
            assert max(errs)<1e-9,(d,h,errs)
            assert abs(sum((nu[len(h)-j]*S[j] for j in range(len(h))))+S[-1]-1)<1e-14
            checks+=len(errs)+1
    # A strictly increasing hazard with a negative dual intermediate at step 3.
    h=[.1,.9,.91]
    U=np.roll(np.eye(3),1,axis=0)
    rho=np.diag([1.,0.,0.])
    S,nu,errors,mins=check(h,U,rho)
    assert nu[1] == .1
    assert abs(nu[2]-.82)<1e-12
    assert abs(nu[3]-.2449)<1e-12
    assert abs(mins[2]-(nu[3]-nu[2])/S[2])<1e-12,(mins,nu,S)
    assert mins[2]<-.6
    checks+=7
    # Cyclic witness for arbitrary selected later decreases in renewal mass.
    for d in (3,4,5,6):
        U=np.roll(np.eye(d),1,axis=0)
        rho=np.diag([1.]+[0.]*(d-1))
        h=[.15,.75,.78,.79,.82,.83][:d]
        S,nu,errs,mins=check(h,U,rho)
        assert max(errs)<1e-8
        for t in range(2,d+1):
            if nu[t]<nu[t-1]:
                assert mins[t-1] <= (nu[t]-nu[t-1])/S[t-1]+1e-12
                checks+=1
        checks+=1
    print('PASS',checks,'independent deterministic finite-matrix comparisons')
    print('strictly increasing hazard',h[:3], 'example renewal probabilities',np.round(nu[:4],6))
    print('specific example nu=[0,0.1,0.82,0.2449], negative eigenvalue',(0.2449-0.82)/(.9*.1))

if __name__=='__main__': main()
