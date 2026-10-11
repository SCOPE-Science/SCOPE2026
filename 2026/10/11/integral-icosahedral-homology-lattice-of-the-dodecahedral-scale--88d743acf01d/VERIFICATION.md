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

Execute `python3 verify.py` from the directory containing the complete embedded files. The script uses only Python's standard library and a literal 20-vertex, 30-edge graph specification.

It checks exactly all 3,272 nonempty simplices and all 120 automorphisms, including all oriented fixed-simplex contributions to the Lefschetz number. It independently enumerates the ten exceptional tetrahedra, their two five-element rotation orbits, the central antipode's exchange, and the two-transitive action on each orbit. It computes all mod-two augmented boundary ranks, not a sampling of boundary columns.

Expected exact output includes:

```
F_VECTOR (20, 150, 540, 1000, 972, 490, 100)
MOD2_BOUNDARY_RANKS (1, 19, 131, 409, 582, 390, 100, 0)
MOD2_REDUCED_BETTI (0, 0, 0, 9, 0, 0, 0)
ROTATIONS 60 FULL_GROUP 120
SPECIAL_TETRA 10 ROTATION_ORBIT_SIZES (5, 5)
VERIFY_OK
```

Integral module correctness is established in `RESULT.md` from the equivariant long exact sequence and the cited integral homology inputs; mod-two verification alone would not certify an integral representation. The script verifies the complete induced rational character as an additional independent finite check. The provided verifier does not establish an equivariant homotopy equivalence, which is not claimed.
