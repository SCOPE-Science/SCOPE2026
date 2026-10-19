"""Independent finite-dimensional checks for average mixing on dimerized flux rings.
Requires Python 3 and NumPy. Run: python verify.py
All calculations are finite corroborations, not proofs of the all-order theorem.
"""
import math
import numpy as np

TOL = 1e-8


def exact_model(m, a, b, phi):
    n = 2 * m
    H = np.zeros((n, n), dtype=complex)
    for j in range(m):
        A, B, A_next = 2*j, 2*j+1, 2*((j+1) % m)
        H[A, B] += a
        H[B, A] += a
        v = b * np.exp(1j * phi/m)
        H[A_next, B] += v
        H[B, A_next] += v.conjugate()
    return H


def average_mixing(eigenvalues, vectors):
    n = len(eigenvalues)
    used = np.zeros(n, dtype=bool)
    M = np.zeros((n, n), dtype=float)
    for i in range(n):
        if used[i]:
            continue
        inds = [j for j in range(n) if abs(eigenvalues[j]-eigenvalues[i]) < TOL]
        used[inds] = True
        P = vectors[:, inds] @ vectors[:, inds].conj().T
        M += np.abs(P)**2
    return M


def bloch_mixing(m, a, b, phi):
    n = 2*m
    modes = []
    levels = []
    for j in range(m):
        z = a+b*np.exp(1j*(phi+2*math.pi*j)/m)
        r = abs(z)
        omega = np.exp(-2j*math.pi*j*np.arange(m)/m)
        if r < 1e-10:
            va = np.zeros(n, complex)
            vb = np.zeros(n, complex)
            va[::2] = omega / math.sqrt(m)
            vb[1::2] = omega / math.sqrt(m)
            modes.extend((va, vb))
            levels.extend((0.0, 0.0))
        else:
            for sigma in (-1, 1):
                v = np.empty(n, complex)
                v[::2] = omega / math.sqrt(2*m)
                v[1::2] = sigma*np.conj(z)/r * omega / math.sqrt(2*m)
                modes.append(v)
                levels.append(sigma*r)
    return average_mixing(np.array(levels), np.column_stack(modes))


def predicted_rank(m, a, b, phi):
    flux = phi % (2*math.pi)
    iszero = min(flux,2*math.pi-flux)<1e-10
    ispi = abs(flux-math.pi)<1e-10
    if not (iszero or ispi):
        return 1
    equal = abs(a-b)<1e-10
    if m % 2 == 1:
        return m + int(ispi and equal)
    return m-1 + (2 if ispi else int(equal))


def main():
    profiles=0
    matrix_entries=0
    max_deviation=0.0
    cases=( (1.,1.),(1.,2.),(2.,1.),(2.,3.),(3.,3.) )
    fluxes=(0.0,math.pi,0.37,1.7,4.6)
    for m in range(2,12):
      for a,b in cases:
       for phi in fluxes:
        H=exact_model(m,a,b,phi)
        assert np.linalg.norm(H-H.conj().T)<1e-12
        vals,vec=np.linalg.eigh(H)
        M=average_mixing(vals,vec)
        N=bloch_mixing(m,a,b,phi)
        dev=float(np.max(np.abs(M-N)))
        max_deviation=max(dev,max_deviation)
        if dev>3e-8:raise AssertionError((m,a,b,phi,'entry',dev))
        expected=predicted_rank(m,a,b,phi)
        eig=np.linalg.eigvalsh(M)
        rank=int(np.sum(eig>1e-7))
        if rank!=expected:raise AssertionError((m,a,b,phi,'rank',rank,expected,eig))
        if np.linalg.norm(M.sum(axis=1)-1.,np.inf)>2e-8:
            raise AssertionError('row sums')
        if phi not in (0,math.pi):
            if np.max(np.abs(M-1/(2*m)))>3e-8:
                raise AssertionError('generic flux not uniformly mixed')
        profiles+=1
        matrix_entries+=(2*m)**2
    print('VERIFY_OK spectral_profiles=',profiles,'matrix_entries=',matrix_entries,
          'orders=2..11 max_entry_discrepancy=',format(max_deviation,'.3e'))

if __name__=='__main__':
    main()
