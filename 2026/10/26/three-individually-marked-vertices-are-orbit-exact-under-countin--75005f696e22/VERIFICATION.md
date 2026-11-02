---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

I reconstructed the wreath-product automorphism group from intrinsic Hamming graph edge directions, and hence the invariant per-coordinate marker-equality/status counts defining each stabilizer orbit. Every status vector is realizable for q>=4, so the stars-and-bars and multinomial formulas include all boundary types n_pi=0. For each mark a_j, counting refinement identifies distances truncated at t+1 after t rounds, hence full three-distance vectors after d-1 rounds. A single extra round recovers the multiplicities of neighbour distance-vector displacements e_S-e_T. On three marker labels, displacements for distinct nonempty partition blocks identify all two- and three-block coordinate statuses, while the distance vector and total n_pi recover the one-block status. Thus round d determines every orbit profile; equivariance gives the reverse inclusion. A separately implemented Hamming adjacency/refinement versus exact orbit-status checker passed 77 new finite triples for q=4,5,6 and dimensions 2–4; that bounded test is not the proof of universal quantifiers.

## originality

PASS

Best-of-knowledge PASS for q>=4,d>=3 with exactly three individually marked vertices, its explicit complete orbit/color-class counts and d-round guarantee. Abstract orbit-equivalence criteria for Tinhofer graphs, and existing q=3 marker or d=2 rook results, do not imply this new domain. Primary full text for the most relevant 2026 Tinhofer paper was inspected. Related Hamming perfect-coloring material remains a residual priority risk.

## value

PASS

The equality of an algorithmically defined coarsest equitable partition with a group-orbit partition is a structural infinite-family theorem. The exact number and sizes of all stable classes, plus a linear-in-d refinement bound, are precise reusable invariants rather than a routine automorphism count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
