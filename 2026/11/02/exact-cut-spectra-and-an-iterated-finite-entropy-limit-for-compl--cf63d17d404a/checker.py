#!/usr/bin/env python3
"""Independent finite-state checks for complete uniform hypergraph-state Schmidt spectra.

Requires Python 3 and NumPy. No external data or network access.
"""
import math
import itertools
import numpy as np


def phase_count(weight, k):
    return -1 if math.comb(weight, k) % 2 else 1


def direct_amplitudes(a, b, k):
    # Here choose is evaluated independently of the residue phase reduction.
    M = np.empty((1 << a, 1 << b), dtype=np.float64)
    factor = 2.0 ** (-(a + b) / 2)
    for i in range(1 << a):
        for j in range(1 << b):
            M[i, j] = factor * phase_count(i.bit_count() + j.bit_count(), k)
    return M


def compressed_amplitudes(a, b, k):
    NA = [sum(math.comb(a, j) for j in range(r, a + 1, k)) for r in range(k)]
    NB = [sum(math.comb(b, j) for j in range(r, b + 1, k)) for r in range(k)]
    F = np.array([[1 if r + s < k else -1 for s in range(k)] for r in range(k)], dtype=float)
    C = np.sqrt(np.outer(np.asarray(NA, dtype=float) / (2.0**a), np.asarray(NB, dtype=float) / (2.0**b))) * F
    return C, F, NA, NB


def positive_spectrum(M):
    sing = np.linalg.svd(M, compute_uv=False)
    return np.sort(sing**2)[::-1]


def check_direct():
    total = 0
    err = 0.0
    # k=2 reproduces complete graph phase; k=4,8 check true higher-order gates.
    for k in (2, 4, 8):
        for a in range(k-1, min(k+3, 10)):
            for b in range(k-1, min(k+3, 10)):
                if a+b > 16:
                    continue
                M = direct_amplitudes(a, b, k)
                C, F, NA, NB = compressed_amplitudes(a, b, k)
                d = positive_spectrum(M)[:k]
                c = positive_spectrum(C)
                assert len(d) == len(c) == k
                err = max(err, float(np.max(np.abs(d-c))))
                assert np.max(np.abs(d-c)) < 2e-12, (a,b,k,d,c)
                assert abs(sum(d)-1) < 2e-12
                assert min(d) > 1e-14
                if M.shape[0] > k:
                    assert np.linalg.matrix_rank(M, tol=1e-9) == k
                total += 1
    return total, err


def check_antiperiodic():
    checks = 0
    for j in range(1,9):
        k = 1 << j
        F = np.array([[1 if r+s<k else -1 for s in range(k)] for r in range(k)], dtype=float)
        T = F@F.T
        T0 = np.array([[k-2*abs(r-s) for s in range(k)] for r in range(k)],dtype=float)
        assert np.array_equal(T,T0)
        L = np.zeros((k,k),dtype=float)
        for r in range(k):
            L[r,r] += 2
            L[r,(r+1)%k] += (-1 if r+1<k else 1)
            L[r,(r-1)%k] += (-1 if r-1>=0 else 1)
        assert np.array_equal(L@T,4*np.eye(k))
        ev = np.sort(np.linalg.eigvalsh(T/(k*k)))
        expected = np.sort([1/(k*k*math.sin((2*h-1)*math.pi/(2*k))**2) for h in range(1,k+1)])
        assert np.max(np.abs(ev-expected))<2e-12
        purity = float(sum(ev*ev))
        assert abs(purity-(1/3+2/(3*k*k)))<2e-12
        assert abs(float(sum(ev))-1)<2e-12
        checks+=1
    return checks


def check_convergence():
    checks=0
    for k in (2,4,8,16):
        for length in (32*k,48*k):
            C,F,na,nb = compressed_amplitudes(length,length+1,k)
            ev = positive_spectrum(C)
            target = np.sort([1/(k*k*math.sin((2*h-1)*math.pi/(2*k))**2) for h in range(1,k+1)])[::-1]
            # The exact residues converge exponentially in block length.
            diff = float(np.max(np.abs(ev-target)))
            assert diff < 2e-3, (k,length,diff)
            checks+=1
    return checks


def check_rootfilter():
    cases=0
    for k in (2,4,8,16):
        for n in range(k-1,5*k+3):
            arr=[sum(math.comb(n,t) for t in range(r,n+1,k)) for r in range(k)]
            z=np.exp(2j*np.pi*np.arange(k)/k)
            for r in range(k):
                root=sum(((1+z[m])/2)**n * z[m]**(-r) for m in range(k))/k
                assert abs(root.real-arr[r]/2**n)<1e-11
                assert abs(root.imag)<1e-11
                cases+=1
    return cases


def main():
    direct,err=check_direct()
    antiperiodic=check_antiperiodic()
    convergence=check_convergence()
    roots=check_rootfilter()
    print(f"DIRECT_SCHMIDT_SPECTRUM_CASES={direct}")
    print(f"MAX_DIRECT_EIGENVALUE_ERROR={err:.3e}")
    print(f"ANTIPERIODIC_MATRIX_AND_PURITY_CASES={antiperiodic}")
    print(f"FINITE_TO_LIMIT_CASES={convergence}")
    print(f"ROOTS_OF_UNITY_COMPONENT_CHECKS={roots}")
    print("ALL_CHECKS_PASS")

if __name__ == "__main__":
    main()
