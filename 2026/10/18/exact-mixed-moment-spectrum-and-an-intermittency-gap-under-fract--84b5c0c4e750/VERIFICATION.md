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

The variance assumption d₁>0 implies gamma+rp log(a)<0 since 1-a²<-2 log(a). The marginal Poisson strong law makes each backward propagator decay exponentially, providing a stationary stochastic integral; solutions coupled to the same future noise and marks contract, giving uniqueness. Given the whole mark history, the independent Brownian noises give independent centered Gaussians with variance V_i=2D∫₀^∞ exp(2 gamma t)a^{2N_i(t)}dt. Tonelli and the k! time orderings yield a product of k positive integrals over successive durations, with Laplace exponent d_j for j distinct active coordinates and b_j for j copies of one coordinate. Each duration contributes the reciprocal of its exponent if positive and infinity otherwise, including equality. The marginal Gaussian even-moment factor is (2k−1)!!. Exchangeability gives F_{j+1}−F_j=(1-a²)E[I_{j+1}a^{2H_j}], whose next difference is no larger by swapping selectors and including the extra multiplier. Hence F_j/j is nonincreasing; the same holds for p(1-a^{2j})/j. This reduces each test to its last denominator. For k≥2 a proper batch has positive probability of partially meeting the k tags, so strict convexity of a^{2h} below its endpoint chord gives F_k>p(1-a^{2k}). Concavity places the mixed threshold at or below the variance threshold, and full batches give equality with the scalar threshold. Expanding (1-s)^{2H_j} uses E H_j=jp and E H_j(H_j−1)=j(j−1)pu; d_j=λjs[2κ−1−2(j−1)u]+O(s²). Taking the product gives the limit and the sign of d_k proves off-boundary divergence. The scalar expansion analogously gives κ=k−1/2. Strict comparison of limiting boundaries concerns k≥2 as in the preceding separation statement; for k=1 they coincide.

## originality

PASS

Scalar moment products and moment loss are substantially covered by standard exponential-functional machinery or overlapping scalar results; the one-particle law is not the distinct contribution. The supported claim is the exact proper-batch mixed spectrum together with its strict separation from scalar moments and the resulting near-critical scaling. Known complete-batch selection, synchronized fractional resets and general finite-time moment closure do not state those results under the same assumptions.

## value

PASS

Proper batches interpolate between independent marginal histories and complete synchrony. The result identifies exactly when a natural observable of collective fluctuations is integrable even though the corresponding scalar moment diverges, and quantifies the gap at every relevant order and in a near-critical weak-reset regime. This is a substantive distinction, not just a new way to write a scalar recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
