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
# Verification of the mathematical result

The derivation is algebraic and holds for all integer dimensions \(d\ge3\). The Walsh eigenvalues and Krawtchouk shell formula are proved in `RESULT.md`. The bounds \(T_d(z)<0.81/d^2\) and \(F_d'(z)<0\) are explicit uniform analytic estimates, not sampled certificates. In particular \(\tau_d\) is the **persistent** horizon; positivity at arbitrary earlier isolated times is not ruled out.

`verify.py` (Python standard library) independently computes shell coefficients, bisects the late antipodal root for dimensions 3 through 32, and tests every radial kernel at the root and just to its right in time. These are finite floating-point spot checks only. Example values are reported in `RESULT.md`.

No independent mathematical review, external certification, or exhaustive automated proof has been performed.
