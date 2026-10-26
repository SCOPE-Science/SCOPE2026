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

# Reproducibility and verification

The second-eigenvalue normalization is \(\lambda_2(D_{\sqrt R})=1-(R+1)e^{-R}\). For \(\widehat h_0=0\) and real \(h\), the exact analytic second-order coefficient is \(e^{-R}\sum_{m\ge2}q_m(R)|\widehat h_m|^2\), with angular \(m=1\) coefficient exactly zero. It follows by computing the first and second derivatives of the infinite Toeplitz matrix and applying the ordinary simple-eigenvalue formula; no numerical spectrum is used as a proof.

To check finite-section numerics, install NumPy and SciPy and execute `python verify_numerical.py`. The script takes \(h(\theta)=\cos(m\theta)\), uses up to 24 analytic Fock basis vectors and 512 equispaced angular quadrature points, then compares centered second differences at two step sizes with the coefficient \(e^{-R}q_m(R)/4\). Its tests cover radii \(R=0.5,1.2,1.5,2\) and harmonics \(m=1,2,4,9\). Numerical results are valid only for the tested finite-section approximations.

The sign proof is exact and does not rely on floating-point checks: \(q_m\) decreases because \(\frac{R}{k+1}\sum_{j=2}^{k-1}t_j=\sum_{j=3}^k\frac j{k+1}t_j<\sum_{j=2}^k t_j\) for \(t_j=R^j/j!\) and integer \(k\ge3\). Both transition parameters follow from the rational \(q_2(R)\) and \(\lim q_m(R)=1-R\).

No higher-order classification of the neutral perturbations or uniform nonlinear stability assertion is verified. Independent mathematical validation has not been performed.
