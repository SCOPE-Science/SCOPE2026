---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the infinite 1D rate-half Glauber chain reset globally to all plus, γ∈(0,1), fixed separation n, the no-reset two-point hierarchy C_n_prime=−2C_n+γ(C_{n−1}+C_{n+1}) with C_0=1 and C_n(0)=1 gives W_n=−C_n_prime solving the killed discrete heat equation with W_n(0)=a=2(1−γ). The reflected Bessel heat kernel sums exactly to S_n(t)=e^(−2t)[I_0(2γt)+2Σ_(j=1)^(n−1)I_j(2γt)+I_n(2γt)]>0. Thus C_n(t)=q^n+a∫_t∞S_n. For t→∞ at fixed n, S_n~(n/√(πγ))t^(−1/2)e^(−at), and same leading factor for C_n−q^n after multiplying by a and integrating. At stationary exponential reset age A~Exp(r), the strictly monotone pushforward yields the exact density and CDF tail: for y↓0, F(q^n+y)~c_n^(−θ)a^(−θ/2)y^θ(log1/y)^(θ/2), density~θ times that over y with θ=r/a. It diverges including √log at r=a and vanishes r>a. Zero-coupling γ=0 is separately exact without log. The stationary spatial mean solves an inhomogeneous second-order difference equation and yields b+(1−b)ξ^n and the positive connected infinite-separation residual. Independent Bessel-kernel evaluations, late-time asymptotics and quadrature of mean agree within bounded numerical error. The variable U_n is a thermodynamic spatial average conditioned on a shared reset age, NOT an instantaneous ±1 bond product; no uniform n→∞ and y↓0 claim.

## originality

PASS

Magoni–Majumdar–Schehr 2020 provides the same global reset Glauber model, exact magnetization distribution and threshold r*=1−γ. Its complete inspected paper explicitly identifies distribution of pair correlations as a future question. The two-point hierarchy has a different relaxation exponent 2(1−γ), yielding doubled critical reset rate and a Bessel t^(−1/2) logarithmic correction absent from the magnetization distribution. The 2024 Chen–Zhong resetting paper treats 2D Metropolis critical dynamics; neither paper directly proves the target 1D spatial-average pushforward law. Novelty remains best-of-knowledge with possible implicit older renewal/Bessel treatments.

## value

PASS

This exact stochastic-process law resolves a natural observable proposed by the model's own initiating paper. It quantitatively distinguishes magnetization and spatial correlation reset thresholds, identifies a critical sqrt(log) singularity, and gives a spatial profile/long-range connected limit caused by shared reset age. The effect is mathematically motivated, not merely an isolated special-function substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
