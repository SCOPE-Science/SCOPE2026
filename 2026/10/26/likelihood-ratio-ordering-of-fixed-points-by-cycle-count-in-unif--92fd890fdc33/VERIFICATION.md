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

# Reproducibility

With Python 3.9 or newer, run `python3 verify.py`. It uses only the Python standard library, exact integers, and rational fractions, and reconstructs the derangement recurrence independently of the analytic proof. Expected output reports 6,171,849 exact assertion instances, covering brute permutation enumeration for orders 2–8, all two-by-two minors for orders 2–41, mixed determinant identities through order 49, and independently enumerated weighted matchings through order 16.

# Proof boundary

The matrix eigenvalue argument and mixed-size determinant induction in RESULT.md establish all \(n\ge2\); enumeration through finite \(n\) is a cross-check and cannot prove the infinite statement. The identity \(J_n(k,f)=\binom nf d(n-f,k-f)\) and real-rootedness are published inputs, not original discoveries. The claimed contribution is TP2 and the resulting conditional MLR order. Independent review and exhaustive historical publication comparison have not been performed.
