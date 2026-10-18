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

`verify_census.py` is a standalone Python 3 certificate. It enumerates every nonisomorphic tree on at most nine vertices by recursive leaf addition, deduplicates by complete canonical rooted-tree codes, computes the stable colour partition of every line graph, and computes automorphism-orbit classes from canonical edge-split codes. It checks exactly one nine-vertex exception and none smaller, as well as all eight choices of one individualized vertex in the exception.

`verify_witness.py` independently enumerates the 8! candidate permutations of the explicit exceptional line graph, filters actual automorphisms, and checks stable partitions against actual orbits for zero and one individualized vertex. It does not use the tree generator or rooted-tree codes. Both programs require only the Python standard library; no external data or downloaded papers are needed for replay.

The output in `verification_output.txt` was obtained by executing these programs from their actual included file paths. Checkers are finite exhaustive proofs only because their search spaces are proved complete in `RESULT.md`. They do not establish any statement for trees with more than nine vertices, and independent scientific audit is not performed.
