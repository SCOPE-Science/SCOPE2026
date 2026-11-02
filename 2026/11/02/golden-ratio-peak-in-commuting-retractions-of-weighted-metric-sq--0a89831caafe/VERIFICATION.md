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

For the metric \(d_{a,b}\) on \(\{0,1\}^2\), the lower bound is proved by a nine-case penultimate-retraction table; it does not assume any particular predecessor assignments. The upper bound is achieved by the explicit commuting maps in the proof. The analytic branch comparison establishes the golden-ratio maximizing aspect ratio for all positive real weights.

The accompanying standalone checker `check_weighted_square.py` directly enumerates six orderings of the three nonroot vertices, four assignments of the two unselected vertices at stage two, and compatible third-stage images. It evaluates Lipschitz constants exactly for all four-point pairs using `Fraction` and compares minima with the formula for 210 integer-weight pairs and two rational-weight pairs. Execution result: `PASS 212 weight pairs, 7632 commuting filtration candidates`. Reproduce with `python3 check_weighted_square.py` using only Python standard-library modules.

Limits: finite exact checks corroborate but do not prove the real-parameter theorem; the finite lower-bound table and constructions supply the proof. Published-literature coverage was checked by targeted full-text reading where accessible and semantic indexing, not exhaustively over all historic mathematical publications. No independent validation has been performed.
