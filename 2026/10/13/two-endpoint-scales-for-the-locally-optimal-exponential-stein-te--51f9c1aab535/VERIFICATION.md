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

With a=e^(λ(u−1)), the differential of the fitted mean product gives ψ(X)=(X−λu)u^X−ua(X−λ). For H=(X−λu)u^X, the Poisson generating function gives E H=0, E[XH]=λua and E[H²]=λu²(1+λ(1−u)²)e^(λ(u²−1)). Subtracting the projection on X gives the stated strictly positive variance on 0<u<1. For the mean-preserving ZIP mixture the exact residual is λuω[e^(λ(u−1)/(1−ω))−1]; a triangular-array CLT with uniformly bounded moments near ω=0, the fitted-mean differential and Slutsky give the negative Gaussian shift. Contiguity also holds: if r_μ is the Poi(μ)/Poi(λ) likelihood ratio then E_λ[(r_μ−1)²]=expm1((μ−λ)²/λ); the structural-zero ratio has finite squared moment, so the mixture has one-observation χ² distance O(ω²), and the product likelihood ratios have bounded second moments for ω=h/√n. The reverse bound follows from the mixture ratio being bounded below by (1−ω)e^(−(μ−λ)) near zero. The statistic's exceptional zero-denominator event vanishes. For the optimization I checked the sign factor G: it equals λ²t³+O_λ(t⁴) near t=0, and G(1)=(1+λ)e^(−λ)−1<0. The uniform small-mean expansion follows by extending the two analytic quotients (e^x−1)/x and [(1+y)e^y−1]/(2y) at zero, giving first correction t−3t²/4 and optimum 2/3. For large λ, the bounds on [0,1/3] and [1/3,1−δ] are o(e^λ) whereas F(1)∼e^λ, so every maximizing t tends to 1. At an interior stationary point the exact equation gives λt²(1−t)=2t−1+o(1), hence λ(1−t)→1. In F the exponential is e^(λ−λ(1−t)²), and the prefactor is asymptotic to 1 at such t. These steps give both maximal values and do not suppose uniqueness.

## originality

PASS

The supported distinction is the rigorous optimization theorem for the specified local experiment, especially the two endpoint scales and optimal values. The fitted exponential Stein statistic, delta-method machinery and weight tuning are prior; the ZIP noncentrality formula is a model-specific substitution and simplification, not a separate novelty basis. No known matching endpoint theorem was established by the inspected statements. The primary article most likely to contain one could not be independently read in full; the decision is not a whole-paper noncoverage claim.

## value

PASS

Weight tuning for an existing goodness-of-fit test is a natural optimization problem. The two limiting choices—a nonzero constant at very small means and inverse mean at very large means—give mathematically and practically different prescriptions and quantify the maximum achievable local noncentrality within the test family. The first-order tie breaking and large-mean stationary balance are the contribution, not reuse of the statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
