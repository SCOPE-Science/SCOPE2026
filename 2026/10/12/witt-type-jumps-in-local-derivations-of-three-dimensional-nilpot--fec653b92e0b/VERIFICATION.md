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

Run the standalone checker with `python3 artifacts/verify.py` from the artifact root. It uses Python 3 and SymPy.

The checker symbolically verifies the multiplication of the three-dimensional algebra, the complete four-parameter derivation matrix, the Leibniz rule for all nine ordered basis products, and the identity
\[
\det(v,J_dv)=x^2+d y^2.
\]
For every nonzero \(d\) in each of \(\mathbf F_3,\mathbf F_5,\mathbf F_7,\mathbf F_{11}\), it exhaustively tests all \(q^4\) two-dimensional matrix blocks against the necessary-and-sufficient pointwise evaluation condition and checks the split/nonsplit dimensions. Over \(\mathbf F_3\), it also enumerates every candidate linear map preserving the derived line and every algebra element, explicitly compares the map's value to the set of values attained by all derivations, and recovers \(2187\) local maps in the anisotropic case and \(243\) in the split case, against \(81\) actual derivations in either case. The checker returns `VERIFY_OK`.

These finite enumerations are replay evidence only; the proof for arbitrary fields of characteristic different from \(2\) is the exact matrix and quadratic-form argument in `RESULT.md`. The counts do not include nonlinear 2-local maps. Independent audit: not performed.
