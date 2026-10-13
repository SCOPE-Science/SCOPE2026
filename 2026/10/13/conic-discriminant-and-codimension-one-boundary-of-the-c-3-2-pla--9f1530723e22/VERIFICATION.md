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

The exact checker `verify.py` was replayed from the packaged artifact against SymPy 1.14.0.

It checks the identity \(F(X,Y,Z)=Q(X^3,Y^3,Z^3)\), all three factored partial derivatives, \(\det M=2\Delta\), the conic determinant \(\Delta/4\), and the three coordinate-side discriminants. It also checks all six identities describing where a side-tangency component meets the conic-discriminant component, the local quadratic/cubic leading coefficients for \(b=\pm2\), a rank-two \(\Delta=0\) witness with singular point off the coordinate triangle, and the Riemann--Hurwitz equality.

Fresh output:

`VERIFY_OK sympy=1.14.0 pullback=conic smoothness_product=exact branch=6x3 boundary=tangency:3A2,conic-discriminant:9nodes`

The checker does not attempt to classify higher-codimension intersections of discriminant components. The assertions that a rank-two projective conic is a pair of distinct lines and that an etale map preserves transverse crossings are proved in the accompanying result and are not replaced by numerical experimentation.
