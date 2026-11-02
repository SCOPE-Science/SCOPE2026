---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

From the exact published T_r and x_c, setting theta=L sqrt(r/D), b=sqrt(1-2/a), eps=1-b and u=eps theta reduces crossing to cosh u-1+tanh(b theta)sinh u = [a(1+b)^2/4]u². Its small-theta coefficient (1-b²)(1-5b²)/24 is negative for a>5/2, but exponential tail is positive, giving at least one positive root. Along every positive root as a→∞, bounded u forces theta bounded and leads to theta tanh theta=theta² (impossible except zero), while the uniform negative small-theta coefficient also excludes theta→0. Thus u→∞, tanh(b theta)→1 superexponentially, and u-2log u=log a+O(1/a). On the increasing branch, u=H+2log H+4log H/H+O((log H)^2/H²); converting theta/a=u/(a eps) changes only O(H/a). Independent high precision exact root checks over six finite c values corroborated the asymptotic but finite scans do not prove all-root assertion.

## originality

PASS

Qualified best-of-knowledge novelty of the precise additional claim only; original definitions, exact source formulas, special cases and existing methods remain prior work. Source readings and explicit residual priority risks are recorded; no assertion of exhaustive literature coverage.

## value

PASS

An exact coupled large-server resetting rate informs queue stability at the previously identified critical start location: the squared logarithm changes the true scaling beyond finite-sample power fits. The explicit loglog refinement is mathematically determined from the moving-boundary crossover equation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
