---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At neutrality the degree-weighted mutant proportion is a martingale. Bias at u contributes first-order drift d_u p(1−p)/(2mn) when p is the mutant fraction of u's neighbors. The factor p(1−p) is the number of unordered disagreeing neighbor pairs divided by d_u². Under the uniform single-mutant seed, conditional on distinct ancestors, disagreement has probability 2/n. For a distinct lineage pair the discrete ancestral process moves with probability 2/n per step; its mean meeting time in steps (the summed survival probabilities) is n times the continuous meeting time ψ for two rate-one walkers. Thus summed disagreement contributes 2ψ, giving exactly the displayed b_T. Finite connectedness ensures almost-sure coalescence with finite mean and a unique rational first-step solution. The independent exact census used the Prüfer bijection, canonical tree classes and rational pair systems; class counts 1,1,2,3,6,11,23 at orders 2–8 all had zero strict failures. On the specified n=9 witness it reproduced b(0)=256096/2909163, b(1)=481465/5818326 and positive difference 30727/5818326, with leaves zero and vertices 5 and 7 both at 1196615/34909956. Vertex 1 alone has degree 4 and vertex 0 alone maximizes the derivative. The neutral absorption system has an invertible transient block and hence the fixation probabilities are analytic locally; their neutral values coincide (1/n), so the strict derivative comparisons persist for sufficiently small positive bias on this witness. Replay: python3 /workspace/branches/6036ea5a-31a0-4c78-8f12-491e9342549c/audit_tree_scores.py; full bounded run in census-through-8.txt (3 s recorded). The frozen verifier was inspected, not run. No assertion for every degree tie or for an arbitrary fixed positive bias follows.

## originality

PASS

The coalescence score and the ability to optimize its derivative graph by graph are prior work. Neither the strongest inspected same-model study nor the near catalogue match establishes the strict degree-first boundary for trees or the specified witness. The scoped distinct claim is the first possible order and exact counterexample, not a new weak-selection algorithm.

## value

PASS

Maximum degree is a natural and previously benchmarked heuristic when full coalescence scores are costly. The first failure even without any degree tie separates degree from weak sensitivity in the simplest connected acyclic setting. The lower bound and exact witness together make this a sharp boundary, not another run of the known algorithm on an arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
