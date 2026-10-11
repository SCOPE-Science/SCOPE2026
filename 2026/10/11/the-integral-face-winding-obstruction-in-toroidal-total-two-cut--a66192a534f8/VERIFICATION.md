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

The accompanying standalone `verify_torus.py` uses the Python standard library. Run `python3 verify_torus.py` from the directory containing this file; the expected final line is `VERIFY_OK group_character_checks 912 direct_cut_checks 208`.

Six toroidal grids are tested, at 912 elements of their natural symmetry groups. For 208 elements, the code separately enumerates vertex-orbit unions of the total two-cut complex, computes the signed reduced Lefschetz number of the actual complex, and compares it to the homological character formula. Translation edge-orbit sums and their winding-index images are constructed directly for all six grids.

The finite computations do not prove the statements for unbounded \(m,n\), nor do they certify the order of an arbitrary Ext class computationally. The uniform proof uses integral cellular chains and the invariant-lift criterion for the two coordinate extension classes. No independent audit has been performed.
