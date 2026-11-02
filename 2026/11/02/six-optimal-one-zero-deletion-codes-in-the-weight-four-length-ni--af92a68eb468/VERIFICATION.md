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

Run `python3 verify.py cert_six_maxima.json`. The checker constructs all degree-five profiles of five coordinates, verifies the cliques, checks an upper-bound branch certificate with four pruned leaves and an exhaustive size-26 enumeration with 379 pruned leaves, and compares the six terminal sets with the checksum-fiber orbit under all 120 coordinate permutations. It relies only on Python standard-library rational arithmetic, not a numerical solver. It proves no independent set has 27 elements and every size-26 set belongs to the six-member orbit. No claims for other graph degrees or other deletion channels are certified.
