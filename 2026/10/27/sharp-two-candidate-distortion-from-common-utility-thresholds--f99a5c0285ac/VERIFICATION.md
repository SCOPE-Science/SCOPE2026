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
# Exact checks and reproducibility

Run the included `verify_two_candidate_thresholds.py` using Python 3 and only its standard library. The program performs a complete exact-rational enumeration of all reported utility-cell profiles for one, two and three voters, for each \(t\)-element threshold subset of \(\{1/10,2/10,\ldots,9/10\}\) with \(t\in\{1,2,3\}\). For each profile, it verifies that the best deterministic choice and the proposed midpoint rule do not exceed \((1+w)/(1-w)\). For each tested threshold set, it confirms that a maximum-width cell paired with its reflection attains the same ratio at two voters. It separately checks all \(2^t\) uniform-mesh threshold selections for \(1\leq t\leq8\) and the algebraic \(1+1/t\) optimum. The executed program prints `PASS: 639 threshold vectors; 57568 exact-rational assertions.`

These finite checks are not an exhaustive computation over arbitrary real-valued thresholds, all voter counts, or all algorithms. The all-quantified conclusion follows from the independent mathematical proof by interval enclosure and two-profile indistinguishability. For boundary values at bin cuts, interpret endpoint lower bounds as limiting feasible profiles from cell interiors. Independent audit has not been performed.
