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

The exact proof in `RESULT.md` does not depend on numerical certification. It uses: (i) the finite-group character-idempotent kernel; (ii) Steinberg's exact character values on semisimple and nonsemisimple classes; (iii) centralizer factorization for semisimple rational canonical types; (iv) the elementary Euler factor \(\sum_m t^m/\prod_{i=1}^m(Q^i-1)=\prod_{r\ge1}(1+tQ^{-r})\); and (v) telescoping plus the \(q\)-binomial expansion. The final strict inequalities follow from the exact coefficient ratio, not from numerical evidence.

Reproduce with `python3 verify.py` (Python 3 standard library only). The checker independently computes the weighted sum over semisimple rational canonical types as exact rational numbers for \(q\in\{2,3,4,5\}\) and \(n=0,\ldots,8\), testing 36 cases. For \(q\in\{2,3\}\), \(n\in\{2,3\}\), it also iterates over every invertible matrix (sizes 6, 48, 168 and 11232) and computes the Steinberg trace from invariant projective points, invariant planes and invariant complete flags. Results agree exactly, with means \(2/3,3/4,2/3,3/4\) in that parameter order. This verifies particular finite instances but is not an exhaustive enumeration of arbitrary prime powers or ranks.

No numerical test establishes worldwide novelty or the limiting infinite-product identity by itself. The fixed-\(q\) asymptotic follows from the absolutely convergent \(q\)-binomial product; the result does not address simultaneous growth of \(n\) and \(q\).
