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
The universal theorem is proved analytically in `RESULT.md`.

For
\[
r=\frac{D\Delta t}{\Delta x^2},
\qquad
\beta=\frac{r}{1+r},
\qquad
\gamma=\frac{1-r}{1+r},
\]
the claimed obstruction for every \(n\ge2\) is
\[
(P_n(r))_{n1}
=
\beta^{\,n-1}\gamma(1+\gamma)
=
\frac{2r^{\,n-1}(1-r)}
{(1+r)^{n+1}}.
\]

The embedded `verify.py` constructs the left-to-right and right-to-left matrices directly from their recurrences, using exact rational arithmetic. It checks:

1. the corner formula for dimensions \(2\) through \(9\) and several rational step ratios;
2. entrywise nonnegativity for representative ratios in the interval \(0\le r\le1\);
3. the one-node identity
\[
P_1(r)=\gamma^2;
\]
4. the exact witness
\[
n=2,\qquad r=2,\qquad (P_2)_{21}=-\frac4{27}.
\]

The finite checks corroborate the derivation. They do not substitute for the all-dimension induction and closed-entry proof.

Unproved limits include periodic or nonhomogeneous boundaries, variable coefficients, modified Saul'yev coefficients, half-step compositions, group-explicit variants, nonlinear diffusion, and finite precision.
