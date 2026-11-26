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

Shattering is equivalent to s not belonging to the hull of S without s for each s, by monotonicity of hull. An intersecting pair ab,ac forces every edge on the complement of {a,b,c}; a disjoint pair forces nothing. At n≥7 this complement has at least four elements, so for each edge not already forced one can choose an intersecting pair on three complementary elements avoiding its endpoints. This forces that edge as well, proving the stable matching classification. At n=6 the intersecting pair closes to the two complementary triangles T_A. Adjoining a mixed edge ad to triangles abc and def first forces be,bf,ce,cf (using ab and ac with ad) and then ae,af,bd,cd (using bc and ef with those mixed edges). Thus a triple in some T_A fails, and one in no T_A shatters. Each bad triple has a unique T_A, so 455−10·20=255. Any four-support contains an intersecting pair; that pair with a third element either already fails shattering or generates the full hull, precluding omission of the fourth. At n=5 an intersecting pair forces its unique disjoint complementary edge, and this hull is convex. Thus the 30 bad triples are exactly a two-edge path plus a disjoint edge. A four-support with no such triple is a four-cycle, a triangle with a pendant edge, or a four-star (check four edges on four or five nonisolated vertices). The last two have a three-star whose hull is full: ab,ac,ad force be,ce,de, then bc,bd,cd, then ae. In a four-cycle each three-edge path extends to a convex five-cycle using the spare base vertex, avoiding the missing edge, so these 15 supports shatter. Two distinct four-cycles cannot share three edges, ruling out five-supports. Independent hull replay in branches/32d2bfb2-619c-47de-bc07-f1fdd3dde6ea/independent_rank2_kneser_check.py reproduced both exceptional profiles and checked pair hulls at n=7,8,9; the finite checks do not replace the all-n argument.

## originality

PASS

Credit is confined to the exceptional shattered-support classifications and exact coefficients at n=5,6, and their contrast with the stable behavior. The n≥7 rank-two shattering formula is a direct consequence of Bedo et al.'s hull-number-two theorem and the fact that all nonadjacent pairs of a rank-two Kneser graph are equivalent under relabeling. It is not counted as a separate original claim.

## value

PASS

The first two diameter-two graphs in the rank-two series have structurally different small hulls from the stable family and from each other. Classifying the exceptional shattered supports identifies the four-cycle mechanism at the Petersen endpoint and the two-triangle obstruction at six, explaining a real dimension drop and separating shattering from ordinary geodesic general position. The finite cutoffs are intrinsic, not arbitrary tabulation ranges.

The dated certificate retains the supplied scientific assessment, sources and limitations.
