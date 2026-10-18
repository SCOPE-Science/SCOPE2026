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

For E_dot=α_E I_m−μ_E E and mammal rectangle 0<=I_m<=K_m=Λ_m/μ_m, at E=H the maximum normal derivative is α_E K_m−μ_E H; it is nonpositive iff H>=α_E K_m/μ_E. The published H=α_E/μ_E works iff K_m<=1. From source Table1 Λ_m=2, μ_m=1/(365*60), α_E=μ_E=1/14 so K_m=43800; admissible state (S_m,I_m,S_v,I_v,E)=(1,2,1,1,1) has total mammals 3<43800, vectors 2<70 and E_dot=1/14>0. Independent exact Fraction arithmetic verified all numbers; no numerical integration required.

## originality

PASS

The biological dynamics and generic inward-boundary criterion are old. The new check targets a particular published invariant-set inequality that tacitly assumes I_m<=1, whereas the paper uses a mammal headcount. The source-specific failed region, exact iff regime, and Table1 counterexample were not found in original or inspected follow-ups.

## value

PASS

The defect is in an invariant region used for mathematical well-posedness and as a domain for epidemic stability arguments. The paper’s own calibration makes the printed cap 43,800 times too small, and an explicit admissible boundary trajectory leaves immediately. Identifying and correcting an essential analytical precondition is substantively useful beyond checking a harmless typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
