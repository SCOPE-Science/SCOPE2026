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

The finite-difference exponential-pair identity applied to p_k=(1−r)r^k+(1−s)s^k−(1−rs)(rs)^k yields Δ_k=(rs)^{k−1}H(k), with a strictly decreasing H and H(1)=rs(1−r)^2(1−s)^2(r+s+2)>0, H(∞)=−(1−r)(1−s)(r−s)^2<0 if r≠s. Thus exactly one real sign crossover; r=s is strictly log-concave. For positive log-concave parents with common support {0,1,2}, c1²−c0c2≥uw(u+w+2)>0. For common {0,1,2,3}, truncated geometric parents r=1/10,s=1/5 produce exact negative curvature −3/50000 before positive normalization. Independently re-expanded H(1) and four-point witness in exact SymPy arithmetic. This proves sharp minimum common support size four, not a classification of arbitrary supports.

## originality

PASS

Badiella–del Castillo–Puig prove log-concavity preservation for order statistics formed from identically distributed discrete samples; this result distinguishes heterogeneity r≠s and obtains a single strict log-curvature reversal and sharp n=3 vs n=4 support boundary. The older Alimohammadi and Kim order-statistic papers may contain more general conditions; their full texts were unavailable, so no blanket claim about absence of special cases is made.

## value

PASS

An exact boundary for closure of log-concavity under maxima of nonidentical independent parents is structural and motivated; it identifies precisely the first finite support where closure fails and determines the entire sign pattern of a natural geometric model. The four-point counterexample is not an arbitrary slice but the minimal universal obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
