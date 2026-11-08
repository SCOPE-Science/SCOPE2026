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

# Reproduction and limits

Execute `python verify.py` with Python 3.10 or newer. The program needs only the standard library and prints `VERIFY_OK checks 971598`. It performs exact-fraction identities for phase endpoints and candidate coefficients, and many finite numerical checks of containment and the one-dimensional volume objective. Its random sampling uses a fixed seed for reproducibility.

These computations do **not** prove correctness for arbitrary real parameters and dimensions. The analytical proof uses the precise support-function constraints, differentiates a strictly unimodal objective, establishes exact reflection inequalities for all directions, and checks cone/cylinder endpoints separately.

Source comparison is claim-based, using the motivating 2026 paper, older truncated-cone optimization work, and published mathematical records. A possible unlocated historically equivalent formula is a literature-priority limitation. No independent external mathematical audit has been performed.
