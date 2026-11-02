---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The final claim fixes the ground field F2, geometrically smooth quartics and conics, rational base points, intersection multiplicity exactly eight, and counts literal nonzero homogeneous forms (scalars F2^×={1}), not isomorphism classes. Reconstructed the conic-first method using all 28 geometrically smooth conics and their 84 rational point flags. Formal conic expansions modulo t^8 give eight homogeneous linear constraints on all 32767 nonzero quartic forms. An independently written GL3(F2) action checks all 168 substitutions and partitions them into 279 orbits. On each orbit representative, independent GF2 Groebner unit-ideal checks in each affine chart give exactly 78 geometrically smooth orbits, total 10920 forms. Their contact histogram is exactly h=0:9849,h=1:840,h=2:210,h=4:21, and the unique h=4 orbit has 21 forms. The two complementary searches together are exhaustive; this is a finite-field proof, not extrapolation. Bezout bounds contact order by 8 for smooth quartic vs conic.

## originality

PASS

PASS (qualified): Best-of-knowledge assessment after comparing maximal conic osculation with sextactic points, canonical genus-three characteristic-two curve classification, and adjacent line/tangency tables. The exact 9849/840/210/21 fixed-coordinate smooth-conic eight-contact distribution is not a stated or logically immediate consequence of inspected primary results. Older unindexed conic-contact tables remain a genuine risk; failure to find them is not a novelty proof.

## value

PASS

PASS: The enumeration is a complete, exact, equation-weighted incidence distribution for a natural canonical genus-three family in the smallest characteristic-two projective plane; the sharp maximum and unique extremal orbit are relevant to Weierstrass/osculating conic geometry. Neither a generic small table nor an arbitrary selected quartic is the central invariant; it exhausts all smooth forms and distinguishes smooth conics from singular line pairs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
