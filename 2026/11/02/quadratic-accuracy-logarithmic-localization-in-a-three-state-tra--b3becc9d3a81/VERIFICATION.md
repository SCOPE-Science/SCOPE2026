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

# Reproducibility and limits

The proof is a direct stationary-renewal argument with explicit integral bounds. The exact holding-age law and entry-state independence give the exponential reference distributions; the all-parameter integrable logarithm bounds give the quantitative total-variation inequalities. Dominated convergence applied to the two alternating holding durations gives the sharp first mean coefficients. These infinite-regime assertions are established in `RESULT.md` analytically, not by numerical approximation.

Run `python verify.py` (standard library only). It checks stationary internal-chain balance, the convergent dilogarithm series, quantitative entry-logarithm bounds for an exact-segment simulation, and agreement of independent finite-parameter estimates with the predicted asymptotic constants. The test is deliberately limited to finite samples and does not independently certify the proof or any unobserved parameter regime.

A publication-priority comparison was made against full primary text for the 2026 finite-tumble conditional distribution, the 2025 exact moment/density predecessor and the 2019 equal-rate three-state stationary solution. The known exact density formulas remain an implicit-coverage risk; independent literature and mathematical audits have not been performed.
