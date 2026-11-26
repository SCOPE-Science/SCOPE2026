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

Reconstructed the first-moment operator on ℓ²(Z^d): for λ>0 the resolvent of A_d exists, and any eigenvector is a multiple of (λ−A_d)^−1δ_0, giving β G_d(λ)=1, a one-dimensional eigenspace and no other positive eigenvalue by strict monotonicity. In the unit per-oriented-edge normalization p_t(0,0)=[exp(−2t)I_0(2t)]^d. With y=2dt and bounded u≥0 the small-y integrand multiplier is 1+y²/(4d)+(y⁴/32−uy/2)/d²; exponentiation of the log expansion on y≤d^(1/8) leaves a uniform O(d^−3) polynomial-weight remainder. Beyond that cutoff up to d, I_0(y/d)≤exp(y²/(4d²)) gives exp(−3y/4). Beyond d, k(z)=e^(−z)I_0(z) is decreasing by its angular integral, k(1)<1 and k(z)=O(z^−1/2) by the quadratic bound on 1−cos θ; thus the remaining integral is at most d k(1)^(d−3)∫_1^∞k³. Integrating the small-y coefficients gives 1/2, 3/4 and −u/2 at the stated orders. Reciprocal expansion gives β_c=2d−1−1/d+O(d^−2); β_dG_d(u/d)−1=(s+1−u)/(2d²)+O(d^−3). The strict sign test at zero and bracketing at s+1±ε give exactly the two stated cases. No decision is claimed at s=−1 or about a random population's trajectory. The supplied verification and numeric log were inspected, not rerun; the recorded finite numerical runs test only G_d(0), not a uniform bound or the spectral conclusion.

## originality

PASS

Pass for the supported high-dimensional Green-function accuracy at the band edge and its exact joint dimension/source critical window, not for the Bessel representation, elementary short-return coefficients or rank-one criterion. The exact known lattice generating function does not itself estimate its total many-step contribution near the band edge. However, an older correctly normalized expansion of the total return Green function to the same order would imply essentially the full window by a short calculation, not just its threshold. This is a material historical risk rather than verified coverage in the inspected sources.

## value

PASS

This identifies the natural source-intensity width d^−1 after the order-one shift, including its exact transition location and the resulting nonzero rescaled eigenvalue. The window distinguishes the existence of a positive first-moment growth mode from its absence in a canonically normalized model where fixed-d strong-intensity asymptotics do not apply. The value is the exact near-threshold benchmark, not the use of Bessel expansions or the rank-one criterion on their own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
