---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Let d=2m-2 on G=K_{2m} minus the perfect matching with sink s and drive u its forbidden partner. The reduced Laplacian sends q=(2 at u, 1 at every W vertex) to d e_u, giving a valid first-excess odometer bound t<=q even if comparison terminal heights at u are negative. Equality requires c_u=d-1 and every other c_v>=1. Dhar burning on H=G-u with same sink gives a precise iff h_v=c_v-1 recurrent, by a one-height and one-threshold shift, and yields determinant count (2m-3)^(m-1)(2m-1)^(m-2). Total recurrent count (2m-2)^m(2m)^(m-2); Green stationary equation Delta E t=e_u yields E T=2m/(2m-2). Product-limit yields e^-1 of mean toppling activity carried by rare extremes. Independent complete enumeration for m=2,3,4 checked total states 4,384,82944, extremal 1,45,6125 and means 2,3/2,4/3. Unbounded m is analytic spectral/burning proof.

## originality

PASS

PASS best-of-knowledge: the closest full published sink-deletion theorem assumes drive adjacent to the sink and proves no site topples twice, so it is inapplicable to the uniquely nonadjacent drive here, which topples twice in the maximizer. The complete-bipartite published e^-1 activity example likewise has adjacent drive, different graph, different counts and odometer. Here a distinct one-vertex deletion and shifted burning characterization yield the exact CP-graph formula. Unindexed sandpile work remains a priority risk.

## value

PASS

The deleted matching creates a natural extremal sandpile regime genuinely different from standard adjacent-sink avalanches: an exactly characterized double toppling, an all-m spanning-tree count and a nonzero asymptotic 1/e share of mean activity from O(1/m) probability events. This is a motivated graph-family structural law with a nontrivial asymptotic effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
