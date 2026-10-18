"""Independent finite-size checks for a centrally lossy open quantum chain.
The analytic all-size argument is contained in RESULT.md; these checks are not a proof.
Run: python verify.py (requires numpy).
"""
from math import gcd, pi, sin
import numpy as np


def chain(m, J, gamma, s, eps):
    size = 2*m + 1
    H = np.zeros((size,size), dtype=complex)
    for i in range(size-1):
        H[i,i+1] = H[i+1,i] = J
    H[m,m] = -0.5j*gamma
    H[s-1,s-1] += eps
    return H


def expected_width(m,J,gamma,s,k):
    theta = pi*k/(m+1)
    return gamma*sin(s*theta)**4/(8*J*J*(m+1)*sin(theta)**2)


def nearest_eigenvalue(m,J,gamma,s,k,eps):
    spectrum = np.linalg.eigvals(chain(m,J,gamma,s,eps))
    energy = 2*J*np.cos(pi*k/(m+1))
    return spectrum[np.argmin(abs(spectrum-energy))]


def run():
    count = 0
    largest_rel_err = 0.0
    for m in range(1,9):
        for s in range(1,m+1):
            for gamma in (0.7, 2.6):
                J = 1.3
                eps = 0.16
                spectrum = np.linalg.eigvals(chain(m,J,gamma,s,eps))
                number_real = int(np.sum(abs(spectrum.imag)<1e-9))
                assert number_real == gcd(m+1,s)-1, (m,s,gamma,number_real)
                # Independently construct exact antisymmetric eigenvectors for arithmetic nodes.
                for k in range(1,m+1):
                    if (k*s)%(m+1) == 0:
                        theta=pi*k/(m+1)
                        psi=np.zeros(2*m+1, dtype=complex)
                        for j in range(1,m+1):
                            psi[j-1] = np.sin(j*theta)
                            psi[2*m+1-j] = -np.sin(j*theta)
                        residual=np.linalg.norm(chain(m,J,gamma,s,eps)@psi - 2*J*np.cos(theta)*psi)
                        assert residual<2e-12,(m,s,k,residual)
                    else:
                        theta=pi*k/(m+1)
                        # Close to the unperturbed eigenvalue: no numerical branch switching at small eps.
                        e1 = nearest_eigenvalue(m,J,gamma,s,k,4e-4)
                        e2 = nearest_eigenvalue(m,J,gamma,s,k,2e-4)
                        predicted = expected_width(m,J,gamma,s,k)
                        measured1 = -e1.imag/(4e-4)**2
                        measured2 = -e2.imag/(2e-4)**2
                        assert measured1>0 and measured2>0,(m,s,k,e1,e2)
                        rel = abs(measured1 - measured2)/max(predicted,1e-12)
                        largest_rel_err = max(largest_rel_err,rel)
                        # Difference between two computations, not pointwise proof.
                        assert rel<0.025,(m,s,k,measured1,measured2,predicted,rel)
                        err = abs(measured2-predicted)/predicted
                        assert err<0.025,(m,s,k,measured2,predicted,err)
                        count += 1
    print(f'VERIFY_OK: {count} nonnode mode/defect/rate checks, gcd node counts m<=8; max half-step relative change={largest_rel_err:.4g}')

if __name__ == '__main__':
    run()
