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

The checked claim is the recurrence and finite-partition optimization stated in `RESULT.md`.

For equal bisection, the critical source definitions are
\[
\mathcal F(h)=\int_{Q_{0,h}}\left(|\Delta_hg|^p-|h|^{p+\gamma}\right)_+,
\qquad
M(h)=|\{|\Delta_hg|>|h|^{1+\gamma/p}\}|.
\]
On the exceedance set, subtracting the full-step threshold after the standard two-term convexity estimate gives
\[
2^p|h/2|^{p+\gamma}-|h|^{p+\gamma}
=(2^{-\gamma}-1)|h|^{p+\gamma}.
\]
This is the only change needed to obtain the sharpened recurrence.

For a finite proportional partition \((t_i)_{i=1}^m\), the weighted-convexity coefficient on the substep threshold is checked by
\[
t_i^{1-p}|t_i h|^{p+\gamma}
=t_i^{\gamma+1}|h|^{p+\gamma}.
\]
Therefore the threshold surplus is exactly
\[
\sum_{i=1}^m t_i^{\gamma+1}-1.
\]
Because \(\gamma+1<0\), strict convexity and Jensen's inequality give
\[
\sum_{i=1}^m t_i^{\gamma+1}\ge m^{-\gamma},
\]
with equality only for equal parts. Since \(m^{-\gamma}\) increases strictly for integers \(m\ge2\), the unique global minimum is the equal bisection and equals \(2^{-\gamma}-1\) after subtracting one.

The source text was checked at the definitions, Lemma 4.4, its proof, the subsequent iteration, and the section on dependence of the global constant. The result is not interpreted as an exponential lower bound for the true global Poincaré constant. No independent audit has been performed.
