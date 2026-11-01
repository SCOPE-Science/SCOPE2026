---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

At P0, X=0 has divisor (q+1)P0+P2, with P2 having a different tangent, proving unique dual branch. The local smooth curve x+t^(q+1)+x^(q+1)t=0 yields ord_t u=q and ord_t v=M=(q+1)²+1 for the Gauss map. For odd q, gcd(q,M)=1; cancellations cannot produce values below qM beyond monomial valuations, and the conductor of <q,M> is (q−1)(M−1)<qM, yielding exact semigroup, delta and conductor. Frobenius permutes the Tallini special tangent points, whereas coordinate points in Pellikaan model are rational. Independent q=3,5,7,9 formal-series and gap checks corroborate, without replacing uniform proof.

## originality

PASS

Published plane-filling Tallini/Pellikaan geometry includes the original curve, its Weierstrass semigroups and special tangent contacts. That does not determine the complete value semigroup of a singular branch of the DUAL curve. The dual-coordinate orders q and M=(q+1)^2+1 are coprime for odd q and produce the claimed explicit cusp invariants. Komeda studies an unrelated degree q²+q+1 family with inseparable Gauss map.

## value

PASS

An exact uniform local-semigroup classification at three geometrically distinguished singular dual points is useful for positive-characteristic plane-curve geometry, including conductor and delta invariants. The odd-char boundary and Frobenius distinction have independent meaning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
