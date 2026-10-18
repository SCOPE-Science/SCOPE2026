---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Summing all displayed SIRS equations cancels progression and recovery to obtain z=N-S0 with z’=-mu*z-Σdelta_j I_j. Positivity and comparison give S-S0<=c exp(-mu t), c=(N0-S0)_+. I1’=[a1(R0-1)+beta(S-S0)] I1, so exponential decay if R0<1. At R0=1 a rescaling by exp[-beta*c*(1-e^-mu*t)/mu] is nonincreasing; hence I1 tends to finite L>=0. If L>0, strictly positive delta1 forces z eventually bounded below zero by a fixed amount, implying I1 declines exponentially, contradiction. Every downstream stage and R are exponentially stable scalar linear systems with vanishing input; N->S0, S->S0. Positive R0>1 eigenvalue gives instability. Checked algebra against source equations, including n=1, all nonnegative data and δ1>0; no claim of critical Lyapunov stability or endemic equilibrium.

## originality

PASS

The motivating full publisher article establishes restricted n=2,3 theorems under α and Condition A, and explicitly describes arbitrary-stage and unconstrained DFE conditions as unproved. Matrix Lyapunov criteria in prior work need positivity that fails when S>S0. The exact all-stage comparison argument supplies a genuine new statement while retaining risk of other specialized epidemiological theorems.

## value

PASS

Closing a biologically counterintuitive auxiliary waning-immunity threshold for global disease extinction across arbitrary stage counts is a motivated structural theorem resolving an explicit limitation of the primary paper, not a parameter substitution or a finite numerical increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
