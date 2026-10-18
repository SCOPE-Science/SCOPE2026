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

# Reproducibility

Execute `python3 ico_cf3_verify.py` with standard Python 3. The program enumerates all masks on twelve vertices, checks the twenty forbidden triangular subsets, verifies all 523 discrete-Morse face-cover pairs and the acyclicity of the full oriented Hasse graph, evaluates the exact oriented integral Morse differential as -2, and calculates the mod-two and mod-three full simplicial boundary ranks.

The direct calculation is finite and exhaustive. It independently checks field homology against the Moore-space homology pattern, but field ranks alone are not a certificate of the integral result; the signed unit-pivot elimination is the decisive computation. No approximate, random, incomplete, or externally certified result is used. Independent audit has not been performed.
