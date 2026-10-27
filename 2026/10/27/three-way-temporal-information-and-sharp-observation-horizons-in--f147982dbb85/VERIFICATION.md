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

# Finite checks and analytical boundaries

Run `python3 verify.py` using standard Python 3. The checker computes every binary Dickson polynomial exactly, verifies the gcd identity for all 119 separation pairs with \(1\le s<t\le16\) and \(s\le14\), confirms the three primitive coefficients and their maximum degree, and independently builds actual Rule 90 Laurent observation forms for all time lengths \(1\le n\le11\). Binary Gaussian elimination establishes all 1,309 predicted ranks. The checks use integers, no floating-point arithmetic.

These checks do **not** prove the result for all integer spacings or arbitrary time lengths. The mathematical proof uses free-module algebra, polynomial gcd, a primitive syzygy and bounded-degree classification to cover all values, plus compactness for the full trace language. Independent verification has not been performed.
