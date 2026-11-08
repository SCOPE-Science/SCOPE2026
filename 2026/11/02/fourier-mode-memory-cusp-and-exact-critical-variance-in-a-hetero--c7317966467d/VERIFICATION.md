---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Independent branch labels yield the stationary Markov kernel P with Pe_j=p e_{2j} for odd j, and Pe_j=q e_{j/2}+p e_{2j} for even j, p=1-2a,q=2a. Dyadic level-return paths from zero are Dyck paths, so lag 2m autocovariance is Cat_m(pq)^m/2 and odd lags zero; odd parts and sin/cos are invariant orthogonal sectors. Stationary covariance convolution gives Var(S_N)=N/2+sum(N-2m)Cat_m(pq)^m. Catalan generating function yields σ²=1/max(p,q)-1/2 with slopes ±8 at a=1/4, and singularity analysis at ±1 gives 3N/2-4 sqrt(2N/pi)+4+O(N^-1/2). For a>1/4, the bounded Poisson series g=(1/q) sum_h(p/q)^h φ(2^h y) supplies martingale CLT using stationary ergodicity, not extended to a≤1/4. Independently checked dyadic walk returns at 4 rational a parameters through lag 16 and critical variance asymptotic at N=1000 (error -0.0757).

## originality

PASS

The M=2 model, stationary mixing, walk comparison and critical decay exponent were published earlier; the parameter-uniform exact Fourier coefficients, cusp and critical square-root finite-time correction are not supplied by the inspected sections/theorems. Best-of-knowledge originality carries risk of another implicit exact harmonic specialization.

## value

PASS

Fourier harmonics are canonical smooth center observables, and the cusp parameter is the dynamically meaningful center-neutrality threshold. Exact temporal memory, the sharp parameter response and finite-time √N anomaly give natural quantitative statistics beyond prior rates/plots.

The dated certificate retains the supplied scientific assessment, sources and limitations.
