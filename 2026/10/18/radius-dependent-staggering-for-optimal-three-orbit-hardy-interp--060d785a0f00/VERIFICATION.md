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

The result follows from exact discriminant and resultant identities, convexity of a quadratic in the mean-angle cosine, and a unique scalar critical point in a bounded interval. All angles and boundary cases are covered in the proof.

The standalone `check.py` requires Python 3, NumPy and SciPy. Run `python check.py`. On the tested configurations it compares directly evaluated monomial Vandermonde Gram determinants to the closed product formula for 30 parameter cases and independently checks 10 numerical two-angle global optima and 10 strict comparisons against equal stagger. It printed `PASS 30 determinant tests, 10 global optimization tests, and 10 strict inequalities`.

Separately, exact symbolic arithmetic at \(m=2\), \(r=1/2\), \(s=1\), \(\alpha=\pi\), \(\beta=0\) gave \(50625/262144\) for both the direct Gram determinant and the cross-resultant formula, and the radical series begins \(-2q+18q^3+O(q^5)\). These are supporting checks, not exhaustive empirical proofs. The source comparison covers the named full mathematical sources and accessible older abstract; an unindexed prior equivalent may remain.
