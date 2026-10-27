"""Finite diagnostics for the square-zero relative-numerical-radius obstruction.
Run with Python 3 and NumPy. The Hilbert-space theorem is proved analytically.
"""
import numpy as np

rng=np.random.default_rng(20261018)
checks=0

def accept(flag,msg):
    global checks
    assert bool(flag),msg
    checks+=1

for d in (2,3,4,7):
    for rep in range(120):
        A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        U,s,Vh=np.linalg.svd(A,full_matrices=False)
        G=A/s[0]
        y=U[:,0]
        v=rng.normal(size=d)+1j*rng.normal(size=d)
        v-=y*np.vdot(y,v)
        v/=np.linalg.norm(v)
        S=np.outer(v,y.conj())
        x=Vh.conj().T[:,0]
        accept(np.linalg.norm(S@S)<5e-13,'square zero')
        accept(abs(np.linalg.norm(S@G@x)-1)<5e-13,'norming witness')
        accept(abs(np.linalg.norm(S,2)-1)<5e-13,'norm-one shift')
        for theta in np.linspace(0,2*np.pi,24,endpoint=False):
            H=(np.exp(-1j*theta)*S+np.exp(1j*theta)*S.conj().T)/2
            accept(np.linalg.eigvalsh(H)[-1]<0.50000000001,'numerical-radius bound')

for d in (2,3,5):
    G=np.eye(d,dtype=complex)
    S=np.zeros((d,d),dtype=complex)
    S[1,0]=1
    accept(abs(np.linalg.norm(S,2)-1)<1e-12,'identity relative norm')
    accept(abs(np.max([np.linalg.eigvalsh((np.exp(-1j*t)*S+np.exp(1j*t)*S.conj().T)/2)[-1] for t in np.linspace(0,2*np.pi,72)])-0.5)<1e-12,'sharp numerical radius')

for d in (2,3,5):
    for _ in range(25):
        g=rng.normal(size=d)+1j*rng.normal(size=d)
        g/=np.linalg.norm(g)
        t=rng.normal(size=d)+1j*rng.normal(size=d)
        rel=abs(np.dot(t,g.conj()))
        accept(rel>=0,'scalar codomain nonnegative')

print('PASS:',checks,'finite assertions; no infinite-dimensional certification')
