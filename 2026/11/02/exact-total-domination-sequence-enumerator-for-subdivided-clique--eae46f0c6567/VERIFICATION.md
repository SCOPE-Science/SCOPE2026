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

The incidence graph is bipartite between originals A and subdivision vertices B. Every open neighborhood of A lies in B and vice versa, so relative legality and eventual coverage of an A subsequence and B subsequence are independent. An A history consists exactly of n−1 originals in any order with n! possibilities, since remaining two originals are connected by an uncovered edge until the (n−1)st choice. A B history is an ordered covering edge sequence of K_n, each edge introducing one or two unseen original vertices; the last edge introduces one new vertex in r(r−1) ways or a new pair in binom(r,2) ways, yielding the stated recurrence. All such histories have ceil(n/2)≤k≤n−1 and shuffle independently in binom(n−1+k,n−1) ways. The extreme coefficients follow ordered matchings and sequential edge introductions. Independent literal graph open-neighborhood DP gave T2=4z², T3=216z⁴, T4=1440z⁵+34560z⁶, but these finite checks are not the universal induction proof.

## originality

PASS

Brešar–Henning–Rall (2016) general incidence-graph theorem already implies the MAXIMAL length 2n−2, which is not novel separately. Earlier total-uniform graph and Grundy covering sequence work does not state this complete exact number of ORDERED sequences at every length for S(K_n). The distribution and extreme multiplicities survive as a natural refined invariant.

## value

PASS

The full legal-history generating polynomial and complete length spectrum are natural finer invariants of total domination sequence dynamics on a canonical family, extending an extremal-only theorem with exact multiplicities; not reducible to the number of unordered edge covers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
