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

# Reproduction and verification

The assertion concerns the complete finite family of unordered edge partitions of the fixed labeled \(K_8\) into seven one-factors. Both scripts use only Python 3 standard-library integers, sets, permutations and breadth-first search; no external data or random choices are used.

Run `python3 check_matching.py > matching_output.txt` and independently `python3 check_coloring.py > coloring_output.txt`. Both outputs must finish with the literal `VERIFY_OK`. The matching script generates \(105\) perfect matchings via recursive vertex pairing and \(6{,}240\) unordered exact covers of the 28 edges. The second generates proper edge-colorings canonically by fixing the colors incident with vertex zero, without consulting the matching partition enumerator.

Both implementations enumerate all \(28\) anchor pairs per state and all eligible bipartite components. Their recorded signed counts of component-side partitions total \(174{,}720\). The generated undirected graph is checked for symmetry, has \(6{,}240\) states, \(66{,}360\) edges, and degree counts \(420,960,30,4200,630\) at degrees \(9,14,21,23,29\), respectively.

The matching implementation computes the exact six \(S_8\)-orbits, of orders \(30,420,630,960,1680,2520\), and performs complete BFS from one member of each orbit; all six BFS traversals reach all states. Representative eccentricities are \(6,6,5,5,5,5\) in the ordering of `RESULT.md`; thus the radius and diameter are precisely \(5\) and \(6\). The coloring implementation independently constructs the same distance profiles and verifies the expected cardinalities. The two methods use different enumeration and canonicalization algorithms.

No unbounded-order generality, external audit, or uniqueness among all possible published works is claimed. The computational proof can be independently reproduced by executing and inspecting the attached standalone algorithms; log files alone are not evidence of exhaustive correctness.
