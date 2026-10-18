"""Independent finite-matrix checks of two-boson onsite-loss dark modes."""
import itertools
import numpy as np
from scipy.linalg import eigh, null_space


def verify(n):
    pairs = [(a, b) for a in range(n) for b in range(a, n)]
    index = {p: k for k, p in enumerate(pairs)}
    size = len(pairs)
    h = np.zeros((size, size))
    for col, (a,b) in enumerate(pairs):
        occ = [0]*n
        occ[a] += 1
        occ[b] += 1
        for src in range(n):
            if occ[src] == 0:
                continue
            for dst in ((src-1)%n, (src+1)%n):
                if dst == src:
                    continue
                new = occ.copy()
                new[src] -= 1
                factor = np.sqrt(occ[src]*(occ[dst]+1))
                new[dst] += 1
                ends = [i for i, x in enumerate(new) for _ in range(x)]
                row = index[tuple(ends)]
                h[row,col] += factor
    assert np.allclose(h,h.T)
    p = np.diag([int(a==b) for a,b in pairs])
    eig, u = eigh(h)
    dark = np.zeros((size,0),dtype=complex)
    i=0
    while i<size:
        j=i+1
        while j<size and abs(eig[j]-eig[i])<1e-7:
            j+=1
        a=u[:,i:j]
        null = null_space(p@a, rcond=1e-9)
        if null.shape[1]:
            dark = np.column_stack([dark,a@null])
        i=j
    expected_dim=(n//2 - (n%4==2)) if n%2==0 else 0
    assert dark.shape[1]==expected_dim, (n,dark.shape[1],expected_dim)
    proj=dark@dark.conj().T
    checks=0
    for a,b in pairs:
        got=proj[index[a,b],index[a,b]].real
        if a==b or n%2:
            want=0
        elif (b-a)==n//2:
            want=2/n if n%4==0 else 0
        else:
            want=1/n
        assert abs(got-want)<2e-8, (n,a,b,got,want)
        checks+=1
    return checks

if __name__=='__main__':
    checks=0
    for n in range(3,13):
        k=verify(n)
        print(f'n={n}: {k} basis-state checks PASS')
        checks+=k
    print(f'PASS: {checks} normalized two-boson basis-state survival probabilities, ten dark-space ranks')
