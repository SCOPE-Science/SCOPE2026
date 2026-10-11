---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For f(x)=x^2/2 and the exact quadratic model, the constrained minimizer is s_k=-Delta_k as long as x_k>Delta_k. The condition Delta_0<(1-q)x_0 makes the total radius mass Delta_0/(1-q) smaller than x_0, so x_k=x_0-Delta_0(1-q^k)/(1-q) stays positive and x_k-Delta_k=x_{k+1}>x_infinity. Model and objective coincide, hence every accepted ratio is rho_k=1 for every eta in (0,1). There are no unsuccessful iterations, so C.2 is vacuous; C.3 holds because Delta_{k+1}=q Delta_k with q<1<gamma_3; C.1 fails because Delta_k tends to zero while the running minimum gradient tends to x_infinity>0. An independent exact-rational replay confirms the recurrence and rho=1, while the infinite conclusion comes from the geometric sum.

## originality

PASS

The 2026 primary survey names C.1 as the lower bound preventing radius collapse and proves convergence for mechanism classes satisfying it, but the inspected full text does not state an all-successful exact-quadratic counterexample showing that C.2 and C.3 alone are insufficient. Yuan's classical nonconvergence example addresses simple-reduction acceptance and is cited in the modern survey in a different acceptance-regime discussion. Fresh Resultary search found only the distinct SPD Cauchy-decrease record as the closest trust-region item. The submitted summable-radius witness therefore survives on a best-of-knowledge basis.

## value

PASS

The example isolates the independent role of a central convergence hypothesis: even a perfect model, exact subproblem solves, positive acceptance threshold and the other two radius controls do not prevent stalling if successful radii can have finite total mass. That is a motivated structural boundary/counterexample, despite the elementary scalar algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
