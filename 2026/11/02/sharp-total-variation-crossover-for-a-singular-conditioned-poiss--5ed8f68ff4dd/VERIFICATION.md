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

Reconstructed the conditional product-Poisson mass and the exact tilt Q/B∝h_n, with h_n the squared falling-factorial correction, zero above n. The Legendre change of variable sends its n roots in (−1,1) to negative roots of the mass polynomial; factoring gives a Bernoulli sum with variance at most its mean, itself at most the Bessel mean <μ=√z by the decreasing tilt. Shifting the mass recurrence proves E_Q K²=(μ/n)² E_Q(n−K)². Expanding its quadratic about k0=nμ/(n+μ) gives 2μd=(1−μ²/n²)(d²+Var_Q), with d=k0−E_Q K≥0 by Jensen and d≤μ; hence d≤1. For B, the Bessel mgf with t=v√(2/μ) gives the standard normal mgf limit and uniform exponential moments for the centered/scaled K. Alternatively E_B K²=μ² by the mass ratio and the classical I1/I0 expansion gives E_B K=μ−1/4+O(μ⁻¹). On every fixed centered window the log h_n ratio equals −δ_n S_n+o(1), δ_n=√2 μ^(3/2)/n; the global majorant exp(C μ(|k−μ|+1)/n) follows by summing increments below floor(μ), with ratio ≤1 above. Thus, for finite c, the unnormalized ratios converge in distribution with a uniform p>1 moment bound, so both normalization and the expectation defining TV converge; this is the precise content of the source's asymptotic L1 wording. The Gaussian likelihood crosses 1 at −δ/2, giving 2Φ(δ/2)−1, including δ=0. For μ^(3/2)/n→∞ and μ=o(n), the mean gap μ²/(n+μ)+O(1) dominates √μ, yielding TV→1 by Chebyshev at the midpoint. Inspected the supplied checker/output without running it. A separate bounded recurrence check (normalizing consecutive-mass ratios around the modes, geometric tail estimate starting at μ+40√μ+100) gave TV 0.02488222, 0.51704034 and ≈1 at n=262144 for μ=n^(1/2), n^(2/3), n^(4/5), respectively; it corroborates but does not prove the limits.

## originality

PASS

The distinct claim is the growing-parameter breakdown scale and exact crossover in total variation, including separation within the vanishing-odds regime. The Fisher mass, fixed-parameter Bessel limit and classical Bessel normal approximation are not themselves originality claims.

## value

PASS

The equal-margin 2×2 array is a canonical rare-cell model. The result gives a sharp criterion for using a Bessel approximation in TV as the rare-cell count itself grows. It explains why support separation becomes essentially complete well before z becomes comparable to n², and the Gaussian profile quantifies an approximation error that a fixed-parameter theorem or ordinary CLT does not resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
