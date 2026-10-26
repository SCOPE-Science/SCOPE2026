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

# Verification of isolation-variance tomography

Run `python verify.py` (Python 3 standard library) from the directory containing `verify.py`. Its sole output is a deterministic compact JSON report; parse and compare to the supplied `certificate.json`. The checker enumerates independent retained-vertex states with rational probabilities at three interior retention levels for nine finite regular graphs (10,968 weighted configurations), checks 27 pairs of first and second moments, independently expands nine cubic-variance coefficients, tests the codegree-to-coefficient inversion, and verifies the decagon/two-pentagon indistinguishability.

The all-graph result is independently proved from pair probabilities, coefficient inversion and wedge counting in `RESULT.md`; no finite enumeration is treated as an infinite proof. Tests cannot establish source originality or empirical stability. No independent review has been performed.
