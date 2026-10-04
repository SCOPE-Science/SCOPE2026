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

The packaged `verify.py` constructs the four-point circle poset and its sixteen-point Cartesian square, then performs the following complete finite checks:

1. Recursively enumerates every order-preserving map \(T\to C\), obtaining \(2836\).
2. Independently enumerates all \(430\) order ideals and evaluates the exact weighted component-coloring sum, again obtaining \(2836\).
3. Builds the graph of all valid one-coordinate raises and checks that its connected-component sizes are \(2828\) and eight copies of \(1\).
4. Computes the two integral first-homology coefficients by restriction to the factor circles and verifies the complete profile \((0,0):2828\), \((1,0):2\), \((-1,0):2\), \((0,1):2\), \((0,-1):2\).
5. Generates the four order automorphisms of \(C\), composes each with both coordinate projections, and checks equality with the eight singleton maps.
6. Checks that all four constant maps lie in the unique \(2828\)-map component.

A replay from the exact packaged verifier bytes must print:

`VERIFY_OK maps=2836 ideals=430 components=2828+8x1 degree_profile=2828,2,2,2,2 isolated=8_projections`

The verifier certifies only this finite mapping-poset computation. The proof in `RESULT.md` supplies the general finite combinatorial justification for the parametrization and adjacency relation used by the program.
