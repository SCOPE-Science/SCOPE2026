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

# Reproducibility and limits

Run `python3 verify.py` with the Python 3 standard library. The script constructs uniformly subdivided complete graphs, applies synchronous color refinement to the specified singleton marks and their common background color, and derives stabilizer orbits independently by enumerating all permutations of branch vertices. It checks equality of the two partitions, the stabilizer order, the entire class-size multiset, the closed class-count formula, and the \(2L-2\) upper bound.

The seeded run exhausts all \(1,024\) marked configurations for \((n,L)=(4,2)\) and tests another \(11,400\) sampled configurations for eight other parameter pairs, for \(12,424\) total. The expected output is included as `verification_output.txt`. The finite tests are not an exhaustive search over all parameters and are not the proof of the theorem. The all-parameter argument is in `RESULT.md`. In tested examples the bound was attained, but no infinite-family sharpness assertion is part of the theorem.

No independent scientific audit has been performed.
