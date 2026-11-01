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

# Reproduction and limits

Run `python3 verify.py` in the same directory. The standalone program uses Python's standard library only. It verifies the definition directly from allowed directed arc subsets, checks all 2,200 augmented Hasse incidences for the five-leaf case and 23,976 for the nine-leaf case, and confirms the stagewise matching acyclic in those complete complexes. For the five-leaf case, 339 pairs leave one critical two-cell and 32 critical three-cells; exact signed elementary unit-incidence cancellations give eleven \(+2\), ten \(-2\), and eleven zero coefficients. Independent characteristic-two and characteristic-three simplicial boundary ranks corroborate the two-primary distinction. The six-leaf pivot list leaves only three-dimensional critical faces for the nine-leaf universal finite representative. Additional sizes six through ten are checked for regression, not substituted for the locality proof.

The source `RESULT.md` proves why every low-dimensional face for an arbitrary number of leaves reduces to the representative with three generic leaves, and separately proves acyclicity for the stagewise matching. Neither raw finite experiments nor character-field ranks alone would justify all-parameter homotopy or the exact integral Moore summand. No independent audit has been performed.

Expected final output marker: `BIDIRECTED_K2N_TORSION_TO_SPHERE_WEDGE_EXACT_OK`.
