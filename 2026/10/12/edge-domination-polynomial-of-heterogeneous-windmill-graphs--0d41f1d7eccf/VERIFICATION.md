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

# Reproducible verification

The supplied standalone Python 3 file `verify_edge_windmill.py` uses only the standard library. Run `python3 verify_edge_windmill.py` to check the closed polynomial and minimum coefficients on many labeled clique windmills. It constructs actual graph edges, enumerates every possible selected edge subset when the graph has at most 19 edges, independently checks edge domination by whether each graph edge shares an endpoint with a selected edge, and compares the resulting complete coefficient array against the displayed inclusion-exclusion expression. Separately it cross-checks the parity and closed count of minimum edge dominating sets against the computed first nonzero coefficient on broader finite tuple ranges.

Actual run:

`VERIFY_OK local_sizes=1..7 exhaustive_tuples=58 brute_edge_subsets=572252 dominated_sets=475022 algebraic_tuples=2..5 blades max_size=5 max_edges=19`

All sampled checks passed. These finite computations are not an exhaustive test of unbounded blade sizes. The proof applies for every integer \(r\ge2\) and every positive blade-size tuple, by the zero-selected-degree lemma, local inclusion-exclusion, and exact equality-case enumeration; no external certificate or independent validation is claimed.
