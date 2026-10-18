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

## Reproduction

Run `python3 verify_pappus_full_character.py` using Python 3.10 or newer. The checker uses only the standard library. It generates the explicit finite-field incidence graph and all 216 automorphisms from an affine family plus a point-line involution; verifies graph edge preservation; enumerates all 2598 independent subsets including the empty subset; and performs exact bitset Gaussian elimination for every mod-two boundary rank. It enumerates all signed fixed simplices to compute the reduced rational Lefschetz character. Finally, it verifies the normality of the specified order-three subgroup, the two projected character degrees, their separate irreducible norms, and the entire 216-element distribution.

## Exact observed checks

- Graph: 18 vertices and 27 edges; 108 affine side-preserving maps and 108 side-exchanging maps.
- Nonempty face vector: `(18,126,438,801,756,348,90,18,2)`.
- Mod-two boundary ranks in degrees one through eight: `(17,109,329,472,274,74,16,2)`.
- Ordinary mod-two Betti vector: `(1,0,0,0,10,0,0,0,0)`; rational concentration follows by the field-rank inequality and Euler characteristic 11.
- Reduced degree-four rational character: identity trace 10; nontrivial vertical translations each have trace 1; total character squared norm 2; character average 0.
- Rational projection characters: dimensions 4 and 6, each squared norm 1, mutual inner product 0.

## Scope of verification

The finite field rank argument certifies rational Betti concentration but does not separately compute Smith normal forms or establish any integral equivariant decomposition. The complete automorphism group and the intrinsic representation splitting also use the mathematical arguments in `RESULT.md`; the checker verifies their finite enumerations, not the correctness of general group-theoretic principles.
