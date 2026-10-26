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

The standalone standard-library checker `verify.py` checks the entire labeled Gibbs partition distribution through size 5, exact rational transition-row and transition-column sums through size 8, conditional probability monotonicity through size 25, and sampled simultaneous refinements through size 17. Invocation: `python verify.py`. Expected success includes 75 partition-probability checks, 494 adjacent-transition checks, 2600 monotonicity checks and 1632 refinement edges. The proof in RESULT.md, rather than numerical extrapolation, establishes all finite sizes. Historical priority is provisional.
