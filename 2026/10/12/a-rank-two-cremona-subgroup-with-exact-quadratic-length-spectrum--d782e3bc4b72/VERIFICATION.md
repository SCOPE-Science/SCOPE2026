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

The accompanying `verify.py` uses only the Python standard library.

It verifies the following exact statements:

1. The affine translation vectors of the two generators are \((1,0)\) and \((1,1)\) in the coefficient basis \((y^4,y^2)\), so \(\phi_0^m\phi_1^n\) has coefficient pair \((m+n,n)\).
2. On a symmetric finite integer window, direct group-law, inverse, injectivity, and case-split assertions are replayed; the symbolic formulas themselves are independent of that finite window.
3. If \(a=0\) and \(b\ne0\), the projective closure has degree \(2\).
4. If \(a\ne0,b=0\), diagonal scaling normalizes the quartic coefficient to \(1\).
5. If \(a\ne0,b\ne0\), setting \(\beta^2=b/a\) and \(\alpha=b^2/a\) makes both normalized coefficients exactly \(1\), checked by rational identities.

The checker does not attempt to reprove Calabri--Nguyen's classification theorem. The imported non-elementary premise is their verified statement that both extremal quartic normal forms have quadratic length \(5\), together with invariance of quadratic length under source/target projective automorphisms. These were checked in arXiv:2609.39943v1.

Limits: algebraic closedness is used for the square root \(\beta\); characteristic zero is used for the faithful embedding of integer coefficients. Positive characteristic and nonclosed fields are not covered.
