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

`verify.py` is a self-contained finite-matrix numerical cross-check (requires Python 3, NumPy and SciPy). Run `python verify.py` and expect `PASS finite cross-checks: 220`.

It checks the reflection-odd projector and its diagonal, dark-dimensional cyclic Krylov rank, and an independent vectorized-Liouvillian solution of the integrated survival equation. Tested cycle sizes are 3–10 with three absorption strengths, all point sources, and one seeded coherent pure state per size and strength. Numerical extrapolation uses two small positive dephasing rates; tolerance is 0.003. The infinite family and sharp prefactor are established by the proof in `RESULT.md`, not by these finite tests.

The first-public-source date is established from arXiv submission history. Relevant inspected primary literature and one unresolved full-text comparison are recorded in `AUDIT.json`. Independent audit has not been performed.
