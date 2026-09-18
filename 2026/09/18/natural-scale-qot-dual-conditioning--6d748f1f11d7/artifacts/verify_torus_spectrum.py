"""Exact spectral scaling check for a one-dimensional periodic QOT model.

The probability space is the circle of length 2*pi with normalized Haar measure.
For the translation-invariant self-transport solution with quadratic local cost,
the active set is |x-y|<r and r^3=3*pi*epsilon.  On Fourier mode k>=1,
the negative dual Hessian has eigenvalues

    lambda_k^+- = (r/pi +/- sin(k r)/(pi k))/epsilon.

The constant gauge-orthogonal mode has eigenvalue 2r/(pi epsilon).
The script prints the low-frequency spectral gap and the rescaled top eigenvalue.
"""

from math import pi, sin


def spectrum(epsilon: float):
    r = (3.0 * pi * epsilon) ** (1.0 / 3.0)
    lam_min_mode1 = (r - sin(r)) / (pi * epsilon)
    lam_max_constant = 2.0 * r / (pi * epsilon)
    condition_proxy = lam_max_constant / lam_min_mode1
    return r, lam_min_mode1, lam_max_constant, condition_proxy


print("epsilon,r,lambda_low,lambda_high,lambda_high*r^2,condition*r^2")
for epsilon in (1e-3, 1e-6, 1e-9):
    r, low, high, cond = spectrum(epsilon)
    print(
        f"{epsilon:.0e},{r:.15e},{low:.15e},{high:.15e},"
        f"{high*r*r:.15e},{cond*r*r:.15e}"
    )

print("expected limits: lambda_low -> 1/2, lambda_high*r^2 -> 6, condition*r^2 -> 12")
