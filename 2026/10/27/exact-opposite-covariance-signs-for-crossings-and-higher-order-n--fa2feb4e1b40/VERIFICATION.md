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

In the uniform ranked-endpoint model each matching has 2^n n! labeled realizations. A specified r-set has either exact pattern with probability p_r=1/(2r−1)!!. Conditional on the internal ranks, one outside arc crosses a rank-gap-d inside arc with probability d(2r+1−d)/binom(2r+2,2), by counting placements of its two endpoints among the 2r+1 gaps. Complete crossings have d=r. Nestings average this expression over d=1,3,…,2r−1 because label ranks are exchangeable; the sum of d(2r+1−d) is r(r+1)(2r+1)/3, giving exactly 1/3. Disjoint candidate pairs are independent. The r(n−r) pairs sharing one arc hence give covariance p_r(r−1)/(3(2r+1)) each for crossings and zero for nestings. The binom(r,2) contained pairs are forced to cross or not, giving 2p_r/3 and −p_r/3, respectively. Multiplying by binom(n,r) and simplifying yields both stated formulas, including n=r and the signs. This checks the repaired proof as well as its unchanged formulas.

## originality

PASS

The distinct earlier edge–triangle record exactly covers the r=3 crossing covariance and is credited in the repaired statement. The tested precedents do not provide the all-r nesting covariance, its one-shared-arc cancellation, or the paired signs for counts of r-arc subsets. These are the supported distinctions, not a priority claim for the r=3 crossing identity or the pattern definitions.

## value

PASS

Crossings and completely nested patterns have equal expectations of each order in a natural matching model, but behave differently as joint statistics with the basic pair crossing count. The exact signed contrast and cancellation identify which overlaps affect joint fluctuations, with a formula usable for all sizes and nesting orders. The value is not the recomputation of the earlier triangle covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
