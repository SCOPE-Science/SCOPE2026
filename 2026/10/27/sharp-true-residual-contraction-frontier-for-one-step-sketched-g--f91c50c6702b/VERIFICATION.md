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

The standalone `verify.py` was run with the Python standard library. It reports 2,543 exact-rational assertion/check groups. It constructs the extremal Gram matrix without referring to the theorem's claimed final norm, verifies eigenvalues using trace and determinant, solves the original sketched normal equation, and checks the critical no-update obstruction. Additional seeded rational matrices test 2,500+ arbitrary admissible approximate sketch Gramians against the analytic bound. These are finite consistency tests only: the infinite-universe statements rely on the proof in `RESULT.md`.

To reproduce, execute `python verify.py` in a directory containing only the packaged files. No optional dependencies, private data, network connection, or external certificates are required.
