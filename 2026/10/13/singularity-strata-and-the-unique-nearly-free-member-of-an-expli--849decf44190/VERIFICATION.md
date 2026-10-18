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

For t != -1 four displayed quadrics have nonzero determinants (-1,-1,-1,-24(t+1)). Independently reconstructed all 6 pairwise y-resultants; moving discriminants are 8(8-t),32(2-t),8(8-t), and fixed-point substitutions yield triple collisions only at t=0 and 7/2. Pairwise local expansions at t=0 give (4,2,2) branch contacts at each of two triple germs; t=7/2 gives two ordinary D4; t=2 gives two A3 and t=8 two extra A7, while pairwise Bezout total24 certifies remaining nodes. Generic: 2A7+16A1 tau30; t2: 2A7+2A3+12A1 tau32; t7/2: 2A7+2D4+10A1 tau32; t8: 4A7+8A1 tau36; t0: two (4,2,2) triples plus 8 nodes mu36 tau<36 by Saito non-quasihomogeneous criterion. The nearly-free octic relation tau=48-r(7-r) forces tau>=36 for admissible r<=4; for t8 exact cubic syzygy and full-rank lower-degree matrices modulo1000003 yield mdr3 and near freeness. Independently checked resultants, jacobian syzygy over Q and modulus. t9 printed by Pokora lies in generic stratum; t-1 excluded. Proof uses exhaustiveness of resultants, not finite t-samples.

## originality

PASS

The full accessible 2024 primary Pokora article Example2.6 actually displays the -9z^2 coefficient (t=9) while claiming an intended 4A7+8A1 nearly-free configuration, which the displayed member fails to realize. The reviewed claim corrects the parameter to t=8 AND enumerates all exceptional strata and unique near-free parameter, beyond bare existence of the configuration (already known). Targeted Resultary and reference searches found no specific complete t-parameter stratification or erratum. Potential unindexed correction retained.

## value

PASS

A complete degeneration and freeness stratification of an explicit naturally published family corrects a materially inconsistent example, identifies non-ADE boundary germs and explains why exactly one smooth-four-conic member is nearly free; this is a motivated parameter-space classification rather than a one-number change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
