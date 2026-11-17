---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For the unit-rate nearest-neighbor generator on infinite Z^d, d≥2 and all t>0, P_{d,t}(x)=e^{-2dt}∏_j I_|x_j|(2t) and q=PΣ_j s_|x_j|. The identity r_m′(z)=1−r_m(z)^2−(2m+1)r_m(z)/z and its first-zero derivative argument give r_m′>0; hence s_m strictly increases with |m| and the smallest off-origin score occurs only at the 2d neighbors. The Fourier identity P′_{d,t}(e1)=∫λ(λ/(2d)−1)e^{−λt}dρ splits positive λ>2d from negative λ<2d: the positive/negative Laplace-transform ratio is strictly decreasing from >1 to 0, proving a unique crossing. The origin remains strictly negative; before/at the crossing all other sites are positive/zero at neighbors. The zero-mass kernel then has total variation −2q(0)=4d e^{−2dt}I0(2t)^{d−1}(I0−I1), the exact ℓ1 and ℓ∞ convolution norms; immediately and permanently afterward negative neighbors make it strictly larger. Since s0<0 the crossing decreases in d. The correct small-t ratio R=t−t^3/2+t^5/3+O(t^7), with the root derivative of order −4d², gives τ_d=1/(2d)+1/(4d²)+1/(8d³)+O(d^−4). No unproved infinite inference is made from finite diagnostics.

## originality

PASS

Best-of-knowledge original as a combined d>=2 theorem: the existing Bessel kernel identity, ratio estimates, and one-dimensional derivative bounds supply ingredients but not the unique first off-origin derivative sign crossing, the exact maximal endpoint-operator-norm interval, dimensional ordering, and the three-term threshold scaling. A separate, genuinely relevant manifold spatial-monotonicity theorem concerns a different quantifier and geometry. Residual priority risks are explicit.

## value

PASS

The first instant at which discrete heat flux reverses sign outside the source is an intrinsically motivated crossover in a canonical infinite graph semigroup. Its location governs the maximal interval of an exact endpoint ℓ1/ℓ∞ operator norm equality, not merely a numerical special-function root. A uniform all-dimensional uniqueness, strict dimension monotonicity and controlled high-dimensional asymptotics would be useful for sharp endpoint semigroup estimates and comparative lattice heat flow. Neither the 1D kernel identity nor elementary normalization by itself gives this exact boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
