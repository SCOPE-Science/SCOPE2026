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

Condition on the independent Poisson history in the backward Brownian integral. It gives stationary variance 2D/[r(1−a²)], and common noise contracts any two initial states by a raised to the jump count, proving uniqueness even without assuming a second moment for competing invariant laws. The stationary construction is an ergodic function of the driving increments. The conditional mean has decay rate λ=r(1−a), so the two-sided transform of the stationary covariance gives exactly the stated PSD. Maximizing its denominator F, the identity F(a)−F(1)=(1−a)[r²(1−a²)−ω²] rules out competing interior maxima for z>1 and singles out a=0 as the only admissible equality for z=1; compactness gives convergence to 1 for every high-frequency infimizing sequence. For z<1, the smaller derivative root is the only interior local maximum (at z=0 the larger root is the endpoint); at the smaller root the excess over F(1) is −2r²a(1−a)²>0. Substitution recovers the optimal value, and differentiation on the two branches gives the two stated one-sided slopes. The covariance integral gives the long-run variance rate. The compensated martingale has bracket per unit time tending to 2D+r(1−a)²E[X₀²]=4D/(1+a); a finite fourth moment follows from the geometrically weighted backward exponential intervals and bounds the normalized large-jump contribution by O(T⁻¹) in expectation. The endpoint difference divided by √T vanishes in L², giving the stated CLT and zero-frequency comparison. The supplied checker was inspected, not executed; these are analytic verifications.

## originality

PASS

The frozen finding's full signed frequency-design classification has distinct content: the branch competition with a forbidden stationary endpoint, exact nonzero-frequency transition and cusp are not supplied by the inspected model, covariance or finite-window papers. The covariance and the temporal-mean asymptotic optimizer/value are already covered in part of the inspected evidence and are not credited as standalone new results. This does not establish historical priority.

## value

PASS

For a natural noise-design objective this gives a complete attained/nonattained transition rather than only an improved local candidate. It shows that a physical reversal helps at low monitored frequencies, whereas arbitrarily weak resetting is limiting-optimal at high frequencies but cannot realize the bound as a stationary process. The cusp and exact crossover separate qualitatively different design regimes; no claim of broad-band or rate-and-multiplier optimality is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
