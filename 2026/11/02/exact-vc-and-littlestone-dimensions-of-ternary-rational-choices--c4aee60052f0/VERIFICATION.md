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

Concepts are strict rankings on seven alternatives queried by designated-top-of-three predicates, not betweenness. There are 105 queries and exactly 2520 distinct concepts because swapping two bottom alternatives preserves all ternary-top answers. Five two-anchor queries shatter all 2^5 patterns. Source verify_top_choice.py implements a symmetry-reduced exhaustive six-support obstruction: every six-query shattered family would be relabeled to contain the fixed q0; its integer-bitmask trace-partition search reports no size-six supports after 286503 viable prefixes. Source certificate top_choice_depth10_certificate.json explicitly gives 1023 internal nodes and 1024 distinct rank witnesses at depth ten; an independent traversal of the actual Git blob checked all 1024 leaves, all 10 branch labels per leaf, exact depth and distinctness with zero violations. Every possible root query is positive on only 840 distinct concepts, below the 1024 required for depth 11. On disjoint query domains, ordinary shattered-set and version-space recursion prove VC and Ldim additive, yielding 5t and 10t for any t>=1; no one-context 7t ranking claim.

## originality

PASS

Exact base dimensions and the concrete adaptivity gap for the ternary highest-choice predicate are distinguishable from axiomatic rational choice theory and from learnability of binary menus. Generic product additivity is prior standard, not claimed as novel. Kalai 2003 concerns rational choice learnability but complete text was inaccessible, leaving nontrivial historical-priority risk.

## value

PASS

Natural finite concept class on seven alternatives, a complete exact pair of static/adaptive dimensions with a nontrivial depth-ten finite certificate, and a rigorous disjoint-context product giving a linear adaptivity gap; precise invariant can be reused in rational choice online-learning comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
