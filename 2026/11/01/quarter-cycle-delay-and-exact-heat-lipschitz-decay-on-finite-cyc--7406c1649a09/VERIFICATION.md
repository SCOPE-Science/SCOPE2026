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

The all-size proof uses graph-metric Kantorovich duality, an exact circular-flow reduction, strict positivity of a tridiagonal cooperative system, four exhaustive median-count cases, shortest-walk Taylor coefficients, and the Fourier spectrum of cycles.

Execute the standalone `verify_cycle.py` using Python 3 (no third-party packages). The executed copy printed:

`CHECK_OK cycle_sizes=78 spectral_coefficients=78 heat_dual_instances=132 exact_Taylor_coefficients=897`

The 132 numerical instances use an independently solved finite Lipschitz dual, represented by integral edge gradients. The integrality reduction follows because any vertex of the cube slice \(\{g\in[-1,1]^n:\sum_jg_j=0\}\) has all but at most one coordinate at a sign endpoint; the last coordinate must be one of \(-1,0,1\). This dual optimization is independent of the radial median selection. The 897 checks use exact integer matrix powers to test vanishing lower Taylor coefficients and the first nonzero coefficient. The 78 spectral comparisons use trigonometric identities in floating-point arithmetic. These tests corroborate only the checked finite cases, not the infinite quantifiers.

Scientific limits: only combinatorial continuous-time heat on simple unit-edge cycles with shortest-path Wasserstein-1 metric and real graph-Lipschitz seminorm is treated. The general circular histogram median formula is earlier mathematics and not a novelty claim. Independent scientific validation has not been performed.
