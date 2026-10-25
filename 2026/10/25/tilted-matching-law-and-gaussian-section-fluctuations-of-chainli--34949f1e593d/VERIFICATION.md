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

Run `python checker.py` in a directory containing the embedded checker with Python 3; no third-party dependencies are needed.

The observed execution finished with `CHECK_OK 87 direct algebra/numerical comparisons` after 63 matching-enumeration comparisons (dimensions 3--9, three link parameters, three tilts), nine direct physical integrations of three-variable defining inequalities, 12 finite-dimensional variance checks by numerical differentiation, and three checks of convergence of the exact variance formula. Direct integration is independent of the combinatorial transfer identity, and the equations in the proof supply the all-dimensional certificate.

The tests do not establish infinite-dimensional convergence by enumeration; the analytical eigenvalue argument and a standard moment-generating-function convergence theorem establish the central limit theorem. The large-deviation conclusion uses a standard differentiable log-moment-generating-function argument. No independent mathematical audit was performed.
