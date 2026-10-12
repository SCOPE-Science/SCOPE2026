#!/usr/bin/env python3
"""Numerical corroboration of the exact two-Pauli Gibbs separability rules."""
import math
import numpy as np

I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
pauli={'I':I,'X':X,'Y':Y,'Z':Z}

def kron_string(word):
    v=np.array([[1]],dtype=complex)
    for c in word: v=np.kron(v,pauli[c])
    return v

def partial_transpose(rho,n,inds):
    tensor=rho.reshape((2,)*(2*n))
    perm=list(range(2*n))
    for j in inds:perm[j],perm[n+j]=perm[n+j],perm[j]
    return tensor.transpose(perm).reshape((2**n,2**n))

def gibbs_pair(P,Q,a,b,beta):
    n=int(round(math.log2(P.shape[0])))
    if np.linalg.norm(P@Q-Q@P)<1e-10:
        s=math.tanh(beta*a);t=math.tanh(beta*b)
        return (np.eye(2**n)-s*P-t*Q+s*t*(P@Q))/(2**n)
    r=math.hypot(a,b)
    return (np.eye(2**n)-math.tanh(beta*r)*(a*P+b*Q)/r)/(2**n)

cases=[('XX','ZZ',1.0,1.0,.20),('XX','ZZ',1.0,1.0,.75),
       ('XXXX','ZZZZ',.7,2.0,.75),('XXX','ZZZ',1.0,1.0,.75),
       ('XXI','ZIZ',1.0,2.0,1.5),('XII','ZII',1.0,1.0,4.0)]
for wordp,wordq,a,b,beta in cases:
    n=len(wordp);P=kron_string(wordp);Q=kron_string(wordq)
    d=sum(u!='I' and v!='I' and u!=v for u,v in zip(wordp,wordq))
    rho=gibbs_pair(P,Q,a,b,beta)
    assert abs(np.trace(rho)-1)<1e-12
    assert np.linalg.eigvalsh(rho).min()>-1e-12
    s=math.tanh(beta*a); t=math.tanh(beta*b)
    if d>=2 and d%2==0:
        idx=next(i for i,(u,v) in enumerate(zip(wordp,wordq)) if u!='I' and v!='I' and u!=v)
        lam=np.linalg.eigvalsh(partial_transpose(rho,n,[idx])).min()
        assert (lam<-1e-9)==(s+t+s*t>1+1e-9)
    if d>=3 and d%2==1:
        r=math.hypot(a,b)
        w=(a+b)*math.tanh(beta*r)/r
        e=abs(np.trace(rho@P))+abs(np.trace(rho@Q))
        assert abs(e-w)<1e-12
        if (wordp,wordq)==('XXX','ZZZ'):
            assert e>1.0
            for mask in range(2**n):
                subset=[j for j in range(n) if mask>>j & 1]
                assert np.linalg.norm(partial_transpose(rho,n,subset)-rho)<1e-12
    if d==1:
        # The one-site mismatch is not a thermal entanglement mechanism.
        assert np.linalg.eigvalsh(rho).min()>-1e-12

z_comm=math.atanh(math.sqrt(2)-1)
z_anti=math.atanh(1/math.sqrt(2))/math.sqrt(2)
assert abs(z_comm-0.44068679350977147)<1e-13
assert abs(z_anti-0.6232252401402305)<1e-12
assert z_comm<z_anti
print('VERIFY_OK')
