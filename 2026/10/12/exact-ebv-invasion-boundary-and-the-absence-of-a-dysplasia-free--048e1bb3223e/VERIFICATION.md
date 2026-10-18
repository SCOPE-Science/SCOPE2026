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

With C=0 at an equilibrium, Cdot=mu H forces H=0, then Hdot=gamma I forces I=0, and Vdot=-d6 V forces V=0. Remaining equations give N0=a1/(d1+alpha)>0 and D0=alpha*N0/q>0. If D=0 the Ddot=alpha N term forces N=0, contradicting Ndot=a1>0. Printed E02=(a1/d1,0,0,0,0,0) has Ndot=-alpha*a1/d1 and Ddot=+alpha*a1/d1. Exact Jacobian factorization gives four strictly negative scalar eigenvalues and infectious quadratic (lambda+k)(lambda+d6)-beta*e*a3*D0. For R>1 it has a positive real root; for R<1 both roots have negative real parts; at R=1 nonhyperbolic only. Explicit apoptosis-dominant rates a_i=1, d_i=2, alpha=gamma=mu=e=1, beta=20 give R=5/3 and positive root -2+sqrt(20/3). A fresh independent SymPy Jacobian reconstruction verified polynomial and witness. The claimed clearance-conditional D->D0 follows stable scalar forcing.

## originality

PASS

The source-specific correction targets the original published six equations, a purported nonstationary second equilibrium and an unjustified unconditional local-stability sufficiency. General virus reproduction-number theory is prior background, but its generic existence does not establish the precise published error, exact six-state factorization and concrete counterexample. The open-licensed primary article transcription was materially inspected for equations and stability assertions.

## value

PASS

The published model gives a mathematically wrong equilibrium and potentially reversed linear-stability prediction. Demonstrating the exact feedback threshold with a positive-parameter counterexample is substantively important for interpreting the stated ODE, beyond a superficial typo or cheap zero check. It makes no clinical inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
