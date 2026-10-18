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

# Reproducibility and scope

Run `python3 check.py` with Python 3's standard library. In the packaged version, the script passed **1,892 checks** of positive-part eigenvalue evaluation, exact local-profile witnesses across ten parameter samples, finite-difference Fréchet linearization in the strictly mixed-sign region, and 600 reproducible random matrix-pair tests in each of the operator, trace, and Frobenius norms.

The analytic argument in `RESULT.md` establishes global validity, not the finite tests. In particular, matrix computations cannot prove a continuum of spectral ratios, the exact endpoint \(2/\sqrt3\), or absence of historical equivalents. A mathematical derivation for the one-variable maximum and a separate treatment of singular crossing paths are included in the proof. The relevant prior idempotent endpoint \(q=1\) is acknowledged; no independence or external validation is asserted.
