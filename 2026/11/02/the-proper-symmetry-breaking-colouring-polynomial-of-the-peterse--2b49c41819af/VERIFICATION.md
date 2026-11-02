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

The finite certificate is reproduced by `python3 verify/independent_blocks.py` and `python3 verify/restricted_growth.py`, both using Python's standard library. Each script constructs the ten-vertex graph and the 120 distinct symbol-induced automorphisms afresh. Their independent enumeration routes agree on all 7430 proper class partitions and every stabilizer count. The first additionally checks the complete ten-orbit classification of four-class partitions; the second directly checks every proper four-palette assignment, both full degree-ten polynomials, and the automorphism orbit-cycle counts. Limits: the computation is exhaustive for the specified ten-vertex graph only; no historical uniqueness or external audit is certified.
