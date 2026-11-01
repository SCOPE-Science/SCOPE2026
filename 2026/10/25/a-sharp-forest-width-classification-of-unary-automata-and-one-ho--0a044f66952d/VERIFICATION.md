---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS. In any undirected forest, a nonsimple directed accepting walk contains adjacent reverse-edge traversal; iterating that 2-step excursion yields acceptance of all sufficiently large lengths of any parity with an infinite accepted set. A directed path feeding terminal two-cycle realizes arbitrary eventual two-periodicity. Every unary regular language is ultimately periodic, represented by directed path into even cycle (treewidth2) when no forest suffices. For hole m≥1, an accepting run length m+2 must be a simple path else deleting a reverse pair wrongly accepts forbidden m; gives m+3 distinct states, attained by a path with bouncing final 2-cycle. Finite constructed checks m=1..11 and 200 lengths each corroborate only.

## originality

PASS

PASS best knowledge. Grobler–Koziel–Siebertz 2026 broad bipartite-cactus existence guarantees graph width≤2 but neither characterizes which unary languages attain width1 nor sharp forest-support state count for one hole. Kutrib–Malcher–Schneider 2021 requires symmetric transition arcs, unlike oriented forest support. Risk unavailable full new cactus paper or older unary graph-complexity result.

## value

PASS

PASS. Characterizes exactly when a unary regular language admits an epsilon-free, loop-free forest-support NFA, settling a natural graph topology threshold prompted by general cactus automata. The positive one-hole family gives an exact unbounded state cost m+3; this is a meaningful natural complete classification and sharp state invariant, not merely a tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
