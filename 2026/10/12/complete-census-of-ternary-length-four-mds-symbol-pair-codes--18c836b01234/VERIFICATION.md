---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Agreement on two adjacent coordinates of different codewords implies pair distance at most three, proving upper bound 3^2=9. Independently rebuilt all 81 vertices and the full pair-distance-four adjacency graph (2268 edges); separately enumerated all maximal cliques, obtaining counts 1296 of size6, 28512 of size7, 8784 of size9, no larger ones. Independent translation-and-additive-closure test of each 9-code gave 252 affine, rest 8532 non-affine. Independently generated S3 coordinate symbol exchanges and D8 rotations/reflections, traversed all 8784 codes into 11 orbits with given sizes; explicit nonlinear code belongs to maxima. This finite enumeration exhausts the full specified finite domain, not a timed lower bound.

## originality

PASS

Singleton maximum size and existence of optimal codes are established prior work, explicitly not claimed new. The all-label extremizer histogram, non-affine majority and 11-group-orbit classification are not implied by existence or known linear constructions, and no matching tabulation appeared in targeted Resultary/primary comparisons. Full finite classification remains best-of-knowledge with unindexed-table risk.

## value

PASS

An exact classification of all equality cases of a natural MDS bound, including the sharp affine/non-affine distinction, is a meaningful finite classification of nonlinear error-correcting codes; 8784 maxima and 11 subgroup orbits are not an arbitrary tiny slice or a repetition of the known Singleton optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
