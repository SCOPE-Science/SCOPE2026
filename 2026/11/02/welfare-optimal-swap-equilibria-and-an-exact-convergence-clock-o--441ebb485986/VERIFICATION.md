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

With common degree d=(m-1)k, the red and blue gain for exchanging a red in part i and a blue in part j is (r_i-r_j-1)/d for each. A gap of at least two guarantees both requisite seats exist; within-part swaps have zero gain. The directed monochromatic neighbor count is a constant minus 2 sum_i r_i^2, so the same balancing move strictly improves welfare by 4(r_i-r_j-1)/d; all balanced vectors have the same welfare. Choosing the larger parts and their red subsets proves the census, with endpoints R=0 and R=mk covered. For k=2, writing b<=m for a chosen minority (either color at a tie), the number of opposite monochromatic pairs is m-b+T, so every improving step consumes one of each kind until T=0. Pair-category enumeration and two- and four-seat inclusion probabilities give the law and its moments. Independently checked 4,928 labeled colorings in four networks with exact adjacency-based rational payoffs, explored all terminal path lengths for 205 two-seat colorings, and verified the unequal-part and three-seat boundary witnesses. No uploaded scripts were executed.

## originality

PASS

Credit the equal-part exact equilibrium/optimum identification with the two-seat dynamical clock, not the known regular-graph potential or the textbook occupancy law. The closest inspected catalogue records change the utility or the graph and do not give this conclusion for every population on the stated multipartite networks.

## value

PASS

The characterization closes the distinction between some equilibrium and every equilibrium in a natural regular family. The two-seat theorem determines exactly how many swaps even an adversarial choice of improvements must use, and therefore yields the exact random-start law without a stochastic swap rule. The three-seat witness shows why strict welfare increase alone is inadequate for that prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
