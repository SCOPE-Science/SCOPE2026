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

# Finite proof verification

Execute `python3 verify_octahedral_two_matching.py` with standard-library Python. The script prints all exact assertion results and the marker `HOMOTOPY_WEDGE_3_S3_AND_7_S4_VERIFIED`; the attached `verify_octahedral_two_matching.out` records a successful execution.

The independent tests enumerate all 4096 edge subsets using degree counts and forbidden triple stars. Full simplicial boundary-squared checks hold over the integers. The greedy matching is tested on all 2940 directed face incidences for acyclicity, and its 378 algebraic cancellations use exact pivots ±1. The surviving signed differential has the displayed rank-three unit minor and two zero rows plus a fourth-row relation; an independent mod-two boundary calculation confirms reduced Betti numbers 3 and 7 in dimensions 3 and 4.

The homotopy conclusion also uses the mathematical identification of 4-cell attaching maps into a wedge of 3-spheres with integral degree vectors. Nothing here certifies arbitrary graphs or future parameter values. Independent external audit has not been performed.
