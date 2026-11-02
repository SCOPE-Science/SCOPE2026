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

# Reproducibility of the rational homology representations

Execute `python3 check_cube.py` with a standard Python 3 interpreter and SymPy available. No input files or network requests are required.

The script builds the eight-vertex, twelve-edge binary cube and the complete unordered two-particle cubical chain complex, with \(28\) zero-cells, \(72\) one-cells and \(42\) two-cells. It checks the signed identity \(\partial_1\partial_2=0\) and exact rational/integer-matrix ranks \(\operatorname{rank}\partial_1=27\), \(\operatorname{rank}\partial_2=39\). A separate bit-vector elimination over \(\mathbb F_2\) finds the same ranks.

The script computes a three-element exact rational basis for \(\ker\partial_2\). For all \(48\) signed coordinate symmetries it verifies both chain-map identities, reconstructs the image of every cycle in all \(42\) coordinates, calculates the homology character and checks equality with the signed-coordinate representation. The remaining first-homology character is derived from the exact equivariant Euler identity and checked elementwise against the stated three-term decomposition. All ten signed-cycle classes, both quotient-invariant dimensions and the group-element counts are printed.

The expected last line is `CUBE_TWO_PARTICLE_FULL_B3_EQUIVARIANT_HOMOLOGY_OK`. This is an exact finite rational representation verification. It is not an independent audit or an integral torsion computation. The transfer argument for rational homology of the quotient and the cubical approximation theorem are mathematical ingredients stated and cited in RESULT.md, not consequences of numerical rank logs alone.
