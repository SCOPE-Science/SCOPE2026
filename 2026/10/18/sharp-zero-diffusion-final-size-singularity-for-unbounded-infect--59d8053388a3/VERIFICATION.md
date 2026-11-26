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

For prescribed continuous s, the transform with A′=ks satisfies the transport equation and initial condition. Dividing by the mass gives the exponential tilt of the initial probability convolved with a Gaussian of variance Dt and mean DJ, where J=∫₀ᵗ(A(t)−A(u))du; at D=0 the Gaussian factor is a point mass. This constructs a positive finite-time solution even for atomic data and justifies differentiation without assuming moment decay first. Append A′=ks and J′=kts to the compartment ODEs with m=K₀′(A)+DJ. The locally Lipschitz system preserves positive s and i by their exponential forms; A,J are nonnegative, so m≥0, and mass conservation and the bound J≤ks₀t²/2 give extension on every finite interval. This also gives finite-time continuity in D at zero. The exact derivative m′=ks(K₀″(A)+Dt) is nonnegative. The time integral of i is finite; monotonicity of s and r gives a limit for i, necessarily zero. For D>0 any positive s∞ forces quadratic growth in m and eventually a uniformly positive logarithmic growth of bounded i, a contradiction. With s∞=0, bounded m contradicts the susceptible exponential and integrability of i. At D=0, or under conservative bounded-support dynamics, m is bounded by the corresponding support cap and the survivor lower bound follows directly.

## originality

PASS

Credit existing coverage of the qualitative discontinuity in a reflecting half-line problem and of the bounded-support comparison. The distinct contribution supported here is the theorem for the full-line Cauchy problem with compactly supported initial measures, including atoms, using the exact cumulant identities to control the sign and divergence of its conditional mean. Neither the reflecting model nor the related reduced social-diffusion model supplies that conclusion for this Cauchy problem.

## value

PASS

The full-line interpretation of the bare diffusion operator permits negative values, making monotonicity and the final-size contrast nontrivial even given the reflecting result. The exact transform explains why the sign of the mean is nevertheless controlled and why this specific unbounded approximation fails at the terminal limit even with atomic initial data. The mathematical value is identifying the consequence of the domain assumption, not extrapolating it to actual transmission.

The dated certificate retains the supplied scientific assessment, sources and limitations.
