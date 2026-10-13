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
# Finite verification and analytic limits

Execute `python3 verify.py` in the package directory. No third-party dependencies are needed.

The verifier constructs all permutations for each of \(n=5\) and \(n=6\). For each ordered permutation pair, it independently computes Kendall distance (1) from the symmetric difference of inversion sets and (2) using breadth-first shortest paths in the adjacent-swap graph; all entries must agree. The complete diameter-three compatibility graph is then traversed by exact Bron--Kerbosch enumeration of maximal cliques. All maximum cliques must match the independently constructed family of adjacent-center unions of radius-one balls, with a unique edge for every union. The exact action of all common label permutations and optional position reversal is computed and the specified orbit sizes and stabilizers are checked.

An independent local enumeration in each of \(n=5,6,7\) checks that the rank-two inversion sets are exactly the disjoint-simple and overlapping-simple patterns and have the degrees used in the proof.

The expected final line is:

`VERIFY_OK n5_max=8 n5_count=240 n6_max=10 n6_count=1800 rank2_n5_to_n7=true`

**Scope:** This code is an exhaustive finite cross-check for two complete instances and a third local lemma instance. The mathematical proof in `RESULT.md`, not these finite enumerations, establishes the theorem for all \(n\ge5\). No external independent audit has been performed.
