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

# Reproducibility and scope

Run `python3 verify_klein_bitangents.py` with Python 3 (standard library only). It checks the projective involution relation, constructs the degree-six residue field of the seventh cyclotomic polynomial at five, enumerates exactly 28 distinct projective dual-line classes in the orbit of the rational bitangent, and computes all six cyclotomic permutations and cycle lengths.

The finite computation is an exact certificate of the cyclotomic Galois permutation and the minimal splitting-field degree. It is not a stand-alone proof that the bitangent scheme specializes étale in all odd good characteristics; that infinite assertion follows from the smoothness and theta-characteristic argument in RESULT.md. It does not check characteristic two, characteristic seven, or tangency-point fields.
