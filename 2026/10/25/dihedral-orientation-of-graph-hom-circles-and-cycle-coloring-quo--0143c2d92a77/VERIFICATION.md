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
# Reproducibility and limitations

Run `python3 verify_hom.py` from the folder containing this file. The checker is entirely self-contained and reconstructs finite simplicial incidence structures and exact one-step coloring moves. It is not a proof of arbitrary parameters.

The executed checker printed the following exact successful completion lines:

```
CYCLE_COMPONENTS_AND_QUOTIENT_VERIFIED 50 48918 281144 934
GENERAL_GRAPH_ORIENTATION_VERIFIED 15 2520
EXACT_GF2_CELLULAR_H1_AND_PRIMITIVE_WINDING_VERIFIED 11 3348 7626 6108 18
DOMAIN_SYMMETRY_POSITIVE_WINDING_VERIFIED 13240
FULL_TARGET_DIHEDRAL_QUOTIENT_BETTI_VERIFIED 50
```

Finite cellular calculations are over the field with two elements; the **integral sign** in the universal theorem is justified by the deck-group conjugation identity, not by these mod-two calculations. The integral component-generator primitivity is also tested independently by integer increment winding gcds in the finite cases. The full quotient statement follows from exact rational transfer and the published circle-component classification.
