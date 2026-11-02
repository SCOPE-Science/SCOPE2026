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

# Verification and reproducibility

Run `python verification/check.py` with Python 3.10 or newer and SymPy installed. The verification uses exact fractions, not floating-point probabilities. Ten bipartite graph families, including nonuniformly weighted paths, cycles and complete-bipartite graphs, are checked at preference strengths \(h=1/3\) and \(h=3/4\). Across their 456 opinion configurations, exact one-step conditional drift agrees with the analytical edge-sum identity and vanishes. The independent absorbing-chain linear-system solutions match the degree-weighted fixation probability in 292 transient states. A triangle with one biased vertex provides the nonzero-drift contrast \(1/54\); fully polarized states have non-change probability \((1+h)/2\).

The script uses matrix inversion only for small finite examples, with the six-vertex case checked by conditional drift rather than solving the full absorbing chain. These tests do not certify the theorem for all graphs: the published proof is the edgewise drift calculation, cut-identity necessity, graph bipartition argument, finite-state absorption, and bounded martingale passage to absorption. Stochastic simulations are not invoked. The limits at \(h=1\), directed/asymmetric weighting, and infinite graphs are not asserted.
