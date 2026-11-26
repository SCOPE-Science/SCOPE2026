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

A thresholded lower median is high iff strictly more than half the samples are high, including when the threshold equals an observed value. Each updated part is constant. At every threshold where the updated parts differ the input cut has weight at least c_w; integrating the cut inequality gives the stated upper bound. Positive weights and connectedness give c_w>0, and the binary indicator of a minimizing cut attains W/c_w. For unit weights the cut is [pq−(p−2|A|)(q−2|B|)]/2. Opposite strict-majority labels maximize the product at −1 when both sizes are odd and at 0 when at least one size is even, using that even part as the nonmajority part at a tie. If some part has size at least two, one can label the opposite part all high and put one high vertex in that part: the majorities differ but positive weight remains uncut. For the weighted K_{2,2} example, a cut can omit the heavy column by labeling it and both row vertices high, leaving exactly the two weight-one edges cut, and all eligible cuts cross at least two edges. The iteration just swaps the two constants, with a fixed point when they coincide. These arguments establish the one-input assertion, not a two-data Lipschitz bound.

## originality

PASS

The supported distinct contribution is the attained positive-edge-weight one-input cut formula for open-neighborhood lower medians on complete bipartite graphs, with the nontrivial cyclic parity and weighted amplification consequences. The threshold method and periodicity are not credited as new, and the exact unweighted odd-star overlap with a distinct same-day record is credited explicitly without inferring priority.

## value

PASS

Edge variation and the standard open-neighborhood order statistic motivate the sharp question independently of computation. The exact constant determines when this nonlinear filter can be relied on not to amplify edge variation. The result gives a complete positive-weight nonexpansivity boundary and a fixed four-vertex example with arbitrarily large attained gain, in contrast to the universal factor at most two for uniform edges. Those conclusions and the parity correction make the contribution more than the generic coarea lifting rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
