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

# Verification details

Run `python3 checker.py` using standard-library Python 3. The program exhausts all 65536 possible two-bit complementary-block BWT columns and accepts exactly those with a single 32-cycle LF permutation. It also enumerates rooted Euler circuits in the 16-vertex, 32-edge de Bruijn graph, checks every five-bit circular factor of each output and independently computes the cyclic BWT by sorting all rotations. Both complete approaches were run on the bundled checker and passed, giving 2048 unique necklaces and bins 20:38, 22:426, 24:840, 26:608, 28:130, 30:6. The two complete sets of BWT last columns agree exactly. The checks use finite enumeration; none relies on statistical extrapolation. The independent expert audit remains unperformed.
