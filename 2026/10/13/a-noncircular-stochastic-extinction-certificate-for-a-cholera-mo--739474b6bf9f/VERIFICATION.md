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
The analytic verification has three parts.

First,
\[
k(g)
=
\xi^2\frac{\zeta}{\sqrt{\zeta^2+(gH\xi)^2}}
\]
is strictly decreasing for \(g>0\), with limits
\[
k(0^+)=\xi^2,
\qquad
k(\infty)=0.
\]
This proves the stated range of \(R^*(g)\).

Second, the environmental coefficient is negative exactly for
\[
g>g_0=\frac{\beta_cH}{\omega K}.
\]
The infected coefficient is bounded by
\[
F(g)-\mu_1,
\qquad
F(g)=\Phi(g)+g\sigma.
\]
Because \(F\) is strictly increasing, a feasible \(g>g_0\) exists if and only if
\[
F(g_0)<\mu_1.
\]

Third, the bundled checker evaluates the published Section 6.3 parameters and confirms the strict certificate margin and the reported rounded value \(R^*(g_0)\approx0.905\). It also checks monotonicity numerically over a broad grid as a consistency test.

The numerical replay corroborates but does not replace the symbolic monotonicity and feasibility proof.
