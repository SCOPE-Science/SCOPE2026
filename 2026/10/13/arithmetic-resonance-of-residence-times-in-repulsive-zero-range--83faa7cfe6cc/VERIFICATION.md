---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

From actual site rates verify local detailed balance x_k=z exp(kh), λ=z exp(h/2), and the reversible product occupation weights; Little’s stationary Palm entrance identity gives λT=sum_k ρ_k. Completing the square yields exact unconstrained integer Gaussian mean t_k+ψ_u(t_k), with a summable O((1+t_k)e^{-b t_k²}) one-sided truncation tail, so constant+o(1) follows. Periodic rational rotations give R_q and bounded periodic deviation; irrational equidistribution gives o(L), Diophantine small-divisor bound plus analytic Fourier exponential coefficients gives uniform O(1), and q-grid Fourier selection gives exp(-σq). Independent direct numerical lattice sums at u=8,c=1/4 show q=1 coefficient -0.13322511983779, q=3 +0.00095804041357, q=2 zero, and irrational √2 Cesàro residual approx 1.4e-5 at L=4000. Only exact stated fixed-reservoir tagged-entrant observable is proved, not remote-tip exit times or random-backbone dynamics.

## originality

PASS

The initiating Majumder–Barma paper already establishes repulsive biased zero-range stationary product and site-density plateaus, and Little’s relation is classical. No inspected source provides exact entry-Palm subleading rational/irrational residence coefficient, denominator exponential suppression or Diophantine bounded remainder; these rely on a separate theta-series/rotation analysis. This is best-of-knowledge only.

## value

PASS

Subleading residence-time behavior in a physically motivated repulsive zero-range branch has a genuine denominator-sensitive discontinuous arithmetic coefficient despite universal quadratic growth. Rational/irrational dichotomy, Diophantine remainder and suppression quantify what the source called population plateaus; explicit fixed-fugacity Palm modeling prevents speculative extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
