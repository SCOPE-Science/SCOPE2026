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

# Reproducible finite verification

The standalone `verify_t6_neighborhood.py` uses Python 3 standard library only; invoke `python3 verify_t6_neighborhood.py`. It recreates all 15 two-element labels of a six-element set and their 15 degree-eight open neighborhoods. It exactly enumerates 2881 faces, including the empty face, with f-vector `{-1:1,0:15,1:105,2:420,3:945,4:840,5:420,6:120,7:15}`. A sequential-toggle matching in the specified order has 1395 matched pairs including the augmented empty-face pair and 91 critical four-vertex faces. An exact directed Hasse-graph topological sort consumes all 2881 faces and checks 12945 cover relations, certifying acyclicity, not merely claiming a partial search found no cycle.

The checker then tests each of all 720 six-label permutations preserves the neighborhood facets and computes the exact signed simplicial chain Lefschetz sum on every fixed face. By degree-three concentration it negates each reduced Lefschetz value to obtain the actual rational H3 character. A distinct implementation of the Murnaghan–Nakayama rim-hook rule gives the eleven Specht multiplicities, with dimension weighted total 91.

Verified terminal markers: `ALL_MORSE_ARROWS_ACYCLIC`, `S6_IRREDUCIBLE_DECOMPOSITION_VERIFIED`, and `FULL_S6_NEIGHBORHOOD_CHARACTER_VERIFIED`.

The verification is exhaustive **only for the finite graph defined here**. No integral equivariant lattice splitting, homotopy classification at seven or more labels, or contractibility of the full group quotient is established.
