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

The proof has two logically separate parts.

First, for every radius \(r\), the centered disk maximizes
\[
A\!\left(Q_a\cap B(c,r)\right)
\]
over the center \(c\). This follows from
\[
\frac12K_c(r)+\frac12K_{-c}(r)\subseteq K_0(r)
\]
and Brunn–Minkowski, using \(K_{-c}(r)=-K_c(r)\). Therefore any measurable subset with circumradius \(r\) has area at most the centered radius-\(r\) intersection area.

Second, for \(a\le r\le\sqrt2\,a\),
\[
A(r)
=
\pi r^2
-
4\left(
r^2\arccos(a/r)
-
a\sqrt{r^2-a^2}
\right),
\]
and
\[
A'(r)
=
2r\left(\pi-4\arccos(a/r)\right).
\]
The sign of the derivative of \(r/A(r)\) reduces to the sign of
\[
\cos x-x,
\qquad
x=\frac{\pi}{2}-2\arccos(a/r).
\]
Since \(\cos x-x\) has exactly one zero \(\alpha\in(0,\pi/2)\), the minimizer is unique at the radius level:
\[
r_*
=
a\sec\!\left(\frac{\pi}{4}-\frac{\alpha}{2}\right).
\]

At this radius,
\[
A(r_*)=4\alpha r_*^2,
\]
so
\[
\frac{r_*}{A(r_*)}
=
\frac{\cos(\pi/4-\alpha/2)}{4a\alpha}.
\]

The embedded `verify.py` was replayed from its package path before packaging and returned:

`VERIFY_OK square circumradius-area constant`

It checks the fixed-point equation, the exact area identity numerically to floating-point precision, the closed-form ratio, a dense independent radius scan, and one-sided perturbations of the critical radius.

The numerical replay is not used as an infinite proof and does not classify all equality cases.
