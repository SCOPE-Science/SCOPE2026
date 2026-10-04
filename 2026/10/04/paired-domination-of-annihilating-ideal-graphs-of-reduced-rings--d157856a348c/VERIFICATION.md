---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The proof is checked through the following structural points.

1. For each minimal prime \(P_i\), the product \(A_i=\prod_{j\ne i}P_j\) is nonzero and is annihilated by \(P_i\).
2. Distinct \(A_i\) multiply to zero, so they induce a clique.
3. Every annihilating ideal is contained in at least one \(P_i\) selected by a nonzero annihilator element; hence the clique totally dominates.
4. Every \(P_i\) is maximal among proper annihilating ideals. Neighbors of the \(P_i\) in a total dominating set therefore have pairwise distinct annihilators, proving the lower bound \(m\).
5. Paired-dominating sets have even order. The clique has a perfect matching for even \(m\); for odd \(m\), adding \(P_1\) permits the matching \(P_1A_1\) plus a perfect matching on the remaining clique vertices.

A standalone exhaustive check on the support model of products of fields gives:

```text
m=2 vertices=2 gamma_pr=2
m=3 vertices=6 gamma_pr=4
m=4 vertices=14 gamma_pr=4
m=5 vertices=30 gamma_pr=6
VERIFY_OK
```

The computation verifies representative finite cases only. The proof of the theorem for arbitrary reduced rings with finite minimal spectrum is the symbolic argument above.
