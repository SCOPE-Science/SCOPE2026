---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The hyperelliptic Cartier matrix H_ij=[x^(7i-j)]f^3, i,j=1..5, was independently reconstructed. Polynomial arithmetic modulo 7 verifies det(H)=-9ab^3(2c^5+b(a^2-b)(a^2+b)^2) and decisive minor -3b^3c^4. Smoothness implies b!=0. For c!=0 rank>=4; for c=0 the five sparse entries are independent except at a^2+b=0, giving rank3. F is Eisenstein at b, coprime to a; F_c=3c^4, and at b=-a^2!=0,c=0 the transverse germ has unit*u^2+2c^5, hence A4. The two components meet transversely where a=F=0. Independent symbolic reconstruction verified the determinant and minor; the package GF7 checker exhausts 343 finite-field triples, though finite checking cannot prove the geometric k-point assertion.

## originality

PASS

Best-of-knowledge originality of the precise final result is retained after direct scope/implication comparisons and meaningful reading, with identified prior machinery and explicit inaccessible-source risks. No failed search is treated as a novelty proof.

## value

PASS

This family-specific Hasse divisor has two components, one with an explicitly located cuspidal locus encoding exactly the a-number-2 jump. The exact stratification and local A4 geometry are meaningful natural invariants for families of hyperelliptic Jacobians, not a routine statement of the generic Cartier coefficient formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
