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
The universal statement is proved analytically from the scalar spectral recurrence.

With
\[
q=\frac{\lambda}{L},
\]
the first four modal multipliers are
\[
p_1=1-q,
\qquad
p_2=(1-q)^2,
\]
\[
p_3=(1-q)^2(1-aq),
\qquad
p_4=(1-q)^3(1-cq).
\]
The fourth-step squared-amplitude difference has the exact factorization
\[
(1-q)^4q\,[a+cq-c-1]\,[cq^2-(a+c+1)q+2].
\]
Its positive region inside \((0,1)\) is exactly
\[
q_-<q<q_+.
\]
Consequently the normalized spectrum \([1/\kappa,1]\) avoids every fourth-step increase if and only if
\[
\kappa\le\frac1{q_+}.
\]

The embedded `verify.py` uses only the Python standard library. It reconstructs the FISTA coefficients at high precision, checks the root ordering and numerical enclosures, replays representative modal signs, and directly computes the \(\kappa=4/3\) witness ratio
\[
\frac{f(x_4)}{f(x_3)}=5.9852687051217627\ldots.
\]

The numerical checker corroborates the displayed constants. The sharp all-SPD conclusion follows from the exact factorization, not from finite sampling.

No later-iterate monotonicity theorem, nonsmooth proximal extension, restart analysis, backtracking analysis, or inexact-gradient statement is claimed.
