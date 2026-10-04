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

The proof has three critical components.

First, under \(A\in\operatorname{GL}(d)\), the hyperplane-section Jacobian contributes
\[
\frac{|\det A|}{\lVert A^Tu\rVert},
\]
while width contributes \(\lVert A^Tu\rVert\) and total volume contributes \(|\det A|\). Their cancellation gives the exact directional identity
\[
F_{AK}(u)=F_K\!\left(\frac{A^Tu}{\lVert A^Tu\rVert}\right).
\]

Second, for an ordered cube normal \(a\ge b\ge c\ge0\), direct plane parameterization gives
\[
\lambda_2(C\cap u^\perp)=\frac4a
\]
when \(a\ge b+c\), and
\[
\lambda_2(C\cap u^\perp)
=
\frac{2(ab+ac+bc)-(a^2+b^2+c^2)}{abc}
\]
when \(a<b+c\).

Third, in the latter chamber the substitution
\[
a=y+z,
\qquad b=z+x,
\qquad c=x+y
\]
gives the exact differences
\[
s(2P-Q)-8abc=8xyz
\]
and
\[
9abc-s(2P-Q)
=
(x+y+z)(xy+xz+yz)-9xyz.
\]
The first is positive, and the second is nonnegative by AM-GM, with equality only when \(x=y=z\).

The embedded `verify.py` was replayed from its actual package path. It checks the polynomial identities in exact rational arithmetic; independently reconstructs central section polygons from the twelve cube edges; compares those polygonal areas against the analytic formula for random directions; and repeats the geometric calculation after random invertible linear maps to test affine covariance.

Replay output:

`VERIFY_OK parallelotope Busemann-Petty profile`

The finite replay is a consistency check. The all-direction theorem and equality classifications are supplied by the analytic proof.
