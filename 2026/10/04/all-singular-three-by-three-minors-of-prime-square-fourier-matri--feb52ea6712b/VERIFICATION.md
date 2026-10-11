---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Alexeev--Cahill--Mixon's prime-power full-spark theorem makes every minor with a type-A row or column set nonsingular. After translating a type-B column set to \(\{0,pa,b\}\), a type-B row set gives determinant \((v_2-v_1)(u_3-u_1)\ne0\); a type-C row set makes the first two columns proportional while the third separates the three lifts, so rank is exactly two. Two type-C sets factor as an outer product, giving rank one. Direct counting yields \(B=p^3(p-1)^2/2\) and \(C_3=p^2(p-1)(p-2)/6\), hence the stated totals. An independent p=3 full minor-rank replay agreed with all type predictions.

## originality

PASS

The prime-power full-spark theorem determines only whether a fixed row set makes every square minor nonsingular; for three rows it settles type A but does not say which individual minors vanish for non-full-spark type-B/C row sets. A separate published SCOPE result classifies three-point principal Fourier minors for arbitrary modulus, but explicitly excludes nonprincipal minors, so it does not imply this complete row/column rank census.

## value

PASS

The result converts a global failure-of-full-spark criterion into a complete local rank census and exact singular-minor count for the first nontrivial prime-power square setting. That is a natural structural refinement with direct uncertainty/harmonic-frame relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
