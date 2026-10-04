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

For each latent uniform \(U_j\), the Cauchy transform \(C_j=\tan\{\pi(1/2-U_j)\}\) is standard Cauchy and the complementary p-value \(1-U_j\) transforms to \(-C_j\). The weighted statistic is therefore \(T=\sum_j d_jC_j\) with \(d_j=w_{j,+}-w_{j,-}\).

Independence across the latent pairs gives
\[
\mathbb E e^{itT}=\prod_j e^{-|d_jt|}=e^{-A|t|},
\qquad
A=\sum_j|d_j|,
\]
so the null law is exactly \(\mathrm{Cauchy}(0,A)\). The identity \(|x-y|=x+y-2\min(x,y)\) for nonnegative weights gives \(A=1-2\sum_j\min(w_{j,+},w_{j,-})\). This proves both the scale and the exact weight criteria without simulation.

The accompanying `verify.py` recomputes cancellation budgets for deterministic examples, checks the one-pair numerical values at \(\alpha=0.05\), checks exact and degenerate endpoints, and checks the small-level ratio. These are transcription checks only; the analytic characteristic-function argument proves the theorem for arbitrary finite \(m\).

The verification does not address imperfect complementarity, dependence among latent pairs, random weights, or truncated/positive Cauchy variants.
