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

# Verification record

Run `python verify.py` from the same directory as these files (Python 3.9+, standard library only). The checker independently enumerates full permutation spaces for every \(2\le n\le9\), and exactly compares conditional record-count distributions, expectations, the fixed-point/record covariances, and reflected-label equality. It also evaluates exact rational four-boundary sign rules and total-fixed-point covariance expressions at every \(5\le n\le400\).

Actual execution returned: `PASS: 161280 independent enumeration and rational identity assertions`.

The conditional probability generating function is proved for all \(n\ge2\) by deletion and two-block factorization; the finite computations do not replace that proof. No external or independent audit has been completed.
