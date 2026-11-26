---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

By the Galois correspondence the extents are intersections of reflexive closed neighborhoods. Distinct centers at distances 1, 2 and ≥3 give respectively their edge, the midpoint and the empty set; no singleton leaf occurs. A star has common center and yields precisely the height-two case. In a nonstar tree the internal neighborhoods are distinct incomparable proper sets: inclusion between different centers forces adjacency, and the smaller center has another neighbor that the larger center cannot contain. Every edge lies in an internal neighborhood and contains an internal endpoint. Between an internal singleton and any internal neighborhood containing it there is an incident edge inside that neighborhood (use the center-to-singleton edge if they differ). Thus there are no rank jumps, and counting the strata gives the claimed polynomials. The incidence of ranks one and two recovers all edges, including one separate leaf per edge with only one internal endpoint. Higher proper extents are joins of their center's incident edge extents, so reconstruction and the action of graph automorphisms are inverse on automorphisms; the star case is permutation of atoms. Three consecutive internal vertices on a diameter path of length ≥4 give the explicit modular-law failure in Step 4. For a double star, the two rational three-spaces intersect in the common edge plane; leaf-edge planes on opposite sides are complementary, and same-side planes meet in their atom and sum to their three-space. Together with the listed atoms and common plane these relations verify closure under intersection and sum, proving modularity. The P3 and P4 lattices are B2 and the product of two three-element chains; larger stars and other double stars contain the indicated M3 sublattices. An independent enumeration intersected closed neighborhoods, computed order ranks, reconstructed edges and checked the two laws on all meet/join triples for all 1440 labeled trees of orders 3–6. It did not enumerate automorphism groups. Replay by decoding length n−2 Prüfer sequences, intersecting neighborhoods over all vertex subsets, and using inclusion to compute ranks and the least upper bounds; the general proof does not depend on the enumeration. Frozen VERIFY.py was inspected but not run.

## originality

PASS

The distinct contribution supported by the checked statements is the exact rank profile, low-rank reconstruction and sharp lattice-law thresholds for the reflexive closed-neighborhood context of every finite tree in scope. The general intersection representation and general context reconstruction principles are not claimed as new. The closest same-day indexed graph reconstruction was compared on its actual incidence and hypotheses; it does not cover this context. Remaining older literature access risks limit any priority claim.

## value

PASS

This gives a complete structural answer for a standard context family, recovers the tree and its symmetry from two lattice ranks, and detects sharp and different modularity and distributivity boundaries. In particular the diameter-three threshold is not obtained by simply counting extents or by applying the generic context representation. The formulas are useful exact invariants beyond the small finite checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
