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

Run `python3 verify.py` from the same extracted package directory. The checker uses Python 3 standard-library rational arithmetic and verifies exact joint covariances by exhaustive enumeration of set partitions through nine elements. It separately verifies the monotonicity and signs through \(n=320\) for \(3\le k\le15\), the non-independent zero-covariance example \((n,k,s)=(6,3,3)\), and numerical closeness of the computed transition index to the fixed-\(k\) asymptotic fraction.

The mathematical proof, not any finite computation, establishes the stated theorems for every permitted \(n,k,s\). The exact threshold fraction concerns fixed \(k\); the checker is not an infinite proof. Independent audit and external validation have not been performed.
