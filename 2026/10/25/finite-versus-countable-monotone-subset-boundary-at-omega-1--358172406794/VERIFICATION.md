---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: For every infinite well-orderable κ, color a pair α<β by whether g(α)≤g(β) or g(α)>g(β). The ZF Erdős–Dushnik–Miller partition theorem (or Shen Corollary 3.3) yields a size-κ nondecreasing homogeneous set: an ω-sized strictly decreasing set of ordinals is impossible. Iteration through any fixed finite list of g_i keeps the full cardinality and previously established monotonicity. For the ZFC obstruction, inject e:ω1→2^ω, allowed by ω1≤2^{aleph0}; define f_{2n}=1-e_n and f_{2n+1}=e_n. For distinct codes one of these two coordinates decreases along either order, so any common nondecreasing subset has at most one element. CH is unnecessary. No finite experiment needed; the two cases and cardinal assumptions are an exhaustive proof. The primary Shen paper full text was not retrieved; its one-map consequence also follows directly from the standard EDM theorem.

## originality

PASS

PASS, qualified by elementary folklore: the finite-family side is already an immediate iteration of Shen’s published one-map corollary and is NOT claimed independently novel; the sharp simultaneous obstruction from a countable family is an explicit complementary-coordinate antichain construction. No searched primary statement asserted the combined finite/countable boundary, but it may be textbook folklore or an immediate reformulation of known antichain results.

## value

PASS

PASS, narrowly: This is a natural exact quantifier boundary for attempting to extend a newly published monotone-subset theorem from finitely to countably many requirements: every finite conjunction preserves an uncountable common subset, but countably many Boolean requirements can prevent even a two-point one. The proof is elementary and reuses a standard antichain mechanism; its worth is the sharp, explicitly motivated failure of countable iteration, not a new result about Cantor antichains or general infinite-dimensional posets. The scope is intentionally modest and the risk of folklore coverage is significant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
