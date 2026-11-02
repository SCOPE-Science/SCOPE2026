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

# Reproduction and proof checks

The universal statement is proved by the positive quadratic root, a geometric bootstrap and a two-step asymptotic expansion in `RESULT.md`. No finite run is treated as an infinite proof.

Run `python verify_sav.py` from the extracted package directory. The checker uses Python standard-library modules only and a fixed random seed. It performs 300 sampled modified-energy and positivity checks, one explicit large-step wrong-attractor example, and twelve large-step asymptotic comparisons. The exact parameter and mathematical limits are in `RESULT.md`.

The initial source record is arXiv:2610.01063v1, public 2026-10-01. The recent source's later sections were unavailable for complete textual comparison; this limits external priority assessment but does not enter the algebraic proof.
