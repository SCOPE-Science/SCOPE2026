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

The proof is exact and symbolic. For \(F=x_1x_2x_3x_4+q^2\) in characteristic \(2\), direct differentiation gives the four cubic edge-ideal generators because \(d(q^2)=0\). Localizing at an interior edge point reduces the edge ideal to the two transverse coordinates, and a simple root of the binary edge restriction makes \(q\) a third local coordinate. This gives completed local equation \(uv+w^2\) and local Jacobian quotient with basis \(1,w\).

The bundled `artifacts/verify.py` is a finite exact consistency check. It constructs the witness \(q_0=\sum_i x_i^2+\sum_{i<j}x_ix_j\), verifies the formal derivative pattern over \(\mathbb F_2\), enumerates the two roots of \(s^2+st+t^2\) on each of the six edges over \(\mathbb F_4\), and checks that all twelve projective points are distinct and satisfy the quartic and all four partial derivatives. It also verifies that no tetrahedron vertex lies on the witness quadric and records the resulting Jacobian-scheme length \(24\).

The finite-field witness is not used to infer the universal theorem. The universal direction and converse are supplied by the binary-quadratic argument in `RESULT.md`. No claim is made about characteristic different from \(2\), unmarked projective equivalence classes, or a classification of boundary degenerations.
