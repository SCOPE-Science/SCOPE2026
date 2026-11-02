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

## Reproduction

Run `python verify.py` with Python 3.10 or later; only the standard library is needed. It should print `PASS: 2975 exact assertions`. The verifier generates directed parent assignments independently of the weighted forest-volume formula, checks root reachability and cycle absence, then compares exact fractions with independently evolved occupancy distributions.

## Proof versus finite checks

The independent finite enumeration covers all fixed-root models through eight vertices with at least two nonroot vertices, and additional occupancy-based tests cover root counts up to 15 and nonroot counts up to 18. These are finite checks only. The all-parameter statements are proved analytically in `RESULT.md`. All rational operations in the verifier use `fractions.Fraction`; neither a numerical tolerance nor Monte Carlo sampling is used.

## Boundaries

An isolated root has degree zero and is not counted as a leaf. There are always at least two nonroot vertices, and strict conditional-mean increase is asserted for at least two roots. The result does not provide a complete stochastic-order classification for every adjacent root-edge count. Independent audit remains unperformed.
