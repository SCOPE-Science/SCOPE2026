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

For a uniform vertex in a fixed retained subgraph, the j-th raw component-size moment is n^{-1} times the sum of component sizes to power j+1. When the independently retained new edge joins components of sizes a,b, the conditional increments for j=1,2 are 2ab/n and 3ab(a+b)/n; otherwise both vanish. Calling their expectations A and B gives a mean increase pA and a variance change p(B-2 mu_G A)-p^2 A^2. The all-closed state proves A>0 for every interior p and supplies the leading values mu_G=1, A=2/n and B=6/n with O(p) errors, giving the coefficient 2/n in the variance change. In every merging state a+b<=n, so B<=3nA/2 and mu_G>=3n/4 yields strict negativity even at equality via -p^2 A^2. Connectedness gives mu_G tending to n, and polynomial continuity gives a crossover, not uniqueness. The threshold uses the original graph's mean; the variance averages over both seed and bonds.

## originality

PASS

Best-of-knowledge pass for the universal one-edge variance reversal and explicit high-mean certificate. Size bias, the independent-bond interpretation, and mean monotonicity are standard ingredients, not standalone novelty claims. The closest inspected comparisons do not have the one-edge edit and resulting uniform bound.

## value

PASS

The statement resolves a natural question that mean monotonicity does not answer: the same single graph edit has opposite signs on unconditional variance at the two ends of a common bond parameter. The original-graph mean alone gives a usable simultaneous sufficient test for all nonedges, without comparing their entire distributions. The variance theorem, not the elementary mean observation or tiny example alone, is the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
