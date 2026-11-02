---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite-rate mixed-endemic convergence theorem

**Analytic identity.** `verify.py` creates symbolic independent variables for epidemic prevalence, susceptible and infected unprotected fractions, costs, transmission, recovery, and learning parameters. After substituting the two equilibrium relations, exact simplification of the difference between the derivative of the proposed entropy and the claimed negative-square-plus-transient expression gives identically zero. This establishes the critical algebraic calculation but not the global convergence proof by itself.

**Admissible exact example.** Rational checks produce \(q=1/4\), \(p=1/2\) and verify strict interior inequalities. They also reproduce the equilibrium vector field exactly.

**Numerical consistency.** Deterministic high-accuracy ODE integration from \((0.02,0.08,0.95)\), \((0.98,0.92,0.2)\), and \((0.4,0.2,0.7)\) converges toward \((1/4,1/2,0)\). This is diagnostic evidence only; the analytic argument uses forward invariance, exact entropy differentiation, integrability of the infected behavior variable, and a uniform-continuity convergence argument.

**Limits.** No exhaustive continuous-state verification, quantified computational roundoff certificate, or independent audit is claimed. The exact theorem excludes the specified invariant boundary faces and does not imply stochastic persistence or convergence for other payoff forms.
