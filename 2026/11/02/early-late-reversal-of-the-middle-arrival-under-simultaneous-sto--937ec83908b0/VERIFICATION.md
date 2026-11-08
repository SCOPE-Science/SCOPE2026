---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

PASS: The conditional common-clock no-hit probability U=product of q0(reset gaps) makes the three hits a Bernoulli mixture, while independent clocks give h(1-E U). f0(t)=erfc(d/sqrt(4Dt)) has strictly positive second derivative for 0<t<d^2/(6D), so for any common-clock partition 0<1-U<=f0(t)<1/2; strict convexity of h(p)=3p^2-2p^3 gives the early inequality. Joint-survival renewal S_j(t)=exp(-rt)q0(t)^j + (r exp(-r.)q0(.)^j)*S_j admits unique tilted poles. Cauchy--Schwarz for Z=exp(theta1 E)q0(E) (Exp rate r) proves theta2<2theta1; the key renewal theorem yields positive c1,c2, and weighted integrability makes S3=o(S2). This yields reversed late tails and the correct strict extremes via Jensen. Independent numerical quadrature at three (d,D,r) triples verifies strict pole order; no finite computation is used as the large-t proof.

## originality

PASS

PASS, qualified best-of-knowledge: closest 2026 work treats rank-dependent resetting/optimal passage times, not the inspected theorem of early-vs-late middle-arrival CDF inversion with explicit spectral tail. Biroli--Majumdar--Schehr treats first arrival, and Belan treats median of a single variable. The 2026 supplement could not be examined completely.

## value

PASS

PASS: Middle of three first-arrival events is the smallest nonextreme rank. It displays a rigorous temporal inversion between otherwise marginally identical reset protocols, contradicting any universal stochastic ranking and giving a sharp exponential late-time rate. This bears directly on rank-dependent search/time-risk decisions, not just a generic Jensen restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
