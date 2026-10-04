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
The symbolic checker reconstructs the moments used by exact steepest descent, differentiates the exact two-step squared Euclidean ratio at the balanced two-mode state, and verifies the polynomial identity for the derivative. It also verifies the cubic discriminant factorization, the positive endpoint values, the signs \(F(13)<0<F(14)\), and the exact finite witness at \(\kappa=14\), \(s=5\), \(\varepsilon=1/2000\).

The checker uses exact symbolic and rational arithmetic except for printing a decimal approximation of the unique threshold. The proof of uniqueness above \(1\) is analytic: after the reciprocal substitution, Descartes' rule gives exactly one positive shifted root. The verification does not establish a global two-step worst-case factor over all spectra or initial errors; that is outside the claim.
