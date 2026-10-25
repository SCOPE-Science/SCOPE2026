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

# Reproducibility

Use `python3 verify.py` (standard Python 3, no external dependencies). Its recorded stdout is in `verify_output.txt`.

The verifier independently constructs the regular bipartite disjointness matching by a deterministic augmenting-path algorithm for all \(4\le n\le9\), and implements the stated \(\binom n2\)-colour assignment for all \(2\le m\le n\). For each of the \(33\) parameter pairs it checks that the palette has exactly the claimed size and that no equally coloured edges are incident or opposite in a diamond (using the four cross-edge adjacency count). It also directly enumerates all four-vertex subsets of the smaller tested rook graphs, locating \(539\) configurations spanning a diamond and confirming rainbow colour sets. It verifies explicit proper colourings of the three smaller graphs and checks the four-colour obstruction for the nine-vertex case.

Recorded output:

`VERIFY_OK small_cases=3 rook_instances=33 complete_quadruple_diamonds=539 max_column_order=9`

The computation does not enumerate all possible D-colourings or prove that an infinite family is valid. The unrestricted lower bound and upper-bound construction are proved in `RESULT.md`; Hall's theorem guarantees the disjoint-pair matching for every \(n\ge4\). No independent audit has been performed.
