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

# Reproduction

From the same directory, execute `python3 verify_box_flips.py` with a standard Python 3 interpreter. The code uses no external packages. `verification_output.txt` contains an actual successful run's output.

The complete certificate independently counts the tilings using two recursions, constructs all elementary squares, identifies flips both by local replacement and by a four-edge symmetric difference, partitions the full graph into components, verifies path degrees and reflection transitivity, and performs breadth-first search from every vertex of the giant component. The largest component has 1825 vertices, so the all-pairs search is exhaustive rather than sampled. A computer implementation is not a formal proof assistant or independent external review. The finite-recursion completeness and geometric flip equivalence are justified in `RESULT.md`.
