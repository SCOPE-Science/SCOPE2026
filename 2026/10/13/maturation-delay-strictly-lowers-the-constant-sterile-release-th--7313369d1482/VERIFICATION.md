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

Using the exact constant-release delay system and equilibrium cubic of Cai–Ai–Fan, positive wild equilibrium with N=w+g>0 requires a>mu1 and b=B_a(N)=N(mu2+xi2 N)(a-mu1-xi1 N)/a. For fixed positive N within the admissible interval, dB/da=N(mu2+xi2N)(mu1+xi1N)/a^2>0, while the admissible interval expands in a, so the positive maximum strictly increases with a and strictly falls with tau through a=a0 exp(-mu0 tau). If a<=mu1 no positive equilibrium. Scaling N=(a-mu1)y/xi1 yields the quadratic endpoint coefficient mu1*mu2*mu0^2/(4xi1). Independent 45-digit decimal maximization gives b0(0)=21.93751602037679, b0(0.2)=21.04329287724136, b0(1.5)=16.04165879781685, b0(4.9)=7.81905967141617 and root b0(tau)=21 at tau=0.209892962986665; these contradict the printed Fig 1 threshold label and Fig 2 positive plateaus under fixed parameters, while preserving published local-stability theorem where equilibria exist. All parameters positive and tau>=0.

## originality

PASS

The specified surviving claim is not established by any inspected prior statement or directly dominating mathematical implication. The four separate equivalence/coverage/table/implication comparisons below identify exactly which named background results are already known and which new mathematical conclusion remains; unpublished and inaccessible-source risks are explicitly retained.

## value

PASS

A critical extinction boundary and its quadratic asymptotic for a biologically motivated delay model, plus a quantitative correction of actual published Figure 1–2 captions, are directly useful to interpreting threshold controls; this is not an endorsement of field application nor merely a numerical last-digit correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
