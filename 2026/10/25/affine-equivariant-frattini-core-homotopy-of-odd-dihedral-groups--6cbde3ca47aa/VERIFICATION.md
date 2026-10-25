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
# Verification notes

The proof checks five nonstandard steps: the maximal-subgroup list, the Frattini intersection, the exact nerve face predicate, invariant-cone contraction, and orientation preservation under all automorphisms. These steps are justified in `RESULT.md`; the script is not treated as a proof of the infinite statement.

Reproduce the finite test with `python3 verify_dihedral.py` using Python's standard library. It enumerates all nonempty subsets of maximal subgroups at \(n=3,5,9,15,21,45,105\), tests exact intersections outside \(\Phi\), and checks the expected reduced Euler characteristics. It computes all affine-group signed Lefschetz characters for \(n=3,5,9,15,21\) and selected cases at \(n=45,105\). Every check completed successfully. Full arbitrary-subgroup fixed-set computations were not separately enumerated; they are proved via the equivariant sphere model. The proof does not cover even dihedral parameters.
