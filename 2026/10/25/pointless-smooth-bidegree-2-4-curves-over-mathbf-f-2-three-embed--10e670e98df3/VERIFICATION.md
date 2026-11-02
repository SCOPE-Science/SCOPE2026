---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

No rational points forces each of the three quartic coefficients to take value 1 on all three F2-rational base points, giving exactly four quartics q19,q21,q25,q31 and 4^3=64 equations. Geometric smoothness is equivalent to gcd(b,(a'c+ac')^2+(b')^2ac)=1; an independent F2 polynomial GCD implementation enumerated all 64 and recovered smooth counts by b of 9,6,9,9 (total 33). An independent substitution implementation of all 36 PGL2(F2)xPGL2(F2) coordinate pairs gave exactly three orbits of sizes 9,18,6. Genus (2-1)(4-1)=3 by adjunction and Deuring–Shafarevich branch count of b gives 2-ranks 3,3,1. The enumeration is genuinely exhaustive for the specified embedded linear system, not all genus-3 curves.

## originality

PASS

The target is an embedded equation/orbit census for one ample linear system over F2, whereas the directly relevant 2004 classification covers abstract genus-three hyperelliptic curves up to field isomorphism. The latter may imply some abstract curve types but does not directly provide counts of fixed (2,4) equations and factorwise PGL2xPGL2 orbit sizes in its accessible abstract. Best-of-knowledge PASS with unusually material priority risk: full 2004 text was inaccessible, so no whole-document noncoverage is asserted.

## value

PASS

A complete natural embedded-model classification for the smallest base field with pointlessness, with exact geometric smoothness and symmetry orbit counts and p-rank stratification. These invariants are useful to algebraic geometers working with explicit curves, model enumeration, and arithmetic surfaces even if abstract isomorphism classes were previously classified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
