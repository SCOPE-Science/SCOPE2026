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

# Verification notes

The exact-arithmetic program `checks/verify.py` requires only Python 3 standard-library modules. It evaluates the coefficient jets after eliminating the independent linear moments and verifies the two Gram determinants for prime characteristics 5, 7 and 11 with admissible values \(r=2,3,4\). It also exhaustively enumerates \(\mathbb F_5\)-rational projective points for \(n=7,8\), identifying exactly the predicted 21 and 56 singular points among solutions. The observed checker terminates with `VERIFY_OK`.

This is a finite verification of formulas and small-field cases only. It is not an exhaustive enumeration over \(\overline{\mathbb F}_p\), and it does not independently validate the infinite-family theorem. The proof of exact singular support uses Vandermonde invertibility; the proof of the associated graded ring uses a regular initial sequence. These arguments explicitly require \(p\ge5\) and \(2\le r<p\). No independent mathematical audit was performed.
