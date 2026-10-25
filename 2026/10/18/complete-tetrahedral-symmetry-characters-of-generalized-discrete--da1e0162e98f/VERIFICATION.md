---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact definition uses the 28 or 24 cover edges of the 15- or 14-nonempty-face Hasse poset and imposes endpoint-disjointness but NOT acyclic Morse matching. For each permutation of four labels, a fixed simplex is a union of mutually compatible edge-orbits; the orientation sign for a j-orbit union cancels the k-edge simplicial sign to give the reduced Lefschetz number minus the signed orbit-independent-set sum. I independently rebuilt that recursion on both Hasse graphs for all 24 permutations: the characters agree and are (39,1,-5,0,3), with classwise admissible-orbit counts matching source. Scoville Theorem 24 supplies the external prerequisite of homology concentrated in degree four with rank 39; this is not reproved by enumeration. Rational character inner products give multiplicities 2,5,2,6,0 and invariants dimension two; exactness of invariants and barycentric subdivision establish quotient rational homology. The interpretation excludes integral and equivariant homotopy claims.

## originality

PASS

The earlier published tetrahedral S4 character (99,1,-1,0,-1) is for the ORDINARY acyclic Morse matching complex (12,820 allowed faces), not the generalized Hasse matching complex (14,720 faces). Scoville Theorem 24 determines the latter nonequivariant 39-sphere wedge but does not furnish the 5-class character. The independence-orbit signed calculation distinguishes the class traces for two different generalized complexes without conflating titles or identical symmetry groups.

## value

PASS

A complete nontrivial rational S4-module calculation for two naturally related tetrahedral generalized matching complexes determines which of 39 homology classes survive symmetry quotient. That information is not mechanically implied by a Betti number or the ordinary acyclic matching representation, making this motivated finite equivariant invariant worthwhile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
