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

The Brownian position at the independent exponential time has the stated symmetric Laplace law: its characteristic function is r/(r+Dk²). Summing the two snapped-jump tails gives the signed mean step in frozen Eq. at lines 43–45. The mean duration of an independent cycle is r⁻¹+τ; dependence between its own reward and duration is allowed. For control of the unfinished cycle, let K(t) be the first cycle index at which cumulative duration exceeds t. Its count is at most one plus the Poisson count using the same exponential durations with all delays omitted. An envelope for the displacement within a cycle is the maximum Brownian displacement up to its exponential capture plus L, and has finite second moment. The envelope of cycle K(t) is o(t) almost surely by the integrable iid envelope tail bound and K(t)=O(t) almost surely. In expectation its magnitude is O(√(1+t)): the square of this envelope is bounded by the sum of squared envelopes up to K(t), and inclusion of cycle i in that sum depends only on preceding cycles. The same predictable sum argument for cycle rewards, with the last reward subtracted, gives the mean limit since K(t)/t converges in mean by the Poisson bound and the renewal law. Strict convexity of sinh gives G_y<0; opposite endpoint signs give the sole global maximizer, and G_η<0, G_δ>0 give the stated strict optimization shifts. For fixed δ the large-delay root tends to 0 and the hyperbolic difference is (1−δ²)y/3+O(y³), so η y_*⁴ tends to 6/(1−δ²); the prefactors of r_* and the maximum speed follow by substitution. For fixed η and δ↑1 the root must diverge. At that root the difference coth y−δ coth(δy), divided by 1−δ, tends to one by the mean-value theorem applied to b coth(by), since its derivative tends uniformly to one for b between δ and 1 there. Therefore the stationary balance gives the two claimed exponents and constants without exchanging limits at a fixed rate. At δ=0 the speed vanishes; at δ=1 the positive speed is increasing in y, with no interior optimum.

## originality

PASS

The instantaneous-capture drift without latency is explicitly covered by Roberts–Sezik–Lardet, and the fixed-latency speed correction is already given by Ghosh et al. Combining these antecedents supplies the objective, so that objective and the renewal overhead factor are not credited as new. The supported distinct part is its all-parameter rate optimization: strict uniqueness and comparative statics, the large-delay scale, and the two different divergences at nearly perfect asymmetry. The strongest inspected exact-current and refractory comparisons do not give those results as stated theorems or direct specializations. This judgment is limited to the inspected sources.

## value

PASS

The optimization is a natural design question for a well-established ideal local-reset ratchet. Knowing the exact current alone does not tell an experimenter whether increasing the reset rate helps or where its optimum moves. The theorem gives unambiguous parameter ordering and shows that any fixed positive dead time changes the near-singular optimal-rate exponent, an effect not captured by the no-delay optimum. This is a parameter-wide structural result, not merely a numerical reoptimization of a known curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
