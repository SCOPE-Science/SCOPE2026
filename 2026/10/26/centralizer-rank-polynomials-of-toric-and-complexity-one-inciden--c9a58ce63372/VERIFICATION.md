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

# Verification and limitations

The standalone `check_incidence_centralizers.py` runs on Python 3 with no external dependencies. It constructs multiplication from the vertex and cover-relation basis, computes each full adjoint matrix by two distinct algebra products, and row-reduces over prime fields without calling the proof's rank decomposition. Its separately implemented subset expansion also checks the graphic-matroid formula coefficient by coefficient.

Run `python3 check_incidence_centralizers.py`. Compare its terminal sentinel with `ALL_INCIDENCE_CENTRALIZER_CHECKS_PASSED 12 26587`. Test cases comprise prime fields with \(q=2\) and \(q=3\); the mathematical theorem applies to all prime powers because the proof uses only arbitrary-field row rank and cardinalities of finite fields. The recorded run tests 26,587 algebra elements. It is not an exhaustive check over unbounded fields or graphs.

The critical unbounded proof steps are the pivot/incidence-matrix rank split, the field-independent graphic-matroid rank formula, and the correction for the uniquely dependent full cycle edge set. These are proved in `RESULT.md`; the checker is corroborating evidence only. No independent mathematical audit has been performed.
