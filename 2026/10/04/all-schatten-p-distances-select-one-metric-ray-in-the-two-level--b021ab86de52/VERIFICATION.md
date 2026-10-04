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

`verify.py` replays the closed-form formulas without third-party dependencies. It checks representative overlap values across trace, Hilbert–Schmidt, intermediate Schatten, and operator norms; compares the formula against a dense positive-coefficient grid; verifies the published \(p=2\) specialization; and samples the analytic monotonicity numerator.

A successful run prints `VERIFY_OK`.

The finite replay is not the proof of the continuum statement. The continuum proof is the trace/determinant reduction, exact scalar minimization, and strict monotonicity calculation in `RESULT.md`. No claim is made outside \(2\times2\) quasi-self-adjoint operators with simple real spectrum and normalized left eigenvectors, or outside Schatten distance from the identity.
