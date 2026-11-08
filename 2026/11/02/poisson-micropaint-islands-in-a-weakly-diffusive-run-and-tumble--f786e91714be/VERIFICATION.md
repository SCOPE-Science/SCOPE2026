---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For D>0 the phase at first passage of successive spatial levels is a homogeneous Markov chain, as in first-passage ladder theory; solving D K² − v diag(1,−1)K+Q=0 gives a=q/(sqrt(v²+2Dq)+v), b=(sqrt(v²+2Dq)+v)/(2D). Alternating Exp(a) and Exp(b) spatial runs are independent. With a→q/(2v), Db→v, coupling their exponential variables yields Poisson negative-run starts of rate q/(2v) and Exp(v) marks for widths/D; boundary-straddling events vanish. FK eigenvalue analysis or exponential-interval bounds yield compound-Poisson Laplace and moment convergence. Independent floating-point Riccati checks and transformed Laplace limits corroborate the formulas.

## originality

PASS

The first-passage spatial Markov property is established general Markov-additive ladder theory, and Sezik et al report minority paint islands of order D/v and average coverage. Neither reviewed source establishes the complete marked spatial island PPP, full negative area compound-Poisson limit and exact empty-window asymptotic. Quantitative new theorem survives crediting all earlier general mechanics.

## value

PASS

A microscopic random geometry of counter-oriented paint has a nondegenerate marked point-process limit even while its spatial measure vanishes. It gives exact random island counts, scaled lengths and area fluctuations for a canonical active-matter model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
