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

The standalone `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing the script. It constructs admissible singleton/two-element vertex orbits under a coordinate transposition, enumerates compatible orbit cliques by testing every pair of underlying original vertices, then computes exact mod-two boundary ranks with integer bit-vectors. A successful run prints each checked case and ends with `JOHNSON_TRANSPOSITION_FIXED_HOMOLOGY_VERIFIED`.

The computations check the entire chain complex of the finite orbit complexes they construct. They do not certify the unbounded domain, integral homotopy type, simple connectivity of the smaller Johnson complexes, or absence of integral torsion. The accompanying proof establishes those properties by the orbit-complex decomposition, simplicial collapses, a distance-level contraction of loops, and homological Whitehead.
