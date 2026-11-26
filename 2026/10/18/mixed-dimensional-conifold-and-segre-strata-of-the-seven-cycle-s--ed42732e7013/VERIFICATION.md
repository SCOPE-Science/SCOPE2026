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

The face and lattice census was independently replayed with python /workspace/branches/record-5-replay.py, not by running the frozen checker. The inequality representation can be seen by first dropping the odd-cycle inequality: a fractional vertex with a proper path of fractional coordinates joined by tight edges could be perturbed in the alternating direction, so the only fractional vertex is the all-half vector. It has seven independent active edge constraints; along each incident edge, the other six equalities form a path, the coordinates alternate t and 1−t with four copies of t, and the feasible segment has 0≤t≤1/2. The sum is 3+t, so cutting off the all-half vertex at total 3 introduces no fractional vertex. The replay generates all common active-facet sets of nonempty subsets of the 29 stable-set vertices, identifies 15 facets, and independently checks ranks using vertex differences and lattice indices by gcds of integral minors. Face counts in dimensions 0–7 are 29,140,301,350,231,84,15,1 (total 1151); nonsmooth counts are 28,105,126,56,7,0,0,0 (total 322). No simplicial cone is nonunimodular, and the inclusion-minimal bad cones are exactly the seven of each displayed type. Each A_i leaves four path vertices with the induced full lattice; each B_i is a unimodular tetrahedron, verified by its vertex differences. For each transverse cone the primitive relation has coefficients +1 on one block and −1 on the other, and a deleted-ray basis spans the saturated cone lattice. The dual affine monoid is thus the set of nonnegative integral vectors with equal totals on the two blocks. Pairing unit masses across the blocks gives the Segre generators, with the 2×2 minors as relations, for a 2×2 and a 2×3 matrix respectively. Saturation splits off the orbit torus, and degrees 2 and 3 give the transverse multiplicities. These integral models and the regular-cone test work in every stated characteristic.

## originality

PASS

The supported distinct result is the complete reduced C7 singular-locus classification, including the Gorenstein conifold components, mixed-dimensionality and the full orbit/cone census. The B_i faces are not new: Miyazaki identifies them as the non-Gorenstein support in the Ehrhart cone and a closer odd-cycle catalogue theorem already gives their projective closures and exact primitive normal-cone circuit. The generic Segre description on those components follows from that known circuit. No source inspected determines the entire singular locus and remaining census of this fan.

## value

PASS

C7 is the smallest chordless odd cycle with a three-pair odd-hole obstruction of this type. The exact fan computation separates non-Gorenstein Segre strata from larger Gorenstein conifold strata and shows that the singular locus is not pure-dimensional. It supplies checked local models and a usable orbit census, not just the already-known existence of the non-Gorenstein subvarieties. Equality of the singular and non-Q-factorial supports is additional useful geometric information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
