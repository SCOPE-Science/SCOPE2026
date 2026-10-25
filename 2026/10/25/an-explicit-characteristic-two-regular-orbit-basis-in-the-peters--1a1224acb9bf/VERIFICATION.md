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

The executable `verify_mod2.py` was run with Python's standard library. Its independently reconstructed 15-edge Petersen graph has 2,000 spanning-tree facets and 4,680 adjacent eight-edge forest faces. The entire mod-two top boundary matrix has rank 1,760 and nullity 240.

Two explicit binary 2,000-coordinate seed cycles (supports 972 and 992 facets), stored as hexadecimal strings in the executable itself, satisfy each boundary equation. After applying all 120 graph-label permutations to each seed, all 240 resulting vectors remain cycles. Exact bitwise elimination gives orbit-matrix rank 240. This is a full finite characteristic-two module certificate; the top homology contains no quotient by boundaries from higher chains.

No claim is made that these orbit columns are an integral basis, or that an equivalent statement has not appeared in inaccessible literature. Independent audit has not been performed.
