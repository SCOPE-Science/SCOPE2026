---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For any coalition C, its utilitarian welfare is exactly 2 W(C)/|C|, where W is the sum of internal signed weights. Split off nonpositive/nonconnected components without loss. Every connected coalition of size q≥4 is a path or entire cycle. On a path or even cycle, two alternating matchings of positive edges ensure a matching contribution at least P/2≥W/2≥2W/q. On an odd cycle q≥5, cyclically averaged (q−1)/2-edge matchings guarantee (q−1)P/(2q)≥2W/q. Thus an optimal partition exists with only connected blocks of sizes 1,2,3. The three-tile path recurrence and six 0-containing cycle cases, plus a triangle special case, completely optimize in O(V+E) real arithmetic/comparisons. Unweighted P3 needs size three (welfare 4/3) and K1,3 shows the max-degree-three boundary (3/2>4/3). Independent exhaustive unrestricted partition comparison verified 275 small signed path/cycle instances, not an all-graph proof.

## originality

PASS

Published bounded-treewidth weighted fractional-hedonic algorithms cover paths/cycles as a class but give magnitude-dependent (nW)^{O(ω)} bounds, not this strongly linear sign-independent algorithm. Prior unweighted-tree diameter-two lemmas and unweighted degree-two easy-case comments do not cover arbitrary signed cycles. No equivalent structural matching replacement was found in inspected material; historical equivalence in graph partition literature remains possible.

## value

PASS

The sharp connected-triple existence threshold and signed-weight-agnostic linear-time algorithm are a robust, nontrivial classification of optimal utilitarian groups on natural degree-two networks; both P3 and claw witnesses explain why the exact cutoff and degree assumption matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
