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
# Verification record

The final claim was checked in two layers.

First, the geometric proof was reconstructed from the explicit reduced component decomposition of the Fermat second-type locus and Zhang's matrix criterion for higher triple lines. The key equivalence is that, on each disjoint-support component, the relevant second-order pencil is block diagonal and degenerates exactly when a Fermat block second fundamental form is singular. For a Fermat factor of size \(r\), its Hessian determinant is \(6^r\prod z_i\), so in block sizes \(3\) and \(4\) this is exactly the coordinate-vanishing condition that also characterizes overlap of distinct reduced components.

Second, `artifacts/verify_fermat_htl.py` symbolically recomputes the two Hessian determinants and exhaustively checks the finite combinatorics. Its recorded output in `artifacts/verification_output.txt` is:

`HESSIAN_r3=216*x0*x1*x2`

`HESSIAN_r4=1296*x0*x1*x2*x3`

`CUBIC_COMPONENTS=45`

`PRODUCT_COMPONENTS=10`

`HTL_CURVES=180`

`DEEP_POINTS=405`

`CURVES_PER_CUBIC_COMPONENT=4`

`CURVES_PER_PRODUCT_COMPONENT=18`

`DEEP_POINTS_PER_CURVE=9`

`CURVES_THROUGH_DEEP_POINT=4`

`VERIFY_OK`

The script verifies finite Hessian algebra and incidence counts only. It is not used as evidence for any unbounded or scheme-theoretic claim. The result is limited to the set-theoretic singular locus of the reduced second-type locus; nonreduced multiplicities, local analytic types, and transversality are unproved here.
