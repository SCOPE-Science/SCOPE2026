---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Read RESULT.md spectral proof. Iteration residual is -(I-eta A)^k b and solution multiplier eta sum_(j=0)^(k-1)(1-beta)^j b at eigenvalue beta=eta lambda in [0,alpha]. This sum is strictly positive for beta<2, preventing 0/0 even for inconsistent systems. The residual-to-normwise-solution ratio is a positive-weight maximum of the scalar g(beta). On [0,1] it decreases and is bounded by 1/(alpha k); for beta>1 the formula increases in u=beta-1, yielding the top-eigenvalue endpoint. Both endpoints are attained by explicit PSD examples. On alpha>1 the first branch decreases and second increases, giving one crossing root; log expansion gives asymptotic. k=2 scalar witness sets sharp all-k bound u<=1/sqrt(3), while all even/odd k satisfy (k+1)u^k<=1 and (k-1)u^k<=1 by elementary recurrence monotonicity. k=1 has no admitted minimizer. Independent scalar spectral tests for k=1..40 and six alpha values over 401-point grids corroborated endpoints; grid search is not the minimax proof.

## originality

PASS

Best-of-knowledge distinct exact minimax optimization: source currently accessible establishes only generic 1/k guarantee; related published Richardson frontier uses another objective. The primary full-text comparison is explicitly incomplete due access; no negative whole-paper assertion or novelty certification.

## value

PASS

Provides exact optimal constant stepsizes for a mathematically motivated universal backward-error metric, improves the unit-step all-k guarantee by a sharp 1+1/sqrt(3) relaxation and asymptotically halves the best horizon-k constant. Crucially, includes inconsistent singular systems which classical forward-error treatments omit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
