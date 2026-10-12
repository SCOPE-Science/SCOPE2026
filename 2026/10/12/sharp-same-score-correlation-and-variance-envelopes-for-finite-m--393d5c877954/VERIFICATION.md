---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytical derivation checks these points: (i) the density is nonnegative and has uniform margins; (ii) the centered Markov operator shifts orthonormal coordinates and vanishes on the orthogonal complement; (iii) its powers produce the exact path-product lag covariances; (iv) lag matrices are symmetric weighted unions of paths, hence have sign-symmetric spectra; (v) the Rayleigh endpoints are attained by actual scores; and (vi) sample-variance normalization gives a symmetric matrix with unit diagonal and an attained spectral interval. All arguments remain valid for zero or negative coefficients and for sample size one.

The concrete counterexample is **exact**, not an empirical fit: \(\lambda_1=\lambda_2=1/4\), Fourier basis functions \(\phi_1=\sqrt2\sin(2\pi u)\), \(\phi_2=\sqrt2\cos(2\pi u)\), \(\phi_3=\sqrt2\sin(4\pi u)\); Fourier orthogonality and \(c\ge0\) show validity. The score coefficients \((1/2,1/\sqrt2,1/2)\) are normalized, giving \(\gamma_1=\sqrt2/8>1/8\) and a three-dimensional long-run matrix with exact eigenvalues \(15/16\) and \((33\pm\sqrt{129})/32\).

For reproducibility run `python longla_spectral_checker.py`. Its 718 finite checks test path shift powers, eigenvalue sign symmetry, homogeneous discrete-sine eigenvalues, finite-horizon variance identities, exact symbolic eigenvalues and witness, plus direct numerical quadrature of one- and two-step copula densities. These checks are auxiliary; no finite computation proves the general Hilbert-space statement. The bounded-density hypothesis matters, and no claim is made for general copulas outside the stated family. Independent audit has not been performed.
