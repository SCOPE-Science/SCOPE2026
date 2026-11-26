---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In uniform fixed-cardinality sampling, a specified v-site union has inclusion probability (k_n)_v/(n)_v, asymptotic to c^v n^(-v/r) at the critical scale. In a fixed mixed factorial moment of h occurrences, the g connected overlap components have O(n^g) placements since each pattern has bounded span. Distinct normalized patterns and distinct starts cannot be the same site set; every nonsingleton component therefore contains at least r+1 sites. Such terms vanish; the disjoint selections contribute (c^r)^h. All mixed moments converge and the independent Poisson law has a moment generating function near the origin, giving joint convergence. For each feasible interior radius-R type with s<r marks, positive-pattern counts have variance at most the mean plus O(n(k_n/n)^(s+1)): disjoint required sets are negatively correlated and only O(n) distinct placements overlap. Specifying zeros removes o(mean) occurrences in probability. The zero-mark case follows from the same first-moment removal bound with deterministic positive-only count. Types with s>r are absent with high probability. For exactly r marks, a type fixes the normalized shape and the root offset; loss through extra marks or a boundary cut has probability o(1). End windows are unmarked with high probability and their truncated counts stabilize. Effective bounded-degree Hanf locality then reduces each sentence to a finite Boolean rule on truncated pattern counts; finite integer atoms converge and the corresponding Poisson probabilities are finite symbolic combinations of masses and tail complements. Conversely any finite Boolean rule on specified exact counts is expressible by bounded successor chains and exact-count sentences. For density, the largest atom of d independent zero-count bits tends to zero. Off-critical regular powers yield vanishing or diverging n(k_n/n)^s for every fixed positive s, so all the truncated local counts stabilize in probability. The proof requires fixed sentence, radius and pattern span, and no global order. The frozen checker was read but not run; it tests finite moment identities, not the limit or locality arguments.

## originality

PASS

The reciprocal critical powers and failure of an off-critical-style zero-one law at those powers are not new in Bernoulli unary-predicate logic. The identified results do not give the exact countable dense spectrum, jointly independent normalized r-pattern coordinates, and fixed-weight successor-only classification at r>=3. The closest Resultary hit is at the square-root scale and concerns finite read statistics; only its indexed summary was accessible.

## value

PASS

The result classifies precisely what fixed-radius first-order sentences can detect at each higher collision power. It identifies independent limiting coordinates and proves both inclusion and realizability for the exact set of probabilities, explaining how a countable spectrum is still dense. This is more informative than the previously known existence of a rare-run obstruction or proof that probabilities converge.

The dated certificate retains the supplied scientific assessment, sources and limitations.
