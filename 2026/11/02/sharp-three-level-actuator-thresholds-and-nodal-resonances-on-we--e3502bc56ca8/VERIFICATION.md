---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the full symmetric Laplacian, PBH reduces to excluding eigenvectors zero on S. Split into hub-zero, zero-sum pair differences and the three-dimensional common-pair space. The pair block has two simple eigenvalues with eigenvectors nonzero at both ports, so each covered pair kills one amplitude and two uncovered pairs give an invisible difference. When a≠c, the hub coupling (a,c) has nonzero projection onto both pair eigenvectors: its orthogonal direction (c,−a) is sent by the pair block to a positive multiple of (1,−1). Thus the common-pair block has simple eigenvalues disjoint from the pair eigenvalues and no hub-zero eigenvector. A nonconstant common mode vanishing at x has z_o=−my by orthogonality to constants; the x equation then gives b=ma, and (−m,0,1) on the common coordinates realizes it. The y counterpart gives b=mc. With equal spokes, antisymmetric pair modes require coverage of all pairs. At the only collision, b=mu, the merged eigenspace has coordinates z_o=−2mr, (x_j,y_j)=(r+t_j,r−t_j). One hit per pair lets the t_j cancel any r; the hub or a double hit forces r=0. Off collision the remaining symmetric modes are visible with all pairs covered. These facts give the minimum sets and their counts, including m=2. A wholly unseeded petal cannot first be forced, and one seed per petal cannot start with a white hub; adding the hub proves Z=m+1.

## originality

PASS

The supported distinct contribution is the all-positive-weight, all-placement classification, especially the two one-port nodal failures and the symmetric weighted collision. The unweighted minimum, placements and zero-forcing baseline already have coverage; no novelty is credited to them.

## value

PASS

The result explains exactly which independent coordinate inputs can be removed by asymmetric weighting, and why merely counting eigenvalue multiplicities is insufficient for placements on the nodal surfaces. It supplies a usable complete criterion across an entire natural repeated-weight family, including examples where actuating one port but not the other changes feasibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
