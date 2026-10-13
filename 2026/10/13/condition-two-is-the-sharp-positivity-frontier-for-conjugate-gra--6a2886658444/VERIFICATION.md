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
The all-dimensional proof is analytic.

For active diagonal data, CG gives
\[
r_k=p_k(A)b,
\qquad
p_k(0)=1,
\]
and residual orthogonality makes \(p_k\) the degree-\(k\) orthogonal polynomial for the positive spectral measure \(\sum_i b_i^2\delta_{\lambda_i}\). Its roots are Ritz values in the active spectral interval, so when \(\kappa\le2\) every factor \(1-\lambda_i/\theta_j\) lies in \([-1,1]\). This gives \(|p_k(\lambda_i)|\le1\) and hence coordinatewise nonnegativity.

Sharpness uses the three-mode family
\[
A_\kappa=\operatorname{diag}(1,\kappa/2,\kappa),
\qquad
b_\varepsilon=(1,1,\varepsilon)^{\mathsf T}.
\]
As \(\varepsilon\downarrow0\), its degree-two CG residual polynomial converges to
\[
(1-\lambda)(1-2\lambda/\kappa),
\]
whose value at the high mode is \(\kappa-1>1\) when \(\kappa>2\).

The embedded `verify.py` uses exact rational arithmetic. It replays the explicit \(\kappa=4\) three-dimensional counterexample and a two-dimensional exact-termination example. Those finite checks corroborate displayed witnesses only.

Unproved limits include nondiagonal systems, finite-precision loss of CG orthogonality, nonzero starting points, inexact line search, and quasi-Newton updates outside the stated identical-iterate setting.
