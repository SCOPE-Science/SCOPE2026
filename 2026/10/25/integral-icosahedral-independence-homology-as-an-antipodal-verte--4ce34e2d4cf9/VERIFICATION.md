---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

From explicit six edge families reconstruct the distance profile (1,5,5,1). All independent edges split as 30 distance-two pairs (each in two triangles) and 6 antipodal pairs (in no triangle); no independent quadruple. The distance-two graph is icosahedral, with 20 triangles and 12 five-cycle vertex links, hence S2. Attaching the six antipodal diameters gives S2 wedge6 S1. Relative LES of (K,S2) gives an equivariant integral H1 isomorphism to oriented antipodal edges mapped [x,alpha x] to e_x-e_alpha x; H2 sphere orientation class. Rotations preserve sphere orientation, central antipode reverses it by Lefschetz fixed-simplex count. Character from signed fixed antipodal edges is rotational (6,-2,0,1,1), the rational six-dimensional irreducible W6. Independent construction verified (f0,f1,f2)=(12,36,20), sphere (12,30,20), six antipodal pairs, exactly 120 graph automorphisms and H1 trace multiplicities {6:1,-6:1,2:15,-2:15,0:40,1:24,-1:24}. All ranks integral from geometric decomposition, not inferred from mod two.

## originality

PASS

Engström 2005/2008 general claw-free independence connectivity provides tools and bounds but does not compute the mixed-dimensional homotopy or integral G-lattice for this exact graph. Two highly relevant published icosahedral computations were read in complete RESULT.md: one is open-neighborhood complex N(I) with 264 nonempty faces and 23-dimensional H2, and the other is distance-neighborhood union D(I,D); neither equals ordinary independence K with 68 nonempty faces. Their representation data do not imply the integral antipodal augmentation lattice.

## value

PASS

Exact integral equivariant homology for the canonical icosahedron, with signed permutation lattice that distinguishes center inversion from rotations, is a mathematically motivated natural invariant not implied by standard graph tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
