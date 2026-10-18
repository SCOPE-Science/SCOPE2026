---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Invariance of first and second lifted momentum moments gives E[kick]=0 and 0=2E[p kick]+E[kick^2], and Cauchy–Schwarz gives the inequality. On the positive-variance equality locus the Cauchy equality coefficient is -1/2, so p-m=-kick/2, P-m=kick/2; invariance gives sin Theta=-sin theta. Consequently the second iterate has p2=p and theta2=theta+2m. Iterating sin(theta+2m)=sin theta shows either sin m=0 or cos(theta+m)=cos(theta+3m)=0; the latter with sin m nonzero forces m=pi/2 modulo pi and then sin theta=0, contradicting positive kick variance. Thus m belongs pi Z and T^2=id on the invariant full-measure set. Ergodicity then restricts support to one two-cycle. Direct exact orbit arithmetic verifies K=2pi: (pi/2,-pi) ↔ (3pi/2,pi), with Var(p)=pi^2 and Var(kick)=4pi^2. The saved verify.py algebra was inspected, but is not used as a proof of the trig branch.

## originality

PASS

Best-of-knowledge original contribution is the full Chirikov-map equality rigidity and sharp boundary, NOT the universal half-anticovariance identity for any stationary additive process. Cross-comparison with published standard-map transients and independently indexed stationary covariance laws on other maps found no prior statement implying the standard-map period-two classification. Absence of an indexed result cannot guarantee absolute priority.

## value

PASS

The exact orbit-rigidity equality case turns a routine second-moment balance into a dynamical diagnostic: all compact stationary states satisfy a sharp measurable variance bound, and a positive-kick ergodic saturator is necessarily a two-cycle. Both the nontrivial dynamical obstruction and explicit sharp orbit distinguish the contribution from textbook covariance algebra. Natural use in standard-map invariant-measure analysis, no claim about chaotic ergodicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
