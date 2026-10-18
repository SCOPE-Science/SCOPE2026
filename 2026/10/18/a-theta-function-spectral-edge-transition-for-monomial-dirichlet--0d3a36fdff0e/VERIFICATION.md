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

# Verification of the stated spectral-edge law

Analytic verification begins with \(T_h e_j=w_{j,h}e_{j-k+m}\), giving the complete nonzero singular spectrum because the output monomials are orthogonal. The Hessian at the unique smooth maximum is \(-h^2/k+O(h^3)\). Bounded-offset Taylor expansions combined with uniform concavity and geometric tail bounds prove the theta sum; on the expanding window of width \(1/(h\sqrt{p_h})\), dominated Riemann sums prove the Gaussian mass. Explicit parameter sequences enforce the two saddle phases, and the positive odd-index terms of the Poisson series separate their limiting values.

Reproduce the supplemental diagnostics using standard Python 3: `python checker.py`. The checker computes directly from the factorial-ratio singular weights and compares with the predicted theta/normal approximations at multiple parameter combinations; it prints `PASS 38 finite numerical diagnostics; theorem proved separately`. These computations are finite approximations, not exhaustive proof or independent validation. All statements are limited to fixed structural parameters, the specified radial operators, and the two stated high-Schatten regimes.
