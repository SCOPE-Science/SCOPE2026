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

The scientific check is analytic. For an invariant measure with compact support in the strict positive octant, differentiating \(\log Z\) along the flow and averaging gives the exact predator per-capita balance. Rewriting the Holling-II response as \(m_2(1-\alpha_2/(\alpha_2+P))\) gives the shifted reciprocal mean exactly.

The reciprocal decomposition
\[
\frac{1}{\alpha_2+P}=\frac{1}{\alpha_2+\bar P}-\frac{P-\bar P}{(\alpha_2+\bar P)^2}+\frac{(P-\bar P)^2}{(\alpha_2+P)(\alpha_2+\bar P)^2}
\]
was expanded directly and averaged. Its last term is nonnegative and vanishes exactly when \(P\) is constant almost surely. The model equations then reduce the equality case to the coexistence equilibrium.

For periodic orbits, normalized time measure is invariant. The exact reciprocal mean cannot equal the reciprocal at \(p_*\) if the nonconstant function \(P(t)\) stays entirely on one strict side of \(p_*\); hence the cycle crosses that level.

The exact illustrative parameter calculations are \(p_*=1/4\) and \(\alpha_2+p_*=3/4\) when \(D_2=1\), and \(p_*=13/34\) and \(\alpha_2+p_*=15/17\) when \(D_2=13/10\), for \(\alpha_2=1/2\), \(\gamma_2=3/2\), and \(m_2=2\).

Limits: no numerical trajectory was used to prove the theorem; no boundary, stochastic, delay, arbitrary-response, existence, uniqueness, or stability conclusion was inferred.
