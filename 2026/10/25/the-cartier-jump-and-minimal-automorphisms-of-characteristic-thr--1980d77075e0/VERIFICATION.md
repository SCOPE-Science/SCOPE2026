---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The displayed valuation formula is checked for the five differential monomials and their completeness within exponents \(0\le j\le2\). Cartier action is computed by \(\mathcal C(x^i dx)=0\) unless \(i\equiv2\pmod3\) and by \(y=y^3-f(x)\). These algebraic equalities give ranks \(2\) and \(3\) exactly when \(B=0\) and \(B\ne0\), respectively. The automorphism proof also depends on the cited uniqueness theorem for the index-three rational subfield, applicable outside the exceptional numerical pairs.

Run `python3 check_cartier.py` from the extracted package. It checks 36 prime-field coefficient models with all \(A,D\in\mathbb F_3^\times\) and \(B,C\in\mathbb F_3\); this arithmetic enumeration is a diagnostic consistency test and does not establish the infinite-field claim. No independent scholarly or machine-proof audit is asserted. Earlier implicit coverage and general Newton polygons remain unverified.
