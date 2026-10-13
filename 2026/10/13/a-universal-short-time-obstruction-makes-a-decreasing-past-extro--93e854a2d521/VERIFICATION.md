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
The defining conditional density is \(g_t(x)=f_Z(x)/F_Z(t)\) on \(0<x<t\), with \(\int_0^t g_t(x)\,dx=1\).

Cauchy–Schwarz gives
\[
1\le t\int_0^t g_t(x)^2\,dx,
\]
hence
\[
\bar J(Z;t)=-\frac12\int_0^t g_t(x)^2\,dx\le-\frac1{2t}.
\]

Thus for every real \(M\) there exists sufficiently small \(t>0\) with \(\bar J(Z;t)<M\). In particular, for any fixed \(t_0>0\) with finite \(\bar J(Z;t_0)\), sufficiently small \(s<t_0\) satisfies \(\bar J(Z;s)<\bar J(Z;t_0)\), contradicting nonincreasing behavior.

The target source was checked at the actual full-text theorem location: it requires the past-extropy functions to be well-defined and decreasing on \((0,\infty)\), and the paper states that “decreasing” is used in the non-strict sense.

No computation, asymptotic approximation, or finite experiment is needed. No claim is made about monotonicity on intervals bounded away from zero.
