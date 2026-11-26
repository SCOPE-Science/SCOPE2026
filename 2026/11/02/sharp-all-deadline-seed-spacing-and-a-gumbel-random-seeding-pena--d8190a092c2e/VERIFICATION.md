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

While a nonempty gap persists, its susceptible interval has two distinct active boundary edges even for a one-vertex remainder or a single initial seed on a simple cycle. Memorylessness makes the successive waits Exp(2λ); disjoint edge sets give independent clearances conditional on the seed set. This yields the product of Gamma CDFs, with shape zero a point mass (including all vertices seeded and t=0). For z>0 the Poisson tail-to-mass ratio strictly decreases in the threshold, by termwise comparison of its factorial series. Hence Q_(m+1)/Q_m decreases strictly; a one-unit transfer between gaps differing by at least two strictly raises the product. Such transfers decrease the sum of squared gap sizes until every gap differs from any other by at most one. These balanced multisets have the same CDF and are realizable. Marking a uniformly chosen seed gives exactly N rooted realizations per ordered weak composition, so the uniform composition law and the exact inclusion–exclusion coefficient are valid without gap independence. For m=floor(d(log k+x))+1 and fixed j, the logarithm of the binomial ratio in the jth factorial moment is −j(log k+x)+O_j((log k)/d+(log k)^2/k+1/d). In particular the finite-population correction to the linear term is o(1); the source's informal linear-term wording means an additive o(1), not convergence to a fixed constant. The alternating Bonferroni bounds for no exceedance then converge to the Gumbel CDF. Conditional on max gap ≤2d log k, unit-exponential Chernoff tails at εd are bounded by 2 exp(−c_ε d/log k) per gap, since their shapes are at most 2d log k. A union bound is o(1) under the stated d/(log k)^2→∞; thus passage from gaps to scaled flooding time is valid at the Gumbel fluctuation scale. Balanced gaps are d+O(1) and the same bound gives concentration. After dividing the random time by d log k in rate-2λ units and the balanced time by d in the same units, both limits are 1, which proves the ratio under any coupling. These are analytic checks, not extrapolations from finite experiments.

## originality

PASS

The reviewed distinct claim is the exact finite completion law and strict all-deadline placement theorem for multiple simultaneous seeds on the simple cycle, together with the comparison to a uniform discrete seed set. The continuous maximum-spacing Gumbel law is established prior work and is not credited as a novelty. The closest catalogue balance theorem with the same graph and clock model optimizes first detection, not last clearance.

## value

PASS

A strict placement theorem that simultaneously optimizes every deadline is stronger than optimizing a mean or a selected quantile. The exact law also links two natural benchmarks, balanced and uniform random placement, and quantifies their logarithmic separation rather than treating ordinary fluctuations and initial spacing as the same effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
