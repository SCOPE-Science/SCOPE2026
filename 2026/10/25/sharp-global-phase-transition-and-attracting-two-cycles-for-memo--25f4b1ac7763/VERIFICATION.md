---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The embedded gradient is sin(theta)*(-sin(theta),cos(theta)); with beta2=0 the preconditioner is diag(|g1|+epsilon,|g2|+epsilon), and the projection-retraction step is exactly F(theta)=theta-arctan(alpha*w_epsilon(theta)). The positive odd coefficient w is as stated. With t=tan(theta) in (0,1), w=tD_epsilon(t)/sqrt(1+t^2); the exact derivative factorization -D' p^2q^2 is positive, making A_epsilon(t)=2sqrt(1+t^2)/((1-t^2)D_epsilon(t)) strictly increasing from 2epsilon to infinity. The symmetric two-cycle condition alpha=A_epsilon(t) therefore has exactly one nonzero solution above 2epsilon. For alpha<=2epsilon the arctangent rotation is strictly between zero and 2|theta| for all noncritical theta, proving strict global radial-angle contraction; the only excluded point theta=pi is the nonminimal stationary point. Local expansion F(theta)=(1-alpha/epsilon)theta+(alpha/epsilon^2)theta|theta|+O(|theta|^3) yields quadratic alpha=epsilon and critical reciprocal law. A second exact positive derivative polynomial for D+t(1+t^2)D' makes w'>0; monotone cycle parameter implies -1<F'(theta*)<1. Endpoint Taylor expansions give amplitude and period multiplier asymptotics. Own SymPy independently verified both polynomial derivative identities and bounded numerical tests for epsilon=0.2,0.8,2 support contraction and local cycle attraction. Analytic inequalities, not those samples, establish global results.

## originality

PASS

Sakai--Iiduka arXiv:2409.00859v1 explicitly defines the embedded projected preconditioned RMSProp framework (Algorithm 1 and Section 2), but its general convergence bounds and numerical experiments do not determine the exact circle normalization dynamics or the sharp alpha=2epsilon threshold. Bock--Weiß arXiv:2210.02070 studies nonconvergence/two-cycles for Euclidean Adam on quadratics, a distinct algorithm/state; Bensaid et al. 2407.15471 analyze adaptive steps under other conditions. Resultary similar scalar Padam and gradient schemes use distinct updates. No implication of the exact two-cycle amplitude/critical reciprocal law from these inspected sources was found.

## value

PASS

A sharp deterministic convergence-versus-stable-oscillation boundary for a natural simplest manifold instance of an adaptive optimizer is useful to understand step-size safety. Explicit decay at the marginal threshold, linear rather than square-root cycle onset, and asymptotic return multipliers are nonroutine mathematical dynamics features.

The dated certificate retains the supplied scientific assessment, sources and limitations.
