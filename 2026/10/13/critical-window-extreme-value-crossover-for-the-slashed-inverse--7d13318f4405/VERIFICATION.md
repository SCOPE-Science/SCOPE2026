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
# Verification record

Run `python verify_sir_crossover.py` with Python 3, `mpmath`, and `scipy`. The checker directly evaluates the exact incomplete-gamma survival, independently integrates \(\Pr(Z_q>z)=\mathbb E[1-\exp\{-\theta/(z^2Y_q^2)\}]\), compares three tail regimes as context, and tests first- and second-order critical-window expressions. All scripted numerical checks passed, including 14 cross-representation comparisons and five moving-parameter second-order tests.

The proof in `RESULT.md` is independent of numerical results. The critical nonstandard step is the uniform remainder estimate: after removing the elementary singular kernel, \(R_0(\eta)\) is continuously differentiable for \(|\eta|<1/2\) and equals \(-\gamma_{\mathrm E}\) at zero. The omitted interval \((0,a)\), when multiplied by \(a^\eta\), has error \(O(a)\). These estimates justify the two-term expansion; finite numerical observations alone cannot establish any asymptotic limit.

Limitations: \(w\) and \(\kappa\) are restricted to compact sets for uniform errors, and the extreme-value normalization applies to a rowwise independent triangular array with \(q_n=2+2\kappa/\log n\). The test environment does not constitute external validation. No independent audit has been performed.
