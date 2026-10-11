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

For the one-point example,
\[
F_1=F_2=1,
\qquad
G_1=G_2=-1.
\]
Thus for every scalar \(z\),
\[
q_i(z)
=
\langle z,1\rangle\langle-1,z\rangle
=
-|z|^2.
\]
No positive lower biframe inequality is possible.

On the tensor product,
\[
F_1\otimes F_2=1,
\qquad
G_1\otimes G_2=1,
\]
hence
\[
q_{\otimes}(z\otimes w)
=
|z|^2|w|^2
=
\|z\otimes w\|^2.
\]
The tensor pair is therefore Parseval.

For the phase classification, suppose
\[
A\|f\|^2\|g\|^2
\le
q_1(f)q_2(g)
\le
B\|f\|^2\|g\|^2.
\]
Fix unit \(g_0\) and let
\[
\zeta=\frac{q_2(g_0)}{|q_2(g_0)|}.
\]
Then
\[
\zeta q_1(f)
=
\frac{q_1(f)q_2(g_0)}{|q_2(g_0)|}
\]
is positive and obeys the factor biframe bounds obtained by dividing by \(|q_2(g_0)|\). Fixing a unit \(f_0\) gives the reciprocal bounds for \(\zeta^{-1}q_2(g)\). Conversely,
\[
(\zeta G_1)\otimes(\zeta^{-1}G_2)
=
G_1\otimes G_2,
\]
so positive rotated factor inequalities multiply to the original tensor inequality.

The target theorem and its complete proof were inspected in the first public full text, including the step that divides by a merely nonzero factor integral. The later Hilbert-\(C^*\)-module tensor theorem was inspected as a broader comparison. No numerical experiment or finite search is used as mathematical evidence.
