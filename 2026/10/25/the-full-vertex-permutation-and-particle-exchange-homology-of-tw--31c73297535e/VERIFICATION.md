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

# Verification

Run `python verify.py` in an environment with Python 3 and SymPy. The program constructs all cubical cells from the complete five-vertex graph and their signed integer cellular boundary matrices, checks composition of boundaries, rational ranks, Smith factors and a primitive surface fundamental cycle. It verifies signed homology characters for every one of the 240 elements of the vertex-permutation and particle-exchange group. Completion markers `ALL_240_GROUP_CHARACTERS_VERIFIED 240` and `INTEGRAL_BOUNDARIES_AND_29_UNIT_SMITH_FACTORS_VERIFIED` appeared during the scientific check. The checker is finite and exact, and the general deformation-retraction premise and Lagrangian conclusion are justified by the written proof rather than inferred from an experiment. Independent mathematical validation has not been performed.
