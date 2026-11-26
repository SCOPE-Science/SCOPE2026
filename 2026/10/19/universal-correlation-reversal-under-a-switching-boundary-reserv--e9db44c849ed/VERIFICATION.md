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

The bath marginal is exactly 1/2; the right drift ζ−η_N is linear, so the discrete Dirichlet problem yields the stated mean without independence. At κ>0 the chain can empty with the right bath held open for removals and can build any target configuration from empty by left injections and exchanges, filling the desired rightmost sites first. For a fixed bath, substitution of the bilinear covariance into the neighboring-pair equation gives the squared mean gradient, with zero covariance on virtual boundaries and the nonadjacent harmonic equation satisfied. The killed two-site walk reaches a boundary, proving uniqueness. As κ↓0 the stationary equations leave two sector invariant laws with fixed weights 1/2; the full-bath sector has only the full stationary configuration. The covariance mixture adds i j/[4(N+1)²], and its numerator bracket is at least 2. As κ→∞ the stationary equations divided by κ force sector equality for every configuration; summing the unscaled equations identifies the averaged bath at density 1/2. The covariance there is strictly negative for i<j. The finite irreducible stationary solution depends continuously on κ, so a crossover exists for each pair. For N=2, multiplying site drifts by ζ and adding κ(m_i−2E[ζη_i]) gives the stated mixed-moment equations; the product drift is m_2+E[ζη_1]−2E[η_1η_2]. Solving yields the stated rational covariance and its decreasing quadratic numerator has exactly one positive root √10/2−1. This reconstruction is analytic; the original finite script was inspected but not executed.

## originality

PASS

The classical fixed-bath covariance is already covered. The distinct claim is the finite-chain all-pair reversal from the combination of positive environmental mixture covariance and negative averaged-process covariance, and the exact N=2 switching threshold. Neither a single static law nor the inspected differently switched or reset models covers it.

## value

PASS

The same stationary means coexist with strictly opposite connected-correlation signs at the two ends of the bath rate, for every pair in every finite chain. The calculation identifies a distinct common-noise mechanism competing with the exclusion anticorrelation and gives an exact two-site benchmark, not just a statement that mixtures may create positive correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
