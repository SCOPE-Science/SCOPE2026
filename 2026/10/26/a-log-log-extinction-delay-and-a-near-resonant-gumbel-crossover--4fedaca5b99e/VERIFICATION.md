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

The self-contained `verify.py` constructs a finite-state generator independently of the conditional-source proof and compares matrix-exponential moments against two analytical inequalities, with 144 parameter tests. It checks 3 larger finite-network detuning examples by sampling source-recovery times and propagating the receiver's exact piecewise two-state equation. All checks passed in the recorded execution.

Reproduce using Python 3 with `numpy` and `scipy` installed: `python verify.py`. The matrix-exponential comparisons and finite samples are numerical support; the infinite-population theorem depends on the independent source-lifetime variance estimate, the rigorously bounded saturation correction, and the conditional Poisson argument given in `RESULT.md`. No theorem concerning bidirectional transmission, uniform parameter windows, or all-graph universality is established.
