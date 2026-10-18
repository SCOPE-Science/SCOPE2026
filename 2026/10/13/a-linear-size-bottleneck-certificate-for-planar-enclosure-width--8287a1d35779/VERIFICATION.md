---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The width identity follows by choosing a lower witness below z and an upper witness above z+t(1,1), with the converse attained by z=lower. Coordinatewise domination pruning preserves scores including negative infeasibility. On sorted antichains the two gaps c_j-a_i and d_j-b_i respectively increase and decrease, so their minimum rises up to the difference-threshold crossing and falls afterward. Checking the two straddling neighbors is sufficient, with equality cases harmless. Since both tau_i=a_i-b_i and delta_j=c_j-d_j increase, a single forward pointer gives the stated bound. Independent brute-force and independently coded front routines agreed on 3,316 exhaustive finite-input pairs and randomized tie/empty instances. The tests support but do not establish the all-real-domain proof.

## originality

PASS

The published 2021/2025 width formula and minimax bound-front pruning are expressly prior results. A linear-size bracketing certificate and monotone two-front merge give additional complexity and witness conclusions not stated in the most relevant examined primary works. These could be independently rediscovered in unindexed Pareto-front scan implementations; novelty is best-of-knowledge and specifically limited to candidate sparsification, not enclosure width itself.

## value

PASS

Width is a recurring quantitative termination diagnostic in biobjective branch-and-bound. Replacing the Cartesian-pair scan by a tight candidate certificate and linear sorted-front merge is a motivated reusable primitive with a constructive optimum/emptiness witness. This is a bounded yet nontrivial algorithmic improvement; no whole-solver speedup or dimension>2 claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
