---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Word reversal keeps R and sends U to mn−U. Given the initial symbol and R, each pair of positive compositions of the specified lengths is equally likely, giving independence. Stars and bars gives the weak-composition factorial moment 2(M−s)(M−s−1)/(s(s+1)); exchangeability plus the fixed sum then gives the displayed projection covariance. After centering both compositions, the two linear terms and one bilinear term have zero pairwise inner products by independence and zero means. Recomputed the staircase sums by subtracting squared row/column sums divided by the other dimension and then adding the squared grand sum divided by the matrix size. The even orientations have equal mass and opposite offsets ±P/(2k); their between-orientation variance is therefore required. The odd orientation weights are (m−k)/(N−2k) and (n−k)/(N−2k), and both feasible orientations have mean P/2. A zero-weight orientation need not have a valid composition; its term is omitted, so substitution and the formula extend to the maximal imbalanced odd stratum. Equal counts at k=m=n exclude the undefined denominator. The symbolic replay verified both variance reductions and all three strict-gap identities. With a=m−k and b=n−k the right-odd gap is positive when a+b>0, the left-odd gap has a positive constant even at a=b=0, and the even-step numerator is positive since P≥k. A separate exact prefix recurrence for counts, inversion sums and squared sums confirmed every feasible stratum up to 14 of each symbol.

## originality

PASS

The supported contribution is the explicit all-size sign classification and positive gap formulas, with evaluated parity-dependent variances as the means of deriving them. The joint enumerability of U and R, and hence extraction of moments as such, are covered by an earlier area/corner identity after endpoint refinement. An exact equivalent of the submitted variance and parity conclusions was also identified in a distinct later-dated catalogue entry; this is documented overlap, not shown earlier coverage or a finding about provenance.

## value

PASS

Two standard statistics of the same fixed-size null exhibit an exact and nonmonotone interaction. Reversal forces the conditional means to be equal, but supplies no ordering of dispersions; the strict peaks at every even count and the exact gaps determine which successive strata gain or lose inversion variability. This is useful information beyond the computable joint enumerator or marginal rank variance. It is a complete boundary-sensitive statement for a natural conditioning variable, not a small-instance anomaly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
