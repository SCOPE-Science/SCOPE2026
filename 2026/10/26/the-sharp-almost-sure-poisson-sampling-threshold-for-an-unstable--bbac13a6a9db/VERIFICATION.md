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

For each fixed gain the hold multiplier is M(h)=k/a+(1−k/a)e^(ah); any zero is simple and has probability zero at a sample, so log|M(H)| is integrable. The two strong laws give the exponent at sample times. The upper bound |M(h)|≤C exp(ah) and H_n/T_n→0 give the matching upper limsup at all times; zeros do not affect this upper bound, and no assertion uniform across gains on one probability-one event is needed. The exponent is positive for k<a and zero for k=a. For k>a, write p=λ/a and θ=1−a/k. Integration by parts in the beta integral, deleting a symmetric interval at y=θ whose boundary-log difference tends to zero, gives the simpler exact identity F_p(θ)=θ^p PV ∫_0^(1/θ) z^(p−1)/(1−z) dz. For 0<p<1 the whole integral to infinity pairs to ∫_0^1 (z^(p−1)−z^(−p))/(1−z) dz, positive below 1/2, zero at 1/2 and negative above. Truncation adds a positive tail correction. This proves strict positivity for 0<p≤1/2 and negativity for small θ for 1/2<p<1. For p=1 the integral is −log(1/θ−1), and for p>1 its eventually negative tail grows in magnitude like (1/θ)^(p−1)/(p−1), confirming the stated small-θ expansion. For the mean-square comparison, when λ≤2a the no-sample event alone gives a nondecaying lower bound at every k≠a; k=a is constant. When λ>2a the proposed minimizer gives E[M(H)^2]<1, and a small exponential weight preserves the mass <1 of the nonnegative first-hold renewal kernel λe^(−λs)M(s)^2; the weighted no-sample term is bounded, giving decay at deterministic times. Independent quadrature of the pole-subtracted integral agrees with the signs and critical closed form at the replay points in /workspace/replays/recheck_frozen.py, poisson(); the proof, not quadrature, resolves all parameters.

## originality

PASS

The supported distinct claim is the sharp fixed-gain Poisson frontier λ>a/2 for pathwise exponential stability, not a new general logarithmic-product principle or the λ>2a mean-square frontier. The closest inspected same-model result is about second moments; no exact or implying coverage of the pathwise frontier was established. This is a best-of-knowledge decision with a material access risk from Beutler (1972).

## value

PASS

The sharp rate answers a natural stability-design question for an existing scalar benchmark. It distinguishes the entire continuous-time path from observations at the sample times, and exhibits a full range where fixed gain is effective almost surely but no fixed gain works in mean square. The strict obstruction at the endpoint, with unchanged state only at k=a, is substantive and cannot be obtained from the existing second-moment frontier alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
