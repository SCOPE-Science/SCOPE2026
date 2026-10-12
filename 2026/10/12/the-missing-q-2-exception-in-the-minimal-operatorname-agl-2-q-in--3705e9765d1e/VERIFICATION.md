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

The verification script `verification/verify.py` uses exact polynomial arithmetic in characteristic \(2\).

It checks the exact \(q=2\) quotient division, the resulting quartic, the three homogeneous partial derivatives, the values at every derivative-critical projective point, the factorization at \(\lambda=1\) modulo \(\alpha^2+\alpha+1\), and smoothness of both conic factors.

A fresh replay with SymPy \(1.14.0\) produced:

`VERIFY_OK q=2_exception=lambda=1 factors=2_smooth_F4_conics smooth_else=all_lambda_ne_1`

The script does not use finite sampling to prove a universal statement. The proof that the derivative common-zero locus is exhausted uses the factorized derivative equations: for \(Z=0\) there are exactly three projective solutions, and for \(Z\ne0\) normalization to \(Z=1\) forces \(X,Y\in\mathbb F_2\).

The remaining limitation is bibliographic rather than computational: absence of a located correction does not prove that no informal or poorly indexed correction exists.
