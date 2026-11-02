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

# Analytical and computational verification

1. Reconstruct the stationary generator recurrence for mixed monomials \(\mathbb E[X^pY^q]\). The checker reproduces the exact published \(m_2,m_4,m_6\) rational functions using an independently ordered computation, rather than assuming these expressions.
2. Symbolically divide the position moments to obtain \(K\) and \(H\). Verify the exact bivariate equality polynomial, the critical derivative, the second-root involution, and the sixth-order separation identity with symbolic factorization.
3. For \(0<b<9\), the positive residual contributions obey \(357b^6+2030b^5<(357\cdot81+2030\cdot9)b^4=47187b^4<436986b^4\). All other residual coefficients are negative. This proves the strict inequality over the complete interval without numerical sampling.
4. Construct two exact rational positive parameter pairs with the same normalized fourth moment, scale them to a common variance, and verify a nonzero normalized sixth-moment difference.

Run `python checker.py` after installing `requirements.txt`. The test code checks exact symbolic equalities, not merely floating-point examples. Even a successful finite test does not itself establish the global theorem; the global proof is in `RESULT.md`.

**Unverified:** independent review, publication-priority completeness, finite-sample conditioning guarantees, other driving laws, and absolute-parameter identification.
