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

# Reproducibility and verification

Run `python3 check_hypercube.py` with Python 3 standard library. The accompanying `check_output.json` records the exact deterministic result of this command. The program computes each cube's edges explicitly, performs canonical one-dimensional refinement, and independently computes marked-coordinate signature count vectors. It checks equality of the two partitions, exact class count, criterion for discreteness, and the round limit.

Exhaustive small-cube cases: all distinct unordered marked sets of sizes at most four in dimensions one to four. Random larger cases: a fixed random seed and 120 sampled marked sets for each cardinality one to six and each dimension five through ten. The explicit optimal signature construction is tested in dimensions one to fourteen. Total: 7030 cases, all PASS; observed maximum 13 rounds for these tests. This evidence is corroboration of a complete mathematical proof, not an exhaustive all-dimension computation.

The needed lemmas are proved independently in `RESULT.md` by the cube automorphism group's signed-coordinate permutation form and signed neighbour-distance profiles. The depth bound need not be optimal. The least landmark count agrees numerically with a known 2009 determining-number theorem; originality is claimed only for the stronger refinement-orbit assertion, exact profiles and depth bound. Independent external audit and literature priority verification have not been performed.
