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

# Verification record

Run the included `checker.py` with `python3 checker.py` (standard-library only) and compare the resulting text with `checker_output.txt`. The retained output reports **14,206 passed finite deterministic assertions**. The checker independently evaluates the eigenintegral using analytic antiderivatives, bisection roots, eigenfunction orthogonality, stationary normalization and detailed balance over multiple values of \(a\) in \((0,1)\). These tests are diagnostics, not a proof of infinite spectral completeness or the exact operator norm. The argument in `RESULT.md` supplies the latter through an exhaustive eigenvalue ODE and a compact self-adjoint spectral representation.

The numerical tolerances in the code account for floating-point computation. The derivation uses exact functional identities for arbitrary real \(0<a<1\). No external or independent audit has been performed.
