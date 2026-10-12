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
The universal proof is analytic.

For every nonzero residual, exact line search gives
\[
\alpha_k^{-1}
=
\frac{r_k^{\mathsf T}Ar_k}{r_k^{\mathsf T}r_k}
\in[\mu,L].
\]
When \(\kappa\le2\), each normalized residual coordinate is multiplied by a number in \([-1,1]\), proving all-iteration componentwise nonnegativity.

In dimension two, direct elimination gives the exact two-step residual law
\[
r_{k+2}
=
\frac{(c-a)^2u^2v^2}
{(au^2+cv^2)(av^2+cu^2)}\,r_k.
\]
The multiplier lies in \([0,1)\), because subtracting its numerator from its denominator gives
\[
ac(u^2+v^2)^2>0.
\]

For every \(\kappa>2\), the three-dimensional family
\[
A_\kappa=\operatorname{diag}(1,\kappa/2,\kappa),
\qquad
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T}
\]
has a second-iterate high-mode numerator tending to \(1-\kappa/2<0\).

The embedded `verify.py` uses exact `Fraction` arithmetic. It checks the explicit \(\kappa=4\) witness and a nontrivial two-dimensional residual-cycle instance. Finite calculations are witness replays only.

Unproved limits include nondiagonal Hessians, nonzero starting points, inexact line searches, projected variants, and finite-precision sign robustness.
