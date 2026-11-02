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

# Verification details

The accompanying standard-library script `verify.py` uses independent integer coefficient construction, exact synthetic division by \(X+1\), exact binomial translation, and verification of all translated Eisenstein conditions. For \(p\in\{3,5,7,11\}\), \(r\in\{3,4,5\}\), it recomputes the entire quotient discriminant from an integer Sylvester determinant by the Bareiss elimination algorithm. It confirms that the \(p\)-adic exponent equals \(p-2\) and the residual unit modulo \(p\) equals \((-1)^{(p-1)/2}\).

For the smaller cases \(p\in\{3,5,7\}\) and \(r\in\{3,4\}\), the script additionally computes exact rational Sturm sequences, checks that all \(p-1\) quotient roots lie on the negative real axis, and verifies that precisely \((p-1)/2\) lie on each side of \(-1\).

Successful execution result: `VERIFY_OK: 12 prime/exponent polynomials, 78 shifted Eisenstein coefficients, 12 independent integer Sylvester discriminants, 6 exact real-root counts`.

**Scientific limits.** These are finite computational spot checks. Universality is proved separately by polynomial symmetries, Eisenstein's criterion, classical multiplier-sequence theory and valuation analysis; no numerical root plots, search failures, or unchecked log entries are used as a proof. Independent validation is not performed.
