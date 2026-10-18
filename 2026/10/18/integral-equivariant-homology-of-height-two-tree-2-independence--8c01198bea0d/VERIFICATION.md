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

# Reproducibility checks and limits

The standalone `verify_height_two.py` needs Python 3.10 or later and only its standard library. Execute `python3 verify_height_two.py` from the extracted package. It independently enumerates all admissible faces using the selected-degree characterization of induced-component size at most two, builds the staged leaf-toggle matching, verifies its full augmented Hasse orientation is acyclic, and computes reduced mod-two Betti numbers by exact binary elimination. It then computes signed fixed-simplex traces, comparing them with the integral augmentation tensor prediction for leaf transpositions and exchanges of equal-size branches.

Nine branch vectors are tested: \((1,1)\), \((1,3)\), \((2,2)\), \((2,3)\), \((2,2,3)\), \((2,3,2)\), \((3,3)\), \((2,2,2)\), and \((3,3,3)\). The largest example has 13 graph vertices, 2,432 augmented complex faces, 11,984 Hasse incidences, 1,212 matched pairs, and eight critical five-faces. Its reduced mod-two homology has rank eight in degree five and zero elsewhere. The verifier prints `VERIFY_OK all cases and symmetry tests` only after all assertions succeed.

The signed enumeration uses the negative of the reduced Lefschetz sum, matching the homology character because the sole possible nonzero reduced homology degree is odd. The finite calculations are corroboration, not an all-parameter proof. The general proof is contained in `RESULT.md` and explicitly handles group-element cycles, join orientations, and contractible branch factors. Independent audit is not yet performed.
