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

# Verification of finite joint cardinality census

Run `g++ -O2 -std=c++17 census.cpp -o census && ./census` and `python3 verify.py` alongside `joint_counts.csv`. The first program enumerates all normalized profiles, computes weak-majority transitive closure using exact bit operations, and prints all 42 cells. The second independently reconstructs the majority graph and checks reachability using breadth-first search, then asserts its complete 42-cell output against the CSV. No stochastic sampling or floating-point comparison enters these certified counts; the Python output reports aggregate integer sums, including the 331,776 four-agent profiles.

The completeness argument is the unique simultaneous house relabeling that fixes the first agent's ranking. Each of the 36 three-agent or 13,824 four-agent normalized profiles represents exactly 6 or 24 complete labeled profiles. Direct pairwise Pareto dominance and strict-preference comparisons are used.

The identical results from two algorithms, the total-count identities, and independently counted 31,104 singleton-top-cycle and 20,736 doubleton-top-cycle profiles provide checks. They do not constitute independent expert audit. Larger populations, preference ties, correlations, and other matching models are unverified by this finite certificate.
