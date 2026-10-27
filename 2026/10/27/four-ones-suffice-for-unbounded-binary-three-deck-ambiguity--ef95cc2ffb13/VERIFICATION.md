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

# Verification guide

The proof is self-contained in `RESULT.md`. Use `python3 verify_three_deck.py` to repeat the reproducible finite tests; no packages beyond the Python standard library are required.

The checker separately computes scattered triples by a streaming dynamic program and, for short words, by explicit increasing-index triples. It compares those counts to the eight closed moment formulas for 2,372 words through length twelve having at most four ones, checks the low-support fiber-size bound for lengths 3–14, and verifies the constructed class sizes and deck equality at \(k=1,2,3,4,5\).

The genuinely infinite steps are algebraic: every integer pair from the displayed product has norm \(6^k\), the derived vector preserves two linear forms and has squared norm \(6^k\), and distinctness follows because the quotient of conjugate factors has rational nonintegral trace and is not a root of unity. Direct tests do not independently certify these steps for all \(k\), and a separately conducted independent audit has not been performed.
