---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For unbiased initial sign S, E[S_sS_t]=exp(-2∫_s^t λ); integrate covariance to obtain D and justify long-time limit with geometric bound exp(-2Λ floor(u/T)). Period splitting gives D=v²/(1-exp(-2Λ))∫_0^T A(w)dw, A(w)=T^-1∫_0^T exp(-2∫_s^{s+w}λ)ds. Sliding hazards lie in [0,Λ] and have phase mean Λw/T. Strict Jensen lower bounds A; the chord from x=0 to Λ upper bounds it. Integrating proves both sharp constants. Equality in Jensen for almost every w plus Lebesgue differentiation forces λ constant a.e. Absolute continuity makes the upper-chord bound strict for positive small w for every L1 protocol; shrinking pulse protocols converge by dominated convergence to the extremal limit. Independent physical-time covariance integration for pulsed schedules confirmed strict bounds and monotone approach; this numerical check proves only selected schedules.

## originality

PASS

The telegraph and run-and-tumble covariance/diffusivity framework and constant-rate formula are classical. The asserted contribution is the universal extremal fixed-budget periodic time-allocation theorem for ALL measurable nonnegative deterministic rates, including strict optimizer conditions and singular supremum. The inspected contextual works concern general active matter or constant-transition-rate dynamics, and the targeted Resultary query did not locate a dominating theorem. A specialist covariance-design inequality under another name remains a priority risk.

## value

PASS

A mathematically natural infinite-dimensional optimization of long-time spreading under an exact reversal-frequency budget; it gives both extremizers, their uniqueness/strictness, and the finite enhancement factor Λ coth Λ. It distinguishes equivalent mean event rates with different physical diffusivities and is not merely the textbook homogeneous telegraph formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
