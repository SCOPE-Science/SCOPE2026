"""Finite checks of renewal resetting and the exact propagator criterion.

The mathematical theorem is proved analytically in RESULT.md. These computations
check its normalization, signs, operator formula, and illustrative examples.
"""
import numpy as np

RNG = np.random.default_rng(401926)
ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def rand_unitary(d):
    a=RNG.normal(size=(d,d))+1j*RNG.normal(size=(d,d))
    q,r=np.linalg.qr(a)
    return q @ np.diag(np.conj(np.diag(r))/np.abs(np.diag(r)))


def rand_density(d, pure=False):
    if pure:
        a=RNG.normal(size=d)+1j*RNG.normal(size=d)
        a/=np.linalg.norm(a)
        return np.outer(a,a.conj())
    a=RNG.normal(size=(d,d))+1j*RNG.normal(size=(d,d))
    out=a @ a.conj().T
    return out / np.trace(out)


def moments(hazard, unitary, rho):
    # Time parameter starts with time zero and hazard[0] = first-age hazard.
    tmax=len(hazard)
    d=len(rho)
    S=np.ones(tmax+1)
    for t in range(1,tmax+1):
        S[t]=S[t-1]*(1-hazard[t-1])
    first=np.array([S[t-1]*hazard[t-1] for t in range(1,tmax+1)])
    event=np.zeros(tmax+1)
    for t in range(1,tmax+1):
        event[t]=first[t-1]+sum(first[k-1]*event[t-k] for k in range(1,t))
    powers=[np.linalg.matrix_power(unitary,j) for j in range(tmax+1)]
    A=[np.zeros((d,d),dtype=complex)]
    for t in range(1,tmax+1):
        out=np.zeros((d,d),dtype=complex)
        for s in range(1,t+1):
            v=powers[t-s]
            out+=event[s]*S[t-s]*(v@rho@v.conj().T)
        A.append(out)
    return S,event,A,powers


def direct(t,hazard,U,rho,initial):
    # Independently enumerate all reset/no-reset histories with their ages.
    # Branch weights are included in subnormalized states.
    history=[(0,initial.copy())]
    for clock in range(t):
        newer=[]
        for age,x in history:
            hz=hazard[age]
            newer.append((age+1,(1-hz)*U@x@U.conj().T))
            newer.append((0,hz*np.trace(x)*rho))
        history=newer
    return sum((x for _,x in history),np.zeros_like(initial))


def choi_of_affine(a,U,Q):
    d=len(U)
    choi=np.zeros((d*d,d*d),dtype=complex)
    for i in range(d):
        for j in range(d):
            e=np.zeros((d,d),dtype=complex); e[i,j]=1
            m=a*(U@e@U.conj().T)
            if i==j: m=m+Q
            choi+=np.kron(e,m)
    return choi


def small_check(hazard,d,pure):
    U=rand_unitary(d)
    rho=rand_density(d,pure=pure)
    S,ev,A,up=moments(hazard,U,rho)
    for t in range(len(S)):
        check(abs(np.trace(A[t])-(1-S[t]))<1e-11,"renewal trace")
        check(np.linalg.eigvalsh(A[t]).min()>-1e-11,"renewal positivity")
        check(abs(S[t]+np.trace(A[t])-1)<1e-11,"map TP")
    for t in range(len(hazard)+1):
        x=rand_density(d)
        model=S[t]*up[t]@x@up[t].conj().T+A[t]
        observed=direct(t,hazard,U,rho,x)
        check(np.linalg.norm(model-observed)<1e-11,"event-path independent enumeration")
    for t in range(1,len(S)):
        a=S[t]/S[t-1]
        V=U
        Q=A[t]-a*V@A[t-1]@V.conj().T
        check(abs(np.trace(Q)-(1-a))<1e-11,"intertwining normalization")
        for _ in range(2):
            x=rand_density(d)
            y=S[t-1]*up[t-1]@x@up[t-1].conj().T+A[t-1]
            target=S[t]*up[t]@x@up[t].conj().T+A[t]
            recovered=a*V@y@V.conj().T+Q
            check(np.linalg.norm(recovered-target)<1e-11,"intertwiner composition")
        c=choi_of_affine(a,U,Q)
        is_Q_positive=np.linalg.eigvalsh(Q).min()>=-1e-10
        is_CP=np.linalg.eigvalsh(c).min()>=-1e-10
        check(is_Q_positive==is_CP,"Q positivity iff Choi CP")
        if np.all(np.diff(hazard)>=-1e-12):
            check(is_Q_positive,"monotone hazard guarantee")
        # Check explicit hazard-coefficient representation.
        rec=ev[t]*rho.copy()
        for s in range(1,t):
            j=t-s
            rec+=ev[s]*S[j-1]*(hazard[t-1]-hazard[j-1])*up[j]@rho@up[j].conj().T
        check(np.linalg.norm(rec-Q)<1e-11,"hazard-difference formula")


for d in (2,3,4):
    for _ in range(42):
        hh=RNG.uniform(.015,.82,size=5)
        small_check(hh,d,False)
        small_check(np.sort(hh),d,True)

# An analytic two-step obstruction for decreasing hazard with orthogonal
# reset-state rotation. The negative eigenvalue is p1*(p2-p1).
U=np.array([[0,1],[1,0]],dtype=complex)
rho=np.diag([1.,0.]).astype(complex)
for p1,p2 in [(.6,.15),(.8,.05),(.4,.0),(.9,.6),(.3,.299)]:
    S,events,A,up=moments([p1,p2],U,rho)
    a=S[2]/S[1]
    Q=A[2]-a*U@A[1]@U.conj().T
    check(np.linalg.norm(Q-np.diag([(1-p1)*p2+p1*p1,p1*(p2-p1)]))<1e-12,"two-step exact diagonal")
    check(abs(np.linalg.eigvalsh(Q).min()-p1*(p2-p1))<1e-12,"negative eigenvalue")
    check(np.linalg.eigvalsh(choi_of_affine(a,U,Q)).min()<0,"Choi not positive")
    check(abs(S[2]/S[1]-(1-p2))<1e-12,"trace distance shrinks")

# The increasing age-hazard profile r_j=min(.08,.001(j-1)) appears as the
# first nonstationary protocol in Carollo-Wald (arXiv:2601.13367).
hz=np.array([min(.08,.001*j) for j in range(100)])
for d in (2,3,4):
    U=rand_unitary(d);rho=rand_density(d,pure=True)
    S,events,A,up=moments(hz,U,rho)
    for t in range(1,len(S)):
        a=S[t]/S[t-1]
        Q=A[t]-a*U@A[t-1]@U.conj().T
        check(np.linalg.eigvalsh(Q).min()>-2e-11,"linear-ramp CP divisibility")

print("PASS",ASSERTIONS,"finite assertions")
