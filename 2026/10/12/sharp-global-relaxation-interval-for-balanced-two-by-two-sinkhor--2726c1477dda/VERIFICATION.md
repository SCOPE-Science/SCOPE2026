---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Writing x=log(u1/u2), y=log(v1/v2) yields exact successive affine omega-relaxations to x_*(y)=log(B/A), y_*(x)=log(D/C). The log-partition potential satisfies Phi(x,y)=log(2sqrt(AB))+log cosh((x-x_*)/2) and analogously for columns, so each half-step strictly decreases it for |1-omega|<1. All Kij positive make Phi strictly convex and coercive, giving unique projective limit through compact-sublevel descent. The common scaling product w follows affine recursion coefficient (1-omega)^2<1 with forcing tending to its balanced value, proving convergence of P rather than ratios alone. At omega=2 each step conserves Phi, and omega>2 never lowers Phi from a nonminimal start, so global convergence fails for each fixed K. Conditions include positive rank-one K and arbitrary positive starts, not unequal marginals.

## originality

PASS

Lehmann et al. (2022) prove local fixed-omega convergence for the whole (0,2) range but global convergence only under omega<2/(1+Lambda(K)); their full open HTML §1-3 explicitly separates those results. Rank-one and all 2x2 balanced kernels are not given a universal global special-case theorem there. Conditional logcosh argument exploits equal two-point marginals and gives strict global improvement; residual risk from older nonlinear SOR / coordinate minimization literature.

## value

PASS

Solves the sharp all-initializations fixed-parameter safety interval for the smallest nontrivial balanced scaling problem, replacing Birkhoff sufficient interval near one on high-contrast K with full (0,2) and demonstrating sharp endpoint conservation. This is a natural convergence question with an exact structural answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
