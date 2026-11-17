---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For each k≥2 the exchangeable pair variables u(t)=P(H≠L1),v(t)=P(L1≠L2) satisfy the exact 2×2 linear ODE u′=−(α+β)u+(k−1)β v/k, v′=2α(u−v) with initial 2ρ(1−ρ). Determinant of stable matrix=2α(α+β/k)>0, negative trace. Cramer resolvent gives Jδ and differentiating at fixed α,k,ρ,δ gives numerator 2ρ(1−ρ)(δ+2α)[α(k−3)−δ], strictly controlling signs for k=2,3,≥4 and equality. Independently factored derivative with symbolic algebra; exact full-state checker was read but not executed unmodified.

## originality

PASS

Exact star rate-sensitivity phase boundary concerns discounted cumulative edge discord under iid initial data, not consensus hitting time or fixation. Same-star published earlier theorem computes different observables, and Masuda/Gibert/Redner treats heterogeneous voter consensus; no inspected statement determines the δ-dependent sign reversal.

## value

PASS

A natural observable (integrated edge disagreement) exhibits a sharp hub-rate reversal exactly between three and four leaves, with a discount threshold independent of the hub rate. It has a mathematically surprising contrast with the strictly faster initial decline under larger β, providing meaningful structural insight beyond known consensus-time results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
