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

# Verification of the result

The exact second moment is obtained by differentiating the renewed survival transform, not by simulating paths. `verify.py` uses only Python's standard library. Running `python3 verify.py` passed 1,998 checks in the present package. Three strict comparisons are certified using rational Taylor remainder intervals for \(e^{1/2}\), \(e\), and \(e^{3/2}\): the midpoint mean exceeds the endpoint mean; the endpoint variance exceeds midpoint variance; and the dimensionless cosh parameter lies below the derivative-sign threshold.

The script also solves independently discretized Neumann/Dirichlet killed-generator tridiagonal systems on three meshes, comparing their mean and second-moment reconstructions with the analytic functions. Those finite meshes are consistency checks, not proofs of the continuum or global optimization theorem. There has been no independent external audit or experimental validation.
