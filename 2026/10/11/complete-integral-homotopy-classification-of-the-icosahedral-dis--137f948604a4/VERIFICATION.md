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

# Verification of the icosahedral distance-neighborhood homotopy classification

Run `python3 verify_icosa_morse.py` and `python3 verify_icosa_homology.py` with Python 3; both use only the standard library. These were run from the package source files and completed successfully, with terminal markers `ICOSAHEDRAL_DISTANCE_MORSE_PASS` and `ICOSAHEDRAL_DISTANCE_HOMOLOGY_PASS`.

The first checks thirty distinct edges, degree five, distance shells \((1,5,5,1)\), all fifteen exact face sets and staged acyclic matchings. It verifies every original Hasse cover through a full topological sort, including all 4,080 incidences for each mixed case and all 24,564 incidences for the full eleven-simplex. The decisive signed integer gradient-path boundary for \(D=\{0,1,3\}\) and \(D=\{0,2,3\}\) is the zero \(6\times21\) matrix. Hurewicz then identifies the attaching classes and proves the claimed mixed wedge. The second uses an independently coded combinatorial face enumeration and binary Gaussian elimination for all boundary maps, reproducing reduced ranks \(\widetilde\beta_2=6\) and \(\widetilde\beta_3=21\) in the mixed cases and all other listed ranks.

The checks establish the stated exact finite computations but do not check homotopy equivalence between complexes for different distance sets beyond the mathematically proven antipodal reindexing, nor do they establish equivariant or persistent homotopy information. Independent scientific validation remains unperformed.
