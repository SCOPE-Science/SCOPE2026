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

For \(p=3\) there is exactly one complementary character pair in the source's codifferential formula.

At \(m=2\), the source gives degrees
\[
(1,1).
\]
The two section spaces are one-dimensional, and their nonzero product gives rank
\[
1.
\]

At \(m=3\), the source gives degrees
\[
(1,2)
\]
up to order. Multiplication by the unique nonzero section of the degree-one line bundle injects the two-dimensional section space of the degree-two line bundle into the three-dimensional target, giving rank
\[
2.
\]

The source parameter dimensions are \(2\) and \(3\), so both generic fiber dimensions equal
\[
1.
\]

For an order-\(3\) Hodge decomposition with nontrivial eigenspace multiplicities \((a,b)\), the invariant part of
\[
\operatorname{Sym}^2(V_\zeta^\vee\oplus V_{\zeta^2}^\vee)
\]
is exactly
\[
V_\zeta^\vee\otimes V_{\zeta^2}^\vee
\]
and has dimension \(ab\). Thus the invariant tangent dimensions are \(1\) and \(2\), matching the two Prym–Tyurin differential ranks.

The packaged verifier checks all dimension identities and ends in `VERIFY_OK`. It does not replace the geometric multiplication-map or deformation-theoretic arguments.
