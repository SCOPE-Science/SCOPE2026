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

Execute `python3 verify.py` from the directory containing `verify.py`. The script needs only Python 3 and its standard library. It constructs each original forbidden-pair transition matrix separately from the gauge matrices and checks exact integer conjugacy and determinant identities for all \(21{,}844\) schedules with periods \(1\) through \(7\). It verifies the number of schedules for each defect count exactly as \(2^p\binom pk\) and the polynomial \(\lambda^2-p\lambda-1\) for all one-defect products. Positive-root comparisons for products with two or more defects are numerical, serving only as spot corroboration of the exact entrywise comparison proof.

For periods at most three, a separate brute-force enumeration computes admissible binary strings at all tested lengths up to nine positions, checks the transfer-matrix counts, and directly enumerates periodic binary strings for short time-\(p\) iterates. Those counts agree with traces of monodromy powers. The checker output ends in `VERIFY_OK`. It does not certify an infinite claim through extrapolation: the all-period statements rest on the proof using the explicit matrices \(L,F\), the nonnegative replacement identity, and Perron–Frobenius strict monotonicity. The endpoint convention and entropy normalization are stated in `RESULT.md`.
