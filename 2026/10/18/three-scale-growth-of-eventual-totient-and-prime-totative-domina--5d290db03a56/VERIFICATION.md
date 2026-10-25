---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Rosser–Schoenfeld uniform n/φ(n)≤e^γ loglog n+O(1/loglog n) and quantitative PNT give F(n)=φ(n)/π(n)≥y/(e^γ log y)(1−O((log y)^−2)), y=log n. Along primorials, effective Mertens/PNT give matching F(P)=y/(e^γ log y)(1+o((log y)^−2)); gaps in log successive primorials O(log y)=o(k). Since (φ−π+ω)/(π−ω)=F−1+o(1), bracketing y=e^γ k(log k+loglog k+γ±ε) proves both log N_k and log M_k with o(k) remainders, no RH. Checked the inversion algebra independently at k=10^3,10^5,10^8.

## originality

PASS

Checked the exact N/M definitions in the original source and derived nontrivial matching effective asymptotic brackets, explicitly separating classical totient and prime number estimates from the claimed sharpened threshold inversion.

## value

PASS

The two explicitly introduced eventual number-theoretic thresholds acquire matched three-term asymptotic locations, separating extremal totient behavior from finitely computed exact thresholds. The third k-scale constant controls previously unavailable precision needed in asymptotic comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
