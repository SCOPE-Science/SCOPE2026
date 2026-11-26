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

For fixed 0<e<1, the Kepler map is invertible, f is strictly decreasing on (0,π) and increasing on the other half, and changing integration variable to E gives the time mean (1-e²)^(-1/2). The normalized periodic exponential kernel averages strictly between the extrema of f. For q=y−f, the integrating-factor derivative has the sign of −f′; together with q(0)<0<q(π), this proves exactly one maximum and one minimum. At the maximum y=f and y is strictly above its own mean, which equals the mean of f. Hence the maximum precedes the descending mean crossing, given by the stated E_e and M_e, with 0<M_e<E_e<π/2. The resolvent identity rewrites the slower response as a strict convex mixture of the faster response and its positive smoothing. At the faster response's maximum that smoothing is strictly smaller, so the slower response is still rising there and peaks later. Transversality gives continuity; the approximate-identity and uniform-mean limits give the two endpoint phases (for the latter use f(m)=y(m), not the argmax of the constant limiting output). Expanding the kernel near each limit gives the optional rates: at small θ use y′=f′−θf″+O_e(θ²); at large θ use the mean-zero primitive of f−μ, with dν/dM=√(1−e²)f. An independent direct periodic-kernel quadrature/root check at e=1/2, θ=1 gave 0.433404826272 rad versus ceiling 0.936395659985 rad, with peak-equation residual below 5×10^−16. That check is finite. The supplied bisection/FFT test was inspected, not executed; see RESULT.md lines 29–65 and verify_thermal_peak.py lines 6–50.

## originality

PASS

The inspected antecedents establish delayed heating/temperature responses in physical models and classical exponential smoothing, not the strict monotone bijection and sharp eccentricity-dependent maximum-phase ceiling for this scalar filter. The strongest located indexed neighbor changes both the filter and the independent variable being compared. This is a bounded, best-of-knowledge assessment, not a priority certification.

## value

PASS

For a natural Kepler inverse-square input, the theorem gives a global identifiability criterion for the idealized time constant and an exact infeasibility boundary for peak lags. It gives substantially more than the single-harmonic quarter-period intuition; e.g. e=1/2 has ceiling about 0.14903 of a period. The conclusions refer to a single constant-coefficient linear proxy, not atmospheric or light-curve inversion in general; as θ grows the response becomes flat and the inverse problem is ill-conditioned.

The dated certificate retains the supplied scientific assessment, sources and limitations.
