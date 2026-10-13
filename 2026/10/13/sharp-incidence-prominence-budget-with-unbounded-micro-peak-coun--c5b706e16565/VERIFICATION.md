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

The symbolic derivation in `RESULT.md` is the proof. The exact incidence derivative is obtained by differentiating the positive SIR incidence; integrating it proves the drop budget. The Gaussian construction is assessed with exact state bounds \(S\geq18/25\), \(I\leq2/17\), \(39/10<\beta\leq4\), \(2867/2125\leq H\leq13/5\); these yield positive incidence-growth derivative at all pulse midpoints, negative derivative at all centers, and strictly positive infectious growth everywhere.

Execute `python verify.py` using Python 3 standard library. The checked execution returned `VERIFY_OK: rational guards and five independent sampled Gaussian schedules`. The checker uses exact rational comparisons for the theorem's finite numerical constants and finite RK4 runs for illustrative values of pulse count one, two, four, seven and twelve. These checks are neither an exhaustive enumeration nor a proof for arbitrarily large pulse count. The unlimited-count and sharpness conclusions come from the written analytic comparisons and the shrinking-width limits, not from a finite checker.

The quantitative prominence inequality is established only for ordered disjoint intervals and nonnegative \(H\); the analytic construction only guarantees arbitrarily many strict, potentially tiny peaks. No tests of noisy observations, discrete aggregation, or intervention outcomes are asserted. An independent scientific audit has not been performed.
