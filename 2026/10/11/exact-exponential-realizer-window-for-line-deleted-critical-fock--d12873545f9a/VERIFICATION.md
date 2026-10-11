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

Let
\[
s=\sqrt\pi
\]
and let \(g_N\) be the source function for the line-deleted lattice zero divisor \(\Sigma_N\).

The source estimates give, outside a compact set,
\[
|g_N(z)|^2e^{-|z|^2}
\le
C_N e^{-2s|\operatorname{Re}z|}(1+|z|^2)^{-N},
\]
and on every sufficiently remote shifted cell disk,
\[
|g_N(z)|^2e^{-|z|^2}
\ge
c_N e^{-2s|\operatorname{Re}z|}(1+|z|^2)^{-N}.
\]

The source Hadamard lemma reduces every exact realizer to
\[
F=C e^{Az^2+Bz}g_N.
\]
If \(A\ne0\), choose a sector on which \(\operatorname{Re}(Az^2)\) is positive quadratic; the lower cell estimate forces divergence. If \(\operatorname{Im}B\ne0\), vertical cells force exponential divergence. Thus
\[
A=0,
\qquad
B=t\in\mathbb R.
\]

For real \(t\), the upper estimate proves membership whenever
\[
|t|<s.
\]
At \(|t|=s\), one half-plane has only the tail
\[
(1+|z|^2)^{-N},
\]
which is integrable in the plane exactly when \(N\ge2\). For \(N=1\), the lower cells with positive horizontal index \(p\) and \(|q|\le p\) yield the divergent lower sum
\[
\sum_{p\ge P}\sum_{|q|\le p}(p^2+q^2)^{-1}.
\]
For \(|t|>s\), a horizontal cell sequence has exponential growth.

These cases prove the complete iff classification. No numerical experiment or finite extrapolation is used.
