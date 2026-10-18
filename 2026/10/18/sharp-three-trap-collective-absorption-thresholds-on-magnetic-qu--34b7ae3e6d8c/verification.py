"""Independent finite-dimensional verification of flux-cycle arbitrary sink-set claim."""
import itertools
import math
import numpy as np


def predicted(n, trap_set, phi):
    t0=trap_set[0]
    ds=[(t-t0)%n for t in trap_set]
    g=math.gcd(n,*ds)
    h=math.gcd(n,*[2*d for d in ds])
    p=phi % (2*math.pi)
    result=np.zeros(n)
    if abs(p)<1e-9:
        for x in range(n):
            if (2*(x-t0))%h:
                result[x]=h/(2*n)
        return (h-1)//2,result
    if abs(p-math.pi)<1e-9 and (n//g)%2:
        for x in range(n):
            y=x-t0
            if y%g:
                result[x]=g/n if (g%2==0 and (2*y)%g==0) else g/(2*n)
        return g//2,result
    return 0,result


def spectral(n,trap_set,phi):
    H=np.zeros((n,n),dtype=complex)
    for j in range(n):
        H[(j+1)%n,j]=np.exp(1j*phi/n)
        H[j,(j+1)%n]=np.exp(-1j*phi/n)
    ev,U=np.linalg.eigh(H)
    total=np.zeros(n)
    dim=0
    i=0
    while i<n:
        k=i+1
        while k<n and abs(ev[k]-ev[i])<1e-8:k+=1
        v=U[:,i:k]
        _,s,vh=np.linalg.svd(v[list(trap_set),:],full_matrices=True)
        null=vh.conj().T[:,np.count_nonzero(s>1e-8):]
        total+=np.sum(abs(v@null)**2,axis=1)
        dim+=null.shape[1]
        i=k
    return dim,total


def run():
    rng=np.random.default_rng(834531)
    ncase=0
    nprob=0
    for n in range(3,29):
        if n<=10:
            masks=(i for i in range(1, 1<<n) if i.bit_count()<n)
            sets=([j for j in range(n) if mask>>j&1] for mask in masks)
        else:
            sets=(sorted(rng.choice(n,size=int(rng.integers(1,n)),replace=False).tolist()) for _ in range(70))
        for trap_set in sets:
            for phi in (0.,math.pi,0.31):
                d1,p1=predicted(n,trap_set,phi)
                d2,p2=spectral(n,trap_set,phi)
                if d1!=d2 or not np.allclose(p1,p2,atol=1e-8,rtol=0):
                    raise AssertionError((n,trap_set,phi,d1,d2, np.max(abs(p1-p2))))
                ncase+=1
                nprob+=n
    print('PASS:',ncase,'full spectral checks,',nprob,'site probabilities')

if __name__ == '__main__':
    run()


def verify_sharp_examples_and_finite_cutoffs():
    # These finite checks complement, but do not replace, the CRT proof.
    for n, traps in ((60, (0,3,5)), (105, (0,3,10))):
        for phi in (0., math.pi, 0.31):
            for sinks in ((traps[0],traps[1]), (traps[0],traps[2]),
                          (traps[1],traps[2]), traps):
                dim, probs = predicted(n,sinks,phi)
                sdim, sprob = spectral(n,sinks,phi)
                assert dim == sdim
                assert np.allclose(probs,sprob,rtol=0,atol=2e-8)
    for mode, first in ((0.,60),(math.pi,105)):
        for n in range(3,first):
            if mode == math.pi and n % 2 == 0:
                # Even cycles are excluded analytically by the 2-adic condition.
                continue
            for b in range(1,n):
                if predicted(n,(0,b),mode)[0] == 0: continue
                for c in range(b+1,n):
                    if predicted(n,(0,c),mode)[0] == 0: continue
                    if predicted(n,(b,c),mode)[0] == 0: continue
                    assert predicted(n,(0,b,c),mode)[0] > 0
    print('PASS: n=60 and n=105 sharp three-sink examples and bounded cutoff scans')

if __name__ == '__main__':
    verify_sharp_examples_and_finite_cutoffs()
