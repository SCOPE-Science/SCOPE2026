---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fink's formula reduces pristineness exactly to \(F_7(c)=q^7\). Exact expansion gives \(5040F_7(c)=(c+8)G(c)\) with \(G(-8)=-2^{14}3^2\), hence \(\gcd(c+8,G(c))\mid2^{14}3^2\). For \(q\ge11\), \(q\) divides only one factor; the elementary lower bound \(F_7(c)>c^7/5040\) gives \(c<4q\), excluding \(q^7\mid c+8\) and forcing \(c+8\le5040\). For \(q=3,5,7\), the same growth bound gives the smaller \(c<28\). Fresh exact arithmetic checked the polynomial identity and every \(1\le c\le5032\); no value is a seventh power. The finite scan is therefore exhaustive only after the proved cutoff.

## originality

PASS

Fink proves nonexistence only for odd exponents three and five, proves merely an at-most-\(d-1\) result for general odd \(d\), and explicitly asks whether all odd exponents have no solutions. The audited result settles the first untreated exponent \(d=7\) by a new factorization/coprimality cutoff and exact finite exhaustion. Resultary returned the assigned theorem as the exact hit and no stronger predecessor.

## value

PASS

This settles the first untreated exponent in an explicit published open family. The combination of a structural cutoff and a small exact certificate is a meaningful finite resolution of a natural Diophantine subproblem rather than an arbitrary search range.

The dated certificate retains the supplied scientific assessment, sources and limitations.
