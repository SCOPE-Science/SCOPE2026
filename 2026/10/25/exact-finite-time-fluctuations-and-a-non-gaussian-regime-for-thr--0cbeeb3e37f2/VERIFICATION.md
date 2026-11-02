---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Rebuilt synchronous FTL recurrence at t>=1 with x(0)=s on graph 1-2-3, uniform independent center sampling, alpha in (0,1) and s1!=s3. For t>=1, the leaf difference is exactly alpha(s1-s3), whereas initial difference is s1-s3; multiplying by pi=(1/4,1/2,1/4) yields E1=c ξ0 and Et=(1-alpha/t)E(t-1)+(alpha*c/t)ξ(t-1) for t>=2, c=(1-alpha)(s1-s3)/4. Gamma product solution gives the exact finite Rademacher law, variance and product characteristic function. For alpha<1/2, coefficients b_j~j^(alpha-1) are square summable, proving almost sure and L2 convergence and strictly negative -2∑weights^4 fourth cumulant. For alpha=1/2 and >1/2, harmonic/power sums with maximal normalized coefficient→0 establish Lindeberg CLTs with respective c²/4 and alpha²c²/(2alpha-1) variances. Independently recomputed all center-choice histories to t=7 for three rational alpha and three leaf/center tuples, checking exact scalar impulse equalities; finite data only corroborate analytic limits. Boundary s1=s3 is excluded to avoid zero-noise degeneracy.

## originality

PASS

Best-of-knowledge originality of the exact network observable law and its cumulants, not of the general stochastic-approximation transition. The relevant primary full text supplies general FTL convergence rates rather than exact distributions; a matching specific scalar law was not found in bounded searches.

## value

PASS

On the smallest connected graph with a random choice of neighbor, an explicit all-time law and three limiting regimes for an actual network observable is a natural exact benchmark. The non-Gaussian limit is certified by a strictly negative fourth cumulant, and exact variance constants sharpen earlier qualitative convergence estimates. This is not merely observing the generic half-exponent stochastic approximation transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
