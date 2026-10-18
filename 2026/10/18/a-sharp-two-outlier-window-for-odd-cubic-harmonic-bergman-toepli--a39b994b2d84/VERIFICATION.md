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

The finite symbolic checker `check.py` was run with its declared SymPy dependency. It verified the two-root determinant factorization, Vieta reduction, one-root cancellation, exact threshold, and the nonzero confluent determinant. Six exact rational parameter instances were also checked for root ordering. Those finite diagnostics do not replace the proof for all complex parameters.

The infinite-dimensional reduction uses harmonic-Bergman Fredholm theory (essential curve and index zero) and the Bergman-kernel representation for the nullspace of an adjoint analytic multiplier; the precise argument is in RESULT.md. The repeated-root extension is obtained by differentiating reproducing kernels and imposing both value and derivative cancellation.

Publication priority is not independently validated: a relevant 2021 article is accessible at abstract level only. The general 2026 polynomial spectral theorem was inspected in its accessible full text and is credited rather than claimed as new.
