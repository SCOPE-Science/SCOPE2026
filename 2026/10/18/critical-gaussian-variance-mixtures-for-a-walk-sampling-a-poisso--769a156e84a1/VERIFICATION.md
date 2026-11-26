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

Conditioning on the independent observer fixes a trace of observation sites. In the compensated Poisson trajectory integral the variance is λ times n plus twice the sum of transition kernels over increasing time pairs. The third moment of one trajectory's trace summed over starting sites is bounded by 6n times the square of the sum of the kernel suprema over gaps, at most 96n². Taylor expanding the centered characteristic exponent at scale n^−3/4 then gives a uniform O(n^−1/4) error. The observer FCLT has unit diffusion and drift κ. At macroscopic gaps its increments always satisfy the particle kernel's parity, producing lattice span two in the local limit; together with the two time orders this gives 4λ/√(2π). Gaps shorter than εn give O(√ε) after scaling, so the Riemann sums converge jointly with the observer and have a bounded limit. Conditional characteristic functions tested against bounded continuous path functions identify the claimed joint mixture. For the polynomial, shared Poisson occupation gives the Charlier covariance δ_(ℓ,m)ℓ!(λQ)^ℓ. Uniformly even before averaging over observers, Q^ℓ=O(k^−ℓ/2), so all ranks ℓ≥2 have total variance O(n log n) and are negligible. Gaussian averaging over an increment gives e^(−κ²u/4)/√2, yielding the stated variance, including 8λc₁²/(3√π) at zero. Full support of B_κ and continuity distinguish neighborhoods of the zero path from steep linear paths, so the mixing variance is not constant and the fourth moment exceeds the Gaussian fourth moment.

## originality

PASS

Pass is for the joint path and statistic critical-window limit, its non-Gaussianity for every finite drift parameter, and the explicit variance crossover. The symmetric n^(3/2) variance and its zero-drift constant are known and excluded from novelty. The closest same-model primary source leaves the non-Gaussian question open in the passages inspected.

## value

PASS

This resolves a specific open distributional question for symmetric sampling while separating the path-conditioned Gaussian law from the annealed non-Gaussian one. The finite scaled-drift family and explicit second moment describe how the statistic changes in the critical regime, not merely that its variance grows faster than n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
