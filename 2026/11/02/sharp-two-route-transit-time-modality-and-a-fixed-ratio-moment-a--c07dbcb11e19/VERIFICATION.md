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

For f(t)=w a e^{-at}+(1-w)b^k t^{k-1}e^{-bt}/(k-1)!, set s=bt and R=a/b. Its derivative divided by positive b²e^{-at} equals -w R² +(1-w)φ_{k,R}(s)/(k-1)!, φ=s^(k-2)(k-1-s)e^((R-1)s). At s≥k-1 the sign is strictly negative. For k≥3 the derivative of logφ decreases strictly from +∞ to -∞, giving a single maximum and exactly two strict peaks (zero and a positive one) when the level C=(k-1)!wR²/(1-w) lies strictly below φ*. Equality is only a horizontal shoulder. For k=2, φ=(1-s)e^((R-1)s) starts at 1 and increases first only when R>2, yielding the separate w0=1/(1+R²) and w* thresholds; for k=1 mixture is decreasing. The two stated rational k3,R3 parameter triples were independently checked to have mean exactly 1, second moment 493/242, variance 251/242, with weights on opposite sides of the rigorous φ* threshold. Numerical derivative sampling is supplemental, not the universal proof. Endpoint equality and nonpeak shoulders were considered.

## originality

PASS

Best-of-knowledge mathematical statement-and-implication comparison of the exact reviewed final theorem with relevant primary literature, published-record searches, and recognized prior ingredients. Search failure is not novelty proof; priority risks remain specified.

## value

PASS

Modality of a physically interpretable mixture of one exponential transit route and a serial Erlang route is a natural density-shape question. The exact all-rate, all-integer-stage phase diagram (including the special k2 boundary) and the explicit fixed-ratio two-moment alias address identifiability: two distributions can have the same low moments yet differ in peak count. The result neither claims complete general gamma-mixture classification nor identifies parameters from noisy data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
