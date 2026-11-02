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

# Computational verification and proof boundary

Execute `python verify.py` with SymPy installed. The program performs only deterministic exact arithmetic and symbolic identities: seven beta-product even moments against the stationary generator recurrence; equality of the two moment-coordinate formulas; the derivative-polynomial factorization; the endpoint and minimum formulas; both exact witness parameter sets and their distinct sixth moments; and 48 rational fixed-variance identities. Its successful execution was checked on the packaged source code.

Analytic parts not certified by this finite run: existence and uniqueness of the invariant process follows from exponential contraction and irreducibility of the velocity chain; the distributional beta product follows from a compact moment problem; the count of all inverse solutions follows from signs of one quadratic and endpoint exclusion, independent of finite scans. The publication comparison is a best-knowledge literature assessment, not an independent priority or correctness certification.
