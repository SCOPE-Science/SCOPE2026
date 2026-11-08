---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For two distinct positive queries x,y, common positive centers are q−2 points on their coordinate line when d_H(x,y)=1, exactly two switch-point centers when distance=2, or empty otherwise. Any third query splits the line into at most one versus the rest, hence the doubly positive candidate family has Ldim<=1; no complete adaptive depth-four tree exists. The packaged TREES.json depth-three witnesses for H(2,3), H(4,2) and depth-two H(3,2) are consistent with distance-one relations; independently computed exact finite Ldim via recursive candidate splitting, obtaining Ldim values 1,1,2,3,3,3,3 for (d,q)=(1,3),(2,2),(3,2),(2,3),(4,2),(3,3),(2,4). Product alphabet/dimension embeddings extend lower bounds, small neighborhood sizes give exceptional upper bounds. Read Adler–Benediktsson–Macpherson Theorem 4.7 in accepted full text: VC=3 exactly for d>=3,q>=3 or d>=2,q>=4 or d>=4,q>=2, and VC=2 at H(2,3). Thus unique strict Ldim>VC gap H(2,3). Infinite upper bound is structural, not inferred from finite enumeration.

## originality

PASS

The same open-neighborhood VC classification is established and explicitly credited to Adler–Benediktsson–Macpherson; adaptive Littlestone dimension and its unique strict VC gap do not follow solely from static VC classification. The exact online formula survived targeted published-search checks, qualified by literature breadth.

## value

PASS

The exact online/adaptive shattering dimension of an infinite natural graph family is a substantial learning-theoretic invariant. The unique H(2,3) gap clarifies that adaptive and static neighborhood complexity differ in one sharp exceptional family. It uses nontrivial structural geometry, not just a trivial VC restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
