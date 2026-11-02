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

From actual RESULT.md, the order polytope indicator is log-supermodular under coordinate min/max, so continuous FKG association applied first conditionally in X and then to F_i(Y_i) yields q(P)>=2^-n, strictly when a pair of coordinates is poset-comparable. Conditional on two linear extensions, the common order-statistic interleavings satisfying X<=Y form a subset of Catalan ballot words; different extensions exclude the alternating ballot word. Hence q<=1/(n+1), strict unless unique extension (chain). Comparing volumes of O(P×C2) and O(P)² yields e(P×C2)/(binom(2n,n)e(P)²); conditioning on star tops yields (p+1)2^(p-1)(p!)²/(2p+1)! and stated Stirling asymptotic. Independently recomputed all 75 forward-oriented relation subsets up to 4 points and five stars by exact integer extension DP; these finite checks do not prove all-poset assertions.

## originality

PASS

Classical association, order-polytope triangulation, ballot/Catalan combinatorics, and Fried’s chain/simplex equality case are acknowledged. The asserted joint all-poset sharp sandwich with both rigidity cases, exact extension-count interpretation, and star interpolation was not mathematically implied by the materially inspected primary results. Best-of-knowledge rather than definitive priority.

## value

PASS

The simultaneous sharp inequalities and rigidity at two natural endpoints classify the comparability probability of every finite order polytope. The doubled-poset count connects geometric probability to standard linear-extension data, while the exact natural star family is a nontrivial interpolation/asymptotic. This is a motivated structural global theorem, not a rearranged textbook calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
