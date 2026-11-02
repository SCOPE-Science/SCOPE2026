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

The standalone `checker.py` verifies the finite consistency grid using only Python's standard library. Exact rational arithmetic checks special exponential values at multiples of \(\log2\); floating-point checks compare the analytic peak with a separate dense deterministic time grid. The reported assertion count is produced by running this very file from the delivered package.

These computations support, but cannot replace, the analytical derivative and supremum arguments in `RESULT.md`. A complete continuum proof is provided there. No independent validation or field calibration is asserted.
