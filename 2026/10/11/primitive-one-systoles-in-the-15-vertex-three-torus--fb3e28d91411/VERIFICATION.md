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

The embedded `artifacts/verify.py` uses only the Python standard library. It reconstructs the 15-vertex three-torus from the six permutations of the step multiset \(\{1,2,4\}\) and all cyclic translates, then performs these checks:

- verifies the face vector \((15,105,180,90)\);
- implements the explicit deck-lattice displacement map and checks it vanishes on every triangular face;
- exhausts all \(275\) missing triangles and verifies all have primitive nonzero displacement;
- verifies exactly seven unoriented displacement classes with multiplicities \(45,45,45,45,45,45,5\);
- verifies the exceptional class is represented exactly by the five triangles \(\{i,i+5,i+10\}\);
- verifies the translation-orbit distribution \(15^{\times18},5^{\times1}\);
- generates the full order-\(120\) simplicial automorphism group from the published generators and verifies systole orbit sizes \(5,30,60,60,120\);
- verifies the seven unoriented homology classes form automorphism orbits of sizes \(1,2,4\);
- independently computes simplicial boundary ranks over \(\mathbf F_2,\mathbf F_3,\mathbf F_5,\mathbf F_7\), obtaining first Betti number \(3\).

Successful replay prints:

`VERIFY_OK f=15,105,180,90 H1_rank=3 missing3=275 essential3=275 primitive3=275 classes=7 multiplicities=45x6+5 translation_orbits=15x18+5 full_group=120 systole_orbits=5,30,60,60,120 class_orbits=1,2,4 exceptional=0-5-10`

The finite exhaustion applies only to this fixed 15-vertex complex. The identification with the integral deck lattice is supplied by the explicit quotient construction in the proof rather than inferred from finite experiments alone.
