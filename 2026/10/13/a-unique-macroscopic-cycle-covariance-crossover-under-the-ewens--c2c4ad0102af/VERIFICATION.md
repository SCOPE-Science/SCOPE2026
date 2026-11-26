---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Marking a j-cycle gives its mean times 1+h_(n−j) for the mixed moment; subtracting the total-cycle mean gives the stated factor δ. The factors are strictly decreasing in j; deleting nonnegative terms lowers the tail, with any flat step already negative, and the remaining negative tail cannot cross back. The variance at cutoff 0 is positive since the Ewens law gives positive mass to permutations with different total counts, and the n−1 cutoff is strictly negative even for n=2. The gamma and harmonic ratios converge uniformly on interior compact intervals. Near j=n, writing s=n−j+1 and grouping dyadically gives O(ε^θ(1+|log ε|)) limsup from the bound n^(−θ)s^(θ−1)(1+log(n/s)), including θ<1. The limiting integrand changes sign at 1−e^(−1/θ), is integrable at 1, and has a positive θ/x singularity at zero. The single integrated root and two-sided cutoff convergence follow. At small θ, differentiating the integration-by-parts expression gives Q/θ→log((1−t)/t); at large θ, u=θx gives E1(c)−e^(−c), dominated on u≤θ/2 by e^(−u/2)(1+2u)/u and with O(2^(−θ)) tail from y=1−u/θ. Two-sided sign tests then prove both parameter limits. Independent exact enumeration corroborated 60 marked moments and 60 cutoff cases; independent root calculations agreed with both numerical constants to the stated digits.

## originality

PASS

Best-of-knowledge pass for the aggregate-tail sign classification, limit root and parameter endpoint laws. The marking identity and limit intensity use standard Ewens theory; their provenance is not the novelty claim. Near matches either change the conditioning, change the observable, or supply moments without analyzing the aggregate threshold.

## value

PASS

The natural statistic compares total cycle count with the number of cycles above a cutoff. Its nonmonotone covariance could permit multiple crossings; the theorem rules them out for every finite n and θ, then locates the macroscopic transition and distinguishes its dilute and high-θ regimes. These are reusable sign and scale statements beyond recomputing a known moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
