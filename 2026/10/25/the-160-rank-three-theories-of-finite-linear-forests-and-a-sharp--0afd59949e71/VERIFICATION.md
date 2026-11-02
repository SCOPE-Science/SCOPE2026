---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

FO adjacency/equality quantifier rank three corresponds to three-move EF equivalence. For each path Pn with n>=7, the ordered-pair one-move adjacency-pattern type depends only on endpoint status and distances 1,2,>=3; pointed rank-two types stabilize, giving Pn≡3P7. Componentwise three-round EF composition truncates each P1,...,P7 multiplicity to at most three without increasing size. This covers all nonempty finite linear forests by 4^7−1=16,383 finite canonical cases. Complete two-vertex rank-one pattern type t_G(x,y), pointed rank-two union mask M_G(x), and rank-three sentence type S(G) are exact back-and-forth recursions. Independently enumerated all 16,383 signatures and obtained 160 distinct classes, sharp minimum-representative maximum order 23, unique sharp class 2P1⊔P2⊔P3⊔P4⊔P5⊔P7. The finite census is exhaustive only because the separate infinite-family normalization argument holds.

## originality

PASS

Brown–Hoshino determine three-move equivalence for INDIVIDUAL paths (threshold seven), not arbitrary disconnected unions or their exact theory census. General disjoint union/EF composition bounds the search but does not imply the actual count 160 or sharp size 23. Verbitsky separator results give asymptotic bounds, not this finite-rank classification. Best-of-knowledge qualified by possible unpublished tables.

## value

PASS

Complete rank-three first-order theory classification of a natural graph class, with a sharp finite-model kernel, gives a useful exact EF benchmark beyond connected paths; these numbers are not routine consequences of the path cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
