import itertools, math, numpy as np
from scipy.linalg import expm

def formula(p,i,j):
    if (i+j)%2==0: return 0.0
    delta_sum = int(i+j==p)
    b = int(j-i==1) - int(j-i==3) + int(i+j in (3,2*p-3))
    return (2+delta_sum-0.5*b*b)/p

def graph(p):
    sites = tuple(itertools.combinations(range(1,p), 2))
    idx = {t: k for k,t in enumerate(sites)}
    H=np.zeros((len(sites),len(sites)))
    for (i,j),k in idx.items():
        for t in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if t in idx: H[k,idx[t]]=1
    return sites,idx,H

suites=0; states=0; overlap=0; nonherm=0; gap_min=float('inf')
for p in (5,7,11,13,17,19):
    sites,idx,H=graph(p)
    e,U=np.linalg.eigh(H)
    zero = np.abs(e)<1e-8
    assert np.count_nonzero(zero)==(p-1)//2
    # Independently build entire dark space from *every* distinct energy.
    Pdark=np.zeros_like(H)
    groups=[]
    for e0 in e:
        if not groups or abs(e0-groups[-1][-1])>1e-8:groups.append([e0])
        else:groups[-1].append(e0)
    ss=np.eye(len(sites))[:,idx[(1,2)]]
    j=0
    for g in groups:
        P=U[:,j:j+len(g)]@U[:,j:j+len(g)].T
        v=P@ss
        vv=v@v
        if vv>1e-11:P-=np.outer(v,v)/vv
        Pdark+=P
        j+=len(g)
    assert np.linalg.norm(Pdark@Pdark-Pdark)<1e-8
    assert np.linalg.norm(Pdark@H-H@Pdark)<1e-8
    assert np.linalg.norm(Pdark@ss)<1e-8
    assert abs(np.trace(Pdark)-(p-3)/2)<1e-8
    for (i,j),k in idx.items():
        overlap=max(overlap,abs(Pdark[k,k]-formula(p,i,j)))
        assert abs(Pdark[k,k]-formula(p,i,j))<3e-12,(p,i,j,Pdark[k,k],formula(p,i,j))
        states+=1
    suites+=1
    if p<=7:
        for kappa in (.5,2.):
            K=H.astype(complex)-.5j*kappa*np.outer(ss,ss)
            for tim in (500.,30000.):
                V=expm(-1j*K*tim)
                sample=V.conj().T@V
                err=np.max(np.abs(np.diag(sample).real - np.diag(Pdark)))
                print('time',p,kappa,tim,'max_err',err)
                if tim==30000:
                    assert err<1e-3,(p,kappa,tim,err)
                nonherm+=len(sites)
print('VERIFY_OK', 'primes',suites, 'states',states, 'time_state_checks',nonherm, 'max_formula_error',overlap)
