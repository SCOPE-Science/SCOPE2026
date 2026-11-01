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

# Reproducible verification

From the same directory, execute `python3 verify.py` using Python 3.10 or later; no third-party libraries or external inputs are required. The script reconstructs the quadratic-residue Paley graph, generates all 17 nine-vertex closed neighborhoods, independently checks every subset of the 17-vertex universe, and obtains the full face vector. It executes the exact vertex-toggle matching given in the proof, checks all matched pairs, then builds every directed codimension-one incidence of nonempty faces and verifies acyclicity with a complete topological sort.

Expected milestone output:
```
FACES_OK (17, 136, 680, 1734, 2074, 1428, 612, 153, 17) simplices 6851
MATCHING_OK pairs 3399 critical {0: 1, 3: 52}
ACYCLIC_OK nodes 6851 incidences 33847
RAW_MOD2_OK ranks {1: 16, 2: 120, 3: 560, 4: 1122, 5: 952, 6: 476, 7: 136, 8: 17} reduced_betti {0: 0, 1: 0, 2: 0, 3: 52, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
HOMOTOPY_OK wedge_of_52_3_spheres
ALL_VERIFY_OK
```

The integral homotopy assertion follows from the acyclic-matching CW theorem and the complete critical-cell profile, not from the mod-two homology. This finite certificate does not prove uniqueness in the literature, nor does it cover other Paley parameters or open-neighborhood inclusion maps. Independent mathematical validation has not been performed.
