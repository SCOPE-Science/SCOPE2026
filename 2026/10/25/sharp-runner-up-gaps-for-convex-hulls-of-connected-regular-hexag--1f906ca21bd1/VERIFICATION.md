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
The analytic argument in RESULT.md is universal and covers every integer n >= 3. The independent `verify_polyhex_runnerup.py` checker uses integer corners of the unit-area hexagons scaled by three, computes their convex hull by monotone chain, and uses the shoelace determinant. It does not invoke the published Minkowski-width formula.

Executed using Python 3.11 with no third-party dependencies. Checks passed: 147 explicit witnesses (n=3..149); every direction-count triple for n=3..109; exhaustive fixed polyhexes through n=9 (counts 11,44,186,814,3652,16689,77359 for n=3..9); exact runner-up six-times-areas 22,34,47,63,81,100,122, respectively. Previous n=10 exploratory enumeration was consistent but is not part of the reproducible certificate.

The checker is finite and does not prove the theorem for all n. Universal validity rests on the integer-defect proof. The cited area identity and tree estimates are published premises and have not been independently formally certified. No independent audit has been performed.
