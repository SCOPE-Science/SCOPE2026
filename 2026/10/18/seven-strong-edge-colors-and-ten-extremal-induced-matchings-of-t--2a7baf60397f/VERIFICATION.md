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

# Verification of the finite statements

Run the programs in the same folder with `python3 verify_exact.py` and `python3 verify_independent.py`. Both use standard-library facilities only, rebuild the graph from all fifteen pairs and all fifteen perfect matchings of a six-set, and compare the independently generated graph, maximum sets and coloring against the included `CERTIFICATE.json`. Their outputs are included verbatim as `verify_exact.out` and `verify_independent.out`.

The first program performs a complete increasing-label enumeration of compatible graph-edge sets. It reports the size distribution \((45,720,5160,16920,22680,8520,720,90,10)\). The second computes all maximal cliques with a different Bron–Kerbosch algorithm, then independently regenerates every clique as a subset of a maximal one. Its maximal-clique profile is sizes five, six, seven and nine with frequencies \(3060,5520,360,10\).

Both verify that each graph edge is in exactly two of the ten nine-edge induced matchings and that distinct maximal nine-edge induced matchings meet in exactly one edge. The direct proof of impossibility with six colors reduces to a single possible class-size profile \((9,8,7,7,7,7)\). Its exhaustive remainder consists of ninety ordered choices of the parent nine-edge classes. Each choice leaves twenty-eight uncovered graph edges and admits exactly thirty-two possible seven-edge induced matchings. The first checker performs recursive exact-cover search; the second tests every four-subset of those thirty-two possibilities. Both reject every case. Both also validate the displayed seven-color witness by checking all incompatible edge pairs.

The proof is of this one finite graph only. Failure of an arbitrary solver to find a coloring would not establish nonexistence; the supplied exact-combinatorial reduction and exhaustive recursion do. The recorded outputs are corroboration, not substitutes for the mathematical argument and executable enumeration.
