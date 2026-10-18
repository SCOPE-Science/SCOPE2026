---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

An edge-open packing S has endpoint-induced graph consisting of nontrivial star components: an unselected joining edge or a four-vertex path contradicts the third-edge exclusion. Conversely such an induced star forest yields a unique S. Canonical selected vertex degree 0/1/>=2 prevents multiplicities (even for K2). Five parent interfaces separate unselected, leaf with selected parent, leaf without selected parent, center with unselected parent, center with selected leaf parent. The specific a,b,h,c,d recurrences in inspected RESULT.md enumerate these classes and attach each parent-child selected edge with exactly one z. Root uses a+h+c; connected components multiply. Induction proves all n, not the finite tests. Independent fresh brute-force third-edge checks on P5, K1,4 and six-vertex fork produced polynomials [1,4,4], [1,4,6,4,1], [1,5,6,2], equal to a separate implementation of the 5-state recurrence. O(n^3) counts polynomial arithmetic not bit complexity.

## originality

PASS

Chelladurai et al. 2022 already noted induced-star support; Brešar–Samadi 2024 compute only the largest EOP size in trees by scalar DP. Their inspected Section 3 and Theorem 3.6 do not present a complete coefficient polynomial. The specific disjoint coefficient-counting recurrence is assessed new best-of-knowledge, not the structural star equivalence or basic tractability.

## value

PASS

The studied natural packing invariant has an all-cardinality distribution, number of optimal solutions, and counting recurrence beyond the known extremal scalar. A canonical state decomposition for every forest is independently useful and not an arbitrary single-graph computation; practical polynomial-time arithmetic produces coefficient multiplicities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
