"""Reproducible numerical cross-checks for nonnegative finite cyclic Gabor rigidity.

This script checks the exact finite Fourier block formula and the dimension-free
stability estimate on independently constructed Gabor frame matrices. The proof
for arbitrary dimensions is analytic and is given in RESULT.md.
"""
import numpy as np

COUNT=0

def verify(cond, message):
    global COUNT
    assert bool(cond), message
    COUNT+=1

def gram(p,q,g):
    n=p*q
    j=np.arange(n)
    cols=[]
    for a in range(p):
        shifted=np.roll(g,q*a)
        for b in range(q):
            cols.append(shifted*np.exp(2j*np.pi*p*b*j/n))
    G=np.column_stack(cols)
    return G.conj().T@G

def block_eigs(p,q,g):
    out=[]
    for u in range(q):
        h=np.array([g[u+q*t] for t in range(p)])
        out.extend(q*np.abs(np.fft.fft(h))**2)
    return np.sort(np.array(out))

def closest_transversal(p,q,g):
    a=np.zeros(p*q)
    for u in range(q):
        z=np.array([g[u+q*t] for t in range(p)])
        k=np.argmax(z)
        a[u+q*k]=1/np.sqrt(q)
    return a

rng=np.random.default_rng(20260515)
for p in range(2,8):
    for q in range(1,7):
        n=p*q
        for trial in range(3):
            raw=rng.random(n)
            g=raw/np.linalg.norm(raw)
            ev=np.linalg.eigvalsh(gram(p,q,g))
            ev2=block_eigs(p,q,g)
            verify(np.max(np.abs(ev-ev2))<2e-11,f'block formula {p},{q}')
        for trial in range(3):
            idx=rng.integers(0,p,size=q)
            h=np.zeros(n)
            for u,k in enumerate(idx):h[u+q*k]=1/np.sqrt(q)
            verify(np.linalg.norm(gram(p,q,h)-np.eye(n),ord=2)<3e-11,
                   f'exact transversal {p},{q}')
            for e in (0.001,0.008,0.03):
                w=h.copy()
                for u,k in enumerate(idx):w[u+q*((k+1)%p)]+=e/np.sqrt(q)
                w/=np.linalg.norm(w)
                ev=block_eigs(p,q,w)
                delta=np.max(np.abs(ev-1))
                if delta<=.1+1e-10:
                    d=np.linalg.norm(w-closest_transversal(p,q,w))
                    verify(d <= (4/3)*delta+2e-12,f'stability {p},{q},{e}')
for p in (2,3,5):
    for q in (1,2,5):
        for t in (1e-3,2e-3,5e-3,1e-2):
            a=np.sqrt(1-t*t)
            g=np.zeros(p*q)
            for u in range(q):
                g[u]=a/np.sqrt(q)
                g[u+q]=t/np.sqrt(q)
            ev=block_eigs(p,q,g)
            delta=np.max(np.abs(ev-1))
            d=np.linalg.norm(g-closest_transversal(p,q,g))
            verify(d>delta/3.5 and d<1.5*delta, 'linear witness')
print('CHECK_OK',COUNT)
