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

`verify.py` is a standard-library numerical consistency check of the closed formula. It evaluates every integer pair \(m=2,\ldots,200\) and \(n=m-1,\ldots,m+100\), computes all subset-cardinality crossing values, checks that their minimum equals the claimed endpoint expression, verifies that the proposed centered ball has at least the claimed distance from every defining halfspace, and checks the predicted active upper facet family.

The analytic argument in `RESULT.md`, not this finite computation, proves the result for all \(m\ge2\) and \(n\ge m-1\). The computation does not address \(n<m-1\), non-Euclidean norms, John ellipsoids, or circumradii.
