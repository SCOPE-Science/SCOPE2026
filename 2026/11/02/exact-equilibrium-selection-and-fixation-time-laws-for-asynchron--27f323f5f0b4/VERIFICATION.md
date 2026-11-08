---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

On labeled complete bipartite K_{a,b}, a,b>=1, independently uniform with-replacement vertex update (null updates counted), before one side empties all initially active vertices deactivate at first update and inactive vertices remain inactive. Their first-update ordering is a uniformly random permutation. Last survivor side gives P(P_A)=i/(i+j), and exact joint suffix mass wA_k=C(i+j-k-1,j-1)/C(i+j,j) (and symmetric wB). Independent Poisson(1) clocks yield commitment E tau=H_i+H_j-H_{i+j}; memoryless completion adds wA_k H_{a-k}+wB_l H_{b-l}. Multiply time by a+b to get expected discrete tick count. Edge cases i=0 or j=0 and both zero are derived separately. Balanced all-producer asymptotic E S=4m log m+(4gamma-2log2)m+o(m) follows geometric-tail bound on survivor count. Independent exact-rational state recursion checks 400 configurations, not used as infinite proof.

## originality

PASS

Random-order greedy maximal independent sets on chain/complete bipartite graphs already yield the EMPTY-start selection law, in particular a/(a+b); claim credits this prior case. The present random scheduler repeatedly selects with replacement and can start with active agents on both sides. Exact commitment survivor probabilities, full fixation-time expectation and m-log-m correction are not implied by one-pass greedy output laws, general best-response convergence theorems, or earlier simulated annealing procedures.

## value

PASS

Quantitative random best-response equilibrium selection is an essential stochastic-dynamics question even where existence and convergence are known. The explicitly resolved nonzero-start extinction lottery and sharp fixation clock give a reusable exact benchmark for asynchronous network games, not just a rephrasing of two Nash equilibria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
