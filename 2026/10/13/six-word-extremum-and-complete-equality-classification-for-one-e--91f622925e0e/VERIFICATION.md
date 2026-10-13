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

# Verification of the finite extremum

The `verify_enumeration.py` and `verify_independent.cpp` programs are self-contained except for `optimal_codes.txt`, which contains the purported complete sixteen-row equality-case list. Run the Python script from its containing directory; compile the C++17 source and pass the list pathname to its executable. The expected successful output includes `VERIFY_OK`.

Both verifiers enumerate all \(54\) primitive binary words of length six (primitive meaning six distinct rotations) and all valid increasing comma-free subsets with minimum Hamming distance at least three. Exact feasible-cardinality counts for cardinalities zero to six are \((1,54,814,3042,2480,324,16)\), a total of \(6731\). No larger code survives their exhaustive branching. Both compare all \(16\) six-word codes against the embedded list, assert four four-member symmetry classes, and check eight distance-three pairs and seven distance-four pairs for each.

Completeness requires the elementary monotonicity property: once a subset contains a forbidden splice or a pair at distance below three, no added word can make that subset valid. The increasing-order DFS does not use a heuristic upper bound or skip a feasible prefix. The result is a complete finite computation; it does not certify novelty of the conclusion or generalize automatically to arbitrary lengths.
