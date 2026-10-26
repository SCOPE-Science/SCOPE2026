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
Run `python3 verify.py` using Python 3 and the standard library. The checker forms every alternating matrix of the tested orders, computes nullities over the prime fields, and checks their exact frequencies against the quotient formula involving the symplectic-group order. It separately tests the total count and the expected number of radical elements. Successful output: `ALTERNATING_FORMS_FINITE_COUNT_OK 26 rank-cells`.

The finite checker uses prime field values \(q=2,3\) at sizes up to six and five. The mathematical statements cover all finite prime powers \(q\ge2\). The exact cardinality formulas, uniform radical-tail estimate, finite-rank Ehrenfeucht–Fraïssé lemma, and first-order exact-dimension formulas in RESULT.md must be inspected as mathematical arguments. Finite counts are not an infinite convergence or logical completeness certificate. No independent audit has been performed.
