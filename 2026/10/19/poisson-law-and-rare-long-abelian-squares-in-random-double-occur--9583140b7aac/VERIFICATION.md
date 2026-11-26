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

Each perfect matching has q! labelings, so removing labels gives the uniform matching. Equal Parikh vectors in a fixed window require one copy of each used symbol in each half, i.e. a matching of the halves with no edge out of the window. There are k! internal pairings times (2q−2k−1)!! external pairings, and 2q−2k+1 possible starts. This gives the exact expectation, including the full-length boundary via (−1)!!=1 and q=1 with only one term. The length-k expectations have increasing successive ratios (k+1)/(2q−2k+1). Up to the middle these are at most 3/4 for q≥4, making the contribution from k≥3 there at most 4E_(q,3)=O(q^−2). Beyond the middle log-convexity bounds each term by the larger of the exponentially small midpoint and the final q!/(2q−1)!!=O(√q·2^−q). Thus all nonadjacent lengths contribute 2/(2q−1)+O(q^−2). The r-fold binomial moments of X_q count r disjoint path edges, of which there are binom(2q−r,r) choices, times their inclusion probability. Dividing that binomial by the product of odd denominators leaves 1/r! times a product of factors 1−(r−j−1)/(2q−2j−1). For r≤q/2 the product error is at most r(r−1)/(2(q+1)); for larger r the factorial bound suffices. Binomial inversion and summing over the output index give a 2^r weight, still summable with the factorial bound, yielding the claimed adjacency TV rate. Coupling to Y_q costs at most E(Y_q−X_q), and avoidance is the event Y_q=0; exact finite adjacency-only avoidance separately follows by inclusion–exclusion. Inspected RESULT.md lines 34–110, VERIFICATION.md and verify.py. The finite normalized-word enumerator and its 146599 count are reported as frozen supplementary checks; the script was not run independently.

## originality

PASS

The exact path-adjacency distribution and its mean one have direct earlier coverage. The supported distinct claim is the all-occurrence expectation with its longer-square correction and the quantitative extension of the Poisson law to all contiguous half-lengths in the fixed-double-occurrence ensemble, not the separate adjacency law or a claim of novelty for an inclusion–exclusion method.

## value

PASS

For a natural fixed-content word model, exact counting and a uniform estimate across all lengths show that longer squares are collectively rare despite the many possible windows. The leading correction isolates length four and determines why a Poisson result for the adjacent-repeat statistic answers a genuinely different full avoidance problem. Value does not rest on rederiving the finite adjacency table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
