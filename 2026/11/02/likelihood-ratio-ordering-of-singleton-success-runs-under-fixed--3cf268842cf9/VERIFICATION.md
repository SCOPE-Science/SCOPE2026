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

The delivered `verify.py` uses only the Python standard library and was run with `python3 verify.py`.

It passed 2,304,064 exact assertions. Independent word enumeration checks the joint distribution and covariance for all fixed-content cases with \(3\le a+b\le13\), \(a\ge2\), \(b\ge1\). Integer binomial checks test adjacent TP2 minors for \(2\le a\le64\) and arbitrary pairs of rows for \(2\le a\le19\).

The infinite theorem is separately established in `RESULT.md`: uniform composition conditional on the number of one-runs, explicit counts of singleton parts, a positive adjacent likelihood-ratio comparison, support-boundary ordering, and Vandermonde factorial-moment algebra. Exhaustive enumeration within a finite range is not used to infer an unbounded theorem. No analysis of total positivity beyond order two is claimed.
