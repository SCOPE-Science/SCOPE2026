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

`verify_partition_rank3.py` runs under Python 3 with only the standard library. Invoke `python3 verify_partition_rank3.py` and compare standard output to `verification_output.txt`.

The program represents a set partition by a restricted-growth sequence, implements refinement as inclusion between its equivalence-pair masks, and constructs the four possible third-element relations to two selected partitions. It asserts full agreement between enumeration and the symbolic extension table for all pairs at ground-set sizes one through seven and for a deterministic 50,000-pair sample at size eight.

It then calculates the full rank-three first-order game profile via second- and third-element relations, using representatives of actual ground-set relabeling orbits for the first element. The seven classes for sizes one through eight and the matching profiles of sizes seven and eight are direct finite computational checks. Only the mathematical proof in `RESULT.md` establishes the classification for all larger ground-set sizes.

The review is not independent. No external mathematical audit or higher-rank verification is claimed.
