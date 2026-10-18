---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Every pendant leaf of a restrained Italian labeling must be 1 or 2: leaf zero with root zero fails Italian neighbor sum, and leaf zero with positive root is isolated in zero-induced graph. Thus zero set S consists only of roots and is admissible iff G[S] has no isolated vertices. For each fixed S, n-|S| outside root/leaf pairs each contribute (z+z²)²; b(S) boundary zero roots have freely 1/2-labeled leaves; |S|-b(S) interior zeros force leaf 2. Product gives exact stated polynomial. Nonnegative distinct terms imply minimum 2n-max b and count of optimizers. On C_n every proper admissible S decomposes into k cyclic 1-runs >=2 and 0-gaps >=1, b=2k. Composition of s selected and n-s unselected into k runs and gaps gives n/k binom(s-k-1,k-1) binom(n-s-1,k-1); k≤floor(n/3). Maximize k to derive minimum 2n-2floor(n/3) and #min n/k binom((n-3k)+2k-1,2k-1). Independent direct ternary enumerations for all 12 graphs on n<=3 incl empty/disconnected bases matched polynomial. The infinite formula follows by case decomposition, not finite checks.

## originality

PASS

The foundational restrained Italian domination paper defines the parameter and classifies extremal values, not its all-weight leaf-corona enumerator. The restrained domination polynomial is a set-valued different invariant. An abstract of a plausible 2023/24 corona-related RID paper mentions minimum values, not all coefficients; full article inaccessible and remains a residual risk. The all-base-graph coefficient identity and explicit sunlet run-profile are best-of-knowledge additions.

## value

PASS

Weight enumerators of restrained dominating functions refine minimum domination numbers and determine a complete distribution relevant to graph polynomial studies; the admissible-zero induced-boundary reduction is a reusable structural lemma for every finite base graph, while sunlet is a natural cycle-corona specialization. No invented algorithmic complexity gain; subset sum may be exponential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
