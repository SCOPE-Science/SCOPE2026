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

# Verification of the folded-cube carrier lattice

Execute `python3 verify.py` in a directory containing the enclosed `requirements.txt`. The program only reconstructs the finite Cayley graph, its full independence complex, and signed integral simplicial boundaries. Its assertions verify the face vector, all 12,870 eight-vertex restrictions, ten affine hyperplane carriers, sphere-cycle orientations, exact boundary relations, a mod-two rank check and the integral Smith form of the boundary-plus-carrier matrix. It reports exactly 25 nonzero unit factors and the primitive ten-term relation.

The combinatorial proof of minimal support is supplied in `RESULT.md`, not assumed from numeric experiments. The Smith-form calculation is over the integers, not floating point or only a field. These checks do not prove priority in the literature, do not apply to other folded cubes, and are not an external or independent scientific audit.
