"""Finite diagnostics for positive rank-one Schatten quasi-class profile tomography.

Requires NumPy. Run: python check_profile.py
No finite experiment certifies an infinite-dimensional theorem.
"""
import numpy as np


def power_trace_hermitian(x, p, absolute=False):
    eigenvalues = np.linalg.eigvalsh(x)
    if absolute:
        return float(np.sum(np.abs(eigenvalues) ** p))
    assert eigenvalues.min() > -1e-10
    return float(np.sum(np.maximum(eigenvalues, 0.0) ** p))


def max_profile(a, v, t, p):
    proj = np.outer(v, np.conj(v))
    return max(power_trace_hermitian(a+t*proj,p,True),
               power_trace_hermitian(a-t*proj,p,True))


def spectral_form(a, v, p):
    lam, u = np.linalg.eigh(a)
    return float(np.real(np.vdot(v, (u*(lam**(p-1))) @ (u.conj().T @ v))))


def main():
    count = 0
    rng = np.random.default_rng(20261018)
    for p in (0.3, 0.5, 0.8):
        for n in (3, 5, 8):
            diag = np.geomspace(0.8, 0.06, n)
            A = np.diag(diag)
            off = np.diag(np.ones(n-1), 1) + np.diag(np.ones(n-1), -1)
            off /= np.linalg.norm(off, 2)
            B = np.diag(np.sqrt(diag)) @ (np.eye(n)+0.22*off) @ np.diag(np.sqrt(diag))
            assert np.linalg.eigvalsh(B-0.78*A).min()>-1e-10; count+=1
            assert np.linalg.eigvalsh(1.22*A-B).min()>-1e-10; count+=1
            for op in (A, B):
                base = power_trace_hermitian(op,p)
                for _ in range(12):
                    vec = rng.normal(size=n)+1j*rng.normal(size=n)
                    vec /= np.linalg.norm(vec)
                    P = np.outer(vec,vec.conj())
                    # A - t P stays positive for t below this exact finite-matrix threshold.
                    invcrit = float(np.real(np.vdot(vec, np.linalg.solve(op,vec))))
                    for t in (1e-5,3e-6):
                        assert t * invcrit < 1
                        assert np.linalg.eigvalsh(op-t*P).min()>=-1e-11; count+=1
                        prof=max_profile(op,vec,t,p)
                        pos=power_trace_hermitian(op+t*P,p)
                        assert abs(prof-pos)<2e-11; count+=1
                        slope=(prof-base)/(p*t)
                        expected=spectral_form(op,vec,p)
                        assert abs(slope-expected)<0.004*(1+abs(expected)); count+=1
            # The profile genuinely distinguishes a noncommuting relative-order pair.
            v=np.zeros(n,dtype=complex); v[0]=1
            qA=spectral_form(A,v,p)
            qB=spectral_form(B,v,p)
            assert abs(qA-qB)>1e-5; count+=1
            assert np.linalg.norm(A@B-B@A)>1e-7; count+=1
    print(f'PASS: {count} finite assertions; fractional response, positivity, and noncommutation.')


if __name__ == '__main__':
    main()
