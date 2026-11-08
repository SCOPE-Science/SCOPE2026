---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For Cr_n=K_{n,n} minus a perfect matching, distance-two pairs are precisely same-bipartition distinct-index pairs. At most one red-isolated vertex per side, so >=n-1 red edges; equality forces a matching omitting one vertex each. If omitted indices differ a same-side pair has no rainbow geodesic, hence both are same s. The n-1 matching corresponds to a permutation of [n]\{s} with no fixed points (graph has missing diagonal); a two-cycle creates an unavailable pair of red intermediates, and conversely absence of 2-cycles makes all same-side pairs have an available red-blue two-step route. EGF for permutations with cycles length>=3 is exp(-z-z^2/2)/(1-z); n choices s gives n*a_{n-1}. At n=3 Cr_3 is C6; two alternating colorings, three red edges. Independently enumerated every subset of red edges through the first feasible cardinality for n=3,4,5, recovering min/count (3,2),(3,8),(4,30); evaluated the n=6..8 constructor and code scope separately. This is not full rainbow connection of diameter-three matched pairs.

## originality

PASS

Existing rainbow connection results under Dirac-style minimum-degree conditions and crown-graph basics do not provide the named-red sparsity optimum and all-optimal-cycle-cover bijection; a binary separating matrix equivalence may have been missed.

## value

PASS

A natural two-color routing-with-minimum-secondary-color-resource problem has a complete extremizer and enumeration theorem. The crown graph is near the Dirac density boundary yet has forced distance-three pairs; the permutation no-short-cycle structure gives more insight than a single minimum number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
