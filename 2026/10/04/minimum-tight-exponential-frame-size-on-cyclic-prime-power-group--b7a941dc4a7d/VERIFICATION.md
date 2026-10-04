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

The analytic proof has four independently checkable steps:

1. For the evaluation matrix \(F_{a,b}=\exp(2\pi iab/p^k)\), tightness is equivalent to vanishing of all off-diagonal row-Gram entries.
2. A nonzero difference of valuation \(v\) produces a primitive \(p^{k-v}\)-th root, so its row-Gram sum vanishes exactly when the mask polynomial is divisible by \(\Phi_{p^{k-v}}\).
3. The product of the distinct required cyclotomic factors divides the mask; evaluating at \(1\) proves \(p^{|R(A)|}\mid |B|\).
4. The explicit digit-set mask is exactly the product of those cyclotomic factors, with 0/1 coefficients by uniqueness of base-\(p\) expansion, so the lower bound is attained.

`verify.py` uses exact integer polynomial division and no floating-point determinant or root tests. It exhaustively checks every nonempty spatial set and every nonempty frequency set in \(\mathbb Z/4\mathbb Z\), \(\mathbb Z/8\mathbb Z\), and \(\mathbb Z/9\mathbb Z\), for a total of 781 spatial sets, and verifies selected larger constructions in orders 32, 27, 25, and 49.

Replay output:

`VERIFY_OK exhaustive_A=781 larger_cases=4`

The finite checks are consistency tests only. They do not substitute for the general cyclotomic proof.
