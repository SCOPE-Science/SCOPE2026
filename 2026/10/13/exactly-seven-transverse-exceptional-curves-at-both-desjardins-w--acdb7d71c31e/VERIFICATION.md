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

# Arithmetic verification

Run `python3 verify.py`. It uses only the standard library, takes the source's exact eight projective points, checks general position, enumerates all 232 plane exceptional classes from the complete degree-one del Pezzo list, checks 225 impossible incidences per example by full column rank modulo 1000003, constructs the seven admissible forms by exact rational linear algebra, and certifies their pairwise distinct first-order tangent gradients. The remaining eight blow-up exceptional divisors are disjoint from Q geometrically. Its final line is:

`VERIFY_OK examples=2 exceptional_curves=240 unique_through_Q=7 each ordinary_sevenfold=2 all_225_plane_exclusions_per_example_mod_1000003=PASS`

This is a finite exhaustive class census, not a sample of an infinite family. A nonzero modular determinant implies a nonzero characteristic-zero determinant, but no reduction statement in characteristic 1000003 is claimed. Published non-torsion is a separate referenced input. No independent audit has been performed.
