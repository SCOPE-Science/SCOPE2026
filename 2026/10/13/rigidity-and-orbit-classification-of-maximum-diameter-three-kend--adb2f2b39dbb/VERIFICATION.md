---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Split diameter-three anticode by inversion parity; each slice has diameter <=2. Normalize a slice member to identity: other members correspond to two-inversion graph edges. Pairwise intersecting edges form a star or triangle; maximum degree n-2, and equality for n>=5 yields a full star (no triangles when n=5). This identifies each full parity slice as unique N(a). For equality total 2(n-1), both slices are such neighborhoods, and if centers are not adjacent a large-inversion neighbor violates cross distance <=3. Adjacent center double balls attain bound, center edge unique; counting edges yields n!(n-1)/2 and orbit positions i~n-i. Independent enumeration verified two-inversion patterns for n5/6/7 and all 240/1800 double balls with distinct center edges for n5/6; unrestricted proof does not rely on finite tests.

## originality

PASS

Best-of-knowledge same-object comparison finds no prior complete final classification; exact source implications, aliases, and residual risks explicitly recorded. No failed search is offered as proof of novelty.

## value

PASS

Determines all equality shapes in an established natural Kendall permutation anticode extremal theorem for every n>=5, not merely reproducing known optimal size. Center-edge uniqueness, exact labeled count and isometry-subgroup orbits are meaningful rigidity refinements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
