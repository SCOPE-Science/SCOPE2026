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

Run `python3 verify.py` from this directory. The standard-library-only checker returns `VERIFY_OK` if every assertion passes. It constructs the indicated Eulerian tour for all integers \(4\le n\le15\), verifies that the cyclic factor multiset contains each required weight-two factor exactly once except for the specified single duplication, and checks all other observed factor weights. It independently checks mandatory necklace components, finite short-period separation for \(4\le n\le9\), and exhaustive short-cover exclusion for \(n=4,5\).

The checker was executed successfully with Python 3 in the package directory. The full all-order lower bound relies on the mathematical residual-cycle and Fine–Wilf argument in `RESULT.md`; no finite enumeration certifies the infinite claim. Neither a solver log nor a computed witness alone proves originality or research value.

Self-review: passed. Independent audit: not yet performed.
