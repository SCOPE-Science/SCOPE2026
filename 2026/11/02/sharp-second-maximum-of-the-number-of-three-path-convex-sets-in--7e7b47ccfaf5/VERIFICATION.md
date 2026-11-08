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

A vertex subset is P3-convex exactly when every unselected vertex has at most one selected neighbor. For rooted trees t>=5, A(H,v)>=2t−2 by leaf removal and two additional sets; for nonstar trees m>=6, one-neighbor defect D(T,v)>=2m−4 via path subsets and disconnected pairs. Adding a leaf yields c(T+)=2c(T)−D(T,v). Exact broom counts c(B_n)=3·2^(n−3)+2n−2 and strict nonhub defects for m>=9 give equality rigidity. Independently generated all 47 unlabeled n=9 tree types using canonical rooted parentheses, directly counted valid subsets and confirmed unique broom maximum 208; induction establishes all n>=9 trees. Additional edges strictly remove at least one convex set; universal-vertex nonstars bounded by star plus leaf-edge, extending to all connected simple nonstars. Finite n=9 enumeration supplies only induction base, not an infinite proof.

## originality

PASS

Dourado–Grippo–Lin–Protti (2026) prove the unique connected STAR maximizing total P3-convex sets and a tree recursion. The second highest nonstar exact formula and broom-only equality are not implied by that first maximum and require sharper rooted defect estimates; searched near-extremal P3 and two-neighbor bootstrap formulations lacked an exact covering result.

## value

PASS

A sharp runner-up extremal graph theorem with unique optimizer is a natural stability layer beyond a recently proven primary extremal question; the rooted recurrence/defect lemma is reusable in P3 convexity and bootstrap closed-set counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
