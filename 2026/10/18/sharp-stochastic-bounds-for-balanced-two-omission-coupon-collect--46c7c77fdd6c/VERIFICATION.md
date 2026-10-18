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

The accompanying `checker.py` was executed using standard-library rational arithmetic. It reported `PASS: 384 exact rational checks; complete direct enumeration for n<=7 and k<=3`. The script covers exact marginal normalization; the full tail identity versus independent enumeration for \(4\le n\le7\) and \(1\le k\le3\); endpoint bounds and strictness for proper mixtures; and closed-form geometric-series means for \(4\le n\le9\).

The logical proof of universal validity is the inclusion-exclusion identity, strict convexity, and classification of the extreme points of the fractional-one-factor polytope provided in RESULT.md. Finite checks are reproducibility aids, not substitutes for proof. The scientific novelty assessment is literature based and does not constitute independent verification of originality.
