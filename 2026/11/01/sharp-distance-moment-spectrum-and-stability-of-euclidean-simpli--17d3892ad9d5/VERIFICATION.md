---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For each full-dimensional Euclidean d-simplex d>=3 (n=d+1), independent uniform barycentric Dirichlet(1,...,1) samples yield E||X-Y||²=2S/[n(n+1)] and an exact fourth moment in Gram invariants S=tr G, T=tr G², H=sum G_ii². Subtracting its regular value gives the positive defect K-kappa=A||G-(S/(n-1))J||_F²/S²+B sum_i(G_ii-S/n)²/S², A=2(n²+3n+3)/((n+2)(n+3)), B=3n(n+1)/((n+2)(n+3)); this forces the unique regular-simplex minimum kappa=n(n+1)(n+6)/((n-1)(n+2)(n+3)). The nonstandard centered quartic inequality sum a_i^4 <= ((n²-3n+3)/(n(n-1)))(sum a_i²)^2 follows via Lagrange stationarity, ruling out three root values by constrained second variation, then optimizing two-level multiplicities. Along with T<=S², it identifies the unique rank-one spike upper-limit U=6n³/((n-1)(n+2)(n+3)); rank n-1 excludes upper attainment. Regular-to-spike positive definite Gram interpolation realizes all [kappa,U). Edge quadratic forms bound shape deviation with optimal 1/2 exponent from trace-zero perturbations. Independently checked Dirichlet/Gram defect interpolation exact fractions n=4..11 and all two-level multiplicities; finite checks are not proof.

## originality

PASS

Best-of-knowledge after comparing the exact claimed quantifiers and mathematical implication with original papers, full relevant primary sections, and semantic published-finding searches. Positive evidence of independent coverage was not found; negative searches do not establish priority. Simplex Dirichlet-moment formulas are established prior; only their sharp Euclidean pair-chord shape spectrum/stability are assessed as new. Implicit equivalent extremal matrix quartic inequality or older stochastic geometry results could be overlooked.

## value

PASS

The exact full range, both sharp extremal shape classifications, quantitative nonnegative Gram-defect identity and sharp square-root edge rigidity solve a natural geometric-probability shape functional rather than computing isolated simplex moments. The Euclidean metric makes the statistic genuinely shape dependent, unlike a difference-body gauge invariant; each exact endpoint is useful in stochastic geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
