---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Re-derive the conservative stage v=(2x+t/2)/(t+2) and final scalar solve x+=(x+tw/2)/(1+t(u+w)/2) with u=x/v,w=(1-x)/(1-v). Symbolic elimination gives delta+=delta*m_t(delta^2) with positive denominator K-HD and strictly negative derivative in D. Endpoint ratios c(t)=(2-t)/(2+t), b(t)=(4-t-t²)/(t²+3t+4), so q=max(c,-b)<1 for each finite t; this proves uniform global geometric contraction. The two monotone endpoints cross at the unique positive zero of t³+2t²-2t-8, yielding optimal t. b(t)>=0 characterizes non-crossing and t=2 yields -delta³/(12-5delta²). Independently symbolic stage computation verified the map, derivative identity, endpoints and cubic equation. Positivity follows from strictly positive numerator and complement. No implication for different stage schemes or more species.

## originality

PASS

Compared exact statements, not shared terminology. An exact global nonlinear one-step Lipschitz contraction on the whole positive simplex is not equivalent to positivity or local spectral stability. The inspected same mathematical model primary material did not establish the sharp multiplier q(t). The proven one-way result is not a two-way symmetric nonlinear global contraction theorem; a general local Jacobian criterion does not imply global behavior. No checked exact threshold database covers the continuous all-step/all-start minimax frontier. Negative searches do not establish originality in isolation. Published local linearization and different variant counterexamples do not imply q(t), cubic cancellation t=2, or sharp no-crossing t=(sqrt17-1)/2 in the positive symmetric two-way scheme.

## value

PASS

Published literature analyzes local versus global Patankar stability and the possibility of spurious fixed points. A global all-initial-state error bound, sharp optimal time step, non-overshoot frontier and exact cubic special step for the canonical conservative exchange scheme answer a motivated stability design question, distinct from mere positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
