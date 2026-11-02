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

For every d>=2, Haar U(d) invariance makes the initial coin vector complex-sphere uniform: E|u_a|^4=2/[d(d+1)], giving E P1=2/(d+1). At t=2 the diagonal reduced-coin purity contributes (d+3)/(d+1)^2, and off-diagonal two-path coincidences at the origin and e_b xor e_bprime contribute 2/(d+1)^2 via distinct Haar-row fourth moments 1/(d^2-1). Therefore E P2=(d+5)/(d+1)^2 and the difference is (3-d)/(d+1)^2; checked d=2 and d=3 boundaries and d>=4 sign. Independent state-amplitude Monte Carlo for d=2..6 (1500 pairs each) agreed within approximately two standard errors; finite samples are not proof. Checked exact normalized purity calculation independently.

## originality

PASS

Inspected the same global-Haar-coin Q_d model in Quillen 2026, including its operator and averaged-channel formula; it treats one-copy channel evolution, not the nonlinear two-copy expectation Tr(rho_C^2). Vieira 2013 and Fang 2023 study different two-state coin settings. Resultary search found dissimilar two-state walk and hypercube outcomes, not the exact d-dependent two-step crossover. Standard Haar fourth moments are prior tools, not a novel identity; general two-copy circuit methods could imply this specialized formula.

## value

PASS

Exact short-time dependence of mean coin-position linear entropy on dimension is a motivated entanglement diagnostic; the d=3 sign boundary is a genuine model-specific effect lost under averaging the channel first. No longer-time or samplewise statement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
