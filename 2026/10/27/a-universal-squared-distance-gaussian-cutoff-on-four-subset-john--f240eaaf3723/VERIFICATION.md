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

The proof uses an exact Newton-binomial incidence decomposition, a full-rank theorem for subset inclusion matrices with an induction included in `RESULT.md`, and two explicitly constructed negative-eigenvalue witnesses on eight ground points.

Execute `python3 check.py`. It verifies 1,584 exact rational matrix-vector equations and trace/moment identities on ground sets of sizes eight and nine, endpoint sign checks, and 135 rational bisection iterations. Its computations concern finite cases only; analytic inequalities and the inclusion-matrix argument establish the all-dimensional result.

Independent audit and independent validation have not been performed. Relevant published literature does not provide an exhaustive novelty guarantee.
