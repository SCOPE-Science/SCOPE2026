---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: The eight specified halfspaces are genuine Voronoi bisectors and the other four bound a signed-permutation chamber. Independent rational reconstruction found 455 invertible intersections among 792 five-hyperplane choices, precisely 41 feasible vertices and four candidates maximizing q=27/50. A provably sufficient bounding box for site displacements (first four <1, fifth <3/2) yields precisely six equidistant nearest sites for each, all with absolute coordinate determinant 1. The 384-element site stabilizer produces three disjoint 192-hole orbits, linked by site-changing symmetries into one global orbit. Double-count 2 sites per D5 period times 576 holes per site divided by six sites per hole =192. Delaunay cells are interior-disjoint; 192 simplices of determinant 1 occupy fraction 192/(120*2)=4/5. The bounded certificate is mathematically exhaustive because of chamber containment and site-distance cutoff, not because of floating-point optimization.

## originality

PASS

PASS best-of-knowledge: the initiating Ahrend–Dutour Sikirić paper establishes the same configuration and covering radius 27/50 and a containing chamber, but accessible primary abstract does not claim the full true-hole orbit/incidence/Delaunay-occupancy classification. The published Resultary exact diagonal-ray optimizer was materially read in full and determines scalar packing-covering optimality across metrics, not the geometry of maximal Delaunay cells. A specifically cited but inaccessible companion note may contain related orbit census; no whole-document NOT_COVERING claim is made.

## value

PASS

PASS: deepest-hole orbits, nearest-site incidence and maximal Delaunay volume occupancy are natural geometrical structural invariants of the record nonlattice periodic configuration. The complete 192-hole/one-orbit/4/5 answer requires exact chamber, nearest-site and periodic counting; a known scalar covering radius alone does not determine these data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
