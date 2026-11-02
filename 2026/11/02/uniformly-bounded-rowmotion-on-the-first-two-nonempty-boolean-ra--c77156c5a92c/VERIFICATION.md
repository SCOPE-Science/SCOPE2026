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

The all-parameter result follows from the explicit rowmotion recurrence on ideal pairs, the proof that every orbit meets a full-singleton state, and the exhaustive classification of such states by universal and isolated vertices. Equations (2)–(5) in the main result are exact symbolic cycles, not finite-sample extrapolations. The labelled-graph inclusion–exclusion produces the complete orbit-count formulas.

Reproduce finite checks with `python3 verify.py` and `c++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`. The first implementation checks complete rowmotion cycles for \(n=3,4,5,6\) and nonexhaustive tests for larger \(n\); the second independently generates ideals as subsets of the entire poset and derives successors from minimal complement elements. Both executed successfully with the full orbit counts in the result. Independent scholarly audit has not been performed.

Finite checks alone cannot prove the asserted statements for arbitrary \(n\); their role is to corroborate the symbolic classification and formula. The theorem does not extend to general graphs or birational rowmotion without further argument. Literature comparison leaves possible unindexed equivalent work as a residual priority risk.
