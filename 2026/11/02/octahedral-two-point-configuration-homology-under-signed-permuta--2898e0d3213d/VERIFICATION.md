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

# Exact finite homology and symmetry certificate

Reproduce with `python3 CHECKER.py CERTIFICATE.json` using Python 3's standard library only. The script rebuilds the graph, all 15 zero-cells, 48 one-cells, 30 two-cells, their signed integer boundaries, and the complete two-particle configuration one-skeleton. It verifies connectivity, an exact 26-by-26 boundary minor determinant \(-1\), four independent integral nullcycles forming a normalized rational basis, and all 48 signed-permutation automorphisms. It computes all homology traces using actual oriented cell maps, confirms the two closed character expressions, and averages them over both the full group and its 24-element determinant-one subgroup.

Expected successful output:

```
OCTAHEDRAL_TWO_POINT_EQUIVARIANT_CERTIFICATE_OK
chain_cells=15,48,30 boundary_ranks=14,26 homology_dimensions=1,8,4
all_48_automorphisms=verified; rational_invariants_full=(1,0,0); rotations=(1,1,0)
```

The checker establishes the finite signed matrix data exactly; the deduction that these cubical calculations compute the continuous configuration space uses the published sufficient-subdivision theorem. Rational character and transfer arguments in the proof are mathematical deductions, not computational guesses. No integral first-homology torsion or stronger quotient homotopy classification is claimed.
