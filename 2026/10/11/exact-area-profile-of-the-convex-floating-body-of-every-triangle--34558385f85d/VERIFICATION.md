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

For barycentric coordinates
\[
\alpha+\beta+\gamma=1,
\]
the triangle halfspace-depth formula is
\[
D=4\min\{\alpha\beta,\beta\gamma,\gamma\alpha\}.
\]

In the chamber
\[
\alpha\ge\beta\ge\gamma,
\]
put
\[
q=\frac{\tau}{4},
\qquad
r=\frac{1-\sqrt{1-8q}}2.
\]
The normalized area is exactly twelve times
\[
\int_r^{\sqrt q}
\left(
\frac{1-\gamma}{2}-\frac q\gamma
\right)d\gamma
+
\int_{\sqrt q}^{1/3}
\left(
\frac{1-\gamma}{2}-\gamma
\right)d\gamma.
\]

The symbolic checker evaluates this expression and verifies that it equals
\[
\frac32\sqrt{1-2\tau}-\frac12
+
\frac{3\tau}{2}
\log\!\left(
\frac{2(1-\sqrt{1-2\tau})}
{1+\sqrt{1-2\tau}}
\right).
\]

It also checks the centroid extinction level
\[
\tau=\frac49
\]
and the small-level expansion. A fixed-seed Monte Carlo calculation over uniformly sampled barycentric points provides a separate numerical regression test.

The finite sampling is not evidence for the quantified theorem. The proof is the exact barycentric reduction and symbolic integral above.
