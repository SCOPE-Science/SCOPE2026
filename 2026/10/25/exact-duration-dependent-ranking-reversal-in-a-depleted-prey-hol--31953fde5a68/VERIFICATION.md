---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Integrating dN/dt=-N/(c+hN) gives T=c log(N0/N)+h(N0-N) and a unique survivor. Equality of survivors yields Nc log(N0/N)=N0-N and T=q log(N0/N), hence necessary-and-sufficient threshold. Continuous dependence and the unique threshold plus low-stock and high-stock scalar comparison determine strict signs. The function s/(1-e^-s) is strictly increasing from 1 to infinity and selects one positive switch; W0 yields u in (0,1), while W_{-1} corresponds to T=0. Independent numerical inversion gives threshold 2.5059407020437066 and correct signs on either side.

## originality

PASS

Rogers depletion equation and Lambert-W inversion are known; Rosenbaum–Rall studies parameter estimation for the same ODE. Inspected text does not establish an explicit two-assay duration/initial-stock threshold or a unique cumulative-ranking reversal. Possible appearance of this simple crossing-comparison consequence in older functional-response literature is a real priority risk.

## value

PASS

The exact threshold determines when measured cumulative consumption rankings can reverse with duration, relevant to interpretation/design of closed feeding assays. It is a complete necessary/sufficient prediction for a motivated parametric tradeoff, although it neither models coupled predators nor measures empirical uncertainty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
