---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The source proof is reconstructible: product algebra C=k⊕V⊕W⊕V⊗W has radical M, M²=V⊗W and M³=0. Since (v+w)²=2v⊗w and char(k) !=2, the intrinsic square-zero locus in M/M² is V union W. For m≠n every augmented algebra automorphism fixes both pieces; its restriction to M² is S⊗T, and intertwining the two oriented operators forces id⊗R=Q⊗id and thus Q=R=cI with c(c+lambda)=0. For m=n, tensor-operator ranks force rank Q=rank R; the relation Q(Q+lambda I)=0 means equal-rank operators are similar, via square-zero Jordan blocks at lambda=0 and 0/-lambda eigenspace decompositions otherwise. The induced factor isomorphisms construct reverse-order isomorphisms. The smallest strictly intermediate balanced example m=2,n=4,ranks1,2 has total dimension15 and rank7 on either order. The finite checker verified tensor rank formulas on four independently constructed examples, but the universal statement rests on the algebraic proof.

## originality

PASS

Compared precise theorems against their implication directions and alternate formulations using inspected primary literature and Resultary; no covering statement identified; residual priority risks remain and absence of a match is not a novelty proof.

## value

PASS

Classifying all reversal isomorphisms, rather than the ordinary flip alone, isolates an intrinsic multiplication obstruction invisible to linear-operator rank and resolves the mathematically motivated fixed-intermediate-ratio braiding question for full monoidal subcategories. The 15-dimensional positive-rank boundary is a sharp natural witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
