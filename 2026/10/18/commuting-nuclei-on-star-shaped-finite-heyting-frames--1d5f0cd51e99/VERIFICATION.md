---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The rooted star P_n has 2^n leaf upsets and one top. A nucleus j has leaf behavior U union (L\A) determined from j(empty), since meet preservation with singleton leaves prohibits introducing an A-leaf not in U. The filter of inputs whose images contain the root is principal; its generator is either top (flag 1) or exactly A (flag 0), the latter forced by idempotence. Thus exactly 2^(n+1) maps J_(a,A). For two maps leaf components of compositions coincide; root membership in mixed flags compares A cap B subset U with A subset U, giving precisely the inclusion criterion. The families F_I are maximal by inserting all eligible subsets and supersets. Per-leaf binary incidence for h flag-zero and k-h flag-one tuple entries gives 2^h+2^(k-h)-1 choices, independent across leaves, proving the all-n,k spectrum and probability. A fresh evaluator computed every ordered commuting pair for n=1..4 (14,50,182,674) using pointwise maps rather than the case proof; the symbolic proof handles all n and k.

## originality

PASS

Lindenhovius and Ochs already supply the Artinian-poset subset/nucleus parametrization, so that general bijection is NOT new. Full Ochs text gives the inverse map explicitly but no root-star composition criterion, maximal commuting family classification or k-tuple spectrum. Searches of published mathematical findings produced no matching dominating formula. The potential general rewriting of composition of subset-generated nuclei remains a priority risk, so originality is best-of-knowledge.

## value

PASS

The exact compatibility graph, maximal-clique stratification indexed by I, all-arity count and asymptotic commutation probability give a natural structural profile of meet-preserving closure operations on the simplest nonchain distributive lattices. These data are not textbook consequences of counting single nuclei and plausibly useful when studying commuting localizations or simultaneous closure operations. Not claimed for arbitrary posets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
