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
The packaged `verify.py` uses only the Python standard library.

It verifies by exact sparse-polynomial arithmetic that
\[
L\left(\frac{x^2+y^2}{2}\right)
=
a x^2-a xy-b y^2.
\]

It checks the factor relations
\[
k_+-k_-=1,
\qquad
k_+k_-=\frac ba
\]
through the common quadratic
\[
ak^2-ak-b=0,
\]
and verifies the support-tangency reduction
\[
a(k-1)+kb
=
a(k-1)(1+k^2)
\]
under that relation.

For the published three-scroll parameters
\[
a=0.977,\qquad b=10,\qquad c=4,\qquad d=0.1,
\]
the checker computes the two equilibrium heights and independently confirms that
\[
\frac b{z_+}=k_+,
\qquad
\frac b{z_-}=-k_-,
\]
to high precision.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The checker validates the critical algebra. The conditional laws require arbitrary antiderivative test functions, and the equality classification additionally uses invariant-support tangency and bounded completeness.
